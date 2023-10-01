echo "Please enter the folder containing MIDI files to train on:"
read INPUT_DIRECTORY

echo "Drums or Melodies?"
read selection

if [ "$selection" = "Drums" ]; then
  # TFRecord file that will contain NoteSequence protocol buffers.
  SEQUENCES_TFRECORD=/tmp/drumsequences.tfrecord

  echo "================================"
  echo "        Processing data..."
  echo "================================"

  convert_dir_to_note_sequences \
    --input_dir=$INPUT_DIRECTORY \
    --output_file=$SEQUENCES_TFRECORD \
    --recursive

  echo "================================"
  echo "        Generating dataset..."
  echo "================================"

  drums_rnn_create_dataset \
    --config=drum_kit \
    --input=$SEQUENCES_TFRECORD \
    --output_dir=/tmp/drums_rnn/sequence_examples \
    --eval_ratio=0.10

  echo "================================"
  echo "        Training..."
  echo "================================"

  drums_rnn_train \
  --config=drum_kit \
  --run_dir=/tmp/drums_rnn/logdir/run1 \
  --sequence_example_file=/tmp/drums_rnn/sequence_examples/training_drum_tracks.tfrecord \
  --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" \
  --num_training_steps=20000

elif [ "$selection" = "Melody" ]; then

  SEQUENCES_TFRECORD=/tmp/notesequences.tfrecord

  echo "================================"
  echo "        Processing data..."
  echo "================================"

  convert_dir_to_note_sequences \
    --input_dir=$INPUT_DIRECTORY \
    --output_file=$SEQUENCES_TFRECORD \
    --recursive

  echo "================================"
  echo "        Generating dataset..."
  echo "================================"

  performance_rnn_create_dataset \
    --config=performance_with_dynamics \
    --input=$SEQUENCES_TFRECORD \
    --output_dir=/tmp/performance_rnn/sequence_examples \
    --eval_ratio=0.10

  echo "================================"
  echo "        Training..."
  echo "================================"

  performance_rnn_train \
    --config=performance_with_dynamics \
    --run_dir=/tmp/performance_rnn/logdir/run1 \
    --sequence_example_file=/tmp/performance_rnn/sequence_examples/training_performances.tfrecord

else
  echo "Invalid input. Please enter 'Drums' or 'Melody'."
fi

