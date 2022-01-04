
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import google.auth

# Create API client.
# credentials = service_account.Credentials.from_service_account_info(
#    st.secrets["gcp_service_account"]
# )


credentials, PROJET_EXEC = google.auth.default()

client = bigquery.Client(credentials=credentials)
# client = bigquery.Client()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT count(*) as nbDim FROM arf-marketing-cocktail-dev.CUBE.CUBE_DE_DIMENSIONS ")

# Print results.
st.write("Nombre de lignes arf-marketing-cocktail-dev.CUBE.CUBE_DE_DIMENSIONS :")
for row in rows:
    st.write("=> " + str(row['nbDim']))