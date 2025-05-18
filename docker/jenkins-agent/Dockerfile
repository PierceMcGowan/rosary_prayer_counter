# Use the official Jenkins inbound agent as the base image
FROM jenkins/inbound-agent:latest

# Switch to root to install tools
USER root

# Install dependencies and tools (e.g., Python, Rust, Git)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add Rust to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Verify installations
RUN python3 --version && pip3 --version && git --version && rustc --version

# Switch back to the Jenkins user
USER jenkins