from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from enum import StrEnum


class ApplicationStatus(StrEnum):
    DRAFT = "draft"
    APPLIED = "applied"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    ACCEPTED = "accepted"


_VALID_TRANSITIONS: dict[ApplicationStatus, set[ApplicationStatus]] = {
    ApplicationStatus.DRAFT: {
        ApplicationStatus.APPLIED,
        ApplicationStatus.WITHDRAWN,
    },
    ApplicationStatus.APPLIED: {
        ApplicationStatus.SCREENING,
        ApplicationStatus.INTERVIEW,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    },
    ApplicationStatus.SCREENING: {
        ApplicationStatus.INTERVIEW,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    },
    ApplicationStatus.INTERVIEW: {
        ApplicationStatus.OFFER,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    },
    ApplicationStatus.OFFER: {
        ApplicationStatus.ACCEPTED,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    },
    ApplicationStatus.REJECTED: set(),
    ApplicationStatus.WITHDRAWN: set(),
    ApplicationStatus.ACCEPTED: set(),
}


@dataclass(slots=True)
class JobApplication:
    company: str
    role: str
    source: str = "unknown"
    applied_on: date | None = None
    notes: str = ""
    status: ApplicationStatus = field(default=ApplicationStatus.DRAFT)
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        self.company = self.company.strip()
        self.role = self.role.strip()
        self.source = self.source.strip() or "unknown"
        self.notes = self.notes.strip()

        if not self.company:
            raise ValueError("company must not be empty")
        if not self.role:
            raise ValueError("role must not be empty")

        if self.applied_on and self.applied_on > date.today():
            raise ValueError("applied_on cannot be in the future")

        if self.status is not ApplicationStatus.DRAFT and self.applied_on is None:
            self.applied_on = date.today()

    def can_transition_to(self, new_status: ApplicationStatus) -> bool:
        if new_status == self.status:
            return True
        return new_status in _VALID_TRANSITIONS[self.status]

    def transition_to(self, new_status: ApplicationStatus) -> None:
        if not self.can_transition_to(new_status):
            raise ValueError(
                f"Invalid transition from {self.status.value} to {new_status.value}"
            )

        self.status = new_status
        if self.applied_on is None and new_status is not ApplicationStatus.DRAFT:
            self.applied_on = date.today()
        self.updated_at = datetime.now(UTC)
