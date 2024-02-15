import numpy as np
import soundfile as sf

# Ear distance in meters
ear_distance = 0.1854

audio, fs = sf.read("quickfox.wav", always_2d=True)
print(audio)
print(audio.shape)

stereo = np.asarray([audio,audio])
# Copy left channel to right channel
audio_stereo = np.append(audio,audio,1)
print(audio_stereo)
print(audio_stereo.shape)
sf.write("teamOrnstein-stereosoundfile-0ms.wav",audio_stereo,fs)

# Delay by 26 samples (avghead)
audio_avghead = audio_stereo
# Calculate delay in samples
avghead_delay = int(ear_distance / 343 * fs)
print(avghead_delay)
audio_avghead[1, avghead_delay:] = audio_avghead[1, :-avghead_delay]
# audio_avghead[1] = np.concatenate(([0] * avghead_delay, audio_avghead[1][:-avghead_delay]))
print(audio_avghead.shape)
print(audio_avghead)
sf.write("teamOrnstein-stereosoundfile-avghead.wav",audio_avghead,fs)

# Delay by 1ms
audio_1ms = audio_stereo
audio_1ms[1] = np.concatenate(([0] * int(fs * 0.001), audio_1ms[1][:-int(fs * 0.001)]))
sf.write("teamOrnstein-stereosoundfile-1ms.wav",audio_1ms,fs)

# Delay by 10ms
audio_10ms = audio_stereo
audio_10ms[1] = np.concatenate(([0] * int(fs * 0.01), audio_10ms[1][:-int(fs * 0.01)]))
sf.write("teamOrnstein-stereosoundfile-10ms.wav",audio_10ms,fs)

# Delay by 100ms
audio_100ms = audio_stereo
audio_100ms[1] = np.concatenate(([0] * int(fs * 0.1), audio_100ms[1][:-int(fs * 0.1)]))
sf.write("teamOrnstein-stereosoundfile-100ms.wav",audio_100ms,fs)