"""
utils.py
--------
"""
from datetime import datetime, timezone


def nowUTC():
    """Returns the dateimte object for the moment the function is called in UTC"""
    return datetime.now(timezone.utc)
    

class ServerStatus:
    """
    ServerStatus
    ------------
    
    Holds different class methods for denoting server statuses.
    Returns a dictionary of a discord embed object.
    """
    def server_up(cls):
        return embed = Embed(
            title="Server Status 🟢",
            description="Server is good to go!",
            timestamp=nowUTC(),
            color=Color.green(),
        ).to_dict()

    def server_down(cls):
        return embed = Embed(
            title="Server Status 🔴",
            description="Server is down! :(",
            timestamp=nowUTC(),
            color=Color.red(),
        ).to_dict()

    def server_maintenance(cls):
        return embed = Embed(
            title="Server Status ⚠️",
            description="Server is down for maintenance and should be up soon.",
            timestamp=nowUTC(),
            color=Color.red(),
        ).to_dict()