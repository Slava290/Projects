import wave
import struct


def chip_and_dale(a):
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())

    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))

    # reverse the list
    newdata = data[::a]

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)
    source.close()
    dest.close()


chip_and_dale(2)
