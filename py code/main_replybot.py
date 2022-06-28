import discord
import os
import requests
import json
import random
from replit import db
# need token on .env file, using repl.it

client = discord.Client()

said_words = ['example', 'other']
start_replies = ['example', 'reply']

if 'responding' not in db.keys():
	db['responding'] = True

# implement API
def get_quote():
  response = requests.get('url')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return quote
  
# user updates direct from discord
def update_replies(example_message):
	if "examples" in db.keys():
		examples = db['example']
		examples.append(example_message)
		db['examples'] = examples
	else:
		db['examples'] = [example_message]

# delete updates direct from discord
def delete_example(index):
	examples = db['examples']
	if len(examples) > index:
		del examples['index']
		db['examples'] = examples

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# command
@client.event
async def on_message(message):
	msg = message.content
	
  # prevents replying to self
  if message.author == client.user:
    return
	
  # replies to others
  if msg.startswith('example'):
    quote = get.quote
    await message.channel.send('quote')
		
		#
	if db['responding']:
		options = start_replies
		if 'examples' in db.keys():
			options = options + db['examples']

		# replies if word in message
		if any(word in msg for word in said_words):
			await message.channel.send(random.choice(options))
		
	# new replies, update from discord
	if msg.startswith('~new'):
		example_message = msg.split('~new', 1)[1]
		update_example
		await message.channel.send('New message added.')

	# delete message
	if msg.startswith('~del'):
		examples = []
		if 'examples' in db.keys():
			index = int(msg.split('~del', 1)[1])
			delete_example(index)
			examples = db['examples']
		await message.channel.send(examples)
	# prints current messages
	if msg.startswith('~list'):
		examples =[]
		if "examples" in db.keys():
			examples = db['examples']
		await message.channel.send(examples)
		
	if msg.startswith('~responding'):
		value = msg.split('~responding ', 1)[1]
		if value.lower() == 'true':
			db['responding'] = True
			await message.channel.send('Responding is on.')
		else:
			db['responding'] = False
			await message.channel.send('Responding is off.')
		
# links token
client.run(os.getnev('TOKEN'))
