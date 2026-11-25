import asyncio
import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler
from bot.handlers import menu_callback_handler, start_handler
from config.database import get_database

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("Falta configurar TELEGRAM_TOKEN en las variables de entorno.")

    # Verifica la conexión con MongoDB Atlas antes de arrancar el polling
    db = get_database()
    db.command("ping")
    logger.info("Conexión exitosa a MongoDB Atlas (%s).", db.name)

    # Python 3.14 no crea un event loop automáticamente en el hilo principal
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CallbackQueryHandler(menu_callback_handler))

    logger.info("Bot iniciado. Esperando mensajes...")
    app.run_polling()


if __name__ == "__main__":
    main()
