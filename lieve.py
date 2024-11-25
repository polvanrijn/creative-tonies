from normalize import normalize_folder
from tonies import upload_folder, resolve_tonie_id
from youtube import download_urls

urls = [
    "https://www.youtube.com/watch?v=4g9b3iARhSg",  # Das rote Pferd
    "https://www.youtube.com/watch?v=2Pjg7h13z2U",  # Wo ist meine Mama?
    "https://www.youtube.com/watch?v=osQgeM6uFJg",  # wie macht der Hund
    "https://www.youtube.com/watch?v=JQDITBpR3ws",  # Wenn du fröhlich bist
    "https://www.youtube.com/watch?v=WjQhHvw1obU",  # So ein schöner Tag (Fliegerlied)
    "https://www.youtube.com/watch?v=XqZsoesa55w",  # Baby Shark Dance
    "https://www.youtube.com/watch?v=xHEv4y22S9I",  # Leo Lausemaus
    "https://www.youtube.com/watch?v=yhskyVfAAF4",  # Die Eule
    "https://www.youtube.com/watch?v=Kas5W8Bkhmk",  # Wer hat die Kokosnuss geklaut?
    "https://www.youtube.com/watch?v=0R7npHubMLA",  # Giraffenaffen Gang – Ich tanz‘ überall
    "https://www.youtube.com/watch?v=MtnnNsbn5gE",  # Feuerwehr Tatü Tata
    "https://www.youtube.com/watch?v=ZFEwlem_r2w",  # Polzeiboot
    "https://www.youtube.com/watch?v=CAMqE8MRkEU",  # Hoofd schouders knie en teen
    "https://www.youtube.com/watch?v=20J8DUJMgA4",  # Dans mee met Nijntje
    "https://www.youtube.com/watch?v=o2j-5rZLLpY",  # Kabouterdans
    "https://www.youtube.com/watch?v=65MpTMtZhKM",  # Zeven heksen
    "https://www.youtube.com/watch?v=qVSALcVpwkc",  # Nina Chuba - Wildberry
    "https://www.youtube.com/watch?v=ysgS4P4uHdo",  # GROSSSTADTGEFLÜSTER - FEIERABEND
    "https://www.youtube.com/watch?v=vmIJUaonHJw",  # Wir Sind Helden - Kaputt
    "https://www.youtube.com/watch?v=i6lvqj7IhBU",  # Dota - Rennrad
    "https://www.youtube.com/watch?v=hdcTmpvDO0I",  # I Like To Move It
    "https://www.youtube.com/watch?v=08-UYbfmFoY",  # Angst
    "https://www.youtube.com/watch?v=ZaI2IlHwmgQ",  # Pump it up
    "https://www.youtube.com/watch?v=ofMX3xnWU7o",  # Pipi langkous
    "https://www.youtube.com/watch?v=UhZwKNqDXwE",  # Querbeat - Nie mehr Fastelovend
    "https://www.youtube.com/watch?v=cS-lecxUKQU",  # Loss mer springe
    "https://www.youtube.com/watch?v=HBjDZMJUduo",  # Laserkraft 3D - Nein Mann
]

tonie_id = resolve_tonie_id("Github tonie Lieve")

output_dir = download_urls(urls, tonie_id)
normalize_folder(output_dir)

upload_folder(output_dir, tonie_id)