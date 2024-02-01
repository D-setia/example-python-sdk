import json
import requests

def addOne(number: int):
    return number + 1

def addTwo(number: int):
    return number + 2

def log_generic_event(ob):

    url = "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5"

    # headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': 'Bearer MpitrzBNNq9HOULxExSTeMOC5lO9F7jkfwnYT1oibbA'
    # }

    # payload = json.dumps({
    #     'teamId':'5b3dfd41-c759-498e-93a4-43066707e471',
    #     'projectId':'7c512bf9-76b0-47e1-97e0-71d617423c69',
    #     'datasourceId':'7a5806b8-2766-4ed2-9f66-e225d57238ad',
    #     'completionProperties':{
    #         'sourceText': ob['query'],
    #         'modelOneSummary': ob['response1'],
    #         'modelTwoSummary': ob['response2'],
    #         'thumbsUp': ob['human']
    #     }
    # })
    
    # response = requests.request('POST',url,headers=headers,data=payload, verify=False)
    response = requests.request('GET',url)
    return response
