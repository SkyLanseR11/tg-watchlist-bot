import requests
import time
import random

API_URL = "https://api.telegram.org/bot"
API_CATS_URL = "https://api.thecatapi.com/v1/images/search"
API_CAPIBARA_URL = "https://api.capy.lol/v1/capybara?json=true"
BOT_TOKEN = "7814264926:AAEXwf6En428uoBvi-fsX_vBC8b3ug7NS48"
TEXT = "Вот тебе милашная картинка ^_^"
ERROR_TEXT = "Здесь должна была быть картинка с милахой :("
MAX_COUNTER = 100
TIMEOUT = 3

counter = 0
offset = -2

while counter < MAX_COUNTER:
    print(f"Attempt = {counter}")

    updates = requests.get(
        f"{API_URL}{BOT_TOKEN}/getUpdates", params={"offset": (offset + 1)}
    ).json()

    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]

            if random.randint(0, 1) == 0:
                try:
                    cat_response = requests.get(API_CATS_URL, timeout=TIMEOUT)
                    if cat_response.status_code == 200:
                        cat_url = cat_response.json()[0]["url"]
                        requests.get(
                            f"{API_URL}{BOT_TOKEN}/sendPhoto",
                            params={
                                "chat_id": chat_id,
                                "photo": cat_url,
                                "caption": TEXT,
                            },
                        )
                    else:
                        requests.get(
                            f"{API_URL}{BOT_TOKEN}/sendMessage",
                            params={"chat_id": chat_id, "caption": ERROR_TEXT},
                        )
                except Exception as e:
                    requests.get(
                        f"{API_URL}{BOT_TOKEN}/sendMessage",
                        params={
                            "chat_id": chat_id,
                            "text": f"Ошибка с сервером картинок с котиками: {e}",
                        },
                    )

            else:
                try:
                    capibara_response = requests.get(API_CAPIBARA_URL, timeout=TIMEOUT)
                    if capibara_response.status_code == 200:
                        capibara_url = capibara_response.json()["data"]["url"]
                        requests.get(
                            f"{API_URL}{BOT_TOKEN}/sendPhoto",
                            params={
                                "chat_id": chat_id,
                                "photo": capibara_url,
                                "caption": TEXT,
                            },
                        )
                    else:
                        requests.get(
                            f"{API_URL}{BOT_TOKEN}/sendMessage",
                            params={"chat_id": chat_id, "text": ERROR_TEXT},
                        )

                except Exception as e:
                    requests.get(
                        f"{API_URL}{BOT_TOKEN}/sendMessage",
                        params={
                            "chat_id": chat_id,
                            "text": f"Ошибка с сервером картинок с капибарами: {e}",
                        },
                    )

    counter += 1
    time.sleep(1)
