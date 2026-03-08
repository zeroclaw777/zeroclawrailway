# ZeroClaw Railway Image

Custom Docker image for deploying ZeroClaw on Railway with Telegram channel support.

## Features

- Generates config from environment variables at runtime
- Supports Telegram channel out of the box
- **Secure by default**: Gateway bound to localhost only, NOT exposed to internet
- No hardcoded secrets
- Includes development tools: git, Node.js, Rust/Cargo, vim, htop

## Security Configuration

The gateway is **NOT exposed to the internet**:
- `host = "127.0.0.1"` - Gateway only accessible from localhost
- `require_pairing = true` - Even local access requires pairing
- `allow_public_bind = false` - Cannot bind to public interfaces

Only the **Telegram channel** can interact with the agent. The HTTP gateway is localhost-only.

## Required Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ZAI_API_KEY` | ZAI API key | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | For Telegram |
| `ZEROCLAW_MODEL` | Model to use (default: glm-5) | No |
| `DEFAULT_PROVIDER` | Provider (default: zai) | No |
| `TELEGRAM_ALLOWED_USERS` | JSON array of allowed users (default: ["*"]) | No |

## Included Packages

The image includes these tools:
- `git` - Version control
- `nodejs` / `npm` - Node.js runtime
- `cargo` - Rust package manager (via rustup)
- `vim` - Text editor
- `htop` - System monitor

## Usage

### Railway

1. Create a new service from this image: `your-org/zeroclawrailway:latest`
2. Set the required environment variables
3. Deploy

### Local

```bash
docker build -t zeroclaw-railway .
docker run -e ZAI_API_KEY=your-key -e TELEGRAM_BOT_TOKEN=your-token zeroclaw-railway
```

## Image Source

Based on [ghcr.io/zeroclaw-labs/zeroclaw:latest](https://github.com/zeroclaw-labs/zeroclaw)
