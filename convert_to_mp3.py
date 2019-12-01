from os import path
from pydub import AudioSegment

file = 'bohemian'
src_path = 'data/sample/' + file + '.mp3'

dest_path = 'data/sample/' + file + '.wav'
                                                           
sound = AudioSegment.from_mp3(src_path)
sound.export(dest_path, format="wav")