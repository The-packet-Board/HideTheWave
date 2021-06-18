# ExposeTheWave
#Inspired by TechChip
# Hide your secret text in a audio file.
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', help='audio file', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True

def ex_msg(af):
    if not arged:
        print ("Define audio file")
        quit('')
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("The Secret Message is: "+msg)
        waveaudio.close()

try:
  ex_msg(af)
except:
  print ("Please try again")
  quit('')
