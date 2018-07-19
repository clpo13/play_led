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

import pygame
from gpiozero import Button, LED

# initialize PyGame mixer
pygame.mixer.init()

# set GPIO pins
led = LED(17)
button = Button(27)

# load audio file (mp3 or ogg)
pygame.mixer.music.load('drum_roll.ogg')

# loop forever until canceled, otherwise
# program will end once the audio does
while True:
    button.wait_for_press()

    # button pressed, play audio and turn on led
    pygame.mixer.music.play()
    led.on()

    # check if audio is still playing
    while pygame.mixer.music.get_busy() == True:
        continue

    # audio done, turn led off
    led.off()

