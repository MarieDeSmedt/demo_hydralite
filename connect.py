
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

    #sector
    if len(st.session_state.mon_perimetre['sector']) >0:
        varlist=st.session_state.mon_perimetre['sector']
        var_string = ', '.join(varlist)        
        sector = 'AND sector IN (%s)' % var_string
    else:
        sector = ""
    st.write(sector)

    #typeTicket
    #     mon_perimetre['typeTicket'] 
    if len(st.session_state.mon_perimetre['typeTicket']) >0:
        varlist=st.session_state.mon_perimetre['typeTicket']
        var_string = (', '.join('"' + item + '"' for item in varlist))       
        typeTicket = 'AND typeTicket IN (%s)' % var_string
    else:
        typeTicket = ""
    st.write(typeTicket)

    #start
    if st.session_state.mon_perimetre['start'] != None:
        date=st.session_state.mon_perimetre['start']     
        start = 'AND day >= "%s"' % date
    else:
        start = ""
    st.write(start)

    #end
    if st.session_state.mon_perimetre['end'] != None:
        date=st.session_state.mon_perimetre['end']     
        end = 'AND day <= "%s"' % date
    else:
        end = ""
    st.write(end)

    #siteCluster
    if len(st.session_state.mon_perimetre['siteCluster']) >0:
        varlist=st.session_state.mon_perimetre['siteCluster']
        var_string = (', '.join('"' + item + '"' for item in varlist))       
        siteCluster = 'AND siteCluster IN (%s)' % var_string
    else:
        siteCluster = ""
    st.write(siteCluster)

    #brandType
    if len(st.session_state.mon_perimetre['brandType']) >0:
        varlist=st.session_state.mon_perimetre['brandType']
        var_string = (', '.join('"' + item + '"' for item in varlist))       
        brandType = 'AND brandType IN (%s)' % var_string
    else:
        brandType = ""
    st.write(brandType)

    #custAgeRange
    if len(st.session_state.mon_perimetre['custAgeRange']) >0:
        varlist=st.session_state.mon_perimetre['custAgeRange']
        var_string = (', '.join('"' + item + '"' for item in varlist))       
        custAgeRange = 'AND custAgeRange IN (%s)' % var_string
    else:
        custAgeRange = ""
    st.write(custAgeRange)

    #customerActivationEasinessLabel
    if len(st.session_state.mon_perimetre['customerActivationEasinessLabel']) >0:
        varlist=st.session_state.mon_perimetre['customerActivationEasinessLabel']
        var_string = (', '.join('"' + item + '"' for item in varlist))       
        customerActivationEasinessLabel = 'AND customerActivationEasinessLabel IN (%s)' % var_string
    else:
        customerActivationEasinessLabel = ""
    st.write(customerActivationEasinessLabel)


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
   

