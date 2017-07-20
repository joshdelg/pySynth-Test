from random import randint
import pysynth

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
durations = [1, 2, 4, 8, 16]

song = []

limit = 5

for i in range(0, limit):
	temp = (alphabet[randint(0, 6)], durations[randint(0, 4)])
	song.append(temp)

pysynth.make_wav(song, fn = 'random.wav')
