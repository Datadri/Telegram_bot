import os
import re
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# ID de los usuarios autorizados
USER_ID_AUTORIZADO_STR = os.getenv("USER_ID_AUTORIZADO")
if not USER_ID_AUTORIZADO_STR:
    raise ValueError("Missing USER_ID_AUTORIZADO environment variable. Please check your .env file.")

# Convertir a lista de enteros - maneja tanto formato "123,456" como "[123, 456]"
if USER_ID_AUTORIZADO_STR.strip().startswith('[') and USER_ID_AUTORIZADO_STR.strip().endswith(']'):
    # Si viene en formato [123, 456]
    numbers = re.findall(r'\d+', USER_ID_AUTORIZADO_STR)
    USER_ID_AUTORIZADO = [int(num) for num in numbers]
else:
    # Formato normal separado por comas
    USER_ID_AUTORIZADO = [int(id_str.strip()) for id_str in USER_ID_AUTORIZADO_STR.split(',') if id_str.strip()]