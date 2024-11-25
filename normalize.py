import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
from glob import glob


def normalize_loudness(audio_file, new_path, scale=0.3):
    rate = librosa.get_samplerate(audio_file)
    data, _ = librosa.load(audio_file, sr=rate)
    normalize_data = scale * data / max(abs(data))
    wavfile.write(new_path, int(rate), np.array(normalize_data * 32768, np.int16))

def normalize_folder(folder):
    for path in tqdm(glob(f"{folder}/*.mp3")):
        normalize_loudness(path, path)
