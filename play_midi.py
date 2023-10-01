import pygame

def play_midi(midi_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

if __name__ == "__main__":
    midi_file = "temp.mid"  # Replace with the path to your MIDI file
    play_midi(midi_file)

    # Keep the script running until the MIDI file finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
