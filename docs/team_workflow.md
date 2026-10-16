# Team Git workflow

## Managers

Mangesh Rajguru and Vaidehi coordinate repository settings, reviews, integration order, and releases. Neither should approve their own PR.

## Exploration phase

Each member creates their own `sandbox/<name>-prototype` branch and can prototype on both customer and order data. Keep experiments separate from production modules. Do not merge sandbox branches into `main`.

## Production phase

1. Sync `main`.
2. Create the assigned feature branch.
3. Implement a small vertical slice and tests.
4. Run lint/tests locally.
5. Push and open a PR to `main`.
6. Request review from someone other than the author.
7. Resolve comments and ensure CI passes.
8. A manager merges the PR after approval.
9. Sync `main` before beginning the next dependent component.

## Recommended branch protection

Once CI has run successfully and the check name is visible in GitHub settings:
- Require a pull request before merging to `main`.
- Require at least one approval from someone other than the author, if supported by the repository's plan/settings.
- Require the CI test status check.
- Dismiss stale approvals when new commits are pushed, if available.
- Restrict direct pushes to `main` where the available GitHub rules allow it.

Administrators may be able to bypass some rules depending on repository settings. Team policy should still prohibit direct commits to `main`.
