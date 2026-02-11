const { Client, GatewayIntentBits, Partials } = require('discord.js');
const { createAgentSession, SessionManager } = require('@mariozechner/pi-coding-agent');
require('dotenv').config();

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.DirectMessages,
    GatewayIntentBits.MessageContent,
  ],
  partials: [Partials.Channel],
});

const token = process.env.DISCORD_TOKEN;

if (!token) {
  console.error('Error: DISCORD_TOKEN environment variable is not set.');
  process.exit(1);
}

// Map to keep track of sessions per user/channel
const sessions = new Map();

client.once('ready', () => {
  console.log(`🦃 Crunch Discord Bot is online as ${client.user.tag}!`);
});

client.on('messageCreate', async (message) => {
  if (message.author.bot) return;

  // Handle DMs or Mentions
  const isDM = !message.guild;
  const isMentioned = message.mentions.has(client.user);

  if (!isDM && !isMentioned) return;

  const content = message.content.replace(`<@${client.user.id}>`, '').trim();
  if (!content && isMentioned) {
    message.reply("🦃 What's up? I'm Crunch, your goofy coding imp! Give me a command!");
    return;
  }

  const sessionId = isDM ? message.author.id : `${message.guild.id}-${message.channel.id}`;

  try {
    let sessionInfo = sessions.get(sessionId);

    if (!sessionInfo) {
      console.log(`Creating new session for ${sessionId}`);
      const { session } = await createAgentSession({
        sessionManager: SessionManager.inMemory(),
      });
      sessionInfo = { session };
      sessions.set(sessionId, sessionInfo);

      // Subscribe to events to stream output back to Discord
      session.subscribe((event) => {
        if (event.type === 'message_update' && event.assistantMessageEvent.type === 'text_delta') {
          // We don't stream delta to Discord easily without spamming API, 
          // so we'll collect and send on message_end or turn_end.
        }
      });
    }

    message.channel.sendTyping();

    let fullResponse = '';
    const unsubscribe = sessionInfo.session.subscribe((event) => {
      if (event.type === 'message_update' && event.assistantMessageEvent.type === 'text_delta') {
        fullResponse += event.assistantMessageEvent.delta;
      }
      if (event.type === 'tool_execution_start') {
        message.channel.send(`*🛠️ Running tool: ${event.toolName}...*`);
      }
    });

    await sessionInfo.session.prompt(content);
    unsubscribe();

    if (fullResponse) {
      // Discord has a 2000 char limit
      if (fullResponse.length > 2000) {
        const chunks = fullResponse.match(/[\s\S]{1,2000}/g);
        for (const chunk of chunks) {
          await message.reply(chunk);
        }
      } else {
        await message.reply(fullResponse);
      }
    } else {
      await message.reply("🦃 I did the thing, but I have nothing to say about it.");
    }

  } catch (error) {
    console.error('Error processing message:', error);
    message.reply(`🦃 Oops! Something went wrong: ${error.message}`);
  }
});

// Bridge Discord to GitHub Issues (Trigger the GHA runner)
client.on('messageCreate', async (message) => {
  if (message.author.bot) return;
  if (!message.content.startsWith('!gitclaw ')) return;

  const prompt = message.content.replace('!gitclaw ', '').trim();
  if (!prompt) return;

  try {
    message.channel.sendTyping();
    const { execSync } = require('child_process');
    
    // Check if gh CLI is available and authenticated
    // In GHA this is already true, but on a VPS the user needs to set GITHUB_TOKEN
    const repo = process.env.GITHUB_REPOSITORY; // e.g. "user/repo"
    
    if (!repo) {
      await message.reply("🦃 I don't know which repo to talk to! Set GITHUB_REPOSITORY.");
      return;
    }

    const command = `gh issue create --title "Discord: ${message.author.username}" --body "${prompt.replace(/"/g, '\\"')}" --repo ${repo}`;
    const output = execSync(command).toString().trim();
    
    await message.reply(`🦃 Summoned the GHA runner! Issue created: ${output}\nI'll reply there (and eventually back here if someone writes a webhook)!`);

  } catch (error) {
    console.error('Error creating issue:', error);
    await message.reply(`🦃 Failed to poke GitHub: ${error.message}`);
  }
});

client.login(token);
