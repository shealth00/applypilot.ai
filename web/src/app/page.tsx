export default function Home() {
  return (
    <div className="flex min-h-full flex-col items-center justify-center bg-zinc-50 px-6 py-24 font-sans dark:bg-zinc-950">
      <main className="w-full max-w-lg text-center">
        <p className="text-sm font-medium uppercase tracking-wide text-zinc-500 dark:text-zinc-400">
          applypilot.ai
        </p>
        <h1 className="mt-4 text-3xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 sm:text-4xl">
          Application pilot
        </h1>
        <p className="mt-4 text-lg leading-relaxed text-zinc-600 dark:text-zinc-400">
          Next.js app scaffold. Extend routes and components under{" "}
          <code className="rounded bg-zinc-200/80 px-1.5 py-0.5 text-sm dark:bg-zinc-800">
            src/app
          </code>
          .
        </p>
      </main>
    </div>
  );
}
