#! /bin/bash
sudo apt update -y
sudo apt install nginx -y
sudo apt install python3-pip -y
sudo apt install python3-venv  -y
sudo apt install certbot -y
sudo apt install python3-certbot-nginx -y
alias python=python3 
alias pip=pip3 

# creating the app file
cd ~
mkdir app

mkdir actions-runner && cd actions-runner

# --- Git Actions

# ---

sudo ./svc.sh install

sudo ./svc.sh start

# Install Certificate SSL

sudo certbot --nginx

