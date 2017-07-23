import pysynth as a
import pysynth_b as b
import pysynth_c as c
import pysynth_d as d
import pysynth_e as e
import pysynth_p as p
import pysynth_s as s

# user selects key
# length determines duration (capped at 100 (doesn't half to be that))
# color determines pitch

notes = []
lines = []

current_synth = a
current_color = 'red'
current_key = sig_c

accidentals = ['f', 'c', 'g', 'd', 'a', 'e', 'b']

sig_c, sig_g, sig_d, sig_a, sig_e, sig_b, sig_fsharp = 0, 1, 2, 3, 4, 5, 6
sig_f, sig_bflat, sig_eflat, sig_aflat, sig_dflat, sig_gflat, sig_cflat = -1, -2, -3, -4, -5, -6, -7

pitches = {
	'red' : 'a'
	'blue' : 'b'
	'white' : 'c'
	'yellow' : 'd'
	'green' : 'e'
	'purple' : 'f'
	'aqua' : 'g'
}

def add_line(length, pitch):
	temp_line = (length, pitch)
	lines.append(temp_line)

def change_synth(new_synth):
	current_synth = new_synth

def change_color(new_color):
	current_color = new_color

def change_key(new_key):
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
		if pitch in accidentals_for_key:
			if key >= 0:
				pitch += '#'
			elif key < 0:
				pitch += 'b'

		if length < 20:
			note_duration = 16
		elif length < 40 and >= 20:
			note_duration = 8
		elif length < 60 and >= 40:
			note_duration = 4
		elif length < 80 and >= 60:
			note_duration = 2
		elif length >= 80:
			note_duration = 1

		note = (pitch, note_duration)
		notes.append(note)

	synth.make_wav(notes, fn = file_name)
  
  # TODO: Add unit tests
