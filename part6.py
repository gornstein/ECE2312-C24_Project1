import numpy as np
import soundfile as sf

# Ear distance in meters
ear_distance = 0.1854

audio, fs = sf.read("quickfox.wav")
print(audio.shape)

def delay_audio(audio,delay_samples):
    delayed_audio = np.zeros_like(audio)
    # Delay audio
    delayed_audio[delay_samples:] = audio[:-delay_samples]
    # Concat and transpose
    stereo_delayed = np.asarray([audio,delayed_audio]).T
    return stereo_delayed

sf.write("teamOrnstein-stereosoundfile-0ms.wav",audio,fs)

audio_avghead = delay_audio(audio,int(ear_distance / 343 * fs))
sf.write("teamOrnstein-stereosoundfile-avghead.wav", audio_avghead,fs)

audio_1ms = delay_audio(audio,int(fs * 0.001))
sf.write("teamOrnstein-stereosoundfile-1ms.wav",audio_1ms,fs)

audio_10ms = delay_audio(audio,int(fs * 0.01))
sf.write("teamOrnstein-stereosoundfile-10ms.wav",audio_10ms,fs)

audio_100ms = delay_audio(audio,int(fs * 0.1))
sf.write("teamOrnstein-stereosoundfile-100ms.wav",audio_100ms,fs)