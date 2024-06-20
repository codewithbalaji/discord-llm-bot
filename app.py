import os
import discord
from discord.ext import commands
import ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the intents for the bot. This allows the bot to receive certain events.
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content

# Initialize the bot with a command prefix and the specified intents
bot = commands.Bot(command_prefix="/", intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")  # Print a message to the console when the bot is ready

# Function to split a message into chunks of specified length
def split_message(message, max_length=2000):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

# Define the hello command
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello, I'm a bot!")  # Send a message in the channel where the command was used

# Define the ask command
@bot.command(name="ask")
async def ask(ctx, *, message):
    async with ctx.typing():  # Simulate typing while processing the request
        try:
            # Make a request to the ollama API with the user's message
            response = ollama.chat(model='llama3', messages=[
                {
                    'role': 'system',
                    'content': 'You are a doctor expert in medical medcines'
                },
                {
                    'role': 'user',
                    'content': message,
                },
            ])
            content = response['message']['content']
            # Split the response if it exceeds the maximum length
            for chunk in split_message(content):
                await ctx.send(chunk)
        except Exception as e:
            # Send an error message if something goes wrong
            await ctx.send(f"An error occurred: {e}")



# Run the bot using the token from the .env file
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
