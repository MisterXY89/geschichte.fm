from pydub import AudioSegment

def convert(fn):
    if ".mp3" in fn:
        fn = fn.split(".mp3")[0]
    sound = AudioSegment.from_mp3(f"{fn}.mp3")
    sound.export(f"{fn}.wav", format="wav")