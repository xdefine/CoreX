# net_utils.py
import socket
import subprocess
import requests

def get_ip_info():
    return {
        "Local IP": socket.gethostbyname(socket.gethostname()),
        "Public IP": requests.get("https://api.ipify.org").text
    }

def ping_host(host="8.8.8.8"):
    result = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE)
    return result.stdout.decode()
