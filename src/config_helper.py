from pathlib import Path
from dotenv import dotenv_values

def get_db_config():
    """
    Centralized configuration helper.
    Locates the root .env file and builds the laptop-safe database configuration payload.
    """
    # Dynamically find the .env file relative to this helper file's folder directory
    SCRIPT_DIR = Path(__file__).resolve().parent
    env_path = SCRIPT_DIR / ".." / ".env"
    
    config = dotenv_values(env_path)
    
    # Enforce strict fallback checks to alert you immediately if your .env file is missing keys
    required_keys = ['DB_NAME', 'DB_USER', 'DB_PASSWORD']
    for key in required_keys:
        if key not in config or not config[key]:
            raise KeyError(f"Configuration Failure: '{key}' variable is missing from your .env file layout.")

    return {
        "dbname": config['DB_NAME'],
        "user": config['DB_USER'],
        "password": config['DB_PASSWORD'],
        "host": "localhost",
        "port": 5432
    }
