# diagnostics.py
from system_info import get_system_info
from proccess_monitor import list_processes

def run_diagnostics():
    return {
        "System": get_system_info(),
        "Running processes": list_processes()[:5],  # Exemple : les 5 premiers
    }
