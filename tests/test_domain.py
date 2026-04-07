from datetime import date, timedelta

import pytest

from applypilot import ApplicationStatus, JobApplication


def test_application_requires_company_and_role() -> None:
    with pytest.raises(ValueError):
        JobApplication(company="", role="Software Engineer")

    with pytest.raises(ValueError):
        JobApplication(company="Acme", role=" ")


def test_application_rejects_applied_date_in_future() -> None:
    future_date = date.today() + timedelta(days=1)
    with pytest.raises(ValueError):
        JobApplication(company="Acme", role="Software Engineer", applied_on=future_date)


def test_valid_status_transitions() -> None:
    app = JobApplication(company="Acme", role="Software Engineer")
    assert app.status is ApplicationStatus.DRAFT

    app.transition_to(ApplicationStatus.APPLIED)
    app.transition_to(ApplicationStatus.INTERVIEW)
    app.transition_to(ApplicationStatus.OFFER)
    app.transition_to(ApplicationStatus.ACCEPTED)

    assert app.status is ApplicationStatus.ACCEPTED


def test_invalid_status_transitions_raise_error() -> None:
    app = JobApplication(company="Acme", role="Software Engineer")

    with pytest.raises(ValueError):
        app.transition_to(ApplicationStatus.REJECTED)

    app.transition_to(ApplicationStatus.APPLIED)
    app.transition_to(ApplicationStatus.REJECTED)

    with pytest.raises(ValueError):
        app.transition_to(ApplicationStatus.OFFER)


def test_notes_strip_whitespace() -> None:
    app = JobApplication(
        company="Acme",
        role="Engineer",
        notes="  reach out in 2 weeks  ",
    )
    assert app.notes == "reach out in 2 weeks"
