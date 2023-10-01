BUNDLE_PATH=<absolute path of .mag file>
CONFIG=<one of 'performance', 'performance_with_dynamics', etc., matching the bundle>

performance_rnn_generate \
    --config=${CONFIG} \
    --bundle_file=${BUNDLE_PATH} \
    --output_dir=./generated/melodies \
    --num_outputs=10 \
    --num_steps=3000 \
    --primer_melody="[60,62,64,65,67,69,71,72]"