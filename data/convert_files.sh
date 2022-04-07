
echo "Converting: MP3 >>>> WAV"
cd downloaded_mp3s/
for f in *.mp3
do
    echo "* $f"    
    ffmpeg -i $f ../converted_waves/$(basename "$f" .mp3).wav
done

cd ..

a=0;
cd converted_waves/
pwd
for i in `ls *.wav`;
do

    let a++;
    echo "Processing file $i"
    sox $i -r 16000 -b 16 -c 1 ../ready_waves/file_$a.wav 

done
