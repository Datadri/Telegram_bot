from telegram import Update
from telegram.ext import ContextTypes
from memory import load_user_data
from config import USER_ID_AUTORIZADO

async def mostrar_objetivos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user:
        user_id = update.effective_user.id

    if user_id not in USER_ID_AUTORIZADO:
        if update.message:
            await update.message.reply_text("No estás autorizado para usar este bot.")
        return

    user_data = load_user_data(user_id)
    objetivos = user_data.get("objetivos", [])

    if objetivos:
        objetivos_unicos = list(set(objetivos))  # Elimina duplicados
        objetivos_formateados = "\n".join(f"• {o.capitalize()}" for o in objetivos_unicos)
        if update.message:
            await update.message.reply_text(
            f"🎯 Tus objetivos actuales son:\n\n{objetivos_formateados}"
        )
    else:
        if update.message:
            await update.message.reply_text("⚠️ No tienes ningún objetivo registrado todavía.")
