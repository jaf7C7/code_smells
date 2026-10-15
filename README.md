# Code smell exercises

Each directory here is a small, self-contained Python or JavaScript
project that exhibits **exactly one** code smell from
[`./smells.md`](./smells.md). Everything else in
it is meant to be clean. Your job:

1. **Identify** the smell -- by name, where it is, and why it qualifies.
2. **Reveal** the answer and compare.
3. **Refactor** the smell away, using the tests and `./check` as a
   safety net.

The directory names describe what the code is about, not the smell,
and are in no particular order.

## Layout of an exercise

```
<exercise>/
  *.py / *.js        production code
  test_*.py / *.test.js
  mutants/*.patch    each introduces one bug into the production code
  check              runs the tests against the real code and each mutant
  .answer            the answer, base64-encoded so you don't see it by accident
  requirements.txt + .venv/        (Python: its own pytest)
  package.json + node_modules/     (JavaScript: its own jest)
```

A couple of exercises are git repositories with a `TASK.md` describing
a change someone wants: for those, the history (`git log --stat`) and
the task are part of the evidence.

Sometimes the smell is in the tests rather than the production code.

## Running the tests

```sh
cd <exercise>
.venv/bin/python -m pytest      # Python
npx jest                        # JavaScript
```

## The check script

```sh
./check
```

runs the suite against the real code three times, then applies each
mutant in turn to a temporary copy and runs the suite against that.
It passes when the real code is green every time and every mutant
turns at least one test red ("killed"). In other words: it checks that
the tests catch the bugs they're supposed to catch.

Use it while refactoring:

- **If you're refactoring tests**, the production code stays put, so the
  mutants keep applying. If a mutant survives after your change,
  you've lost coverage while "cleaning up".
- **If you're refactoring production code**, mutants are patches
  against the *old* code, so once you've restructured it they'll be
  reported as "no longer applies (skipped)". That's expected; at that
  point the tests are your safety net.

`./check` should pass on an untouched exercise. If it doesn't, the
failure is part of the exercise, not a bug in it.

## Revealing the answer

```sh
base64 -d .answer
```

The answer gives the smell's name (and who named it), where it is,
why it qualifies, and refactorings that would remove it.
