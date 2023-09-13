import discord
import os
import datetime
from dotenv import load_dotenv
from discord import app_commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guildId = os.getenv("guildId")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@tree.command(name = "hi", description = "My first application Command", guild=discord.Object(id=guildId)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guildId))
    print("Ready!")

@tree.command(name = "clear", description = "Clears all messages sent after a certain amount of days", guild=discord.Object(id=guildId)) 
@app_commands.describe(days="Delete all messages from before x days ago")
@app_commands.rename(days='days')
async def clear(interaction, days:int):
    def is_me(m):
        return m.author == interaction.user
    channel = client.get_channel(interaction.channel_id)
    deleted = await channel.purge(limit=100, check=is_me, before=datetime.datetime.utcnow()-datetime.timedelta(days))
    await channel.send(f'Deleted {len(deleted)} message(s) from user {interaction.user}')

@tree.command(name = "clear_bot", description = "Clears all bot messages", guild=discord.Object(id=guildId)) 
async def clear_bot(interaction):
    def is_incog(m):
        return m.author == client.user
    channel = client.get_channel(interaction.channel_id)
    deleted = await channel.purge(limit=1000, check=is_incog)
    await channel.send(f'Deleted {len(deleted)} message(s) from user {client.user}')

    


client.run(os.getenv('token'))