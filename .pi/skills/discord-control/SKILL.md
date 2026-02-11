---
name: discord-control
description: Unleash Crunch on Discord! This skill provides setup for controlling the agent via Discord. NOTE: Currently only works if running on a long-lived server.
---

# 🦃 Discord Control

Hey boss! I see you want to take me to Discord. 

**Wait a minute!** 🛑 I'm currently living in a GitHub Actions runner. I only wake up when you post an issue or a comment, and I go back to sleep as soon as I'm done. 

A Discord bot needs to stay awake 24/7 to respond to messages. If I start the bot here in this Action, it will die the moment the Action finishes.

### 🏗️ How to make this work:
1.  **Clone this repo** to a long-lived server (like a VPS, Raspberry Pi, or a computer that stays on).
2.  **Run the bot there.** That way, I'm always available on Discord!

## 🛠️ Setup (On your long-lived server)

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
- If you want me to stop, just tell me "bye" or "shut down".

## ⚠️ Notes
- I run in the directory where you start the bot.
- I use the pi SDK to handle your requests.
- Be careful! I have full access to the system where the bot is running.
