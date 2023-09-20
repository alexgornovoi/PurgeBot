import discord
import os
import datetime
import time
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guildId = os.getenv("guildId")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guildId))
    print("Ready!")

        
@tree.command(name = "incogbot", description = "Test that incogbot is listening.", guild=discord.Object(id=guildId))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "clear", description = "Clears all messages sent after a certain amount of days", guild=discord.Object(id=guildId)) 
@app_commands.describe(days="Delete all messages from before x days ago")
@app_commands.rename(days='days')
async def clear(interaction, days:int):
    await interaction.response.send_message(f'Clearing {interaction.user}\'s messages. This may take a while...')
    
    def is_me(m):
        return m.author == interaction.user
    
    channel = client.get_channel(interaction.channel_id)
    last = datetime.datetime.utcnow()-datetime.timedelta(days)
    total = 0
    finished = False
    
    while not finished:
        messages = [message async for message in channel.history(limit=100,before=last)]
        if len(messages)!=100:
            finished = True
        deleted = await channel.purge(limit=100, check=is_me, before=last)
        total += len(deleted)
        time.sleep(5)
        last = messages[-1].created_at
        print(f'Deleted {total} messages')
        
    await channel.send(f'Deleted {total} message(s) from user {interaction.user}')

@tree.command(name = "clear_bot", description = "Clears all IncogBots messages.", guild=discord.Object(id=guildId)) 
async def clear_bot(interaction):
    await interaction.response.send_message("Clearing bot messages...")
    def is_incog(m):
        return m.author == client.user
    channel = client.get_channel(interaction.channel_id)
    deleted = await channel.purge(limit=100, check=is_incog)
    await channel.send(f'Deleted {len(deleted)} message(s) from user {client.user}')

    


client.run(os.getenv('token'))