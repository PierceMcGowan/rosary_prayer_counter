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

# Install GitHub CLI
run (type -p wget >/dev/null || (apt update && apt-get install wget -y)) \
	&& mkdir -p -m 755 /etc/apt/keyrings \
        && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        && cat $out | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& apt update \
	&& apt install gh -y

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add Rust to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Verify installations
RUN python3 --version && pip3 --version && git --version && rustc --version

# Install Wine and dependencies for Windows builds
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y wine64 wine32

# Download and install Windows Python (3.11) into Wine
RUN wget https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe -O /tmp/python311-installer.exe && \
    wine /tmp/python311-installer.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir=C:\\Python311 && \
    rm /tmp/python311-installer.exe

# Switch back to the Jenkins user
USER jenkins