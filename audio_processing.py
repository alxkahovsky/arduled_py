import pyaudio
import struct
import numpy as np
from scipy.fftpack import fft, rfft


CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()


# for i in range(25):
#     print(p.get_device_info_by_index(i))

stream = p.open(format=FORMAT,
                channels=1,
                rate=RATE,
                output=True,
                input=True,
                frames_per_buffer=2*CHUNK,
                input_device_index=1)


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    # print(data)
    data_int = struct.unpack(str(2*CHUNK) + 'B', data)
    # print(len(data_int))
    # a = (fft(data_int))
    # # print(data_int[4095])
    # print(int(a[2000]))
    fftData = fft(data_int)
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max

    y0, y1, y2 = np.log(fftData[which - 1:which + 2:])
    x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
    # find the frequency and output it
    thefreq = (which + x1) * RATE / CHUNK
    print(
    "The freq is %f Hz." % (thefreq))
        # else:
        #     thefreq = which * RATE / CHUNK
        #     print(
        #     "The freq is %f Hz." % (thefreq))
        # read some more data



