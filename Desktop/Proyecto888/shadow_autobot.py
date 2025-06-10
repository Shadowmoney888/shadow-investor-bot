import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import random
import schedule
import time

TOKEN = 'TU_TOKEN_DEL_BOT'
CHANNEL_ID = '@NOMBRE_DEL_CANAL'  # o el ID numérico

bot = Bot(token=TOKEN)

def obtener_frase():
    url = "https://www.proyectoaprender.org/frases-para-reflexionar/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    frases = soup.find_all("li")
    lista_frases = [frase.get_text(strip=True) for frase in frases]
    return random.choice(lista_frases)

async def enviar_frase():
    phrase = obtener_frase()
    print("🟢 Bot autónomo ejecutándose...")
    await bot.send_message(chat_id=CHANNEL_ID, text=phrase, parse_mode='Markdown')
    print("✅ Frase enviada correctamente.")

def tarea_programada():
    asyncio.run(enviar_frase())

# Programa la tarea cada 1 minuto (puedes cambiar esto)
schedule.every(1).minutes.do(tarea_programada)

print("📡 Bot en espera...")

while True:
    schedule.run_pending()
    time.sleep(1)
