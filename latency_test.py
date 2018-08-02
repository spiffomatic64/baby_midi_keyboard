#!/usr/bin/env python2
import sys
import pygame, pygame.midi
import instrument
import time
import datetime


def setup_midi():
    TIMIDITYPORT = 2

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
    i_port = 3
    print ("default output_id :%s:" % o_port)
    print ("using output_id :%s:" % TIMIDITYPORT)
    print ("using input_id :%s:" % i_port)
    return (pygame.midi.Input(i_port,1000),pygame.midi.Output(TIMIDITYPORT))

# open a specific midi device
inp,midi_out = setup_midi()

instrument = instrument.Instrument(midi_out)    
midi_out.set_instrument(0)
midi_out.set_instrument(0,1)

midi_out.note_on(72, 127)
midi_out.note_off(72, 127)
print("sleeping...")
time.sleep(5)

if inp.poll():
        #[[[144, 79, 75, 0], 4340]]
    midi_data = inp.read(1000)
    print(midi_data)
    


data = False

print("latency test...")
a = datetime.datetime.now()
midi_out.note_on(100, 127)


while data == False:
    data = inp.poll()
    
midi_data = inp.read(1000)
b = datetime.datetime.now()
print(midi_data)
delta = b - a
print(delta)
midi_out.note_off(100, 127)
