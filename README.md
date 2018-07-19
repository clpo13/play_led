# play\_led

Keep an LED lit while playing a sound. When the user presses a button, an audio clip corresponding to that button will play via a speaker. A Python script will run continuously to grab button presses and play audio.

# Requirements

## Hardware

- Raspberry Pi
- solderless breadboard
- 1x LED
- 1x 330 ohm resistor
- 1x tactile button
- 2x male-to-male jumper leads
- 3x male-to-female jumper leads

## Software

- Python 3, GPIO Zero, and PyGame (all preinstalled in Raspbian)

# Set up and run

See the included `play_led_bb.png` file for the hardware layout. Connect the short leg of the LED and one set of legs of the button to ground. The other set of button legs goes to GPIO pin 27 on the Pi. The long leg of the LED connects to one end of the resistor and the other end of the resistor connects to GPIO pin 17.

Make sure `play_led.py` is executable (`chmod a+x play_led.py`) and run it with `./play_led.py` or `python3 play_led.py`. Press the button to play the sound and light up the LED. Once the sound is finished playing, the LED will turn off. Press `Ctrl+C` to quit the program.

## Command line options

The GPIO pins for the LED and button as well as the sound file can be specified via the command line:

```bash
./play_led.py <LED> <BUTTON> <SOUND FILE>
```

For example, if you've connected the LED to pin 4 and the button to pin 27 and you want to play a file called `vinyl_backspin.ogg`, you would run the following:

```bash
./play_led.py 4 27 vinyl_backspin.ogg
```

All parameters must be specified for now, though a future update will allow setting them individually.

# To do

- [X] Pressing a button causes audio to play
- [X] Pressing the same button again while audio is playing does nothing
- [ ] Pressing a different button while audio is playing stops the first clip and plays a new one
- [X] Turn on an LED above the button when the audio clip is playing to provide feedback to the user
- [ ] Use a switch or button to control power to the device; flipping the switch or pressing the button signals to the device to start shutting down gracefully
- [ ] Start script as soon as the device is booted and keep running as long as the device is on
- [ ] Set command line options with flags instead of positional parameters

# License

This project's source code, `play_led.py`, and documentation, `README.md` (this file), are licensed according to the terms of the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3).

The included sound files, `drum_roll.ogg` and `vinyl_backspin.ogg`, have been released into the public domain under the [CC0 1.0 Universal Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/) (CC0 1.0). The original files can be found at [freesound.org](https://freesound.org/):

- [drumroll.aiff](https://freesound.org/people/Heigh-hoo/sounds/19433)
- [backspin.wav](https://freesound.org/people/il112/sounds/182316/)

These versions of the files were copied from the [Sonic Pi](https://sonic-pi.net/) distribution [samples folder](https://github.com/samaaron/sonic-pi/tree/master/etc/samples) and converted from FLAC to OGG.

The breadboard diagram, `play_led_bb.png`, was created with [Fritzing](http://fritzing.org/) and is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0).
