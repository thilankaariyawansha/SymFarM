# Import requied libraries 

from influxdb_client import InfluxDBClient
import time 

class Machine:
    def __init__(self, user):
        self.user = user
    
    def machine_connect(self,url,token,org,bucket, command):
        client = InfluxDBClient(url=url, token=token)
        query_api = client.query_api()

        query = f'from(bucket:'+bucket +') |> range(start: -5s)'

        df = query_api.query_data_frame(query, org=org)

        try:
            dflen = len(df['host'] )
            print("Machine connected " )
            command=command
        except:
            print("Machine not connected....! Sensor connection" )
            
            