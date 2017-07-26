import pysynth

# Ex. > e 4 d 4 c 4 d 4 e 4 e 4 e 2
notes = input('Enter notes: ').split()

song = []

# after playing around, decided a while lope would be better for incrementing
i = 0

while i < len(notes) - 1:
  
	temp = (notes[i], int(notes[i + 1]))
	song.append(temp)
  
	i += 2

pysynth.make_wav(song, fn = 'input.wav')
