
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

    #define perimetre:---------------------------------------------------------------

    def create_string_variable(nameOfMultiSelect):
        if len(st.session_state.mon_perimetre[nameOfMultiSelect]) >0:
            varlist=st.session_state.mon_perimetre[nameOfMultiSelect]
            var_string = (', '.join('"' + item + '"' for item in varlist))       
            stringVariable = f'AND {nameOfMultiSelect} IN ({var_string})'
        else:
            stringVariable = ""
        return(stringVariable)

    sector = create_string_variable('sector')
    typeTicket = create_string_variable('typeTicket') 
    siteCluster = create_string_variable('siteCluster')
    brandType = create_string_variable('brandType')
    custAgeRange = create_string_variable('custAgeRange')
    customerActivationEasinessLabel = create_string_variable('customerActivationEasinessLabel')

    if st.session_state.mon_perimetre['start'] != None:
        date=st.session_state.mon_perimetre['start']     
        start = 'AND day <= "%s"' % date
    else:
        start = "" 

    if st.session_state.mon_perimetre['end'] != None:
        date=st.session_state.mon_perimetre['end']     
        end = 'AND day <= "%s"' % date
    else:
        end = "" 
       
    
    st.write(start)
    st.write(end)
    

    rows="test"
    # rows = run_query(f"""p
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
    #         {sector}
    #         {start}
    #         {end}
    #         {typeTicket}
    # ),

    # cust as (
    #     SELECT scope.*,
    #         customer.custNumberSid as custNumberSid ,
    #         customer.sumSalesAmountId as sumSalesAmountId, 
    #         customer.custAgeRange as custAgeRange, 
    #         customer.customerActivationEasinessLabel as customerActivationEasinessLabel
    #     FROM scope, unnest(customer) as customer    
    # )

    # SELECT 
    #     count(distinct custNumberSid ) as nbCust
    # FROM cust
    # WHERE 1=1
    #     {siteCluster}
    #     {brandType}
    #     {custAgeRange}
    #     {customerActivationEasinessLabel}
        
    # """)

    return rows
   

