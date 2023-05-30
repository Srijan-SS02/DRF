import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

get_response=requests.get(endpoint) #HTTP request
print(get_response.text)  #print whatever the response is

print(get_response.status_code)

# print(get_response.json()['message'])

# print(get_response.status_code)

# JSON -> JavaScript Object Notion