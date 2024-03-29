import discord
import datetime
import os

from get_menu import get_menu

#Version 1, for V1 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    today = str(datetime.date.today())
    channel = client.get_channel(975940259818930206)
    day_of_week = datetime.date.today().weekday()
    if day_of_week >= 5:
            await channel.send("No menu posted on weekends, come find out :smiling_imp: ")
            os._exit(0) # other exit/quit methods create an error message from asyncio
    menus = get_menu(today)
    msg = ""
    newline = "\n"
    msg += f"Dinner Menu for V1 on **{today}** {newline}"
    for item in menus[1]:
        msg += f"> {item} {newline}"
    await channel.send(msg)
    print(msg)
    os._exit(0) # other exit/quit methods create an error message from asyncio

if __name__ == "__main__":
    client.run(os.environ.get("CLIENT"))
