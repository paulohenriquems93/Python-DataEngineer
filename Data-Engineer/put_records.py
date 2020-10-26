
#Python Library
import boto3
import jsonfrom fake_web_events import Simulation

client = boto3.client('kinesis')

def put_record(event):
    data = (json.dumps(event) + '\n').encode('UTF-8')
    response = client.put_record(
        StreamName='kinisis-stream',
        Data=data,
        Partitionkey-'test'
    )
    return response

simulation = Simulation(user_pool_size=200,sessions_per_day=10000)
events = simulation.run(duration_seconds=300)

for event in events:
    put_record(event)