#! /bin/bash
sudo apt update -y
sudo apt install nginx 
sudo apt install python3-pip -y
sudo apt install python3-venv -y

# setting the git config
sudo git config --global user.name "HML_Server"
sudo git config --global user.email patrickbpiccini@hotmail.com

# creating the virtual enviroment to aplication
cd ~
mkdir app
cd app/
python3 -m venv venv
source venv/bin/activate

# cloning the repository0
git clone https://github.com/patrickpiccini/devicons.git

cd devicons/
pip install -r requirements.txt

deactivate

#to test Gunicorn
# gunicorn --bind 0.0.0.0:8000 app:app

# moving the devicon.service
sudo mv devicon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start devicon

# moving the devicon to config the proxy from nginx

sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

sudo mv devicon /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/devicon /etc/nginx/sites-enabled/devicon
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl restart nginx


## AINDA FALTA O STATICS FUNCIONAR!!!!!!!!!!!!!!!!
## verificar o traço no nomo do DEV-ICON

####https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
# https://wolfx.io/how-to-serve-static-and-media-files-in-nginx
# https://forum.djangoproject.com/t/configure-static-files-to-work-with-nginx/5689/6
# https://github.com/yeshwanthlm/YouTube/blob/main/flask-on-aws-ec2.md


sudo vim /etc/nginx/sites-available/devicon
sudo nginx -t


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



gunicorn -b 0.0.0.0:8000 app:app 
