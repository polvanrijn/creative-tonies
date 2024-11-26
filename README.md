# Creative-Tonies downloader
## Kreativ-Tonies Downloader

Tonies are amazing toys for kids, but the interface to upload songs is pretty terrible.

### Description
This little script allows parents to:
- Upload a folder of songs to a Creative-Tonie (use zero-padding for numbering, e.g. `001-song1.mp3`)
- Download youtube playlists to a folder
- Download a list of youtube urls to a folder
- Normalize all audio such that the loudness of the songs is the same

### Installation
1. Install [ffmpeg](https://ffmpeg.org/download.html)
2. `pip install -r requirements.txt`

### Usage
- Put your Creative-Tonie on the Toniebox
- Go to https://my.tonies.com/creative-tonies
- Login or make an account if you haven't
- Click on the Creative-Tonie you want to upload songs to and rename the Tonie to an intuitive name, e.g. "My tonie"
- Create the file `.tonies` in your home directory (i.e. `~/.tonies`) with the following content:
```
[user]
USERNAME = <your_email>
PASSWORD = <your_password>
```

- Now you can use the low-level API to download and upload songs (this can be useful if you want to do some processing on the songs before uploading them, e.g. cropping the songs or adding a fade-in/fade-out effect):
```python
from normalize import normalize_folder
from tonies import upload_folder, resolve_tonie_id
from youtube import download_urls, download_playlist

urls = [
    "https://www.youtube.com/watch?v=4g9b3iARhSg",  # Das rote Pferd
]

tonie_id = resolve_tonie_id("My tonie")

output_dir = download_urls(urls, tonie_id)
# Or download a youtube playlist
# output_dir = download_playlist("https://www.youtube.com/playlist?list=PL8F4F9A1B2A4C3A3A", tonie_id)

# You can also upload an existing folder of songs

normalize_folder(output_dir)

upload_folder(output_dir, tonie_id)
```

- Or use the high-level API:
```python
from process import download_and_upload
download_and_upload(playlist_id="PLmR3bjwQNCDfW7DcheXqKe_99CbHBkkjt", tonie_name="My tonie")
```

- Finally, when all uploads are finished, you can sort the songs by alphabetical order (note, this will only work once the uploaded files are uploaded). By default, the songs are NOT sorted by the order they were uploaded in:
```python
from tonies import sort_all_tonies
sort_all_tonies()
```

### TODO
- [ ] Make a little pypi package

### Contributing
Feel free to open a PR if you want to contribute!

### License
MIT