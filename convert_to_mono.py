from pydub import AudioSegment

file = 'not_smart'
sound_path = 'data/sample/' + file + '.wav'

sound = AudioSegment.from_wav(sound_path)
sound = sound.set_channels(1)
sound.export(sound_path[:-4] + '_mono' + '.wav', format="wav")