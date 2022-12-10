import pandas as pd
from typing import cast


def merge_dataframe_chunks(dataframe_chunk) -> pd.DataFrame:
    # TODO: add doc strings
    dfs = list(dataframe_chunk)
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
