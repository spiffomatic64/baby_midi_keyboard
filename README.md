# baby_midi_keyboard
Using a raspberrypi and a midi keyboard to create piano "training wheels"

Uses jackd and fluidsynth for low latency (based on guides from: http://tedfelix.com/linux/linux-midi.html and https://wiki.linuxaudio.org/wiki/raspberrypi)

## Requirements:
 python
 pygame
 jackd
 fluidsynth fluid-soundfont-gm fluid-soundfont-gs 
 
 
To start automatically, add to rc.local:
 /bin/bash /root/start_midi.sh &> /root/rc_start.log

