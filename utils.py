import datetime
import time

def is_user(user):
  def check(m):
    return m.author == user
  return check

async def clear(days, client, interaction, user):
    channel = client.get_channel(interaction.channel_id)
    last = datetime.datetime.utcnow()-datetime.timedelta(days)
    total = 0
    finished = False
    
    await interaction.response.send_message(f'Clearing {user}\'s messages. This may take a while...')
    
    while not finished:
        messages = [message async for message in channel.history(limit=100,before=last)]
        if len(messages)!=100:
            finished = True
        deleted = await channel.purge(limit=100, check=is_user(user), before=last)
        total += len(deleted)
        time.sleep(5)
        last = messages[-1].created_at
        print(f'Deleted {total} messages')
    
    await channel.send(f'Deleted {total} message(s) from user {user}')
    
async def clear_all(client, interaction):
    channel = client.get_channel(interaction.channel_id)
    last = datetime.datetime.utcnow()
    total = 0
    finished = False
    
    await interaction.response.send_message(f'Clearing all messages. This may take a while...')
    
    while not finished:
        messages = [message async for message in channel.history(limit=100,before=last)]
        if len(messages)!=100:
            finished = True
        deleted = await channel.purge(limit=100,  before=last)
        total += len(deleted)
        time.sleep(5)
        last = messages[-1].created_at
        print(f'Deleted {total} messages')
    
    await channel.send(f'Deleted {total} message(s) from channel.')