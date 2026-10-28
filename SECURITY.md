# Security Policy

## Supported versions

This project has no tagged release yet. Security fixes are made on the `main` branch.

## Reporting a vulnerability

**Please do not open a public issue, discussion or pull request for a security problem.**

Report it privately through GitHub: **Security → Advisories → "Report a vulnerability"** on this repository (<https://github.com/SigmaHQ/pySigma-plugin-directory/security/advisories/new>).
If you cannot use GitHub, open a public issue that says only that you have a security report and asks for a private contact. Do not include any details in that issue.

Please include:

- the affected directory entry and why you believe it is not controlled by the legitimate maintainers;
- the impact you see (see the scope below) and, if you have one, a proposed fix.

## What we treat as a vulnerability

This repository holds the directory that `sigma plugin` uses to discover and install pySigma backends, pipelines and validators. An entry here decides which package users install. The following are in scope:

- **Plugin supply chain:** a directory entry that points to a package, project or repository that is not controlled by the plugin's legitimate maintainers (for example a typo, an abandoned or re-registered package name, or a hijacked repository).
- **Directory tampering:** weaknesses in this repository's CI or review workflows that could let an outsider change the directory without maintainer review.
- **Tooling:** code in this repository (for example the directory check script) that can be made to execute code or access files when processing a crafted directory entry.

**Out of scope (report publicly as bugs):**

- Outdated descriptions, broken links or wrong compatibility ranges without a security impact.

Vulnerabilities inside a listed plugin belong in that plugin's repository. Problems in the plugin installation logic belong in [SigmaHQ/sigma-cli](https://github.com/SigmaHQ/sigma-cli) or [SigmaHQ/pySigma](https://github.com/SigmaHQ/pySigma).

## Our process

| Step                                                                          | Target                                        |
| ----------------------------------------------------------------------------- | --------------------------------------------- |
| Acknowledge the report                                                        | within 5 working days                         |
| Initial assessment and severity (CVSS 3.1)                                    | within 14 days                                |
| Fix developed in the advisory's temporary private fork                        | as soon as practical, normally within 90 days |
| Coordinated release, then GitHub Security Advisory published (CVE via GitHub) | at the fix release                            |

- We credit reporters in the advisory unless they ask not to be credited.
- When a fix affects other SigmaHQ projects, we may coordinate their releases.
- We ask reporters to keep details private until the advisory is published or 90 days have passed, whichever comes first, unless agreed otherwise.
