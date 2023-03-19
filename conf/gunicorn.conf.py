# gunicorn.conf.py
bind = "localhost:8000"

accesslog = "/home/ubuntu/app/devicons/logs/devicon.access.log"
errorlog = "/home/ubuntu/app/devicons/logs/devicon.error.log"

capture_output = True
enable_stdio_inheritance = True
loglevel = "debug"

