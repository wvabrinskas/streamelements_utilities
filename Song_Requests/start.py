import data

def start(): 
    payload = data.payload(True)
    headers = data.headers()
    r = data.requests.put(data.url(), data=payload, headers=headers)

start()