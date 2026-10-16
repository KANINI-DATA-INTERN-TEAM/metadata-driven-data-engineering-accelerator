# Metadata-Driven Data Engineering Accelerator

A team-built, metadata-driven Bronze–Silver data engineering framework. The initial MVP uses synthetic CSV/JSON inputs and targets Microsoft Fabric, while keeping storage/runtime boundaries explicit for future Azure compatibility.

## Team and ownership

| Member | Production ownership |
|---|---|
| Sakshi Dubey | `configs/`, `src/core/config_parser.py` |
| Krushna Palekar | `src/core/engine.py`, `src/adapters/` |
| Vaibhav Masal | `src/core/bronze_ingestion.py` |
| Vaidehi | `src/core/silver_quality.py`, `src/core/silver_scd2.py` |
| Mangesh Rajguru | `src/core/audit_logger.py`, `tests/` |

Mangesh and Vaidehi coordinate repository administration and review. They should still use pull requests for their own changes.

## Branch strategy

- `main`: reviewed, integrated production framework only.
- `sandbox/<name>-prototype`: individual experiments; do not merge these branches into `main`.
- `feature/<component>`: production implementation, merged through pull requests.

Planned production integration order:
1. `feature/metadata-config` — Sakshi
2. `feature/engine-adapters` — Krushna
3. `feature/bronze-ingestion` — Vaibhav
4. `feature/silver-scd2` — Vaidehi
5. `feature/audit-and-tests` — Mangesh

Agree on module interfaces and metadata contracts before parallel implementation. Integration order is a coordination plan, not a reason to block everyone from drafting tests and contracts early.

## Quick start

Requirements: Python 3.12 recommended, Git, and a virtual environment.

```bash
git clone https://github.com/YOUR-ORG/metadata-driven-accelerator.git
cd metadata-driven-accelerator

python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
```

The initial modules are scaffolding, not a completed Fabric/Delta implementation. Fabric-specific integration may require execution in an appropriately configured Fabric workspace. Do not put secrets in configuration files or commit credentials.

## Sample data

- `sample_data/batch_1/`: initial customer and order records.
- `sample_data/batch_2/`: a changed customer, a new customer, and incremental orders.

The data is synthetic and intended for local tests.

## Pull request workflow

1. Update your local `main`.
2. Create a feature branch.
3. Implement a small, focused change and add/update tests.
4. Run `pytest` and `ruff check .`.
5. Push the branch and open a PR into `main`.
6. Request review from the other manager or an appropriate component owner.
7. Merge only after review and required checks pass.
8. Delete the feature branch after merge if no longer needed.

Never approve your own PR. For high-impact contract changes, seek both managers' review when practical.

## Local prototype branches

Create your own branch after cloning:

```bash
git switch -c sandbox/mangesh-prototype
git push -u origin sandbox/mangesh-prototype
```

Replace `mangesh` with your own name. Do not push experimental work directly to `main`.

## Security and data policy

Use only synthetic or explicitly approved data. Confirm internship/company authorization before uploading project materials to a personal or organization GitHub account. Private repositories do not automatically grant permission to upload company-owned code or data.
