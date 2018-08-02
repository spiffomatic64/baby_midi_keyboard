#!/usr/bin/env bash

for cpu in /sys/devices/system/cpu/cpu[0-9]*; do echo -n performance | sudo tee $cpu/cpufreq/scaling_governor; done

export DISPLAY=:0
# dbus-launch started, DBUS_SESSION_BUS_ADDRESS exported:
export `dbus-launch | grep ADDRESS` 

# dbus-launch started, DBUS_SESSION_BUS_PID exported
export `dbus-launch | grep PID` 


sleep 5

pkill jackd
jackd -P70 -p16 -t2000 -dalsa -dhw:1 -p512 -n3 -r44100 -s 2> /root/jack_error.log > /root/jack_output.log &

pkill fluidsynth
fluidsynth -i --server --audio-driver=jack --connect-jack-outputs /usr/share/sounds/sf2/FluidR3_GM.sf2 2> /root/fluid_error.log > /root/fluid_output.log &

pkill python
/home/pi/midi_test.py 2> /root/midi_error.log > /root/midi_output.log &

