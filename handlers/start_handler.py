from telegram import Update
from telegram.ext import ContextTypes
from config import USER_ID_AUTORIZADO

# Comando /start o /hello
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        if update.effective_user:
            user_id = update.effective_user.id
            username = update.effective_user.username or "Sin username"
            first_name = update.effective_user.first_name or "Sin nombre"
        
        if user_id not in USER_ID_AUTORIZADO:
            # Mostrar el ID del usuario para configuración
            await update.message.reply_text(
                f"🆔 Tu User ID es: {user_id}\n"
                f"👤 Usuario: @{username}\n"
                f"📝 Nombre: {first_name}\n\n"
                f"Copia este ID ({user_id}) y reemplaza el valor de USER_ID_AUTORIZADO en el código."
            )
        
        # Si ya está autorizado, mostrar el mensaje principal
        if user_id in USER_ID_AUTORIZADO:
            await update.message.reply_text(
                "👋 Hola, soy tu entrenador personal IA.\n"
                "Puedes decirme tus objetivos o mandarme tus entrenamientos exportados de Strava.\n"
                "Por ejemplo:\n- 'Quiero entrenar para una media maratón'\n"
                "- 'Mi objetivo es perder peso'\n"
                "- 'Te envío mi actividad de esta semana'\n"
                "Estoy escuchando..."
            )