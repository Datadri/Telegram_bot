import os
import json
from datetime import datetime

def get_user_file(user_id):
    return os.path.join("data", f"{user_id}.json")

def load_user_data(user_id):
    user_dir = os.path.join("data", str(user_id))
    os.makedirs(user_dir, exist_ok=True)
    file_path = os.path.join(user_dir, "user.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {
            "user_id": user_id,
            "objetivos": [],
            "inicio": datetime.now().strftime("%Y-%m-%d"),
            "historial_mensajes": []
        }

def save_user_data(user_id, data):
    user_dir = os.path.join("data", str(user_id))
    file_path = os.path.join(user_dir, "user.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
