- Subir uma instancia EC2 de acordo com o terraform do projeto.
- conectar na EC2.
    * Caso não instale as dependencias, fazer os seguintes comandos manualmente.


~~~ sh
sudo apt update -y
sudo apt install nginx -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt install certbot -y
sudo apt install python3-certbot-nginx -y
alias python=python3 
alias pip=pip3 

# creating the app file
cd ~
mkdir app
~~~

### Iniciar conexão com GitHub Actions

- Ir no GitHub > devicons > Settings > Actions > Runners > [New self-hosted runner]

- Na instancia, execute os comandos que p GitHub Runners mostrar
~~~ sh
# Exemplo:

mkdir actions-runner && cd actions-runner

curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

echo "29fc8cf2dab4c195bb147384e7e2c94cfd4d4022c793b346a6175435265aa278  actions-runner-linux-x64-2.311.0.tar.gz" | shasum -a 256 -c

tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

./config.sh --url https://github.com/patrickpiccini/devicons --token AP246LD4PKPNDSLXNUJMBETFJWNM2
~~~

- Usar mais os seguintes comandos para iniciar a comunicação entre GitHub e EC2:

~~~ sh
sudo ./svc.sh install
sudo ./svc.sh start
~~~

### Deploy Automático

- Vá em "Actions"
    - Clique primeira task
    - Botão Re-run all jobs (isso fará com que o a pipeline seja executada e crie os arquivos na instancia EC2)

### Configurar arqiovos NGINX

Dentro da instancia, ir até o diretório:

~~~ sh

cd /home/ubuntu/actions-runner/_work/devicons/devicons

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
sudo systemctl daemon-reload
sudo systemctl enable nginx
sudo systemctl start nginx
~~~

#### Configurar Certificado

Rodar a sequencia a seguir de comandos:

~~~ sh
sudo certbot --nginx

# colocar o emain

opção - Yes
opção -  No

# Escolher o dominio devicons
~~~


#### COnfiguração de Route 53

Vá até o Route 53 e crie um Zona hospedada.

Após a inicialização do serviço, deve-se criar os registros

- devicons.dev.br       - A - Simples - IP da EC2
- www.devicons.dev.br   - A - Simples - IP da EC2


# Esta pornto seu DEPLOY!