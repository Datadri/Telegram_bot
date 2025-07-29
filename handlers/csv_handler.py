import os
from telegram import Update
from telegram.ext import ContextTypes
from config import USER_ID_AUTORIZADO
import pandas as pd

async def manejar_csv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user:
        user_id = update.effective_user.id
    if user_id not in USER_ID_AUTORIZADO:
        if update.message:
            await update.message.reply_text("No estás autorizado para enviar archivos a este bot.")
        return
    if update.message:
        document = update.message.document
    if document:
        if document.mime_type != "text/csv":
            if update.message:
                await update.message.reply_text("El archivo enviado no parece ser un CSV válido.")
            return

    user_dir = os.path.join("data", str(user_id), "strava")
    os.makedirs(user_dir, exist_ok=True)
    file_path = os.path.join(user_dir, "actividades.csv")
    if document:
        file = await context.bot.get_file(document.file_id)
    await file.download_to_drive(file_path)
    if update.message:
        df = pd.read_csv(file_path)
        await update.message.reply_text(f"✅ Archivo CSV recibido correctamente y guardado como:\n`{file_path}`\n Actividades: {df.shape[0]}", parse_mode="Markdown")
