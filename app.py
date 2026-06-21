import random
from flask import Flask, render_template_string
import os

app = Flask(__name__)

CASINO_SECRET_KEY = os.environ.get("CASINO_PASS", "Brak_Dostepu_Default")

STATUS_BARU = [
    "W normie",
    "Ostrzeżenie: Krytycznie niski poziom alkoholu",
    "Alarm: Ktoś zamówił wodę niegazowaną!"
]

STATUS_OCHRONY = [
    "Spokój",
    "Wykryto licznika kart przy stole do Blackjacka!",
    "Ktoś próbuje wynieść darmowy żeton o wartości 1$."
]


@app.route('/')
def index():
    # Emulate Data
    slot_machine_payout = round(random.uniform(70.0, 99.9), 2)
    bar_status = random.choice(STATUS_BARU)
    security_alerts = random.choice(STATUS_OCHRONY)

    html_template = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Casino IoT Dashboard</title>
        <style>
            body { background-color: #121212; color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding-top: 50px; }
            h1 { color: #ff007f; text-shadow: 0 0 10px #ff007f, 0 0 20px #ff007f; font-size: 3em; }
            h2 { color: #00ffff; text-shadow: 0 0 10px #00ffff; }
            .container { max-width: 600px; margin: 0 auto; background: #1a1a1a; padding: 20px; border-radius: 15px; border: 2px solid #ff007f; box-shadow: 0 0 15px rgba(255, 0, 127, 0.5); }
            .sensor { margin: 20px 0; padding: 15px; background: #262626; border-left: 5px solid #00ff00; text-align: left; border-radius: 5px; }
            .footer { margin-top: 30px; font-size: 0.8em; color: #888; }
            .version { color: #ffbc00; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Casino IoT System</h1>
            <h2>Panel Monitorowania Systemów Kasyna</h2>
            <hr style="border-color: #333;">

            <div class="sensor">
                <strong>Sensor Jednorękich Bandytów (Slot Machine #07):</strong><br>
                Aktualny zwrot dla kasyna (RTP): <span style="color: #00ff00; font-weight: bold;">{{ slot_machine_payout }}%</span>
            </div>

            <div class="sensor" style="border-left-color: #ffbc00;">
                <strong>Sensor Głównego Baru:</strong><br>
                Status: {{ bar_status }}
            </div>

            <div class="sensor" style="border-left-color: #ff0000;">
                <strong>System Detekcji Oszustw (AI-CCTV):</strong><br>
                Ostatni komunikat: {{ security_alerts }}
            </div>

            <div class="footer">
                System operuje w kontenerze Docker<br>
                <span class="version">Ver: 1.0</span>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template,
                                  slot_machine_payout=slot_machine_payout,
                                  bar_status=bar_status,
                                  security_alerts=security_alerts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)