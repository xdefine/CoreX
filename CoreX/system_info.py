# system_info.py
import psutil

def get_system_info():
    return {
        "CPU usage (%)": psutil.cpu_percent(interval=1),
        "RAM usage (MB)": psutil.virtual_memory().used / 1024 / 1024,
        "Disk usage (%)": psutil.disk_usage('/').percent
    }
