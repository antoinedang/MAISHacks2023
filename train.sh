echo "Please enter the folder containing MIDI files to train on:"
read INPUT_DIRECTORY

echo "Drums or Melodies?"
read selection

if [ "$userInput" = "Drums" ]; then
  # TFRecord file that will contain NoteSequence protocol buffers.
  SEQUENCES_TFRECORD=/tmp/drumsequences.tfrecord

  convert_dir_to_note_sequences \
    --input_dir=$INPUT_DIRECTORY \
    --output_file=$SEQUENCES_TFRECORD \
    --recursive

  drums_rnn_create_dataset \
    --config=drum_kit \
    --input=$SEQUENCES_TFRECORD \
    --output_dir=/tmp/drums_rnn/sequence_examples \
    --eval_ratio=0.10

  drums_rnn_train \
  --config=drum_kit \
  --run_dir=/tmp/drums_rnn/logdir/run1 \
  --sequence_example_file=/tmp/drums_rnn/sequence_examples/training_drum_tracks.tfrecord \
  --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" \
  --num_training_steps=20000

elif [ "$userInput" = "Melody" ]; then
  echo "You selected Melody."
else
  echo "Invalid input. Please enter 'Drums' or 'Melody'."
fi

