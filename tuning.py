from math import log, floor, pi
tonic = 1 # Hz
harmonics = [n * tonic for n in range(1, 24)]
tuning = [h / 2**floor(log(h / tonic, 2)) for h in harmonics]
# print tuning
octave = sorted(set(tuning))
# print octave, len(octave)

cents = [round(1200*log(note, 2),5) for note in octave]
print cents, len(cents)