import subprocess
import os

try:
    print("Installing dependencies...")
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    print("Packages installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    exit()

try:
    print("Getting started RaidBot...")
    os.system("python RaidBot.py")
except Exception as e:
    print(f"Error executing the bot: {e}")
