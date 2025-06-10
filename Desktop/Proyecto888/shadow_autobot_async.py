
import asyncio
import random
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import datetime

BOT_TOKEN = '7889975807:AAEI9-wBypSY30hPr1cRIKc14Kargmd6i-g'
CHANNEL_ID = '-1002777400942'

bot = Bot(token=BOT_TOKEN)

# Frases motivadoras
phrases = [
    "💡 Las oportunidades no llegan solas, se construyen.",
    "📈 Invierte en conocimiento. Es el activo que nunca falla.",
    "🧠 La paciencia es la mayor virtud del inversionista.",
    "💼 No pongas tu futuro en manos de la suerte. Fórmalo.",
    "🔍 La sombra es donde nace el pensamiento libre."
]

# Buscar una noticia destacada
async def fetch_news():
    try:
        url = 'https://es.finance.yahoo.com/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titulares = soup.select('h3')[:3]

        for h in titulares:
            text = h.get_text(strip=True)
            if len(text) > 30:
                await bot.send_message(chat_id=CHANNEL_ID, text=f"🗞️ Noticia destacada:
{text}")
                print("🗞️ Noticia enviada.")
                break
    except Exception as e:
        print(f"⚠️ Error al obtener noticia: {e}")

# Enviar frase aleatoria
async def send_phrase():
    phrase = random.choice(phrases)
    await bot.send_message(chat_id=CHANNEL_ID, text=phrase)
    print("✅ Frase motivadora enviada.")

# Tarea diaria combinada
async def daily_task():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"⏰ Ejecutando tarea diaria a las {now}")
    if random.choice([True, False]):
        await send_phrase()
    else:
        await fetch_news()

# Bucle principal
async def main_loop():
    print("🤖 Bot autónomo async ejecutándose...")
    while True:
        await daily_task()
        await asyncio.sleep(86400)  # espera 24 horas

if __name__ == '__main__':
    asyncio.run(main_loop())
