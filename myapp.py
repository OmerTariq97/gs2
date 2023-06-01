import requests
import json

URL='http://127.0.0.1:8000/StudentAPI/'



def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)

#get_data()


def post_data():
    data={
        'name':'test',
        'roll':200,
        'city':'newcity'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)

post_data()
