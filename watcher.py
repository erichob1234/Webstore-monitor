import os
import re
import json
import random
import requests
import schedule
import time
from datetime import datetime, timezone 

#functions*********


webhookurl = "https://discord.com/api/webhooks/1391859279480229928/gjK1GuVNNtm0M7aud2GA7r_jB3FE683nMu-ED3kMLb2pf3MDi6Qd-13Af28CXt59T1Yl"
if not webhookurl:
    raise RuntimeError("Please set DISCORD_WEBHOOK_URL in your environment")

#function to choose random static proxy to use
proxies = ["http://7zuFZFbF:4RJgcH6L@207.246.206.98:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.97:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.96:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.95:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.94:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.93:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.92:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.91:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.90:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.9:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.89:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.88:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.87:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.86:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.85:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.84:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.82:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.81:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.80:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.8:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.79:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.78:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.77:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.76:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.75:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.74:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.73:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.72:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.71:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.70:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.69:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.68:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.67:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.66:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.65:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.64:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.62:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.61:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.60:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.59:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.58:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.57:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.55:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.54:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.53:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.52:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.51:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.50:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.49:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.48:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.47:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.46:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.45:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.44:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.43:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.41:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.40:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.39:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.37:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.35:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.34:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.33:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.31:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.216:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.215:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.214:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.213:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.212:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.211:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.210:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.209:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.208:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.207:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.206:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.205:8888",
    "http://7zuFZFbF:4RJgcH6L@207.246.206.204:8888"]
def get_proxy():
    if proxies and proxies[0]:
        p = random.choice(proxies)
        return {"http": p, "https": p}
    return None

#dict within list to store webpage urls
webpages = [
    {
        "name": "humidifier",
        "url": "http://thecpapstore.ca/products/airsense-10-elite-cpap-machine-with-humidair-heated-humidifier",
        "parser": "html",  # static‐HTML parsing
    },
    {"name": "Adidas Ultraboosts",
      "url": "https://www.adidas.ca/en/ultraboost-1.0-shoes/HQ4202.html",
      }
]

#name of file that will store json data for product characteristics
STATE_FILE = "last_state.json"

#function to get info from webpage
def get_html(url):
    response = requests.get(url, timeout=10, proxies=get_proxy())
    response.raise_for_status()#raise error if there is an error opening the webpage
    return response.text #returns string with information on the webpage

#function to check the attributes of interest
def check_price_and_stock(html):
    """
    - price: first occurrence of $X,XXX.XX
    - in_stock: False if keywords like "unavailable", "out of stock", "backordered" appear
    """
    #Price
    match = re.search(r"\$\s?[\d,]+\.\d{2}", html)
    price = match.group(0) if match else "n/a"

    #Stock status
    lc = html.lower()
    if "in stock" or "available"in lc:
        in_stock = True

    #Backordered check
    if "backordered" in lc:
        in_stock = "backordered"

    if "in stock" and "backordered" in lc:
        in_stock = "in stock but backordered"

    #Out of stock / unavailable check
    for kw in ("out of stock", "unavailable"):
        if kw in lc:
            in_stock = False
    else:
        in_stock = "unknown"

    return price, in_stock

#function to load the previous state of the webpage data if it exists
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}

#function to update previous webpage data
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# fucntion to send data to discord webhook api
def send_webhook(target, price, in_stock):
    
    embed = {
        "title": f"{target['name']} update",
        "url": target["url"],
        "color": 0x2ECC71,
        "fields": [
            {"name": "URL",       "value": target["url"],       "inline": False},
            {"name": "Price",     "value": price,                "inline": True},
            {"name": "In Stock?", "value": "Yes" if in_stock else "No", "inline": True},
        ],
    }
    payload = {
        "username": "Monitor",
        "embeds": [embed], 
    }
    r = requests.post(webhookurl, json=payload, timeout=5)
    r.raise_for_status()

#main

def check_all():
    state = load_state()
    for page in webpages:
        try:
            html = get_html(page["url"])
            price, in_stock = check_price_and_stock(html)
        except Exception as e:
            print(f"[{datetime.now()}] ERROR getting {page['url']}: {e}")
            continue

        last = state.get(page["url"], {})
        if last.get("price") != price or last.get("in_stock") != in_stock:  #logic for when to update
            # only send on first run or on change
            if last:
                send_webhook(page, price, in_stock)
                print(f"[{datetime.now()}] Change detected for {page['url']} → webhook sent")
            else:
                send_webhook(page, price, in_stock)
                print(f"[{datetime.now()}] First snapshot for {page['url']}: {price}, in_stock={in_stock}")

            state[page["url"]] = {"price": price, "in_stock": in_stock}

    save_state(state)

# Using functions*****************

# Run once immediately
check_all()

# Then every 2 minutes
schedule.every(2).minutes.do(check_all)

print("Watcher started: checking every 2 minutes…")
while True:
    schedule.run_pending()
    time.sleep(5)