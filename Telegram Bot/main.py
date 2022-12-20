import requests
import telegram

parameters = {
    "district_id": "294",
    "date": "08-05-2021"
    }

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Accept-Language": "en-US"
}

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
response = requests.get(URL, params=parameters, headers=HEADERS)
print(response)

data = response.json()

centers_data = data["centers"]

message_data = []

for center in centers_data:
    sessions = center["sessions"]
    for session in sessions:
        if int(session["available_capacity"]) > 0:
            message = f"""
NAME: {center["name"]}
DATE: {session["date"]}
PIN CODE: {center["pincode"]}
MINIMUM AGE: {session["min_age_limit"]}
AVAILABLE CAPACITY: {session["available_capacity"]}
TIME SLOTS: {", ".join(session["slots"])}

"""
            message_data.append(message)


print(message)

TOKEN = ""


def send(msg, chat_id, token=TOKEN):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg)


for each_message in message_data:
    send(msg=each_message, chat_id=0)


