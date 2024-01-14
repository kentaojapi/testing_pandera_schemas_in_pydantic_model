import pandas as pd
from pandas.testing import assert_frame_equal
from pandera.errors import SchemaError
import pytest

from src.schema import DataFrameSchema


def test_valid_dataframe() -> None:
    df = pd.DataFrame({
        "name": ["zero", "one", "two"],
        "xcoord": [0, 1, 2],
        "ycoord": [3, 4, 5]
    })
    assert_frame_equal(DataFrameSchema(df), df)


@pytest.mark.parametrize(
    "df",
    [
        (  # case0: including invalid type data.
            pd.DataFrame({
                "name": ["zero", "one", "two"],
                "xcoord": ["dummy", "dummy", "dummy"],
                "ycoord": [0, 1, 2]
            })
        ),
        (  # case1: existing an unexpected column.
            pd.DataFrame({
                "name": ["zero", "one", "two"],
                "xcoord": ["dummy", "dummy", "dummy"],
                "ycoord": [0, 1, 2],
                "zcoord": [3, 4, 5]
            })
        ),
        (  # case2: lacking column.
            pd.DataFrame({
                "name": ["zero", "one", "two"],
                "xcoord": [0, 1, 2],
            })
        ),
    ]
)
def test_invaid_dataframe(df: pd.DataFrame) -> None:
    with pytest.raises(SchemaError):
        _ = DataFrameSchema(df)
