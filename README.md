# RockPaperScissors
Rock Paper Scissors with coin hopper

## Install on Raspberry Pi OS
```
cd /home/pi
git clone https://github.com/rinalim/RockPaperScissors
mkdir /home/pi/.config/autostart
cp /home/pi/RockPaperScissors/rps.desktop /home/pi/.config/autostart/
sudo reboot
```

## How to play
1. KEY_1: Insert coin
2. KEY_LEFT: Scissors
3. KEY_DOWN: Rock
4. KEY_RIGHT: Paper

## For raspberry pi 2B
Use CLI mode to achive full framerate.
Edit /etc.rc.local for autostart
```
...
/usr/bin/python3 /home/pi/RockPaperScissors/game_all.py &
exit 0
```
