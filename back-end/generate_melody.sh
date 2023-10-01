source activate magenta;
sudo rm /tmp/melody_rnn/generated/*;
primer="$1";
melody_rnn_generate --config=basic_rnn --run_dir=/tmp/melody_rnn/logdir/run1/train --output_dir=/tmp/melody_rnn/generated --num_outputs=1 --num_steps=500 --hparams="batch_size=64,rnn_layer_sizes=[128,128]" --primer_melody=$primer;
sudo cp /tmp/melody_rnn/generated/* ./;
sudo mv *.mid /mnt/c/Users/antoi/Documents/Projects/Git/MAIS_HACKS/midi-player/input.mid;