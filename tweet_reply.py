import json,requests
def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling API...")


    res = json.loads(response.text)
    return res['content'] + " by " +"'" +res['author']+"'"


# s=get_quote()
# print(s)        