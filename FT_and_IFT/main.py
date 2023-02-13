import librosa
import librosa.display
import scipy as sp
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np

#incarcare player audio
cale_audio = "audio/note.wav"
ipd.Audio(cale_audio)

#extragere fisier audio
semnal, er = librosa.load(cale_audio)

#afisare forma de unda
plt.figure(figsize=(18,8))
librosa.display.waveshow(semnal, sr=er, alpha=0.5)
plt.show()

#derivare spectru utilizand Transformata Fourier
tf = sp.fft.fft(semnal)
magnitudine = np.absolute(tf)
frecventa = np.linspace(0, er, len(magnitudine))

#afisare spectru
plt.figure(figsize=(18,8))
plt.plot(frecventa[0:5000], magnitudine[0:5000]) #spectrul magnitudinii
plt.xlabel("Frecventa (Hz)")
plt.ylabel("Amplitudine")
plt.show()

print(f"Lungimea semnalului este:{len(semnal)} esantioane")

d = 1/er
d

d_523 = 1 / 523

print(f"Durata unui ciclu a fundamentalei este:{d_523} secunde")

d_400_esantioane = 400 * d

#vizualizarea unei portiuni din semnal
esantioane = range(len(semnal))
t = librosa.samples_to_time(esantioane, sr=er)

plt.figure(figsize=(18,8))
plt.plot(t[10000:10400],semnal[10000:10400])
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.show()

#generarea unui semnal sinusoidal

f = 523
faza = 0
faza_2 = 0.2
sin = 0.5 * np.sin(2 * np.pi * (f * t - faza))
sin2 = 0.5 * np.sin(2 * np.pi * (f * t - faza_2))

plt.figure(figsize=(18,8))
plt.plot(t[10000:10400], sin[10000:10400], color= 'r')
plt.plot(t[10000:10400], sin2[10000:10400], color= 'y')

plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.show()

#comparare semnal si sinusoida
f = 523
faza = 0.55
sin = 0.1 * np.sin(2*np.pi * (f * t - faza))
plt.figure(figsize=(18,8))
plt.plot(t[10000:10400], semnal[10000:10400])
plt.plot(t[10000:10400], sin[10000:10400], color='r')

plt.fill_between(t[10000:10400], sin[10000:10400]*semnal[10000:10400], color='y')
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.show()

#afisare spectru
plt.figure(figsize=(18, 8))
plt.plot(frecventa[0:5000], magnitudine[:5000]) #spectrul amplitudinii
plt.xlabel("Frecventa (Hz)")
plt.ylabel("Amplitudine")
plt.show()

#refacerea semnalului folosint IFT(domeniul frcventa->timp
#suprapunerea tonurilor pure
f = 1
t = np.linspace(1, 10, 10000)

sin = np.sin(2*np.pi * (f * t))
sin2 = np.sin(2*np.pi * (2*f * t))
sin3 = np.sin(2*np.pi * (3*f * t))

suma_semnal = sin + sin2 + sin3
plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(t, suma_semnal, color='r')

#descompunerea in frecvente armonice
plt.subplot(4, 1, 2)
plt.plot(t, sin)

plt.subplot(4, 1, 3)
plt.plot(t, sin2)

plt.subplot(4, 1, 4)
plt.plot(t, sin3)

plt.show()