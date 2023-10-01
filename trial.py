import magenta.music as mm

# Load a MIDI file
midi_file_path = './data/melody midi/youhavechanged.mid'
midi_sequence = mm.midi_file_to_note_sequence(midi_file_path)

for note in midi_sequence.notes:
    print(f"Note: {note.pitch}, Start Time: {note.start_time}, End Time: {note.end_time}, Velocity: {note.velocity}")

output_midi_file_path = './test_output.mid'
mm.note_sequence_to_midi_file(midi_sequence, output_midi_file_path)
