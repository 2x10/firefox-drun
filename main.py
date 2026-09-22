import sys
import re as regex
import subprocess as cmd
from config import config

def get_profiles():
    file = open(f"{config["firefox_path"]}", "r")
    file_content = file.read()
    
    matched_names = regex.findall(r"\bName=.*", file_content)
    
    profiles = []
    for match in matched_names:
        profiles.append(match.split("=")[1])

    return "\n".join(profiles)

def open_profile(selected):
    cmd.Popen([config["firefox_bin"], "-P", selected])

def main():
    result = cmd.run(
        config["dmenu"].split(" "),
        input=get_profiles(),
        text=True, capture_output=True,
    )
    
    choice = result.stdout.strip()
    
    if choice:
        open_profile(choice)

main()


