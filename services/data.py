import requests
BASE_URL = "Your api url"
def get_data(message: str):
    response = requests.get(BASE_URL + f"?text={message}")
    status = response.json()["status"]
    data = response.json()["answer"]
    if status == "false":
        return "Xatolik yuz berdi"

    return data
