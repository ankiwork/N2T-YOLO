import os
import json


settings_file = "project/configuration/yolo/data/launch_settings.json"

def check_settings():
    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            json.dump({"launch_denial": 0}, f, indent=4)

    with open(settings_file, "r") as f:
        settings = json.load(f)

    return settings.get("launch_denial")

def update_launch_settings():
    with open(settings_file, "r") as f:
        settings = json.load(f)
        if settings["launch_denial"] == 1:
            settings["launch_denial"] = 0
        else:
            settings["launch_denial"] = 1
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)

def cleanup():
    update_launch_settings()
