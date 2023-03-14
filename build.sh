#! /bin/bash
sudo apt update
sudo apt install nginx -y
sudo apt install python3-pip -y
sudo apt install python3-venv  -y
alias python=python3 
alias pip=pip3 

# setting the git config
git config --global user.name "HML_Server"
git config --global user.email patrickbpiccini@hotmail.com

# creating the app file
cd ~
mkdir app
cd app/

# cloning the repository
git clone https://github.com/patrickpiccini/devicons.git

# running venv
python -m venv venv
source venv/bin/activate

# Install python packeges
cd devicons/
pip install -r requirements.txt

deactivate

# moving the devicon.service
sudo mv devicon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start devicon

# moving the devicon to config the proxy from nginx
sudo systemctl stop nginx
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

sudo mv devicon /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/devicon /etc/nginx/sites-enabled/
sudo systemctl enable nginx
sudo systemctl start nginx



## AINDA FALTA O STATICS FUNCIONAR!!!!!!!!!!!!!!!!
#https://medium.com/@prithvishetty/deploying-multiple-python-3-flask-apps-to-aws-using-nginx-d78e9477f96d
## verificar o traço no nomo do DEV-ICON

####https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
# https://wolfx.io/how-to-serve-static-and-media-files-in-nginx
# https://forum.djangoproject.com/t/configure-static-files-to-work-with-nginx/5689/6
# https://github.com/yeshwanthlm/YouTube/blob/main/flask-on-aws-ec2.md

#to test Gunicorn
# gunicorn --bind 127.0.0.1:5000 -w 2 app:app

# sudo vim /etc/nginx/sites-available/devicon
# sudo nginx -t


# sudo systemctl daemon-reload
# sudo systemctl start devicon
# sudo systemctl enable devicon
# sudo systemctl restart devicon
# sudo systemctl status devicon
# sudo systemctl stop devicon


# sudo systemctl start nginx
# sudo systemctl enable nginx
# sudo systemctl reload nginx
# sudo systemctl status nginx
# sudo systemctl stop nginx

sudo rm -rf /etc/nginx/sites-available/devicon
sudo rm -rf /etc/nginx/sites-enabled/devicon
sudo rm -rf /etc/systemd/system/devicon.service