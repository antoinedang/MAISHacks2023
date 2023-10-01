from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import requests
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

primer_file = "primer_notes.txt"
generate_midi_script = "generate_melody.sh"

note_to_int_mapping = {
    "C": "60",
    "C#": "61",
    "D": "62",
    "D#": "63",
    "E": "64",
    "F": "65",
    "F#": "66",
    "G": "67",
    "G#": "68",
    "A": "69",
    "A#": "70",
    "B": "71"
}

@app.route('/playmidi', methods=['GET'])
def get_midi():
    print("Generating midi from primer...")
    try:
        primer_notes_string = request.args.get('primer')

        bash_script_arguments = [note_to_int_mapping[note] for note in primer_notes_string.split(',')]  # You can use the file data as the argument
        
        bash_arg_str = ""
        for arg in bash_script_arguments:
            bash_arg_str += arg + ","
        
        bash_arg_str = "[" + bash_arg_str[:-1] + "]"

        threading.Thread(target=generateMIDI, args=[bash_arg_str]).start()

        print("Finished generation.")
        return jsonify({'result': "success", "message": ""}), 200
        
    except Exception as e:
        # Return the response
        print("ERROR" + str(e))
        return jsonify({'result': "error", "message": str(e)}), 500
    
def generateMIDI(bash_arg_str):
    print(type(bash_arg_str))
    subprocess.call(["bash", generate_midi_script, bash_arg_str])
    requests.post("http://localhost:3000/play")
    

if __name__ == '__main__':
    app.run(debug=True)