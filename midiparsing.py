from mido import MidiFile
import os

for filename in os.listdir("."):
	if filename.endswith('.mid'):
		print filename
		for msg in MidiFile(filename):
			if msg.type == 'lyrics':
				print '\t{}'.format(msg.text)
