from pandas import DataFrame as pddataframe
from polars import DataFrame as pldataframe
from qatarcars._utils import (
    check_dataframe_types,
    return_read_function,
    check_import_package,
)
from qatarcars import get_qatar_cars
from qatarcars._errors import df_assert_error  # the custom assertion message

# --------------------------------------------------------------------------- #
#  Tests
# --------------------------------------------------------------------------- #
def test_check_dataframe_types_valid():
    """Normal mapping works for all accepted values (case‑insensitive)."""
    for raw, expected in [
        ("pandas", "pandas"),
        ("PD", "pandas"),
        ("pd", "pandas"),
        ("POLARS", "polars"),
        ("pl", "polars"),
    ]:
        assert check_dataframe_types(raw) == expected


def test_check_dataframe_types_invalid():
    """Anything else returns ``False``."""
    assert check_dataframe_types("unknown") is False
    assert check_dataframe_types("") is False

def test_check_pandas():
    test = get_qatar_cars()
    assert isinstance(test, pddataframe)
    assert test.shape == (89, 15)


def test_check_polars():
    test = get_qatar_cars("polars")
    assert isinstance(test, pldataframe)
    assert test.shape == (89, 15)

# --------------------------------------------------------------------------- #
#  End of file
# --------------------------------------------------------------------------- #