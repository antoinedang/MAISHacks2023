performance_rnn_generate \
    --run_dir=/tmp/performance_rnn/logdir/run1 \
    --output_dir=/tmp/performance_rnn/generated \
    --config=performance_with_dynamics \
    --num_outputs=1 \
    --num_steps=3000 \
    --primer_melody="[60,62,64,65,67,69,71,72]" \
    --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" \

sudo cp /tmp/performance_rnn/generated/* ./generated/melodies/