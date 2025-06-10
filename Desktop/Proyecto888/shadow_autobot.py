import requests
from bs4 import BeautifulSoup
import asyncio
import schedule
import time
from telegram import Bot

# Configuración del bot
TOKEN = TOKEN = "7889975807:AAEI9-wBypSY30hPr1cRIKc14Kargmd6i-g"
CHANNEL_ID = '@TU_CANAL'

bot = Bot(token=TOKEN)

def obtener_frase():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    frase = soup.select_one('.quote .text').text
    return frase

async def enviar_frase():
    phrase = obtener_frase()
    await bot.send_message(chat_id=CHANNEL_ID, text=phrase, parse_mode='Markdown')

def tarea_programada():
    asyncio.run(enviar_frase())

schedule.every(1).minutes.do(tarea_programada)

print("📡 Bot en espera...")

while True:
    schedule.run_pending()
    time.sleep(1)