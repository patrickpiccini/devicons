import os
from datetime import datetime
import shutil

def load_file_log() -> object:
    check_file_log = os.path.exists("./logs/devicon.log")

    if not check_file_log:
        with open(f"./logs/devicon.log", "w+") as log_file:
            log_file.write("----- Start system -----")
    else:
        today = datetime.now()
        shutil.copyfile("./logs/devicon.log", f"./logs/{today.strftime('%d%m%Y-%H%M%p')}.log")