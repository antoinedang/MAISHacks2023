source activate magenta
sudo rm /tmp/performance_rnn/generated/*

primer="$1";

performance_rnn_generate \
    --run_dir=/tmp/performance_rnn/logdir/run1 \
    --output_dir=/tmp/performance_rnn/generated \
    --config=performance_with_dynamics \
    --num_outputs=1 \
    --num_steps=3000 \
    --primer_melody=$primer \
    --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" \

sudo cp /tmp/performance_rnn/generated/* ./

mv *.mid /mnt/c/Users/antoi/Documents/Projects/Git/MAIS_HACKS/midi-player/input.mid
