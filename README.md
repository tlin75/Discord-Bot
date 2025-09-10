# 🤖 Simple Discord Bot

A lightweight Discord bot that responds to commands. Built with discord.py and the Meme API .

# 🚀 Getting Started

1. Install Dependencies
```
pip install discord.py requests
```

2. Get Your Bot Token
   - Go to Discord Developer Portal
   - Create a new application → Add a Bot → Copy the token

3. Run the Bot
   - Open bot.py, replace 'YOUR_DISCORD_BOT_TOKEN' with your actual token:
      ```
      client.run('MTA...your_token_here')
      ```
    - Then run program in terminal:
      ```
      python bot.py
      ```
      ✅ Bot will say “Logged on as [BotName]!” when ready.

# 🎮 How to Use
In any Discord channel where the bot is active:
- Type $hello → Bot says: Hello World!
- Type $meme → Bot ends a random meme from Reddit
