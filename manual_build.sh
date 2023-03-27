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
cd app/

# cloning the repository
git clone https://github.com/patrickpiccini/devicons.git
# git clone -b hml https://github.com/patrickpiccini/devicons.git

# running venv
python -m venv venv
source venv/bin/activate

# Install python packeges
cd devicons/
pip install -r requirements.txt

deactivate

# moving the devicon.service
sudo mv conf/devicon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start devicon

# moving the devicon to config the proxy from nginx
sudo systemctl stop nginx
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

sudo mv conf/devicon /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/devicon /etc/nginx/sites-enabled/
sudo systemctl enable nginx
sudo systemctl start nginx

# install certified SSL
sudo certbot --nginx

sudo systemctl daemon-reload
sudo systemctl start devicon
sudo systemctl enable devicon
sudo systemctl restart devicon
sudo systemctl status devicon
sudo systemctl stop devicon


sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl reload nginx
sudo systemctl status nginx
sudo systemctl stop nginx


sudo tail -f /home/ubuntu/actions-runner/_work/devicons/devicons/logs/devicon.error.log
sudo tail -f /home/ubuntu/actions-runner/_work/devicons/devicons/home/ubuntu/app/devicons/logs/devicon.access.log