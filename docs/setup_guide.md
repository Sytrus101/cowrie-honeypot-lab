# Cowrie Honeypot Setup Guide

## Hardware Requirements
- Raspberry Pi 5
- MicroSD card (16GB+)
- Network connection (WiFi or Ethernet)

## Software Requirements
- Kali Linux ARM (Raspberry Pi image)
- Python 3.x
- Git

## Installation Steps

### 1. Create Cowrie User
sudo adduser --disabled-password cowrie

### 2. Install Dependencies
sudo apt install git python3-virtualenv libssl-dev libffi-dev \
build-essential libpython3-dev python3-minimal authbind -y

### 3. Clone and Configure
sudo su - cowrie
git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv --python=python3 cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
cp etc/cowrie.cfg.dist etc/cowrie.cfg

### 4. Create Required Directories
mkdir -p var/run var/log/cowrie var/lib/cowrie/downloads

### 5. Start Cowrie
twistd --unmask=0022 --pidfile=var/run/cowrite.pid cowrie

###6. Veryify Running
ps aux | grep cowrie
tail -f var/log/cowrie/cowrie.json or cowrie.log

## Configuration Notes
- Cowrie listens on port 2222 by default
- Logs stored in var/log/cowrie/
- JSON logs compatible with Splunk/ELK ingestion
