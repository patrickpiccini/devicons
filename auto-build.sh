#! /bin/bash
sudo apt update -y
sudo apt install nginx -y
sudo apt install python3-pip -y
sudo apt install python3-venv  -y
alias python=python3 
alias pip=pip3 

cd ~
mkdir app

mkdir actions-runner && cd actions-runner

# ---- Git Action
curl -o actions-runner-linux-x64-2.303.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.303.0/actions-runner-linux-x64-2.303.0.tar.gz

echo "e4a9fb7269c1a156eb5d5369232d0cd62e06bec2fd2b321600e85ac914a9cc73  actions-runner-linux-x64-2.303.0.tar.gz" | shasum -a 256 -c

tar xzf ./actions-runner-linux-x64-2.303.0.tar.gz

./config.sh --url https://github.com/patrickpiccini/devicons --token AP246LF5NW4J72SLKTS24KTEC7DBO

sudo ./svc.sh install

sudo ./svc.sh start


# ----
