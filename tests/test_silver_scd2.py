import pytest
from src.core.silver_scd2 import apply_scd2


def test_scd2_is_explicitly_unimplemented_in_starter():
    with pytest.raises(NotImplementedError):
        apply_scd2()
