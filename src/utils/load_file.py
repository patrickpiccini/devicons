import os
from datetime import datetime
import shutil

def load_file_log():
    check_file_log = os.path.exists("../devicons/logs/devicon.log")

    if not check_file_log:
        with open(f"../devicons/logs/devicon.log", "w+") as log_file:
            log_file.write("----- Start system -----")
    else:
        today = datetime.now()
        shutil.copyfile("../devicons/logs/devicon.log", f"../devicons/logs/{today.strftime('%d%m%Y-%H%M%p')}.log")
        


