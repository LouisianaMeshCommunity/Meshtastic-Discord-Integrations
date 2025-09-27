import requests, time, datetime, os


API_URL = "https://meshview.louisianamesh.org/api/chat"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1421395763069587557/SKDp9gRUaX9c_l11cHSp9ESzlVZSTuLmQxh77UttijYg9AXHN1xOjN1l6xGh5QPGNgH_"

last_time = datetime.datetime.utcnow().isoformat()

while True:
    params = {"limit": "100"}
    if last_time:
        params["since"] = last_time

    try:
        resp = requests.get(API_URL, params=params, timeout=10)
        data = resp.json()

        for pkt in data.get("packets", []):
            msg = f"[{pkt['import_time']}] {pkt['long_name']} ({pkt['channel']}): {pkt['payload']}"
            requests.post(DISCORD_WEBHOOK, json={"content": msg})

        if "latest_import_time" in data:
            last_time = data["latest_import_time"]

    except Exception as e:
        print("Error:", e)

    time.sleep(3)
