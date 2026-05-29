# Security Policy

## Supported Versions

The project is pre-1.0. Security fixes will target the latest `main` branch until formal releases begin.

## Reporting A Vulnerability

Do not open a public GitHub issue for:

- PHI exposure
- de-identification bypasses
- unsafe DICOM metadata export
- dependency vulnerabilities with exploit details
- token or secret exposure

Instead, contact the maintainers privately. If no private channel is available yet, open a minimal issue saying that you need a private security contact without including sensitive details.

## PHI And Clinical Safety

Treat all generated outputs as potentially sensitive. The packet builder reduces PHI risk but does not guarantee complete anonymization.

Known risk areas:

- filenames
- free-text notes
- DICOM private tags
- burned-in pixel annotations
- photos
- PDF metadata and embedded text
- logs and markdown reports

## Maintainer Response

Maintainers should:

1. acknowledge reports promptly
2. reproduce the issue without requesting real PHI
3. patch and add tests
4. document the privacy or security impact
5. publish a fix before public disclosure when possible

