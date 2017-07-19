# Run this file after installing pysynth and play the output file

# Importing module
import pysynth

# Writes first verse of 'Mary Had a Little Lamb' in native syntax
song = (
  ('e', 4), ('d', 4), ('c', 4), ('d', 4), ('e', 4), ('e', 4), ('e', 2), ('d', 4), ('d', 4), ('d', 2), ('e', 4), ('g', 4), ('g', 2)
)

# Calls function to make .wav file
pysynth.make_wav(song, fn = "Mary Had a Little Lamb.wav")
