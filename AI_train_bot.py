import os
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from memory import load_user_data, save_user_data
from core import mostrar_objetivos
from handlers import start, manejar_csv
from config import USER_ID_AUTORIZADO

# Cargar variables de entorno desde .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN environment variable.")

# Lógica de respuesta general
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if update.effective_user:
            user_id = update.effective_user.id
            if user_id not in USER_ID_AUTORIZADO:
                await update.message.reply_text("No estás autorizado para usar este bot.")
                return

        user_data = load_user_data(user_id)
        message = update.message.text.lower()
        user_data["historial_mensajes"].append(message)

        respuesta = ""

        if "objetivo" in message or "entrenar" in message or "maratón" in message:
            user_data["objetivos"].append("media maratón")
            respuesta = "📌 Objetivo 'media maratón' registrado."
        elif "peso" in message or "adelgazar" in message:
            user_data["objetivos"].append("perder peso")
            respuesta = "💡 Objetivo 'perder peso' registrado."
        else:
            respuesta = f"📬 Recibido: \"{update.message.text}\"\nTodavía no tengo una respuesta definida."

        save_user_data(user_id, user_data)

        await update.message.reply_text(respuesta)

def main():
    if not TOKEN:
        raise ValueError("TOKEN is required but not found.")
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler(["start", "hello"], start))
    application.add_handler(CommandHandler("objetivos", mostrar_objetivos))
    application.add_handler(MessageHandler(filters.Document.FileExtension("csv"), manejar_csv))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    application.run_polling()

if __name__ == '__main__':
    main()
