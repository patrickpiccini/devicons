# gunicorn.conf.py
bind = "localhost:8000"

accesslog = "/home/ubuntu/app/devicons/logs/devicon.access.log"
errorlog = "/home/ubuntu/app/devicons/logs/devicon.error.log"

capture_output = True
loglevel = "debug"


# COLOCAR DEBUG MODO TRUE PARA TESTAR
# https://docs.gunicorn.org/en/stable/settings.html#settings