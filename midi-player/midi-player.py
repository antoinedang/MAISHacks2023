from flask import Flask, request, jsonify
import pygame
import mido
from mido import MidiFile, MidiTrack
import random

app = Flask(__name__)

midi_file = "input.mid"
drumMidiFilenameList = ["drums1.mid", "drums2.mid"]

@app.route('/play', methods=['POST'])
def play_midi():
    try:
        pygame.mixer.music.stop()
        createMelodyWithBeat()
        pygame.mixer.music.load(midi_filename)
        pygame.mixer.music.play()
        
        print("Playback has begun.")
        return jsonify({'result': "success", "message": ""}), 200
        
    except Exception as e:
        # Return the response
        return jsonify({'result': "error", "message": str(e)}), 500
    
    
@app.route('/stop', methods=['POST'])
def stop_midi():
    pygame.mixer.music.stop()

@app.route('/pause', methods=['POST'])
def pause_midi():
    pygame.mixer.music.pause()

@app.route('/unpause', methods=['POST'])
def unpause_midi():
    pygame.mixer.music.unpause()
    
def createMelodyWithBeat():
    # Load the piano MIDI file
    piano_file = MidiFile(midi_file)

    random_drum_midi = "drum_midis/" + random.sample(drumMidiFilenameList, 1)
    # Load the drum MIDI file
    drum_file = MidiFile(random_drum_midi)

    # Create a new MIDI file for the merged tracks
    merged_file = MidiFile()

    # Create a new track for the merged file
    merged_track = MidiTrack()
    merged_file.tracks.append(merged_track)

    # Iterate through the piano file's tracks and add them to the merged track
    for track in piano_file.tracks:
        merged_track.extend(track)

    # Iterate through the drum file's tracks and add them to the merged track
    for track in drum_file.tracks:
        merged_track.extend(track)

    # Save the merged MIDI file
    merged_file.save('merged.mid')

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    midi_filename = "input.mid"
    app.run(debug=True, port=3000)
