import requests

id_parameter = 1

response = requests.delete(f"https://api.restful-api.dev/objects/{id_parameter}")

print(response.status_code)
