# Radar Summer School (RadarCon2019)
## Introduction to Radar Signal Processing
### Basic concepts
- First radar by Hüilsmeyer 1904 (detection with reflected EM wave
- Palindrome radar (mimicking transmission and reflecting?): radio detection and ranging, first coined in 1941
- Resolve two objects if $\Delta R = c \tau / 2 = c / (2B)$, where $\tau$ is pulse duration, and also echo duration; B is the bandwidth.
- **To resolve better, we need shorter pulse, and broader band.**
- Azimuth resolution: $R \lambda / d$, angular resolution $\lambda / d$ in radians. If d = 10 $\lambda$, then angular resolution is about 1/10 radian, or 6 degrees.
- High resolution radar: high res in distance (through broad-bandwidth pulses) and in azimuth (through synthetic aperture processing)
- range ambiguity (maximum target range, using long pulse repetition frequency) and eclipsing (minimum target range)
- L radar band (1-2 GHz)

## Radar Imaging
- High resolution radar
- A single dot (detection) --> high range resolution radar (range cells) --> 2D imaging radar with high range and azimuth resolution
- When high resolution is achieved in 2D, a target image image can be obtained
- Wide antenna aperture needed for high azimuth (cross range)/angle resolution
- Pulse compression: maintaining high energy while keep pulse short for high range resolution
- Sometimes cannot build physically large aperture, therefore need high synthetic aperture radar. $\delta \theta \approx \lambda /R$.
- Antenna arrays have wider antenna aperture --> move one array to build a synthetic array (synthetic aperture), under the assumption that the scene does not change
- Darker for smoother surface (oil slick and airport runway). Buildings usually have higher intensity due to trihedrals (radar reflector).
- Spotlight SAR: The antenna can be steered toward the object to get better resolution
- SAR vs ISAR: If the aperture is known, then SAR. Use radar to detect object that is not under the observer's control, therefore the aperture is unknown (ISAR). 
- Sometimes both radar (airborne, eg) and target (ship on the sea, eg) are moving and the aperture is unknown.
- Using SAR will cause motion blur for moving objects. Use ISAR will bring radar image into focus.

## Radar Waveforms
- Range resolution depends on bandwidth/pulse length. Energy needs pulse to be long, but then range (fast time) resolution need the pulse to be short.
- Waveform decouples the range resolution and energy
- Waveform: FM or AM are common forms of modulation
- Range resolution is generally measured at 3dB below main lobe.
- Drawback of AM
- LFM (upchirp or downchirp)
- Phase coded
- Frequency coded
- types of waveforms: Say you have a carrier signal given by 𝑥(𝑡)=𝐴⋅cos(2𝜋𝑓𝑡+𝜑)
	- There are three obvious ways to encode data onto this signal:
		- Varying 𝐴: This is Amplitude Modulation.
		- Varying 𝑓: This is Frequency Modulation.
		- Varying 𝜑: This is Phase Modulation.

## Array Signal Processing
- Array Configuration: 
	- Sensor radiation pattern: isotropic or directive
	- Array Geometry (1D, 2D, 3D), sensor location pattern
- Spherical waves in nearfield, plane waves in farfield
- Beamforming: array processing algorithm that focus the array's signal capturing abilities in a particular direction
- Beam forming for a particular direction $\theta_0$ can boost the signal by N and increasing SNR. The array coefficients can be carefully chosen to offset the phase shift for signals arriving at different elements and thus coherently combine them. (This is better than mechanically rotating array).
	- This only requires HW to implement **phase shifters**. (You can also do time delays.)
	- Alternatively, you can say that the array has been steered to look in direction $\theta_0$.
- In many applications, we want to adjust the gain to adjust the side lobe pattern.
- Narrow band condition: as long as the longest time of arrival difference is much smaller than ???
- Capon and MUSIC beamforming







