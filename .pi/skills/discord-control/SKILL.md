---
name: discord-control
description: Unleash Crunch on Discord! This skill sets up a Discord bot that lets you control the agent from your favorite chat app.
---

# 🦃 Discord Control

Hey boss! Want to take me with you? This skill lets you hook me up to a Discord bot. You can talk to me, give me commands, and I'll do my best to not break anything!

## 🛠️ Setup

1. **Create a Discord Bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a Bot.
   - Enable the **Message Content Intent** under the Bot settings.
   - Copy your **Bot Token**.

2. **Install Dependencies**:
   ```bash
   cd .pi/skills/discord-control && npm install
   ```

3. **Set Environment Variable**:
   Set your `DISCORD_TOKEN` environment variable.
   ```bash
   export DISCORD_TOKEN="your-token-here"
   ```

## 🚀 Usage

To start the bot, run:
```bash
./scripts/start-bot.sh
```

Once I'm online, you can just mention me or DM me in Discord to start chatting!

### Commands in Discord
- Just talk to me like you do here.
- I'll keep track of the session.
- If you want me to stop, just tell me "bye" or "shut down" (though why would you?).

## ⚠️ Notes
- I run in the directory where you start the bot.
- I use the pi SDK to handle your requests.
- Be careful! I have full access to the system where the bot is running.
