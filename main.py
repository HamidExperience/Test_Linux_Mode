# Import library

import subprocess

# coba bikin perintahnya jadi gampang dulu

def jalanin(P):
    subprocess.run(P)

def menu():
    print("1. Mode Personal 🎮")
    print("2. Mode Office 💼")
    print("3. Mode Public ☕")

# Kasih menu dulu ges

menu()

# Suruh user milih

PilihanUser = input("Pilih opsi (1-3): ")
if PilihanUser == "1":
    a = ['xrandr', '--output', 'eDP-1', '--mode', '1400x1050']

elif PilihanUser == "2":
    a = ['xrandr', '--output', 'eDP-1', '--mode', '1680x1050']

elif PilihanUser == "3":
    a = ['xrandr', '--output', 'eDP-1', '--mode', '1920x1080']

# eksekusi

jalanin(a)