from flask import Flask, request, jsonify
import subprocess
import requests

app = Flask(__name__)

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

@app.route('/playmidi', methods=['POST'])
def get_midi():
    try:
        print("Generating midi from primer...")
        
        primer_notes_string = request.get_json().get('primer')

        bash_script_arguments = [note_to_int_mapping[note] for note in primer_notes_string.split(',')]  # You can use the file data as the argument
        
        bash_arg_str = ""
        for arg in bash_script_arguments:
            bash_arg_str += arg + ","
        
        bash_arg_str = bash_arg_str[:-1]

        subprocess.call(["bash", generate_midi_script, bash_arg_str])

        requests.post("http://localhost:3000/play")
        
        print("Finished generation.")
        return jsonify({'result': "success", "message": ""}), 200
        
    except Exception as e:
        # Return the response
        return jsonify({'result': "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)