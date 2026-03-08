# ZeroClaw Railway Image

Custom Docker image for deploying ZeroClaw on Railway with Telegram channel support.

## Features

- Generates config from environment variables at runtime
- Supports **all ZeroClaw providers** via environment variables
- **Telegram channel** out of the box
- **Secure by default**: Gateway bound to localhost only, NOT exposed to internet
- No hardcoded secrets
- Includes development tools: git, Node.js, Rust/Cargo, vim, htop
- **Full autonomy mode** - autonomous execution within policy bounds

## Security Configuration

The gateway is **NOT exposed to the internet**:
- `host = "127.0.0.1"` - Gateway only accessible from localhost
- `require_pairing = true` - Even local access requires pairing
- `allow_public_bind = false` - Cannot bind to public interfaces

Only the **Telegram channel** can interact with the agent.

## Environment Variables

### Provider Configuration (All Providers Supported)

| Variable | Description | Example |
|----------|-------------|---------|
| `ZEROCLAW_API_KEY` | Generic API key (fallback for all providers) | `sk-...` |
| `ZEROCLAW_PROVIDER` | Provider name | `openrouter`, `openai`, `anthropic`, `zai`, `ollama` |
| `ZEROCLAW_MODEL` | Model name | `openrouter/auto`, `gpt-4o`, `claude-sonnet-4` |

### Provider-Specific API Keys

| Variable | Provider |
|----------|----------|
| `ZAI_API_KEY` | Z.AI |
| `OPENAI_API_KEY` | OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic |
| `OPENROUTER_API_KEY` | OpenRouter |
| `GEMINI_API_KEY` | Google Gemini |
| `GLM_API_KEY` | GLM / Zhipu |
| `OLLAMA_API_KEY` | Ollama (for remote) |

### Autonomy Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_AUTONOMY_LEVEL` | Autonomy level: `read_only`, `supervised`, `full` | `supervised` |
| `ZEROCLAW_WORKSPACE_ONLY` | Restrict to workspace only | `false` |
| `ZEROCLAW_BLOCK_HIGH_RISK` | Block high-risk commands | `false` |

### Telegram Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | Yes (for Telegram) |
| `TELEGRAM_ALLOWED_USERS` | JSON array of allowed users | No (default: `["*"]`) |

### Git Configuration

| Variable | Description |
|----------|-------------|
| `GITHUB_TOKEN` | GitHub personal access token for authenticated clone |
| `GH_TOKEN` | GitHub CLI token |

## Allowed Commands

The agent can execute these commands:
- **Git**: `git`, `gh`
- **Node.js**: `npm`, `node`, `npx`, `yarn`, `pnpm`
- **Rust**: `cargo`, `rustc`, `rustup`
- **Python**: `python3`, `pip3`, `pip`
- **System**: `ls`, `cat`, `grep`, `find`, `echo`, `pwd`, `wc`, `head`, `tail`, `date`
- **File ops**: `mkdir`, `mv`, `cp`, `touch`, `rm`
- **Network**: `curl`, `wget`
- **Editors**: `vim`, `nano`

## Included Packages

- `git` - Version control
- `nodejs` / `npm` - Node.js runtime
- `cargo` - Rust package manager (via rustup)
- `vim` - Text editor
- `htop` - System monitor

## Usage

### Railway

1. Create a new service from this image: `ghcr.io/your-org/zeroclawrailway:latest`
2. Set the required environment variables
3. Deploy

### Local

```bash
docker build -t zeroclaw-railway .
docker run \
  -e ZEROCLAW_PROVIDER=openrouter \
  -e ZEROCLAW_API_KEY=your-key \
  -e TELEGRAM_BOT_TOKEN=your-token \
  zeroclaw-railway
```

## Image Source

Based on [ghcr.io/zeroclaw-labs/zeroclaw:latest](https://github.com/zeroclaw-labs/zeroclaw)
