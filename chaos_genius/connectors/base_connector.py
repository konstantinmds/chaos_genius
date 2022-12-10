import pandas as pd
from sqlalchemy import create_engine
from .connector_utils import merge_dataframe_chunks 

def get_df_from_db_uri(db_uri, query):
    engine = create_engine(db_uri)
    return merge_dataframe_chunks(
        pd.read_sql_query(query, engine, chunksize=20000)
    )
