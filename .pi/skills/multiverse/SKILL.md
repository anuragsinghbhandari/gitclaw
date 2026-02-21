# Multiverse Skill

This skill allows Crunch to operate across multiple repositories, clone external codebases for analysis, and spawn new agent instances ("hatchlings").

## Tools

### `clone_and_analyze`
Clones a repository into a temporary directory and runs analysis tools on it.
- **Usage**: `scripts/clone_and_analyze.sh <repo_nwo> <analysis_command>`
- **Example**: `scripts/clone_and_analyze.sh "facebook/react" "ls -R"`

### `hatch_agent`
Creates a new repository from a template and sets it up as a new gitclaw agent.
- **Usage**: `scripts/hatch_agent.sh <new_repo_name> [template_repo]`
- **Note**: Requires `GH_PAT` with `repo` scope to create repositories and set secrets.

### `remote_issue`
Creates an issue in a different repository to communicate with other agents or track work.
- **Usage**: `scripts/remote_issue.sh <repo_nwo> <title> <body>`

## Setup
To fully utilize this skill (especially pushing changes or creating repos), ensure a Personal Access Token (PAT) is available in the environment as `GH_PAT`.
