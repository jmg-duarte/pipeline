# Following pip packages need to be installed:
# !pip install git+https://github.com/huggingface/transformers sentencepiece datasets

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

inputs = processor(
    text="In May, the Texas state House voted one hundred and twenty one to twenty three to impeach Attorney General Ken Paxton. He faced accusations of using his influence to benefit a real estate developer named Nate Paul. Paxton was acquitted after a Senate trial, which also dismissed four articles of impeachment. His defense argued the impeachment was politically motivated, targeting him by political opponents, including George P. Bush, who ran against him in two thousand and twenty two. Paxton's lawyer accused the Bush family of manufacturing the allegations.",
    return_tensors="pt",
)

# load xvector containing speaker's voice characteristics from a dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

sf.write("data/output/speech.wav", speech.numpy(), samplerate=16000)
