print("Hello World!")
import time
import random
import usb_midi

try:
    usb_midi.enable()
except:
    print("ERROR enabling MIDI")

import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")

print("Default output MIDI channel:", midi.out_channel + 1)

import board
from digitalio import DigitalInOut, Direction, Pull
btn = DigitalInOut(board.IO0)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    if not btn.value:
        midi.send(NoteOn(44, 120))  # G sharp 2nd octave
        time.sleep(0.25)
        a_pitch_bend = PitchBend(random.randint(0, 16383))
        midi.send(a_pitch_bend)
        time.sleep(0.25)
        midi.send([NoteOff("G#2", 120),
                   ControlChange(3, 44)])
        time.sleep(0.5)
        print("Sending more midi notes")
