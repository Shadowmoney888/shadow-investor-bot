import logging
import random
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.error import TelegramError
import schedule
import time

# Token del bot y canal
BOT_TOKEN = '7889975807:AAEI9-wBypSY30hPr1cRIKc14Kargmd6i-g'
CHANNEL_ID = '-1002777400942'

# Frases financieras
PHRASES = [
    "💼 *La riqueza no se grita. Se construye en silencio.*\n\n📌 Consejo del día: Diversifica tu dinero, pero nunca tu atención.",
    "💰 *El dinero ama el silencio.*\n\nInvierte en activos que generen ingresos mientras duermes.",
    "👤 *Los millonarios se hacen en las sombras, no en el escenario.*\n\nEstudia más de lo que posteas.",
    "📈 *El dinero inteligente observa, el dinero impulsivo reacciona.*\n\nSé paciente y constante.",
    "💸 *No trabajes por dinero. Haz que el dinero trabaje para ti.*"
]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)

def send_phrase():
    phrase = random.choice(PHRASES)
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=phrase, parse_mode='Markdown')
        print("✅ Frase enviada correctamente.")
    except TelegramError as e:
        print(f"❌ Error al enviar frase: {e}")

def fetch_news():
    try:
        url = 'https://es.finance.yahoo.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.select('h3')  # Titulares
        for h in headlines:
            text = h.get_text(strip=True)
            if 50 < len(text) < 150:
                bot.send_message(chat_id=CHANNEL_ID, text=f"📰 *Noticia destacada:*\n{text}", parse_mode='Markdown')
                print("✅ Noticia publicada.")
                break
    except Exception as e:
        print(f"❌ Error al obtener noticias: {e}")

# Alternar tareas cada minuto
def daily_post():
    if random.choice([True, False]):
        send_phrase()
    else:
        fetch_news()

schedule.every(1).minutes.do(daily_post)
daily_post()

print("🟢 Bot autónomo ejecutándose...")

while True:
    schedule.run_pending()
    time.sleep(10)

