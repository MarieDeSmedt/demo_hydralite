
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import google.auth

def query():
   
    credentials, PROJET_EXEC = google.auth.default()

    client = bigquery.Client(credentials=credentials)
 
    # Perform query.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def run_query(query):
        query_job = client.query(query)
        rows_raw = query_job.result()
        # Convert to list of dicts. Required for st.cache to hash the return value.
        rows = [dict(row) for row in rows_raw]
        return rows

    #define perimetre

    #sector
    if len(st.session_state.mon_perimetre['sector']) >0:
        varlist=st.session_state.mon_perimetre['sector']
        var_string = ' '.join(varlist)
        
        sector = 'AND sector IN (%s);' % var_string
    else:
        sector = st.session_state['authorised_sectors']
    st.write(sector)


#     mon_perimetre["start"] 
#     mon_perimetre["end"]
#     mon_perimetre['siteCluster'] 
#     mon_perimetre['typeTicket'] 
#     mon_perimetre['brandType'] = st.sidebar.multiselect("MARQUE:",brandType)
#     mon_perimetre['custAgeRange'] = st.sidebar.multiselect("AGE:",custAgeRange
#     mon_perimetre['customerActivationEasinessLabel'] =    

    rows="test"
    # rows = run_query(f"""
    # with 
    # scope as (
    #     SELECT day,siteCluster, typeTicket, sector, sectorlabel,
    #         market, marketlabel, category, categorylabel,
    #         family, familylabel, brandType, 
    #         segmentation,SegmentValue, SegmentLabel, 
    #         sumSalesAmountId as sumSales,
    #         customer, 
    #     FROM `arf-marketing-cocktail-dev.UC_COCKTAIL_DATA.A_customerSegmentation_clusterCircuitMarque` 
    #     WHERE 1=1
    #         and sector in (?)
    #         --and day>="2021-12-01" mon_perimetre["start"]
    #         --and day<="2021-12-30"  mon_perimetre["end"] 
    #         --and typeTicket in ("HYPER") 

            
    # ),

    # cust as (
    #     select scope.*,
    #         customer.custNumberSid as custNumberSid ,
    #         customer.sumSalesAmountId as sumSalesAmountId, 
    #         customer.custAgeRange as custAgeRange, 
    #         customer.customerActivationEasinessLabel as customerActivationEasinessLabel
    #     from scope, unnest(customer) as customer    
    # )

    # select 
    #     count(distinct custNumberSid ) as nbCust
    # from cust

    # """)

    return rows
   

