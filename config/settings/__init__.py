from os import environ
from dotenv import load_dotenv

load_dotenv()
stage = environ.get("STAGE")

if not stage:
    raise ValueError("STAGE is not set")

if stage == "PRODUCTION":
    from config.settings.production import *
else:
    from config.settings.dev import *
