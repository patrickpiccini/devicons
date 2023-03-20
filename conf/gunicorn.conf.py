# gunicorn.conf.py
bind = "localhost:8000"

accesslog = "/home/ubuntu/actions-runner/_work/devicons/deviconslogs/devicon.access.log"
errorlog = "/home/ubuntu/actions-runner/_work/devicons/devicons/logs/devicon.error.log"

capture_output = True
enable_stdio_inheritance = True
loglevel = "debug"

