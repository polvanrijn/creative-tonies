from typing import List

import yt_dlp
from tqdm import tqdm
import os.path

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'abort_on_unavailable_fragments': False,
    'ignoreerrors': True,
    'nocheckcertificate': True,
}

def _make_output_dir(folder: str):
    output_dir = f"albums/{folder}"
    if os.path.exists(output_dir):
        # remove existing folder
        import shutil
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def download_urls(urls: List, tonie_name: str):
    output_dir = _make_output_dir(tonie_name)
    for i, url in tqdm(enumerate(urls), total=len(urls)):
        video_info = yt_dlp.YoutubeDL().extract_info(
            url=url, download=False
        )

        number = str(i + 1).zfill(3)

        options = {
            **ydl_opts,
            'outtmpl': f'{output_dir}/{number}_%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    return output_dir

def download_playlist(playlist_id: str, tonie_name: str):
    output_dir = _make_output_dir(tonie_name)

    options = {
        **ydl_opts,
        'outtmpl': f'{output_dir}/%(playlist_index)03d_%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([f'https://www.youtube.com/playlist?list={playlist_id}'])

    return output_dir