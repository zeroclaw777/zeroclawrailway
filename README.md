# ZeroClaw Railway Image

Custom Docker image for deploying ZeroClaw on Railway with Telegram channel support.

## Features

- Generates config from environment variables at runtime
- Supports **all ZeroClaw providers** via environment variables
- **Telegram channel** out of the box
- **Secure by default**: Gateway bound to localhost only, NOT exposed to internet
- No hardcoded secrets
- **Full autonomy mode** - autonomous execution within policy bounds
- Comprehensive development tools pre-installed

## Security Configuration

The gateway is **NOT exposed to the internet**:
- `host = "127.0.0.1"` - Gateway only accessible from localhost
- `require_pairing = true` - Even local access requires pairing
- `allow_public_bind = false` - Cannot bind to public interfaces

Only the **Telegram channel** can interact with the agent.

---

## Environment Variables

### Core Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_API_KEY` | Generic API key (fallback for all providers) | - |
| `ZEROCLAW_PROVIDER` | Default provider name | - |
| `ZEROCLAW_MODEL` | Default model name | - |
| `ZEROCLAW_TEMPERATURE` | Temperature (0.0-2.0) | `0.7` |
| `ZEROCLAW_WORKSPACE` | Workspace directory path | `/zeroclaw-data/.zeroclaw/workspace` |
| `ZEROCLAW_CONFIG_DIR` | Config directory path | - |

### Provider Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| `ZEROCLAW_PROVIDER` | Provider name | `openrouter`, `openai`, `anthropic`, `zai`, `ollama` |
| `ZEROCLAW_MODEL` | Model name | `openrouter/auto`, `gpt-4o`, `claude-sonnet-4` |
| `ZEROCLAW_MODEL_PROVIDER` | Alternative provider setting | `openrouter` |

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
| `GROQ_API_KEY` | Groq |
| `MISTRAL_API_KEY` | Mistral |
| `DEEPSEEK_API_KEY` | DeepSeek |
| `XAI_API_KEY` | X.AI / Grok |
| `TOGETHER_API_KEY` | Together AI |
| `FIREWORKS_API_KEY` | Fireworks AI |
| `PERPLEXITY_API_KEY` | Perplexity |
| `COHERE_API_KEY` | Cohere |

### Autonomy Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_AUTONOMY_LEVEL` | Autonomy level: `read_only`, `supervised`, `full` | `full` |
| `ZEROCLAW_WORKSPACE_ONLY` | Restrict filesystem to workspace only | `false` |
| `ZEROCLAW_BLOCK_HIGH_RISK` | Block high-risk commands | `false` |
| `ZEROCLAW_REQUIRE_PAIRING` | Require pairing for gateway access | `true` |
| `ZEROCLAW_ALLOW_PUBLIC_BIND` | Allow binding to 0.0.0.0 | `false` |

### Gateway Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_GATEWAY_PORT` | Gateway server port | `42617` |
| `ZEROCLAW_GATEWAY_HOST` | Gateway server host | `127.0.0.1` |
| `PORT` | Alternative port (Railway convention) | - |
| `HOST` | Alternative host (Railway convention) | - |

### Web Search Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_WEB_SEARCH_ENABLED` | Enable web search | - |
| `ZEROCLAW_WEB_SEARCH_PROVIDER` | Web search provider | - |
| `ZEROCLAW_BRAVE_API_KEY` | Brave Search API key | - |
| `ZEROCLAW_WEB_SEARCH_MAX_RESULTS` | Max search results (1-10) | - |
| `ZEROCLAW_WEB_SEARCH_TIMEOUT_SECS` | Search timeout in seconds | - |

### Skills Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_OPEN_SKILLS_ENABLED` | Enable open skills (`true`/`false`) | `false` |
| `ZEROCLAW_OPEN_SKILLS_DIR` | Open skills directory | - |
| `ZEROCLAW_SKILLS_PROMPT_MODE` | Skills prompt mode (`full`/`compact`) | `full` |

### Runtime Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `ZEROCLAW_REASONING_ENABLED` | Enable reasoning mode | - |

### Telegram Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | Yes (for Telegram) |
| `TELEGRAM_ALLOWED_USERS` | JSON array of allowed users | No (default: `["*"]`) |

### Git/GitHub Configuration

| Variable | Description |
|----------|-------------|
| `GITHUB_TOKEN` | GitHub personal access token for authenticated clone |
| `GH_TOKEN` | GitHub CLI token |
| `GIT_AUTHOR_NAME` | Git author name |
| `GIT_AUTHOR_EMAIL` | Git author email |
| `GIT_COMMITTER_NAME` | Git committer name |
| `GIT_COMMITTER_EMAIL` | Git committer email |

---

## Allowed Commands

The agent can execute these commands:

| Category | Commands |
|----------|----------|
| **Git & GitHub** | `git`, `gh` |
| **Node.js** | `npm`, `node`, `npx`, `yarn`, `pnpm` |
| **Rust** | `cargo`, `rustc`, `rustup`, `rustfmt` |
| **Python** | `python3`, `pip3`, `pip`, `black` |
| **HTTP Clients** | `curl`, `wget`, `http`, `https` |
| **Database Clients** | `psql`, `mysql`, `redis-cli`, `sqlite3` |
| **Cloud & Secrets** | `aws`, `vault` |
| **Code Quality** | `eslint`, `prettier` |
| **Data Processing** | `jq`, `yq` |
| **System** | `ls`, `cat`, `grep`, `find`, `echo`, `pwd`, `wc`, `head`, `tail`, `date` |
| **File Ops** | `mkdir`, `mv`, `cp`, `touch`, `rm` |
| **Editors** | `vim`, `nano` |
| **Process Management** | `htop`, `ps`, `kill` |

---

## Included Packages

| Package | Description |
|---------|-------------|
| `git` | Version control |
| `gh` | GitHub CLI |
| `nodejs` / `npm` | Node.js runtime |
| `cargo` / `rustup` | Rust toolchain |
| `python3` / `pip3` | Python runtime |
| `httpie` | HTTP client (better than curl) |
| `postgresql-client` | PostgreSQL client |
| `mysql-client` | MySQL client |
| `redis-tools` | Redis client |
| `sqlite3` | SQLite client |
| `aws-cli` | AWS CLI v2 |
| `vault` | HashiCorp Vault CLI |
| `jq` | JSON processor |
| `yq` | YAML processor |
| `eslint` | JavaScript linter |
| `prettier` | Code formatter |
| `black` | Python formatter |
| `vim` / `nano` | Text editors |
| `htop` | System monitor |

---

## Usage

### Railway

1. Create a new service from this image: `ghcr.io/your-org/zeroclawrailway:latest`
2. Set the required environment variables
3. Deploy

### Local

```bash
docker build -t zeroclaw-railway .
docker run \
  -e ZEROCLAW_PROVIDER=zai \
  -e ZAI_API_KEY=your-key \
  -e TELEGRAM_BOT_TOKEN=your-token \
  -e GITHUB_TOKEN=your-github-pat \
  zeroclaw-railway
```

---

## ZeroClaw Native Documentation

For complete documentation of all ZeroClaw environment variables and configuration options, see:

- **ZeroClaw Repository**: [github.com/zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)
- **Configuration Reference**: [docs/config-reference.md](https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/config-reference.md)
- **Commands Reference**: [docs/commands-reference.md](https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/commands-reference.md)
- **Providers Reference**: [docs/providers-reference.md](https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/providers-reference.md)
- **Troubleshooting**: [docs/troubleshooting.md](https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/troubleshooting.md)

---

## Image Source

Based on [ghcr.io/zeroclaw-labs/zeroclaw:latest](https://github.com/zeroclaw-labs/zeroclaw)
