import discord
import os
# need token on .env file, might have to use repl.it to code bot

client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
  # prevents replying to self
  if message.author == client.user:
    return
  # replies to others
  if message.content.startswith(''):
    await message.channel.send('')
    
client.run(os.getnev('TOKEN'))
