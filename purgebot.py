import discord
import os
from dotenv import load_dotenv
from discord import app_commands
import utils

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

        
@tree.command(name = "purgebot", description = "Test that PurgeBot is listening.", guild=discord.Object(id=guildId))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "clear", description = "Clears all messages sent after a certain amount of days", guild=discord.Object(id=guildId)) 
@app_commands.describe(days="Delete all messages from before x days ago")
@app_commands.rename(days='days')
async def clear(interaction, days:int):
    await utils.clear(days, client, interaction, interaction.user)

@tree.command(name = "clear_bot", description = "Clears all PurgeBots messages.", guild=discord.Object(id=guildId)) 
async def clear_bot(interaction):
    await utils.clear(0, client, interaction, client.user)
    
@tree.command(name = "clear_all", description = "Clears all messages from all users.", guild=discord.Object(id=guildId)) 
async def clear_bot(interaction):
    await utils.clear_all(client, interaction)

client.run(os.getenv('token'))