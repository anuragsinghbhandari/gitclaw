![gitclaw banner](banner.jpeg)

A personal AI assistant that runs entirely through GitHub Issues and Actions. Like [OpenClaw](https://github.com/openclaw/openclaw), but no servers or extra infrastructure.

Powered by the [pi coding agent](https://github.com/badlogic/pi-mono). Every issue becomes a chat thread with an AI agent. Conversation history is committed to git, giving the agent long-term memory across sessions. It can search prior context, edit or summarize past conversations, and all changes are versioned.

Since the agent can read and write files, you can build an evolving software project that updates itself as you open issues. Try asking it to set up a GitHub Pages site, then iterate on it issue by issue.

## 🦃 Crunch & Fun Stuff

This repo is home to **Crunch**, a quirky CI-dwelling turkey imp. Crunch maintains several "fun" features:

- **[Comic Studio](index.html)**: Auto-generated comics about repo life and chaotic PRs. Open `index.html` (or `viewer.html` directly) to see the latest masterpiece.
- **[The Hall of Weirdness](MUSEUM.md)**: A curated collection of the most bizarre, hacky, and "why?" code snippets found in this repository.
- **Crunchy CLI**: Run `bun crunchy` to generate a health report, a new comic, and hunt for weirdness.

## How it works

1. **Create an issue** → the agent processes your request and replies as a comment.
2. **Comment on the issue** → the agent resumes the same session with full prior context.
3. **Everything is committed** → sessions and changes are pushed to the repo after every turn.

The agent reacts with 👀 while working and removes it when done.

### Repo as storage

All state lives in the repo:

```
state/
  issues/
    1.json          # maps issue #1 -> its session file
  sessions/
    2026-02-04T..._abc123.jsonl    # full conversation for issue #1
```

Since sessions are in git, the agent can grep its own history and edit or summarize past conversations.

## Setup

1. **Fork this repo**
2. **Add your Anthropic API key** - go to **Settings → Secrets and variables → Actions** and create a secret named `ANTHROPIC_API_KEY`.
3. **Open an issue** - the agent starts automatically.
4. **Comment on the issue** - the agent resumes where it left off.

## Security

The workflow only responds to repository **owners, members, and collaborators**. Random users cannot trigger the agent on public repos.

If you plan to use gitclaw for anything private, **make the repo private**. Public repos mean your conversation history is visible to everyone, but get generous GitHub Actions usage.

## Configuration

Edit `.github/workflows/agent.yml` to customize:

- **Model:** Add `--provider` and `--model` flags to the `bunx pi` command.
- **Tools:** Restrict with `--tools read,grep,find,ls` for read-only analysis.
- **Thinking:** Add `--thinking high` for harder tasks.
- **Trigger:** Adjust the `on:` block to filter by labels, assignees, etc.

## Acknowledgments

Built on top of [pi-mono](https://github.com/badlogic/pi-mono) by [Mario Zechner](https://github.com/badlogic).

Thanks to [ymichael](https://github.com/ymichael) for nerdsniping me with the idea of an agent that runs in GitHub Actions.
