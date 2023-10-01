from flask import Flask, request, jsonify
import pygame

app = Flask(__name__)

midi_file = "input.mid"

@app.route('/play', methods=['POST'])
def play_midi():
    try:
        pygame.mixer.music.stop()
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

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    midi_filename = "input.mid"
    app.run(debug=True, port=3000)
