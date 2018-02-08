import data

def stop():
    payload = data.payload(False)
    headers = data.headers()
    r = data.requests.put(data.url(), data=payload, headers=headers)


stop()
