from normalize import normalize_folder
from tonies import upload_folder, resolve_tonie_id
from youtube import download_playlist

playlist_id = "PL19BE8300C018E2A9"

tonie_id = resolve_tonie_id("Weihnachtsmann Jakob")

output_dir = download_playlist(playlist_id)

normalize_folder(output_dir)

upload_folder(output_dir, tonie_id)