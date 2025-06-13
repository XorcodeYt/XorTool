import yt_dlp
import os
import sys
from tqdm import tqdm
import main

def get_download_folder():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    download_folder = os.path.join(parent_dir, 'downloads')
    os.makedirs(download_folder, exist_ok=True)
    return download_folder

progress_bar = None
last_bytes = 0

def my_hook(d):
    global progress_bar, last_bytes
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            if progress_bar is None:
                progress_bar = tqdm(total=total, unit='B', unit_scale=True, desc='Téléchargement', ncols=80)
                last_bytes = 0
            delta = downloaded - last_bytes
            progress_bar.update(delta)
            last_bytes = downloaded
    elif d['status'] == 'finished':
        if progress_bar is not None:
            progress_bar.n = progress_bar.total
            progress_bar.close()
            print("Téléchargement terminé !")
        progress_bar = None
        last_bytes = 0

def download_youtube(url, mode, ext, output_folder):
    ydl_opts = {
        'progress_hooks': [my_hook],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noprogress': True
    }
    if mode == 'video':
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': ext
        })
    elif mode == 'audio':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': ext,
                'preferredquality': '192',
            }]
        })
    else:
        print("Type inconnu.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def yt_dwn():
    url = input("Lien YouTube à télécharger : ").strip()
    print("Selectionne le format de téléchargement :")
    print("[1] Vidéo (mp4) || [2] Vidéo (webm)")
    print("[3] Audio (mp3) || [4] Audio (wav)")
    choice = input("Format : ").strip()

    if choice == '1':
        mode, ext = 'video', 'mp4'
    elif choice == '2':
        mode, ext = 'video', 'webm'
    elif choice == '3':
        mode, ext = 'audio', 'mp3'
    elif choice == '4':
        mode, ext = 'audio', 'wav'
    else:
        print("Choix non reconnu.")
        os.system("cls" if os.name == "nt" else "clear")
        yt_dwn()

    downloads_folder = get_download_folder()
    print(f"Le fichier sera téléchargé dans : {downloads_folder}")

    download_youtube(url, mode, ext, downloads_folder)
    input("Appuyez sur Entrée pour continuer...")  
    main.main()