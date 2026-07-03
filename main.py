# Import library

import subprocess

# coba bikin perintahnya jadi gampang dulu

def jalanin(P):
    subprocess.run(P)

# Kasih menu dulu ges

print("1. Mode Personal 🎮")
print("2. Mode Office 💼")
print("3. Mode Public ☕")

# Suruh user milih

PilihanUser = input("Pilih opsi (1-3): ")
if PilihanUser == "1":
    a = ['whoami']

elif PilihanUser == "2":
    a = ['echo', 'ngetes', 'pilihan', 'kedua']

elif PilihanUser == "3":
    a = ['neofetch']

# eksekusi

jalanin(a)