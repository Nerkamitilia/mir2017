from mido import MidiFile
import os

mididir = 'midifiles/kpcorpus'

for filename in os.listdir(mididir):
	if filename.endswith('.mid'):
		print filename
		filepath = os.path.join(mididir, filename)
		for msg in MidiFile(filepath):
			print msg
			if msg.type == 'lyrics':
				print '---------------- CHORD -------------------'
				#print '\t{}'.format(msg.text)
	break
