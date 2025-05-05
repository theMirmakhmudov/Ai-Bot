import requests
BASE_URL = "https://api.smtv.uz/ai/index.php"
def get_data(message: str):
    response = requests.get(BASE_URL + f"?text={message}")
    status = response.json()["status"]
    data = response.json()["answer"]
    if status == "false":
        return "Xatolik yuz berdi"

    return data
