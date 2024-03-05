import musicpy as mp
import numpy as np
from midi2audio import FluidSynth


a = mp.note('A', 5)
mp.play(a, instrument="Violin")

fs = FluidSynth()
fs.midi_to_audio('temp.mid', 'output.wav')