performance_rnn_generate \
--run_dir=/tmp/performance_rnn/logdir/run1 \
--output_dir=./generated/melodies/ \
--config=performance_with_dynamics \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60,62,64,65,67,69,71,72]"