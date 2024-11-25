import os


def download_and_upload(playlist_id=None, urls=None, tonie_name=None, overwrite=False):
    from normalize import normalize_folder
    from tonies import upload_folder, resolve_tonie_id
    from youtube import download_playlist, download_urls
    tonie_id = resolve_tonie_id(tonie_name)
    assert tonie_id, f"Tonie with name {tonie_name} not found"
    output_dir = f"albums/{tonie_name}"
    if os.path.exists(output_dir):
        print(f"Folder {tonie_name} already exists. Please remove it first or set overwrite=True")
    else:
        if playlist_id:
            output_dir = download_playlist(playlist_id, tonie_name)
        elif urls:
            output_dir = download_urls(urls, tonie_name)
        else:
            raise ValueError("Either playlist or urls must be provided")
    normalize_folder(output_dir)
    upload_folder(output_dir, tonie_id)
    print(f"Finished {tonie_name}")