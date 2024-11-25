import configparser
import logging
import os.path
from glob import glob

from tonie_api.api import TonieAPI
from tqdm import tqdm


def get_tonie_api():
    # set up detailed logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    parser = configparser.ConfigParser()
    parser.read(os.path.expanduser(os.path.join("~/", ".tonies")))
    credentials = {k: v for k, v in parser.items("user")}
    username = credentials["username"]
    password = credentials["password"]
    return TonieAPI(username, password)


def upload_folder(folder, tonie_id):
    api = get_tonie_api()
    output_dir = folder
    songs = {os.path.basename(f)[:-4]: f for f in glob(f"{output_dir}/*.mp3")}

    creative_tonies = api.get_all_creative_tonies()

    print(f"Found {len(creative_tonies)} creative tonies")

    tonies_mapping = {tonie.id: tonie.name for tonie in creative_tonies}

    assert tonie_id in tonies_mapping, f"Tonie with ID {tonie_id} not found"

    tonie = None
    for creative_tonie in creative_tonies:
        if creative_tonie.id == tonie_id:
            tonie = creative_tonie
            break
    assert tonie, f"Tonie with ID {tonie_id} not found"

    api.clear_all_chapter_of_tonie(tonie)

    for i, item in tqdm(enumerate(songs.items()), total=len(songs)):
        title, video_url = item
        file = f"{output_dir}/{title}.mp3"
        api.upload_file_to_tonie(tonie, file, title)
    print("Upload complete...")

def list_tonies():
    api = get_tonie_api()
    tonies = api.get_all_creative_tonies()
    for tonie in tonies:
        print(f"{tonie.id}: {tonie.name}")

def resolve_tonie_id(tonie_name):
    api = get_tonie_api()
    tonies = api.get_all_creative_tonies()
    for tonie in tonies:
        if tonie.name == tonie_name:
            return tonie.id
    return None

if __name__ == "__main__":
    list_tonies()