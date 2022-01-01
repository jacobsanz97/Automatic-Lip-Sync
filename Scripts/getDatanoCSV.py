from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("/home/jacob/Desktop/lack/u.wav" , "wav") 
chunk_length_ms = 2000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

j = 4152
for i, chunk in enumerate(chunks):
    chunk_name = str(j) + "-t-" + "u.wav".format(i)
    chunk.export(chunk_name, format="wav")
    j = j + 1
