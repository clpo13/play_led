#!/usr/bin/env python3
# Copyright (C) 2018 Cody Logan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Usage:
    play_led.py [-v] [-l PIN] [-b PIN] FILE
    play_led.py (-h | --help)
    play_led.py --version

Arguments:
    FILE  audio file to play

Options:
    -h --help            show this help message and exit
    --version            show version and exit
    -v --verbose         print more information
    -l PIN --led=PIN     set the GPIO pin for the LED [default: 17]
    -b PIN --button=PIN  set the GPIO pin for the button [default: 27]

"""

import pygame, sys
from gpiozero import Button, LED
from docopt import docopt

arguments = docopt(__doc__, version='0.0.1')

# initialize PyGame mixer
pygame.mixer.init()
print(arguments)

# take command line input if present
#led_gpio = int(sys.argv[1]) if len(sys.argv) >= 2 else 17
#btn_gpio = int(sys.argv[2]) if len(sys.argv) >= 3 else 27
#snd_file = sys.argv[3] if len(sys.argv) >= 4 else 'drum_roll.ogg'
led_gpio = int(arguments['--led']) if not arguments['--led'] == None else 17
btn_gpio = int(arguments['--button']) if not arguments['--button'] == None else 27
snd_file = arguments['FILE']

# set GPIO pins
led = LED(led_gpio)
button = Button(btn_gpio)

# load audio file (mp3 or ogg)
pygame.mixer.music.load(snd_file)

# loop forever until canceled, otherwise
# program will end once the audio does
while True:
    button.wait_for_press()

    # button pressed, play audio and turn on led
    pygame.mixer.music.play()
    led.on()

    # check if audio is still playing and wait for it to finish
    while pygame.mixer.music.get_busy() == True:
        pygame.time.wait(100)

    # audio done, turn led off
    led.off()

