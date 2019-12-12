from os import path
from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np

# Convert mp3 file to wav
def convert_to_wav(src_path): 
    print('Converting mp3 to wav...')
    print('')
    dest_path = src_path[:-4] + '.wav'                                                   
    sound = AudioSegment.from_mp3(src_path)
    sound.export(dest_path, format="wav")
    return dest_path

# Convert to single channel for spectrogram
def convert_to_mono(src_path):
    sample_rate, samples = wavfile.read(src_path)
    try:
        channels = np.shape(samples)[1]
        print('Converting to mono...')
        print('')
        dest_path = src_path[:-4] + '_mono' + '.wav'
        sound = AudioSegment.from_wav(src_path)
        sound = sound.set_channels(1)
        sound.export(dest_path, format="wav")
        return dest_path
    except IndexError:
        return src_path

# Preprocess Audio
def preprocess(sound_path):
    print('Commencing preprocessing...')
    print('')
    if sound_path[:-4] == '.mp3':
        sound_path = convert_to_wav(sound_path)
        sound_path = convert_to_mono(sound_path)
    else:
        sound_path = convert_to_mono(sound_path)
    print('Done preprocessing!')
    return sound_path