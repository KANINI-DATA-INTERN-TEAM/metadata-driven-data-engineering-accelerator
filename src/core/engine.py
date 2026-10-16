"""Pipeline coordinator scaffold.

Implementation owner: Krushna. Coordinate module contracts with all component owners.
"""


def run_pipeline(config: dict, adapter, batch_id: str):
    """Coordinate read -> Bronze -> Silver -> audit.

    TODO: finalize contracts with the team before wiring components together.
    """
    raise NotImplementedError("Pipeline orchestration contract is not implemented yet.")
