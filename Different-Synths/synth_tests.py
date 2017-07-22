# importing each synth as a variable so we can use multiple without conflict of their functions
import pysynth as a     # default synthesizer is not titled 'synth a' but is not labeled in files
import pysynth_b as b   # synth b
import pysynth_c as c   # synth c
import pysynth_d as d   # synth d
import pysynth_e as e   # ...
import pysynth_p as p   # ...
import pysynth_s as s   # ...

song = (
    ('g', -8), ('e', 16), ('c', 4), ('e', 4), ('g', 4), ('c5', 2), ('e5', -8), ('d5', 16), ('c5', 4), ('e', 4), ('f#', 4), ('g', 2),
    ('g', 8), ('g', 8), ('e5', -4), ('d5', 8), ('c5', 4), ('b', 2), ('a', -8), ('b', 16), ('c5', 4), ('c5', 4), ('g', 4), ('e', 4), ('c', 4)
)

# if you go to the website it has more full descriptions of all the synths and what they are made to represent.

#synth a (default, piano-ish)
a.make_wav(song, fn = 'a.wav')

# synth b (slighly more accurate piano)
b.make_wav(song, fn = 'b.wav')

# synth c (made to emulate bowed string (violin, cello, etc.))
c.make_wav(song, fn = 'c.wav')

# synth d (subtractive synth, woodwind (flute, clarinet etc.))
d.make_wav(song, fn = 'd.wav')

# synth e (takes significantly longer than the other to process, made to emulate electric piano)
e.make_wav(song, fn = 'e.wav')

# synth p (a percussion synth, no pitch, made to emulate drum. Probably wouldn't be used in our project.)
p.make_wav(song, fn = 'p.wav')

# synth s (made to emulate plucked strings, (guitar, ukelele)
s.make_wav(song, fn = 's.wav')
