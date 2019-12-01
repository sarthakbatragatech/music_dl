import os
from pydub import AudioSegment
from pydub.playback import play
from tinytag import TinyTag

file = 'not_smart'
sound_path = 'data/sample/' + file + '.wav'

# Grab Metadata
tag = TinyTag.get(sound_path)
# Print to terminal
print(f'File Name: {file}')
print(f'Artist: {tag.artist}')
print(f'Duration: {round(tag.duration, 2)} seconds')
print(f'Bitrate: {round(tag.bitrate, 2)} kBits/s')   
print(f'Size: {round(tag.filesize/1024, 2)} kilobytes')
print(f'Sample Rate: {round(tag.samplerate, 2)}')
# print(tag.album) - For mp3 files
# print(tag.title)

sound = AudioSegment.from_wav(sound_path)
play(sound)
