import asyncio
import random
from telegram import Bot
from telegram.request import HTTPXRequest
from datetime import datetime

API_TOKEN = 'TU_TOKEN_DEL_BOT'
CHANNEL_ID = 'TU_CANAL_O_ID_PRIVADO'

# Frases para alternar
FRASES = [
    "📈 No pongas excusas, pon acciones. Tu futuro financiero depende de lo que hagas hoy.",
    "💸 Mientras otros duermen, tú inviertes. La sombra es tu aliada.",
    "🕵️‍♂️ El conocimiento es el arma más poderosa de un inversor silencioso.",
    "⏳ Cada minuto cuenta. Cada decisión suma.",
    "💰 En el mundo de las finanzas, el que observa en silencio gana primero."
]

# Inicializa el bot con timeout extendido
request = HTTPXRequest(connect_timeout=10.0, read_timeout=10.0)
bot = Bot(token=API_TOKEN, request=request)

async def send_phrase():
    phrase = random.choice(FRASES)
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=phrase)
        print("✅ Frase enviada correctamente.")
    except Exception as e:
        print(f"❌ Error enviando mensaje: {e}")

async def main_loop():
    print("🤖 Bot de prueba async ejecutándose cada minuto...")
    while True:
        print(f"⏰ Ejecutando tarea a las {datetime.now().time()}")
        await send_phrase()
        await asyncio.sleep(60)  # Espera 1 minuto

if __name__ == '__main__':
    asyncio.run(main_loop())