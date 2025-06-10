
import asyncio
import random
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import datetime

BOT_TOKEN = '7889975807:AAEI9-wBypSY30hPr1cRIKc14Kargmd6i-g'
CHANNEL_ID = '-1002777400942'

bot = Bot(token=BOT_TOKEN)

phrases = [
    "💡 Las oportunidades no llegan solas, se construyen.",
    "📈 Invierte en conocimiento. Es el activo que nunca falla.",
    "🧠 La paciencia es la mayor virtud del inversionista.",
    "💼 No pongas tu futuro en manos de la suerte. Fórmalo.",
    "🔍 La sombra es donde nace el pensamiento libre."
]

async def fetch_news():
    try:
        url = 'https://es.finance.yahoo.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titulares = soup.select('h3')[:3]

        for h in titulares:
            text = h.get_text(strip=True)
            if len(text) > 30:
                await bot.send_message(chat_id=CHANNEL_ID, text=f"🗞️ Noticia destacada:\n{text}")
                print("🗞️ Noticia enviada.")
                break
    except Exception as e:
        print(f"⚠️ Error al obtener noticia: {e}")

async def send_phrase():
    phrase = random.choice(phrases)
    await bot.send_message(chat_id=CHANNEL_ID, text=phrase)
    print("✅ Frase motivadora enviada.")

async def daily_task():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"⏰ Ejecutando tarea a las {now}")
    if random.choice([True, False]):
        await send_phrase()
    else:
        await fetch_news()

async def main_loop():
    print("🤖 Bot de prueba async ejecutándose cada minuto...")
    while True:
        await daily_task()
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main_loop())
