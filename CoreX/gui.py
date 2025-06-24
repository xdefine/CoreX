# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from system_info import get_system_info
from file_cleaner import clean_temp_files
from net_utils import get_ip_info, ping_host
from password_generator import generate_password
from encryption import encrypt, decrypt
from proccess_monitor import list_processes
from diagnostics import run_diagnostics

def launch_app():
    root = tk.Tk()
    root.title("CoreX")
    root.geometry("700x700")

    output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    output.pack(pady=10)

    def show_output(data):
        output.delete('1.0', tk.END)
        if isinstance(data, dict):
            for k, v in data.items():
                output.insert(tk.END, f"{k}: {v}\n")
        elif isinstance(data, list):
            for item in data:
                output.insert(tk.END, f"{item}\n")
        else:
            output.insert(tk.END, str(data))

    def action_system_info():
        show_output(get_system_info())

    def action_clean_temp():
        show_output(clean_temp_files())

    def action_network_info():
        show_output(get_ip_info())

    def action_ping():
        host = "8.8.8.8"
        show_output(ping_host(host))

    def action_generate_password():
        pwd = generate_password()
        show_output(f"Mot de passe généré : {pwd}")

    def action_encrypt():
        msg = "Message secret"
        key = "cle123"
        enc = encrypt(msg, key)
        show_output(f"Chiffré : {enc}")

    def action_decrypt():
        msg = encrypt("Message secret", "cle123")
        dec = decrypt(msg, "cle123")
        show_output(f"Déchiffré : {dec}")

    def action_processes():
        show_output(list_processes())

    def action_diagnostics():
        show_output(run_diagnostics())

    # Boutons
    btns = [
        ("Analyse Système", action_system_info),
        ("Nettoyer Temp", action_clean_temp),
        ("Infos Réseau", action_network_info),
        ("Ping Google", action_ping),
        ("Générer MDP", action_generate_password),
        ("Chiffrer", action_encrypt),
        ("Déchiffrer", action_decrypt),
        ("Processus", action_processes),
        ("Diagnostic Complet", action_diagnostics),
    ]

    for label, cmd in btns:
        tk.Button(root, text=label, command=cmd, width=30).pack(pady=2)

    root.mainloop()
