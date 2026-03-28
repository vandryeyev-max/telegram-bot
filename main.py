from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/ping")
def ping():
    return {"status": "ok"}

def run_server():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_server).start()

    while True:
        print("Bot running...")
        time.sleep(10)
