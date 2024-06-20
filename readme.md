# Discord Bot with Local LLM

This is a simple Discord bot that uses the `discord.py` library to interact with Discord and the `ollama` library for chat functionality.

## Features

- Responds with a greeting when the `/hello` command is used.
- Answers questions concisely using the `/ask` command.

## Prerequisites

- Python 3.7 or higher
- A Discord account and a bot token
- `pip` (Python package installer)

## Setup

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/codewithbalaji/discord-bot-local-llm.git
cd discord-bot-local-llm
```

### 2. Create and Activate a Virtual Environment

It's a good practice to use a virtual environment to manage your dependencies. You can create and activate one using:

```bash
# On Windows
python -m venv bot_env
bot_env\Scripts\activate

# On macOS/Linux
python3 -m venv bot_env
source bot_env/bin/activate
```

### 3. Install Dependencies

Install the required packages using:

```bash
pip install discord.py python-dotenv ollama
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of your project and add your Discord bot token:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
```

Replace `your_discord_bot_token` with your actual Discord bot token.

### 5. Run the Bot

You can start the bot by running the following command:

```bash
python app.py
```

You should see a message in the console indicating that the bot has logged in successfully.

## Usage

### Commands

- `/hello`: The bot will respond with a greeting.
- `/ask <question>`: The bot will answer your question concisely.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

