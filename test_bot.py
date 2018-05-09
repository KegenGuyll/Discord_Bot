import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import requests
import urllib.parse
import random
import json

Client = discord.Client()
client = commands.Bot(command_prefix = "")

chat_filter = ["PINEAPPLE", "APPLE", "JELLO"]
bypass_list = ["250738639418556427"]
body_parts = ["head", "knee", "leg", "elbow","chin","face","nose","ear"]
insults = ["triangle","fat","short","long","stupid","slow","oblong"]
# Define data

@client.event
async def on_ready():
	print("Bot is ready!")

@client.event
async def on_message(message):
	global member_list
	
	contents = message.content.split(" ")
	for word in contents:
		if word.upper() in chat_filter:
			if not message.author.id in bypass_list:
				await client.delete_message(message)
				await client.send_message(message.channel, "**Hey you can't say that bucko!**")

	if message.content.upper().startswith('!PING'):
		print("!PING")
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	
	if message.content.upper().startswith('!SAY'):
		print("!SAY")
		if message.author.id == "250738639418556427":
			args = message.content.split(" ")
			# args[0] = "!SAY"
			# args[1] = message
			await client.send_message(message.channel,"%s" % (" ".join(args[1:])))
			print((" ".join(args[1:])))
		else:
			userID = message.author.id
			await client.send_message(message.channel,"<@%s> No" % (userID))

	if message.content.upper().startswith("!AMIADMIN"):
		print("!AMIADMIN")
		if "439614850361196554" in [role.id for role in message.author.roles]:
			userID = message.author.id
			await client.send_message(message.channel,"<@%s> Yes" % (userID))

		else:
			userID = message.author.id
			await client.send_message(message.channel,"<@%s> No" % (userID))
	if message.content.upper().startswith("!QUOTE"):
		import json
		print("!QUOTE")
		r = requests.get("https://talaikis.com/api/quotes/random/")
		quote = r.content
		j = json.loads(r.content)
		await client.send_message(message.channel,j['quote'] + " - " +  j['author'])

	if message.content.upper().startswith("!MEMESTARTER"):
		print("!MEMESTARTER")
		number = random.randint(1,101)
		main_api = "https://api.imgflip.com/get_memes"
		url = main_api
		print(url)

		json_data = requests.get(url).json()
		#print(json_data)

		json_success = json_data['success']
		if json_success == True:
			status = "Passed"

		else:
			status = "Failed"

		print('API success: ' + status)

		meme_url = json_data['data']['memes'][number]['url']
		print(meme_url)
		await client.send_message(message.channel,meme_url)

	if message.content.upper().startswith("!HELP"):
		print("!HELP")
		await client.send_message(message.channel,"https://docs.google.com/document/d/12MkEN0oJhJMNiCvr5X6eaUAU1ry2B10nml7s1O1kxPM/edit?usp=sharing")

	#if message.content.upper().startswith("!HEYYOU"):
	#	print("!HEYYOU")
	#	name = message.author.name
	#	content = random.choice(insults)
	#	URL = "http://webknox.com/api/jokes/insult?name=" + name + "&content=" + content + "&apiKey=bfcfcgfggjrykddbfoqqhdqxnqxzwmb"

	#	json_data = requests.get(url = URL).json()
	#	joke_content = json_data['text']

	#	await client.send_message(message.channel,joke_content)
	#	print(joke_content)

	if message.content.upper().startswith("!GUESS"):
		print("!GUESS")
		ran_number = random.randint(1,11)
		args = message.content.split(" ")
		print(ran_number)
		print((" ".join(args[1:])))

		if (" ".join(args[1:])) == ran_number:
			await client.send_message(message.channel,"Right!")
			await client.send_message(message.channel,"The number was " + str(ran_number))
		else:
			await client.send_message(message.channel,"Wrong!")
			await client.send_message(message.channel,"The number was " + str(ran_number))


	if message.content.upper().startswith("!DATA"):
		# -*- coding: utf-8 -*-
		import json

		# Make it work for Python 2+3 and with Unicode
		import io
		try:
		    to_unicode = unicode
		except NameError:
		    to_unicode = str

		data = {'member list': [{member.name for member in message.server.members}]}
		member_list = data
		# Write JSON file
		with io.open('data.json', 'w', encoding='utf8') as outfile:
		    str_ = json.dumps(data,
		                      indent=4, sort_keys=True,
		                      separators=(',', ': '), ensure_ascii=False)
		    outfile.write(to_unicode(str_))

		# Read JSON file
		with open('data.json') as data_file:
		    data_loaded = json.load(data_file)
		    print(data_loaded['member list'])
		   	
		print(data == data_loaded)

	if message.content.upper().startswith("!MEMLIST"):
		print("!MEMLIST")
		print(member_list)
		await client.send_message(message.channel,member_list['member list'][0:])

       		

	if message.content.upper().startswith("!READ"):
		with open('data.json') as data_file:
		    data_loaded = json.load(data_file)
		    print(data_loaded)    	

#Enter server-id here
client.run("NDM5NTk5MzgyMDExMzE0MTgx.DcViWw.-i4BuoYQDL61PLUays9oERxvkhQ")
