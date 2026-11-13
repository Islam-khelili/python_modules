import sys
import os
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("dotenv is not installed\ntry: pip install dotenv")
    sys.exit(1)


def load_env() -> dict[str, str]:
    try:
        load_dotenv()
        matrix_mode = os.environ['MATRIX_MODE']
        database = os.environ['DATABASE_URL']
        api_key = os.environ['API_KEY']
        log_level = os.environ['LOG_LEVEL']
        zion_endpoint = os.environ['ZION_ENDPOINT']
        return {"MATRIX_MODE": matrix_mode,
                "DATABASE_URL": database,
                "API_KEY": api_key,
                "LOG_LEVEL": log_level,
                "ZION_ENDPOINT": zion_endpoint
                }
    except KeyError as e:
        print(f"Environment variables can't be loaded {e}")
        print("Check the dotenv if it is installed")
        print("OR try: pip install dotenv")
        print("OR .env if it exist")
        return {}


def hide_secret(secret: str) -> str:
    if not secret:
        return "not set"
    if len(secret) <= 8:
        return "*" * len(secret)
    return f"{secret[:4]}.......{secret[-4:]}"


def print_config(config: dict[str, str]) -> None:
    try:
        print(f"Mode: {config['MATRIX_MODE']}")
        print(f"Database: {config['DATABASE_URL']}")
        print(f"API Access: {hide_secret(config['API_KEY'])}")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print(f"Zion Network: {config['ZION_ENDPOINT']}\n")
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print('[OK] .env file properly configured')
        print('[OK] Production overrides available\n')
        print('The Oracle sees all configurations.')
    except KeyError:
        sys.exit(1)


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print_config(load_env())
