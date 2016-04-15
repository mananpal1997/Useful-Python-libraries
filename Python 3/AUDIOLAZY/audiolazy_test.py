from audiolazy import *
#sa-re-ga-ma-pa
rate = 50000
s, Hz = sHz(rate) # Seconds and hertz
ms = 1e-3 * s
note1 = karplus_strong(240 * Hz) # Pluck "digitar" synth
note2 = zeros(300 * ms).append(karplus_strong(270 * Hz))
note3 = zeros(600 * ms).append(karplus_strong(300 * Hz))
note4 = zeros(900 * ms).append(karplus_strong(337.5 * Hz))
note5 = zeros(1200 * ms).append(karplus_strong(360 * Hz))
note6 = zeros(1500 * ms).append(karplus_strong(400 * Hz))
note7 = zeros(1800 * ms).append(karplus_strong(450 * Hz))
note8 = zeros(2100 * ms).append(karplus_strong(480 * Hz))

notes = (note1 + note2 + note3 + note4 + note5 + note6 + note7 + note8) * 0.5

sound = notes.take(int(4 * s)) # 2 seconds of a Karplus-Strong note

with AudioIO(True) as player: # True means "wait for all sounds to stop"
    player.play(sound, rate = rate)
