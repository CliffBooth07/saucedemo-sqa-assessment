# SauceDemo SQA Assessment

This repository contains a focused Selenium + Python automation slice for the SauceDemo application, along with the assessment notes in [`docs/assessment.md`](docs/assessment.md).

Public repository: https://github.com/CliffBooth07/saucedemo-sqa-assessment

Final single-document report: [`SauceDemo-SQA-Assessment.pdf`](SauceDemo-SQA-Assessment.pdf)

Evidence is stored under [`artifacts/`](artifacts/), and the report links each file to its corresponding defect.

## Prerequisites

- Python 3.10+
- Google Chrome
- Internet access to `https://www.saucedemo.com/`

Selenium Manager downloads the compatible Chrome driver automatically in current Selenium versions.

## Setup and run

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
pytest -q
```

The test runs headlessly by default. To watch the browser:

```powershell
$env:HEADLESS="false"
pytest -q
```

On a failure, a screenshot is saved under `artifacts/` with the test name.

## Automation scope

The automated test covers the highest-value happy path: standard-user login, product selection, cart verification, checkout data entry, and order confirmation. It intentionally uses stable `id` and `data-test` selectors, page objects, explicit waits, and a fresh browser per test. It does not claim coverage of payment, API behavior, cross-browser behavior, accessibility, or performance.
