def download_and_upload(playlist_id=None, urls=None, tonie_name=None):
    from normalize import normalize_folder
    from tonies import upload_folder, resolve_tonie_id
    from youtube import download_playlist, download_urls
    tonie_id = resolve_tonie_id(tonie_name)
    assert tonie_id, f"Tonie with name {tonie_name} not found"
    if playlist_id:
        output_dir = download_playlist(playlist_id)
    elif urls:
        output_dir = download_urls(urls, tonie_name)
    else:
        raise ValueError("Either playlist or urls must be provided")
    normalize_folder(output_dir)
    upload_folder(output_dir, tonie_id)