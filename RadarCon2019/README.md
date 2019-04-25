# Radar Conference 2019
## Monday

### Tutorial Session I: Machine Learning Technique for Radar ATR (automatic target recognition)
- [Slides](assets/T-03 Machine Learning Techniques for Radar ATR.pdf)
- Speaker: Uttam Majumder, Air Force Research Laboratory (ra)
	- Identify objects in RF imagery, SAR image (classification, ATR)
	- Neuromorphic processor implementation
	- Multi-target
- RF ML
	- Radar ATR (DARPA TRACE program)
	- RF parameter estimation
	- RF comm signal cls
- Challenges
	- Train with limited data while maintain desired accuracy
	- Robust performance (adversarial machine learning) in extended operating conditions (environments, sensors, target types)
	- Real-time training (federated learning, distributed learning)
	- Energy efficient ML computing (IBM TrueNorth, Intel Loihi)
	- Radar is more robust than images (works under rainy/snowy days)
- Recent DARPA initiatives
	- CAML: compentancy aware ML
	- RTML: real time machine learning
- Open dataset (MSTAR, that is perhaps the only one with ~1000 images)
	- [ML on MSTAR](https://github.com/hunterlew/mstar_with_machine_learning)
	- [DL on MSTAR](https://github.com/hunterlew/mstar_deeplearning_project)
- DARPA
	- model based approach to generate radar imagery (Q: what modality captured those arial imagery? SAR)

### Intro to ML
- [History of DL](https://www.import.io/post/history-of-deep-learning/)
- SAR ATR (SAR has many parameters that can affect radar imagery)
- Object detection are usually provided with a reference image (background) to subtract
- Traditional approaches for SAR ATR is template matching
- Current SOTA on MSTAR cls is DL based and achieves accuracy of 99%
- MSTAR dataset (moving and stationary target acquisition and recognition)
	- 10 target classes with images taken at various angles
	- ~250 images per taget class, per angle (15 for training, 17 for testing. Q: how different is the dataset from diff angles?)
- TrueNorth neuromorphic processor (train model, then export to TN file to deploy on TN processor). EEDN (energy efficient) 

### Multiple object recognition
- Input: full frame multi-object SAR image with clutter
- Detection (CFAR-based detection)
	- preprocess input image with wavelet transform (optional)
	- Run detector to crop out "chip" of 128x128 pixels
- Classification

### RF data
- RF data are hard and expensive to collect 
	- radar senspors
	- detailed DOE (collection scenarios
	- Groudtruthing



### Tutorial Session II: Basic theory of radar detection, and CFAR techniques

- [Slides](./assets/T-15 Radar Detection, Performance Analysis, and CFAR.pdf) 
- Presenter: Dr. Augusto Aubry (ra)

### Basic theory of radar detection
- Slow-fast data matrix
- Under the assumption that the dwell time is short so that the distance to the radar (and thus round trip delay) is constant. 
- Coherent if A and $\phi$ are the same for all pulses.
- Slow-time: Dopler, phase, in-between pulses
- Fast-time: in-between subpulses
- NP detector (Neyman Pearson) detector is the best, but it is not practically implementable. In implementation, we resort to GLRT.


### CFAR
- This is basically an adaptive thresholding algorithm to keep a constant probability of false alarm independent of the interference pdf parameters. 
- The CFAR filter includes leading/lagging reference windows, guard cells, and a cell under test (CUT). Basically different CFAR algorithms entail manually crafting the filter.  (This needs a lot of fine-tuning of the filters. Maybe CNN can be of help?)
- The CFAR window may be implemented across: range, Doppler, angle, time, and some combination of the above. The CFAR window does not need to have the same size in different dimension.
- Most popular CFAR algorithm is CA-CFAR (cell-averaging) and its variants.
- The vanilla CA-CFAR has the problem of self-masking and target masking, ergo its variants.


## Tuesday

### Planetary Session
David @ UM Amherst, @ Raytheon
- Dense radar network
- Low altitude gap in existing radar network (due to curvature of the Earth)
- Only 30% of the first 1km is covered in aviation
- Raytheon product: Skyler x-band (9Ghz) 2D electronic scan
- Spectrum pressure (X-band under-utilized)

### Waymo
- Matt Markel @ Waymo, formerly Raytheon
- Radar is key to autonomous driving cars
- "Asking people to take over when necessary" simply does not work. Waymo targets to take human out of the picture entirely
- Driver assistance --> partial --> conditional --> highly autonomous --> fully autonomous
- 4 areas:
	- Localization: where am I
	- Perception: what is around me (x-views? tool by Waymo for planning) 
	- Behavior planning: what is about to happen
	- Motion planning: what am I gonna do
- Challenges and solutions for Radar
- Unprotected turns (left)
- Recall == Safety, Precision == Comfort (High Pd, Low Pfa)
- Bridge and Signs: can you detected stopped small vehicle under a large bridge or sign at a safe distance? Elevation resolution, angular resolution
- 6 Radar (76-81 GHz): how to avoid interference (RFI, jamming)?
	- Turn on radar as needed to avoid jamming
	- As much anti-jam capability as possible
- MIMO can increase angular resolution, fewer receiver to achieve the same resolution
- Data: range, Doppler, Spatial
	- 20 Gbps or greater data
	- centralized processing

#### Trivials
- Cars are parked 95% of the time, 60% car trips are one mile or less
- 160 billion $ in time and gas loss due to traffic jam
- 94% of traffic accident involves human error -- Why is Waymo doing autonomous driving
- Waymo 10 x 100,000 mile
- 2017 collaboration with Chrysler
- 10 million miles in the past 10 years on public roads

### Google
- Jian Wang @ Google, system lead for Project Soli, formerly at Raytheon
- Automotive radars: a few watts, ARS4-A, Bosch LRR4
- Fast time, slow time, channel
- Hardware Abstraction Layer (HAL): need to separate hardware specific and hardware agnostic stages
- finger gestures have easy and intuitive controls



## Automotive Radar Session
### Accurate Target Localization with automotive radars
- Faruk Uysal From TU Delft
- Low angular estimation
	- Due to limited number of antennas
	- insufficient onboard processing power
- Bridge, car (elevation resolution)
- Current solution:
	- super resolution (MUSIC, or iterative approach, etc), drawback: calculation
- For single target use MIMO monopulse approach to improve angular resolution
- Demo for cyclist detection

### Comparison of Automotive radar interference mitigation algorithms
- Mate Toth @ TU Graz, infineon
- FMCW / chirp sequence radar
- fast: distance, slow: speed, 2D range doppler spectrum
- SINR (signal to inference-plus-noise ratio)



### Mount angle calibration
- @ TI
- sensor calibration: x, y and $\phi$ (only in the azimuth direction), as Z is always pointing up
- Calibration is especially important when
	- multiple radars are installed
	- Used with other sensors (cameras, lidars)
- Manual calibration (with 3 objects with known reletive position). drawback: need to recalibrate often, tedious
- automatic calibration
	- Occupancy grid map (transitional techniques)
	- Find angle that minimizes the smearing of a point object in an occupancy map
- Elevation calibration is not accounted for currently

### Cognitive interference mitigation
- Cognitively allocate chirps to minimize the interference.

### Estimation of Trailer articulation angle with 2d point cloud
- Articulation angle $\theta$ is the trailer's rotational deviation from the reference plane
- Two sets of 2D point cloud with some noise, how to estimate the angle?
	- OLS: rotational variant! (why not using TLS)
	- PCA to extract the principal axis
	- MLE




## Machine Leanring in Radar
### RFI detection 
- classification of images
- imbalanced dataset
- future: compare classifier performance against human baseline, expert performance (have multiple experts mark data)

### Reconstruction of SAR from sensor data
- Ali Gurbuz @ Mississippi state
- sensor domain and image domain
- Complex sensor data --fc layer--> proxy images --CNN--> reconstructed image
- Used CIFAR-10 to pre-train data, then apply on MSTAR dataset


### Differentiate true targets from sea clutter
- True targets (ships, RIB) vs Wave targets
	- Longer trajectory, less variance in number of objects
	- Shorter trajectories, high variance
- conventional methods: adaptive thresholding
- proposed method: integration of temporal information


## Wednesday
### CT reconstruction with multi-static ground penetration radar (GPR)
- Tian Xia @ Univ. of Vermont
- Ground coupled GPR has better resolution than air launched GPR, but moves slowly (manual vs vehicle mounted)
- Multistatic (multi transimtter tx and multi receiver rx): spatial diversity, facilitate wide sensing coverage and fast 3D formation

### RF cls and anomaly detection with CNN

- Marvin Conn @ US Army Research Lab
- RF spectrum is a limited and critical resource for sensing and communication
- waveform classification and waveform anomaly detection

### Rain detection with sea radar
- Feature: normalized histogram from image
- SVM for classification

### L-corner NLOS (not in direct line of sight) target detection
- X-band//mmWave/THz radar cannot be used in through wall detection (due to wavelength)
- L-band UWB (Utra Wide-Band) radar (600 MHz bandwidth, 1~2 GHz)
- CA-CFAR detection algorithm
- EM wave propagation model for L band, and model-based target loalization


## Cognitive Radar
### sparse array selection with CNN
- Uses CNN to approximate complex function for quick inference
- Cognitive radar: adjust transceiver and receiver according to context
- Combinatorial search of sparse array
- Labeling data: with Cramer Rao Bound (conventional algorithm)
- data: Real, Imaginary, Phase (Amplitude did not help much)
- Q: many binary head for the CNN?

### Applying DQN for target tracking
- the wider the bandwidth, the higher the resolution
- Define states (environment, interference), actions and reward (SINR)
- Previously: Policy iteration --> DQN
- Num of states increases exponentially as num of bands and num of memory increases
- DQN performs better than Policy iteration in determining the optimal policy (previous methods needs to build enough statistics to switch)
- Input: states
- Handles more memory without increasing computational complexity
- What are the Action? --> which transmitters to use. 

### GO-CFAR trained CNN target detector
- Replace CFAR with a NN
- Input: CFAR window, output: threhsold
- Use GO-CFAR as a training mentor (generate label). 
- Why not using GT? --> CFAR has the constant false alarm property. Using label may be more challenging. 

## Automotive Radar
### Deep Radar Detector
- Daniel Brodeski @ GM Isreal
- Imaging radar --> target goal: lidar
- Radar point cloud differs quite a lot even for the same object 
- Statistical nature of radar sensor + user-defined parameters of conventional radar processing techniques
- Conventional pipeline: ADC --> 2D fft --> detection --> beamforming --> cls/object detection
- Goal: use 4D (range, doppler, azimuth and elevation) data directly
- Data (labeled data) --> Data augmentation --> Network --> Training
- Dimension: ant (antenas)
- Use calibration data as training data, but lack diversity, with zero Doppler
- Multiply by a phase shift in range-doppler image (?). This correspondns to a spatial displacement in image domain.
- RD detector uses U-Net, framing the problem as a segmentation
- Used CA CFAR and Bartlett BF (beamforming) as baseline
- RD accuracy ~ CA CFAR, but azimuth and elevation is much better than classical BF
- DL is much more robust to noise
- able to perform detection in 50 FPS


### Design Estimation of DoA (degree of arrival) for mutually incoherent arrays
- David @ Fraunhofer

### Mitigation of Vehicle Vibration Effect on Automotive Radar
- Oren Longman @ GM Isreal
- Vibration induce inaccuracies in the estimation in the Moving Object velocity
- Assume vibration in the longitudinal axis
- Traditional: ADC, Range FFT, Doppler FFT, Detector, Digital Beamforming
- proposed method: swap digital BF and Doppler FFT
- Effect of vibration is more pronounced when moving with higher frequency. For 77 GHz it is relatively easy to counter the vibration effect, no so for 300 GHz.
- Main Lobe and Side Lobe in the power-Hz map
- Assumes constant velocity


### Two-Dimensional Beamforming Automotive Radar with Orthogonal Linear Arrays
- Radar in Reality: high range-Doppler resolution, but low angular resolution
- Hundreds of channels needed for a full planar array
- Achieving high resolution 4D data with affordable hardware
- Mount antennas perpendicularly.
- Resolve in range-doppler image (RDI) domain. Beam matching --> image matching


	


## Trivias learned at the RadarCon

#### People
<!--
- John Pierro @ Telephonics
- Wolfgang Doerr @ Aptiv
- Euan Ward @ U of Edinburgh
- Thomas Feuillen @ UCL
- 
-->

#### Stuff
- TI radar
	- provides 3 levels of abstraction: raw data, point cloud and list of tracked objects. Need datacard to extract the raw data
	- at least 5 dim: elevation, dopler, depth, azimuth, SNR
- RadarLog
	- provides raw data, 2D imaging radar

#### Radars
- In radar, "detection" means applying the threshold to the ADC. In computer vision, "detection" means drawing bounding boxes around an object.
- Radar imaging
	- Real and imaginary of radar signal: [I and Q](http://www.radartutorial.eu/10.processing/sp06.en.html)
	- The direction of arrival (DOA) of all detections in the RD- map are obtained via beamforming (BF). Beamforming requires sensor array calibration, where array responses to targets at various known positions are collected to construct a sensor array calibration matrix.
	- Notice that the quality of the radar point cloud is mainly determined by the detector and beamforming.
	- Notice that multiple user-defined parameters, such as threshold, margin, sizes and shapes of the reference and guard windows determine the performance of the conventional radar signal processing. Automotive radar is required to operate in a variety of significantly different scenes, and therefore, selection of a single optimal set of these parameters is extremely challenging and frequently an impossible task. 

