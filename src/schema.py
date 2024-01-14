import pandas as pd
import pandera as pa
from pandera.engines.pandas_engine import PydanticModel
from pydantic import BaseModel


class Record(BaseModel):
    name: str
    xcoord: int
    ycoord: int


class DataFrameSchema(pa.DataFrameModel):
    """Pandera schema using the pydantic model."""

    class Config:
        """Config with dataframe-level data type."""

        dtype = PydanticModel(Record)
        coerce = True  # this is required, otherwise a SchemaInitError is raised
