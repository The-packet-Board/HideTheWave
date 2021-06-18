# HideTheWave
#Inspired by TechChip
# Hide your secret text in a audio file.
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', help='(a)udio File', dest='audiofile')
parser.add_argument('-m', help='Secret (m)essage', dest='secretmsg')
parser.add_argument('-o', help='(o)utput', dest='outputfile')
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if af and string and output:
    arged = True

def em_audio(af, string, output):
    if not arged:
        print ("need a, m and o")
        quit('')
    else:
      print ("Please wait...")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("Complete")
try:
  em_audio(af, string, output)
except:
  print ("Please try again")
  quit('')
