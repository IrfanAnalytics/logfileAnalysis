from iics_login import iics_v2_login,iics_server_url
import pandas as pd

li= 'DTEMPLATE'



server_url, iics_v2_session_id, response_df = iics_v2_login("informaticaStagecloudagt@torchmarkcorp.com", "V@ig7)L9tk5qdbl")

    
server_url1="https://na1.dm-us.informaticacloud.com/saas/public/core/v3/objects?q=type=="+li
   

df = iics_server_url("GET",server_url1,iics_v2_session_id)   
    
#print(json_response1)
print(df)

