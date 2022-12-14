import os
from .bot import Bot
from .db.session import users

def start():
    client = Bot()
    client.load_commands()
    print(os.getenv("TOKEN"))
    client.run(os.getenv("TOKEN"))
    