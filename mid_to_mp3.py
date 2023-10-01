import mido
from pydub import AudioSegment
import subprocess
import time

# MIDI file input and output paths
midi_file = "ItalianconteT1000_Sotto_le_stelle_del_jazz_Conte1.mid"
output_mp3_file = "output.mp3"

# Initialize FluidSynth with a default SoundFont
fluidsynth_command = ["fluidsynth", "-a", "alsa", "--audio-driver=alsa", "--gain=0.5", "--reverb=0", "--chorus=0", "/usr/share/soundfonts/default.sf2"]
fluidsynth_process = subprocess.Popen(fluidsynth_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Give FluidSynth some time to initialize
time.sleep(1)

# Convert MIDI to WAV using FluidSynth
subprocess.run(["fluidsynth", "-T", "wav", "/usr/share/soundfonts/default.sf2", midi_file])

# Load the generated WAV file
midi_audio = AudioSegment.from_wav(midi_file.replace('.mid', '.wav'))

# Export the audio as MP3
midi_audio.export(output_mp3_file, format="mp3")

# Clean up
fluidsynth_process.terminate()