from transformers import *
import torch
import soundfile as sf
# import librosa
import os
import torchaudio

data_dir = "data/"
audio_uri = f"{data_dir}test_001.wav"
audio_url = "https://github.com/x4nth055/pythoncode-tutorials/raw/master/machine-learning/speech-recognition/30-4447-0004.wav"


class Speech2Text():
  
  def __init__(self, model_type="german") -> None:
      self.model_type = model_type
      self.data_dir = "data/"
      self.model, self.processor = self.init_module()

  def init_module(self):
    models = {
      "s": "facebook/wav2vec2-base-960h",
      "l": "facebook/wav2vec2-large-960h-lv60-self",
      # "german": "flozi00/wav2vec-xlsr-german"
      "german": "jonatasgrosman/wav2vec2-large-xlsr-53-german"
    }
    model_name = models[self.model_type]
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    return model, processor


  def get_transcript(self, uri):
    # load our wav file
    speech, sr = torchaudio.load(uri)
    speech = speech.squeeze()
    # or using librosa
    # speech, sr = librosa.load(audio_file, sr=16000)
    print(sr, speech.shape)

    # resample from whatever the audio sampling rate to 16000
    resampler = torchaudio.transforms.Resample(sr, 16000)
    speech = resampler(speech)
    print(speech.shape)

    # tokenize our wav
    input_values = self.processor(speech, return_tensors="pt", sampling_rate=16000)["input_values"]
    print(input_values.shape)

    # perform inference
    logits = self.model(input_values)["logits"]
    print(logits.shape)

    # use argmax to get the predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)
    predicted_ids.shape

    # decode the IDs to text
    transcription = self.processor.decode(predicted_ids[0])
    return transcription.lower()


s2t = Speech2Text()
t = s2t.get_transcript("data/converted_waves/gag02.wav")
print(t)