import numpy as np
import soundfile as sf

# Ear distance in meters
ear_distance = 0.1854

audio, fs = sf.read("quickfox.wav")
print(audio.shape)

def delay_atten(audio,delay_samples,attenuation):
    delayed_audio = np.zeros_like(audio)
    # Delay audio
    if delay_samples != 0:
        delayed_audio[delay_samples:] = audio[:-delay_samples]
        print(delay_samples)
    else:
        delayed_audio = audio
        print("Not delaying")

    # Calculate attentuation factor from db
    attenuation = 10**(attenuation / 10)
    print(attenuation)
    # Attenuate right channel
    delayed_audio = delayed_audio * attenuation

    # Concat and transpose
    stereo_delayed = np.asarray([audio,delayed_audio]).T

    return stereo_delayed

# 0dB attenuation samples
sf.write("teamOrnstein-stereosoundfile-0ms.wav",audio,fs)

audio_avghead = delay_atten(audio,int(ear_distance / 343 * fs),0)
sf.write("teamOrnstein-stereosoundfile-avghead.wav", audio_avghead,fs)

audio_1ms = delay_atten(audio,int(fs * 0.001),0)
sf.write("teamOrnstein-stereosoundfile-1ms.wav",audio_1ms,fs)

audio_10ms = delay_atten(audio,int(fs * 0.01),0)
sf.write("teamOrnstein-stereosoundfile-10ms.wav",audio_10ms,fs)

audio_100ms = delay_atten(audio,int(fs * 0.1),0)
sf.write("teamOrnstein-stereosoundfile-100ms.wav",audio_100ms,fs)

# Attentuated 0ms samples:
audio_0ms1_5 = delay_atten(audio,0,-1.5)
sf.write("teamOrnstein-stereosoundfile-0ms-1.5db.wav",audio_0ms1_5,fs)
audio_0ms3 = delay_atten(audio,0,-3)
sf.write("teamOrnstein-stereosoundfile-0ms-3db.wav",audio_0ms3,fs)
audio_0ms6 = delay_atten(audio,0,-6)
sf.write("teamOrnstein-stereosoundfile-0ms-6.wav",audio_0ms6,fs)

# Attentuated avghead samples:
audio_avgheadms1_5 = delay_atten(audio,int(ear_distance / 343 * fs),-1.5)
sf.write("teamOrnstein-stereosoundfile-avghead-1.5db.wav",audio_0ms1_5,fs)
audio_avgheadms3 = delay_atten(audio,int(ear_distance / 343 * fs),-3)
sf.write("teamOrnstein-stereosoundfile-avghead-3db.wav",audio_0ms3,fs)
audio_avgheadms6 = delay_atten(audio,int(ear_distance / 343 * fs),-6)
sf.write("teamOrnstein-stereosoundfile-avghead-6.wav",audio_0ms6,fs)