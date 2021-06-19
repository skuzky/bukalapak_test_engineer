import requests
import json

host_url = "https://jsonplaceholder.cypress.io/posts"

response = requests.get(host_url)

print('the response for this GET request is : ')
print(response.status_code)
print(response.text) 

response_result = (json.dumps(response.json(), indent=4))
# print(response_result)