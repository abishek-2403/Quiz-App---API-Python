import requests


api_url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
