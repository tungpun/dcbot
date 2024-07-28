


# Clone the repo

```bash
git clone https://github.com/ssuuttt/dcbot.git 
cd dcbot
```


# Building the docker image
```bash
docker build -t dcbot-bot .
```

# Creating bot with token

Follow the guide at: https://discordpy.readthedocs.io/en/stable/discord.html

# Creating OpenAI API token

https://platform.openai.com/account/api-keys

# Make environment variable

The content of .env file look like:
```

DISCORD_BOT_TOKEN="MTA5OTk......"
OPENAPI_API_KEY="sk-a1......."

```

# Run the bot to create discord server 
```bash
docker run -v $(pwd):/app dcbot-bot                                                                                                                                                      
WARNING:discord.client:PyNaCl is not installed, voice will NOT be supported
INFO:root:Loaded command: blog
INFO:discord.client:logging in using static token
INFO:root:Attempting to create a new server...
INFO:root:Created new server: Discuss with LLM (ID: 1267065164390338660)
INFO:root:Created new channel: llm (ID: 1267065188981674025)
INFO:root:Invite link created: https://discord.gg/XnRYPR
Join the newly created server using this invite link: https://discord.gg/XnRYPR
After joining, please restart the bot.

```

Using the link above to join channel
After this command `.env` should have content with the channel id:
```
DISCORD_BOT_TOKEN="MTA5OTk......"
OPENAPI_API_KEY="sk-a1......."
DISCORD_CHANNEL_ID=1267065188981674
```

# Run the bot to begin using

```bash
docker run -v $(pwd):/app dcbot-bot
WARNING:discord.client:PyNaCl is not installed, voice will NOT be supported
INFO:root:Loaded command: blog
INFO:discord.client:logging in using static token
INFO:discord.gateway:Shard ID None has connected to Gateway (Session ID: 388b826d2805f2301f031c9d4e24b935).
INFO:root:Bot is ready as milito#2064

```

Now try to send `https://blog.ret2.io/2024/07/17/pwn2own-auto-2024-charx-bugs/` to the `llm` channel

It should look like:
![summary](pics/sum.png)


And when click on `technical step` button:

![steps](pics/steps.png)








