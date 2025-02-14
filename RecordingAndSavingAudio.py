import wave,sys,pyaudio,keyboard
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
print("Press\'q\'to STOP recording.")
with wave.open('output.wav', 'wb') as wf:
    p = pyaudio.PyAudio()
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)
    print('Recording...')
    while keyboard.is_pressed('q')!=True:
        wf.writeframes(stream.read(CHUNK))
    print('Done')
stream.close()
p.terminate()
wf.close()
