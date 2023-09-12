import discord
import os
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
    channel = client.get_channel(824163732518731779)
    print(channel)
    await tree.sync(guild=discord.Object(id=guildId))
    print("Ready!")
    async for message in channel.history():
        print(message.created_at)


client.run(os.getenv('token'))