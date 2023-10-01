import mido
from mido import MidiFile, MidiTrack, MetaMessage, Message

def append_tracks(input, output, do_meta, bpm=None):
    for track in input.tracks:
        new_track = MidiTrack()
        for msg in track:
            if msg.is_meta and do_meta:
                # Calculate the new time scale factor based on the tempo change
                if msg.type == "set_tempo":
                    new_tempo = mido.bpm2tempo(bpm)
                    new_track.append(mido.MetaMessage('set_tempo', tempo=new_tempo, time=msg.time))
            else:
                new_msg = msg.copy()
                new_track.append(new_msg)
        output.tracks.append(new_track)



def merge_midi_files(input_file1, input_file2, output_file):
    # Load the MIDI files
    midi1 = MidiFile(input_file1)
    midi2 = MidiFile(input_file2)

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
                # new_msg.time *= 2.5
                # new_msg.time = int(new_msg.time)
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



    merged_midi.save(output_file)

if __name__ == "__main__":
    input_file1 = "drums.mid"  # Replace with the path to your first MIDI file
    input_file2 = "melody.mid"  # Replace with the path to your second MIDI file
    output_file = "merged.mid"  # Replace with the desired output file name

    merge_midi_files(input_file1, input_file2, output_file)
