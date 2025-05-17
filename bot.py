import requests
import time

API_URL = "https://api.telegram.org/bot"
BOT_TOKEN = "7814264926:AAEXwf6En428uoBvi-fsX_vBC8b3ug7NS48"
TEXT = "Сообщение получено"
MAX_COUNTER = 100

counter = 0
offset = -2

while counter < MAX_COUNTER:
    print(f"Attempt = {counter}")

    updates = requests.get(
        f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}"
    ).json()
    print(updates)

    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            requests.get(
                f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}"
            )

    time.sleep(1)

    counter += 1
