from flask import Flask, request, jsonify
from flask_cors import CORS
import pygame
import mido
from mido import MidiFile, MidiTrack
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

midi_file = "input.mid"
drumMidiFilenameList = ["drums.mid"]

@app.route('/play', methods=['GET'])
def play_midi():
    pygame.mixer.music.stop()
    merge_midi_files()
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()
    global paused
    paused = False
    
    print("Playback has begun.")
    return jsonify({'result': "success", "message": ""}), 200
    
    
@app.route('/stop', methods=['GET'])
def stop_midi():
    pygame.mixer.music.stop()
    return jsonify({'result': "success", "message": ""}), 200

@app.route('/pause', methods=['GET'])
def pause_midi():
    global paused
    if paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
        
    paused = not paused
    return jsonify({'result': "success", "message": ""}), 200
    
def createMelodyWithBeat():
    try:
        # Load the piano MIDI file
        piano_file = MidiFile(midi_file)

        random_drum_midi = "drum_midis/" + random.sample(drumMidiFilenameList, 1)[0]
        print(random_drum_midi)
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
    except Exception as e:
        print(str(e))
 
def merge_midi_files():
    # Load the MIDI files
    index = int(random.random()*len(drumMidiFilenameList))
    drums = drumMidiFilenameList[index]
    midi1 = MidiFile("drum_midis/" + drums)
    midi2 = MidiFile(midi_file)

    # midi1.tracks = [track for track in midi1.tracks if not any(msg.type == 'set_tempo' for msg in track)]
    # midi2.tracks = [track for track in midi2.tracks if not any(msg.type == 'set_tempo' for msg in track)]

    # Create a new MIDI file for the merged output
    merged_midi = MidiFile()
    # append_tracks(midi1, merged_midi, False)
    # append_tracks(midi2, merged_midi, True, bpm=30)

    for track in midi1.tracks:
        new_track = MidiTrack()
        for msg in track:
            if not msg.is_meta:
                new_msg = msg.copy()
                new_msg.time *= 0.15
                new_msg.time = int(new_msg.time)
                new_track.append(new_msg)
        merged_midi.tracks.append(new_track)


    for track in midi2.tracks:
        new_track = MidiTrack()
        # program_change = Message('program_change', channel=0, program=89)
        # new_track.append(program_change)
        for msg in track:
            if msg.type == "set_tempo":
                new_tempo = mido.bpm2tempo(60)
                new_track.append(mido.MetaMessage('set_tempo', tempo=new_tempo, time=msg.time))
            else:
                new_msg = msg.copy()
                new_track.append(new_msg)
        merged_midi.tracks.append(new_track)
    merged_midi.save("merged.mid")

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    paused = False
    midi_filename = "merged.mid"
    app.run(debug=True, host='0.0.0.0', port=3000)
