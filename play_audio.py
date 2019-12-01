import os
from pydub import AudioSegment
from pydub.playback import play

sound_path = 'data/sample/not_smart.wav'

sound = AudioSegment.from_wav(sound_path)
play(sound)
