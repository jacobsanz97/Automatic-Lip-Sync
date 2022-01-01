from pydub import AudioSegment
from pydub.utils import make_chunks
import csv

myaudio = AudioSegment.from_file("/home/jacob/gg.wav" , "wav") 
chunk_length_ms = 4000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

mycsv = 'data.csv'

with open(mycsv, 'wb') as csvfile: #Make the CSV
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Filename', 'Category'])

#Export all of the individual chunks as wav files, add labels to csv
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        chunk.export(chunk_name, format="wav")
        filewriter.writerow([chunk_name, 'Whisper'])
