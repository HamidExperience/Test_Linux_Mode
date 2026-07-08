# Import library

import subprocess

# Ini variable, yang ada '🥰️' itu bisa kalian ubah sesuai kebutuhan kalian

# Variabel format-uri

uri = "file://"

# Ini lokasi Wallpaper 🥰️ tapi 'uri'nya jangan di hapus ya kalau memang tidak tau fungsinya
WallpaperPersonal = uri + "/home/hamid/Pictures/Wallpaper/warmmountain.jpg"
WallpaperOffice = uri + "/home/hamid/Pictures/Wallpaper/coldmountain.jpg"
WallpaperPublic = uri + "/home/hamid/Pictures/Wallpaper/linuxmintwallpaperdark.png"

# Ini untuk variable resolusi layar 🥰️
Rasio4banding3 = "1400x1050"
Rasio16banding10 = "1680x1050"
Rasio16banding9 = "1920x1080"


# Coba bikin perintahnya jadi gampang dulu

def jalanin(p):
    subprocess.run(p, check=True)

def UbahWallpaper(w):
    return ['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', w]

def UbahRasio(r):
    return ['xrandr', '--output', 'eDP-1', '--mode', r]

def ModePersonal():
    print("1. Old (Ratio Aspect 4:3)\n2. New (Ratio Aspect 16:9)")
    PilihanUser2 = input("Mau yang mana?: ")
    if PilihanUser2 == "1":
        jalanin(UbahRasio(Rasio4banding3))
        jalanin(UbahWallpaper(WallpaperPersonal))
    elif PilihanUser2 == "2":
        jalanin(UbahRasio(Rasio16banding9))
        jalanin(UbahWallpaper(WallpaperPersonal))
    else:
        print("Pilihan tidak valid!")

def ModeOffice():
    jalanin(UbahRasio(Rasio16banding10))
    jalanin(UbahWallpaper(WallpaperOffice))

def ModePublic():
    jalanin(UbahRasio(Rasio16banding9))
    jalanin(UbahWallpaper(WallpaperPublic))

def menu():
    print("1. Mode Personal 🎮")
    print("2. Mode Office 💼")
    print("3. Mode Public ☕")

# Kasih menu dulu ges

menu()

# Suruh user milih

PilihanUser = input("Pilih opsi (1-3): ")

# Eksekusi sesuai pilihan

if PilihanUser == "1":
    ModePersonal()

elif PilihanUser == "2":
    ModeOffice()

elif PilihanUser == "3":
    ModePublic()

else:
    print("\nPilihan tidak valid!\n")