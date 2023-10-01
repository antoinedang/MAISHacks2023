from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

midi_file = "input.mid"

@app.route('/play', methods=['POST'])
def play_midi():
    try:
        print("Generating midi from primer...")
        # Read the contents of the file
        
        primer_notes_string = request.get_json().get('primer')

        # Define the argument for the Bash script
        bash_script_arguments = [note_to_int_mapping[note] for note in primer_notes_string.split(',')]  # You can use the file data as the argument
        
        bash_arg_str = ""
        for arg in bash_script_arguments:
            bash_arg_str += arg + ","
        
        bash_arg_str = bash_arg_str[:-1]

        subprocess.call(["bash", generate_midi_script, bash_arg_str])

        # Delete the file after processing
        os.remove(primer_file)
        print("Finished generation.")
        return jsonify({'result': "success", "message": ""}), 200
        
    except Exception as e:
        # Return the response
        return jsonify({'result': "error", "message": str(e)}), 500
    
    
@app.route('/stop', methods=['POST'])
def stop_midi():


if __name__ == '__main__':
    app.run(debug=True)