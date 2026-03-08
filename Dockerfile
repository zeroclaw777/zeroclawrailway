FROM ubuntu:24.04

# ============================================================================
# BASE DEPENDENCIES
# ============================================================================
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# ============================================================================
# INSTALL NIX PACKAGE MANAGER
# ============================================================================
# Install Nix using the official installer script
RUN curl -L https://nixos.org/nix/install | sh -s -- --daemon -- --no-daemonise -- --yes

# Add Nix to PATH
ENV PATH="/root/.nix-profile/bin:/nix/var/nix/profiles/default/bin:${PATH}"

# ============================================================================
# INSTALL PACKAGES VIA NIX
# ============================================================================
# Install development tools for the agent to use
# Packages: git, gh (GitHub CLI), nodejs, cargo (Rust), vim, neovim, htop, bun, fastfetch
RUN /root/.nix-profile/bin/nix-env -i nixpkgs.git gh nodejs cargo vim neovim htop bun fastfetch -A nixpkgs --run \
    && nix-collect-garbage -d \
    && rm -rf /root/.cache

# Verify installations
RUN git --version && gh --version && node --version && cargo --version

# ============================================================================
# INSTALL ZEROCLAW
# ============================================================================
ADD https://github.com/zeroclaw-labs/zeroclaw/releases/download/v0.1.7/zeroclaw-x86_64-unknown-linux-gnu.tar.gz /tmp/zeroclaw.tar.gz

RUN tar xzf /tmp/zeroclaw.tar.gz -C /usr/local/bin zeroclaw && \
    rm /tmp/zeroclaw.tar.gz && \
    chmod +x /usr/local/bin/zeroclaw

# ============================================================================
# ENTRYPOINT
# ============================================================================
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENV HOME=/zeroclaw-data

WORKDIR /zeroclaw-data

EXPOSE 42617

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["zeroclaw", "daemon"]
