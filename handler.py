import json
import requests

def post-one(event, context):
    r = requests.get("https://reqres.in/api/users")
    r_dict = r.json()
    #print(r_dict['data'][1]['first_name'])
    #print(r.text)
    count = 0
    inp = event
    num = int(inp)
    tim = 0
    names_l = {}
    list_of_names = []

    while (count < num ):
        fname = r_dict['data'][tim]['first_name']
        lname = r_dict['data'][tim]['last_name']
        fullname = fname+" "+lname
        names_l = {'fullname': fullname}
        list_of_names.append(names_l)
        tim = tim +1
        count = count +1
        
    
    
    #body = {
    #    "message": "Go Serverless v1.0! Your function executed successfully!",
    #    "input": event
    #}

    response = {
        "statusCode": 200,
        "response": list_of_names
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
 #   """
  #  return {
   #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #    "event": event
    #}
    #"""
