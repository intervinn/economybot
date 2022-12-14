import disnake
import os
from disnake.ext import commands

class Bot(commands.InteractionBot):

    def __init__(self):
        super().__init__(
            intents=disnake.Intents(guilds=True, message_content=True, guild_messages=True, guild_reactions=True, members=True),
            command_sync_flags=commands.CommandSyncFlags(sync_commands_debug=True)
        )

    def load_commands(self):
        print("loading")
        for filename in os.listdir("src/bot/commands"):
            if filename.endswith(".py"):
                self.load_extension(f"bot.commands.{filename[:-3]}")