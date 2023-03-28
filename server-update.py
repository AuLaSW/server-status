"""
server-update.py
----------------

A python script for sending server updates through a discord webhook
"""
from discord import Embed, Color
from dotenv import load_dotenv
from os import getenv
import json
import requests

from utils import *


def main():

    load_dotenv()
    embed = Embed(
        title="Server Status",
        description="The current status of the server",
        timestamp=nowUTC(),
        color=Color.green(),
    ).to_dict()
    
    webhook = {
        "embeds": [embed],
    }
    
    print(webhook)
    
    r = requests.post(url=getenv("DISCORD_URL"), json=webhook)
    
    print(r)
    

if __name__ == "__main__":
    main()