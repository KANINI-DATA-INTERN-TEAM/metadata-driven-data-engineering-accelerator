# Architecture and initial contracts

## Pipeline shape

Metadata config -> config validation -> source reader -> Bronze raw landing with lineage -> Silver casting/quality/quarantine -> append or SCD2 persistence -> audit.

## Contracts to agree before parallel implementation

1. Batch/run identifiers and source lineage fields.
2. Config schema, relative-path resolution, and environment-specific configuration.
3. Reader output type and error behavior.
4. Bronze technical columns and raw payload representation.
5. Silver accepted/rejected record shape and reject reason fields.
6. SCD2 column names, effective interval boundaries, current-row flag, version numbering, and change-detection rules.
7. Adapter method signatures and persistence semantics.
8. Audit status vocabulary and count reconciliation definitions.

## Suggested lineage fields

`batch_id`, `source_file`, `ingested_at_utc`, `table_name`, `run_id`.

## SCD2 acceptance criteria

- A changed tracked attribute closes the previous current row and creates exactly one new current version.
- Unchanged rows do not create new versions.
- Exactly one current version exists per business key after successful processing.
- Replaying an identical batch does not create duplicate history.
- Failed runs have clear audit status and error context.

## Platform boundary

Keep core logic independent from Fabric APIs. The Fabric adapter is the initial working platform target. The Azure adapter is a contract/extension point for the MVP unless deployment scope is separately approved.
