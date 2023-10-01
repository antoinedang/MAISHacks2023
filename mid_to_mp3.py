from midi2audio import FluidSynth
import os


songs = ["ItalianconteT1000_Sotto_le_stelle_del_jazz_Conte1"]

for s in songs:
    # using the default sound font in 44100 Hz sample rate
    fs = FluidSynth()
    path = os.path.join(os.getcwd(), s + ".mid")
    print(path)
    fs.midi_to_audio(path, s + ".wav")