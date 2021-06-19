import requests
import json

host_url = "https://jsonplaceholder.cypress.io/posts"

body = {
	"tittle" : "recommendation",
	"body" : "motorcycle",
	"userid" : 12
}


response = requests.post(host_url, data = body)

print(response)

response_result = (json.dumps(response.json(), indent=4))

print (response_result)

