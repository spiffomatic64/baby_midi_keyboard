#!/usr/bin/env python2
import sys
import pygame, pygame.midi
from bisect import bisect_left
import time

#pentatonic scale (in A)
notes =[21,24,26,28,31,
        33,36,38,40,43,
        45,48,50,52,55,
        57,60,62,64,67,
        69,72,74,76,79,
        81,84,86,88,91,
        93,96,98,100,103,
        105,108,110,112,115]
        
#synth Lead 1 (square)
instrument = 81
volume = 50

#get the closest note in the "notes" list
def takeClosest(myNumber):
    pos = bisect_left(notes, myNumber)
    if pos == 0:
        return notes[0]
    if pos == len(notes):
        return notes[-1]
    before = notes[pos - 1]
    after = notes[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

def setup_midi():
    in_port = 3
    out_port = 4

    pygame.init()
    pygame.midi.init()
    
    devices = pygame.midi.get_count()
    print("devices: %d" % devices)
    
    count = 0
    for device in range(0,devices):
        print(count)
        print(pygame.midi.get_device_info(device))
        count += 1

    o_port = pygame.midi.get_default_output_id()
    
    print ("default output_id :%s:" % o_port)
    print ("using output_id :%s:" % out_port)
    print ("using input_id :%s:" % in_port)
    return (pygame.midi.Input(in_port,1000),pygame.midi.Output(out_port))

# open a specific midi device
print("Setting up midi")
midi_in,midi_out = setup_midi()


midi_out.set_instrument(instrument)

#play a note automatically to let you know its "running"
midi_out.note_on(69, volume)
time.sleep(2)
midi_out.note_off(69, volume)


notes_on = {}

#keep track of notes
for note in range(127):
    notes_on[note] = False

# run the event loop
print("Starting...")
while True:
    if midi_in.poll():
        #[[[144, 79, 75, 0], 4340]]
        midi_data = midi_in.read(100)
        for data in midi_data:
            data = data[0]
            note = takeClosest(data[1])
            if data[2] == 75:
                midi_out.note_off(note, volume)
                notes_on[note] = True
                midi_out.note_on(note, volume)
            else:
                notes_on[note] = False
                midi_out.note_off(note, volume)
            print(data,note)
        

    # wait 10ms - this is arbitrary, but wait(0) still resulted
    # in 100% cpu utilization
    pygame.time.wait(10)
