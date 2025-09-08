# A program that allows bot to respond to my messages in a discord channel 

# Import and install required packages
import discord as dc
import requests
import json

"""
Function that fetches a random meme from the public meme API.
Returns the direct image URL of the meme.
"""
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

"""
Discord client class that handles different events (bot logging in, message sent in channel).
"""
class MyClient(dc.Client):
    # Event handler: Called when the bot successfully logs in
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    """
    Event handler: Listens for specific commands in messages and responds accordingly.
    Ignores messages sent by the bot itself to avoid loops.
    """
    async def on_message(self, message):
        # Ignores messages sent by bot itself
        if message.author == self.user:
            return
        
        # Responds to $hello command
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        # Responds to $meme command with random meme
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# Allow bot to read message content
intents = dc.Intents.default()
intents.message_content = True

# Initialises the client using own specific bot's token
client = MyClient(intents=intents)
client.run('YOUR_DISCORD_BOT_TOKEN') # replace with your own discord bot token 