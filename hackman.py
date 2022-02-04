import requests
import config

def getWord(parameters):
    response = requests.get("http://clemsonhackman.com/api/word", parameters)
    return response.json()["word"]

params = {
    "key": config.api_key,
    "length": 7
}
print(getWord(params))

 