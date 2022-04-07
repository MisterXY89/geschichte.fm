#!/bin/bash
name=$1
url=$2

echo "> Downloading Episode #$name";
cd downloaded_mp3s/;
wget -O $name.mp3 $url;

echo "> Converting: MP3 ---- WAV";
ffmpeg -i $name.mp3 ../converted_waves/$(basename "$f" .mp3).wav;

cd ..;

cd converted_waves/;
echo "> Setting Samplerate and Bit-Depth [$name.wav]";
sox $name.wav -r 16000 -b 16 -c 1 ../ready_waves/$name.wav;

