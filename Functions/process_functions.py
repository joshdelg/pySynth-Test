import pysynth as a
import pysynth_b as b
import pysynth_c as c
import pysynth_d as d
import pysynth_e as e
import pysynth_p as p
import pysynth_s as s

# user selects key
# length determines duration
# color determines pitch

notes = []
lines = []

current_synth = a
current_color = 'red'

accidentals = ['f', 'c', 'g', 'd', 'a', 'e', 'b']

sig_c, sig_g, sig_d, sig_a, sig_e, sig_b, sig_fsharp = 0, 1, 2, 3, 4, 5, 6
sig_f, sig_bflat, sig_eflat, sig_aflat, sig_dflat, sig_gflat, sig_cflat = -1, -2, -3, -4, -5, -6, -7

current_key = sig_c

pitches = {
	'red' : 'a',
	'blue' : 'b',
	'white' : 'c',
	'yellow' : 'd',
	'green' : 'e',
	'purple' : 'f',
	'aqua' : 'g'
}

def add_line(length, pitch):
	temp_line = (length, pitch)
	lines.append(temp_line)

def change_synth(new_synth):
	global current_synth
	current_synth = new_synth

def change_color(new_color):
	global current_color
	current_color = new_color

def change_key(new_key):
	global current_key
	current_key = new_key

def color_to_pitch(color):
	pitch = pitches.get(color)
	return pitch

def accidentals_for_key(key):
	if key >= 0:
		key_accs = accidentals[:key]
	else:
		key_accs = accidentals[key:]

		return key_accs

def make_song(lines, key, file_name, synth):
	accs = accidentals_for_key(key)
	note_duration = 0

	for line in lines:
		length, pitch = line
		if accs == None:
			pass
		elif pitch in accs:
			if key >= 0:
				pitch += '#'
			elif key < 0:
				pitch += 'b'

		if length < 20:
			note_duration = 16
		elif length < 40 and length >= 20:
			note_duration = 8
		elif length < 60 and length >= 40:
			note_duration = 4
		elif length < 80 and length >= 60:
			note_duration = 2
		elif length >= 80:
			note_duration = 1

		note = (pitch, note_duration)
		notes.append(note)

	synth.make_wav(notes, fn = file_name)

print("Testing add line")
print(lines)
print("Adding len 5 pitch a each '()' is a line")
add_line(5, 'a')
print(lines)

print("Testing change synth")
print(current_synth)
print ("Changing synth to s")
change_synth(s)
print(current_synth)

print("Testing change color")
print(current_color)
print("Changing color to blue")
change_color('blue')
print(current_color)

print("Testing change key")
print(current_key)
print("Changing key to F (-1)")
change_key(sig_f)
print(current_key)

print("Testing color to pitch")
print(current_color)
print("Pitch should be b")
print(color_to_pitch(current_color))

print("Testing accidentals for key")
print(current_key)
print("accidentals should be B")
print(accidentals_for_key(current_key))

print("Testing make song")
print("adding lines to make a C chord")
lines = []
add_line(50, 'c')
add_line(50, 'e')
add_line(50, 'g')
add_line(100, 'c5')
print("Making song with current lines, key of C, file name of test.wav, and synth S")
change_key(sig_c)
make_song(lines, current_key, "test.wav", s)


#EXAMPLES:

# line is length 50 and color yellow (yellow is the pitch D)
line = [50, 'yellow']
#line[0] passes in length, color_to_pitch converts line[1] (the color) of the line to the respective pitch,
#then passes it into the function.
add_line(line[0], color_to_pitch(line[1]))

#user wants synth to be synth_s
user_synth = s
change_synth(user_synth)

#change_key and change_color work exactly the same way
#accidentals_for_key is only used by this program in the make_wav function
#for input of make_song, see tests above
#make_song should be called when the user presses the play button. Once the file loads, it should play the created music file
