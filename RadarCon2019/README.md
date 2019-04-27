# Radar Conference 2019
Disclaimer: If you are the author of any of the images and would not like to share the information, please contact me at `patrickl_at_xsense_dot_ai`.

  * [Monday](#monday)
    + [Tutorial Session I: Machine Learning Technique for Radar ATR (automatic target recognition)](#tutorial-session-i--machine-learning-technique-for-radar-atr--automatic-target-recognition-)
    + [Tutorial Session II: Basic theory of radar detection, and CFAR techniques](#tutorial-session-ii--basic-theory-of-radar-detection--and-cfar-techniques)
  * [Tuesday](#tuesday)
    + [Radar Network](#radar-network)
    + [Waymo](#waymo)
    + [Google](#google)
    + [Accurate Target Localization with automotive radars](#accurate-target-localization-with-automotive-radars)
    + [Comparison of Automotive radar interference mitigation algorithms](#comparison-of-automotive-radar-interference-mitigation-algorithms)
    + [Mount angle calibration](#mount-angle-calibration)
    + [Cognitive interference mitigation](#cognitive-interference-mitigation)
    + [Estimation of Trailer articulation angle with 2d point cloud](#estimation-of-trailer-articulation-angle-with-2d-point-cloud)
    + [RFI detection](#rfi-detection)
    + [Reconstruction of SAR from sensor data](#reconstruction-of-sar-from-sensor-data)
    + [Differentiate true targets from sea clutter](#differentiate-true-targets-from-sea-clutter)
  * [Wednesday](#wednesday)
    + [CT reconstruction with multi-static ground penetration radar (GPR)](#ct-reconstruction-with-multi-static-ground-penetration-radar--gpr-)
    + [RF cls and anomaly detection with CNN](#rf-cls-and-anomaly-detection-with-cnn)
    + [Rain detection with sea radar](#rain-detection-with-sea-radar)
    + [L-corner NLOS (not in direct line of sight) target detection](#l-corner-nlos--not-in-direct-line-of-sight--target-detection)
    + [sparse array selection with CNN](#sparse-array-selection-with-cnn)
    + [Applying DQN for target tracking](#applying-dqn-for-target-tracking)
    + [GO-CFAR trained CNN target detector](#go-cfar-trained-cnn-target-detector)
    + [Deep Radar Detector [**]](#deep-radar-detector-----)
    + [Design Estimation of DoA (degree of arrival) for mutually incoherent arrays](#design-estimation-of-doa--degree-of-arrival--for-mutually-incoherent-arrays)
    + [Mitigation of Vehicle Vibration Effect on Automotive Radar](#mitigation-of-vehicle-vibration-effect-on-automotive-radar)
    + [Two-Dimensional Beamforming Automotive Radar with Orthogonal Linear Arrays](#two-dimensional-beamforming-automotive-radar-with-orthogonal-linear-arrays)
  * [Thursday](#thursday)
    + [DL object classification on automotive radar spectra](#dl-object-classification-on-automotive-radar-spectra)
    + [Personal identification and BMI via Micro-Doppler analysis with DL](#personal-identification-and-bmi-via-micro-doppler-analysis-with-dl)
    + [Cross-frequency classification of indoor activities](#cross-frequency-classification-of-indoor-activities)
    + [multiple patients behavior detection using mmWave](#multiple-patients-behavior-detection-using-mmwave)
    + [Indoor gait asymmetry detection with indoor radar](#indoor-gait-asymmetry-detection-with-indoor-radar)
    + [See multiple heartbeats through the wall](#see-multiple-heartbeats-through-the-wall)
    + [High resolution automotive radar to estimate elevation via interferometry [*]](#high-resolution-automotive-radar-to-estimate-elevation-via-interferometry----)
    + [Passive Activity Classification Using Just WiFi Probe Response Signals](#passive-activity-classification-using-just-wifi-probe-response-signals)
    + [Gesture recognition using Doppler, time and range based features](#gesture-recognition-using-doppler--time-and-range-based-features)
    + [GAN-based synthetic radar micro-doppler augmentation for improved human activity recognition](#gan-based-synthetic-radar-micro-doppler-augmentation-for-improved-human-activity-recognition)
  * [Trivias learned at the RadarCon](#trivias-learned-at-the-radarcon)
      - [People](#people)
      - [Hardware](#hardware)
      - [Radars](#radars)


## Monday

### Tutorial Session I: Machine Learning Technique for Radar ATR (automatic target recognition)
- [Slides](assets/T-03_Machine_Learning_Techniques_for_Radar_ATR.pdf)
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

#### Intro to ML
- [History of DL](https://www.import.io/post/history-of-deep-learning/)
- SAR ATR (SAR has many parameters that can affect radar imagery)
- Object detection are usually provided with a reference image (background) to subtract
- Traditional approaches for SAR ATR is template matching
- Current SOTA on MSTAR cls is DL based and achieves accuracy of 99%
- MSTAR dataset (moving and stationary target acquisition and recognition)
	- 10 target classes with images taken at various angles
	- ~250 images per taget class, per angle (15 for training, 17 for testing. Q: how different is the dataset from diff angles?)
- TrueNorth neuromorphic processor (train model, then export to TN file to deploy on TN processor). EEDN (energy efficient) 

#### Multiple object recognition
- Input: full frame multi-object SAR image with clutter
- Detection (CFAR-based detection)
	- preprocess input image with wavelet transform (optional)
	- Run detector to crop out "chip" of 128x128 pixels
- Classification

#### RF data
- RF data are hard and expensive to collect 
	- radar senspors
	- detailed DOE (collection scenarios
	- Groudtruthing



### Tutorial Session II: Basic theory of radar detection, and CFAR techniques
- [Slides](./assets/T-15_Radar_Detection_Performance_Analysis_and_CFAR.pdf) 
- Presenter: Dr. Augusto Aubry (ra)

#### Basic theory of radar detection
- Slow-fast data matrix
- Under the assumption that the dwell time is short so that the distance to the radar (and thus round trip delay) is constant. 
- Coherent if A and $\phi$ are the same for all pulses.
- Slow-time: Dopler, phase, in-between pulses
- Fast-time: in-between subpulses
- NP detector (Neyman Pearson) detector is the best, but it is not practically implementable. In implementation, we resort to GLRT.


#### CFAR
- This is basically an adaptive thresholding algorithm to keep a constant probability of false alarm independent of the interference pdf parameters. 
- The CFAR filter includes leading/lagging reference windows, guard cells, and a cell under test (CUT). Basically different CFAR algorithms entail manually crafting the filter.  (This needs a lot of fine-tuning of the filters. Maybe CNN can be of help?)
- The CFAR window may be implemented across: range, Doppler, angle, time, and some combination of the above. The CFAR window does not need to have the same size in different dimension.
- Most popular CFAR algorithm is CA-CFAR (cell-averaging) and its variants.
- The vanilla CA-CFAR has the problem of self-masking and target masking, ergo its variants.


## Tuesday

### Radar Network
- David @ UM Amherst, formerly Raytheon
- Dense radar network
- Low altitude gap in existing radar network (due to curvature of the Earth)
![](assets/IMG_1267.jpg.warped.jpg)
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
- finger gestures have easy and intuitive controls, with distinctive advantages compared to other sensors
![](assets/IMG_1269.jpg.warped.jpg)
![](assets/IMG_1273.jpg.warped.jpg)
- Hardware Abstraction Layer (HAL): need to separate hardware specific and hardware agnostic stages
![](assets/IMG_1272.jpg.warped.jpg)


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
![](assets/IMG_1276.jpg.warped.jpg)
![](assets/IMG_1277.jpg.warped.jpg)

### Comparison of Automotive radar interference mitigation algorithms
- Mate Toth @ TU Graz, infineon
- FMCW / chirp sequence radar
- fast: distance, slow: speed, 2D range doppler spectrum
- SINR (signal to inference-plus-noise ratio)


### Mount angle calibration
- @ TI
- sensor calibration: x, y and $\phi$ (only in the azimuth direction), as Z is always pointing up
![](assets/IMG_1278.jpg.warped.jpg)
- Calibration is especially important when
	- multiple radars are installed
	- Used with other sensors (cameras, lidars)
![](assets/IMG_1279.jpg.warped.jpg)
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

### RFI detection 
- classification of images
- imbalanced dataset
- future: compare classifier performance against human baseline, expert performance (have multiple experts mark data)

### Reconstruction of SAR from sensor data
- Ali Gurbuz @ Mississippi State
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
![](assets/IMG_1281.jpg.warped.jpg)

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
![](assets/IMG_1282.jpg.warped.jpg)

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

<!--## Automotive Radar-->
### Deep Radar Detector [**]
- Daniel Brodeski @ GM Isreal
- Imaging radar --> target goal: lidar
- Radar point cloud differs quite a lot even for the same object 
![](assets/IMG_1283.jpg.warped.jpg)
- Statistical nature of radar sensor + user-defined parameters of conventional radar processing techniques
- Conventional pipeline: ADC --> 2D fft --> detection --> beamforming --> cls/object detection
![](assets/IMG_1284.jpg.warped.jpg)
![](assets/IMG_1285.jpg.warped.jpg)
![](assets/IMG_1286.jpg.warped.jpg)
- Goal: use 4D (range, doppler, azimuth and elevation) data directly
![](assets/IMG_1287.jpg.warped.jpg)
- Data (labeled data) --> Data augmentation --> Network --> Training
![](assets/IMG_1288.jpg.warped.jpg)
- Dimension: ant (antenas)
- Use calibration data as training data, but lack diversity, with zero Doppler
- Multiply by a phase shift in range-doppler image (?). This correspondns to a spatial displacement in image domain.
- RD detector uses U-Net, framing the problem as a segmentation
- Used CA CFAR and Bartlett BF (beamforming) as baseline
- RD accuracy ~ CA CFAR, but azimuth and elevation is much better than classical BF
- DL is much more robust to noise
- able to perform detection in 50 FPS
![](assets/IMG_1289.jpg.warped.jpg)
![](assets/IMG_1290.jpg.warped.jpg)
![](assets/IMG_1291.jpg.warped.jpg)
![](assets/IMG_1292.jpg.warped.jpg)
![](assets/IMG_1293.jpg.warped.jpg)
![](assets/IMG_1294.jpg.warped.jpg)
![](assets/IMG_1295.jpg.warped.jpg)
![](assets/IMG_1296.jpg.warped.jpg)
![](assets/IMG_1297.jpg.warped.jpg)
![](assets/IMG_1298.jpg.warped.jpg)
![](assets/IMG_1300.jpg.warped.jpg)

### Design Estimation of DoA (degree of arrival) for mutually incoherent arrays
- David Nunez @ Fraunhofer, formerly @ UCSD
![](assets/IMG_1301.jpg.warped.jpg)

### Mitigation of Vehicle Vibration Effect on Automotive Radar
- Oren Longman @ GM Isreal
- Vibration induce inaccuracies in the estimation in the Moving Object velocity
- Assume vibration in the longitudinal axis
- Traditional: ADC, Range FFT, Doppler FFT, Detector, Digital Beamforming
- proposed method: swap digital BF and Doppler FFT
![](assets/IMG_1304.jpg.warped.jpg)
![](assets/IMG_1305.jpg.warped.jpg)
- Effect of vibration is more pronounced when moving with higher frequency. For 77 GHz it is relatively easy to counter the vibration effect, no so for 300 GHz.
- Main Lobe and Side Lobe in the power-Hz map
- Assumes constant velocity


### Two-Dimensional Beamforming Automotive Radar with Orthogonal Linear Arrays
- Shaogang Wang @ Aurora
- Radar in Reality: high range-Doppler resolution, but low angular resolution
- Hundreds of channels needed for a full planar array
- Achieving high resolution 4D data with affordable hardware
- Mount antennas perpendicularly.
![](assets/IMG_1306.jpg.warped.jpg)
- Resolve in range-doppler image (RDI) domain. Beam matching --> image matching
![](assets/IMG_1307.jpg.warped.jpg)

## Thursday
### DL object classification on automotive radar spectra
- Kanil Patel @ Bosch
- robust to weather and lighting conditions
- DL can be used to replace part of the image processing chain
- Previous arts: Detection --> point cloud --> semantic segmentation
![](assets/IMG_1311.jpg.warped.jpg)
- DL on FFT spectrum for human fall detection, human robot cls, and human pose estimation
- Datasets: 7 objects
- 77 GHz carrier frequency, azimuth resolution 6 degrees 
- Challenges
	- Polar representation of spectra and side lobes of targets
	- Solution: Give CNN the cues to learn the distortions: distance to center map
- Radar spectra varies from frame to frame: use temporal filtering (majority voting) after cls on each frame
![](assets/IMG_1313.jpg.warped.jpg)
![](assets/IMG_1314.jpg.warped.jpg)
![](assets/IMG_1315.jpg.warped.jpg)
![](assets/IMG_1316.jpg.warped.jpg)



### Personal identification and BMI via Micro-Doppler analysis with DL
- Fady Aziz @ Fraunhofer
- Application: surveillance, driver assistance/monitoring in autonomous driving
- Put objects on treadmill. They have the same speed
- Unsupervised learning through convolutional AE, then use t-SNE for dimension reduction
- training/test split done on the same set of subjects --> Confirmed with author that it is if for re-identification this could be understood.
![](assets/IMG_1317.jpg.warped.jpg)

### Cross-frequency classification of indoor activities
- radar monitoring: contactless and no-invasive monitoring (do not need to be worn or to interact with no plain images or videos recorded)
- Asymmetric confusion matrix --> doest this mean premature training?


### multiple patients behavior detection using mmWave
- Feng Jin @ Arizona Univ
- Each subject, 2 to 20 points with mmWave radar
- Doppler-bin vs Time spectrum image.
- One Doppler-time image for each cluster
![](assets/IMG_1318.jpg.warped.jpg)
![](assets/IMG_1319.jpg.warped.jpg)

### Indoor gait asymmetry detection with indoor radar
- Medical gait asymmetry analysis
- manual feature extraction from spectrogram (micro-Doppler vs Time) with machine learning
- Performs better if detected from behind
- Time resolution vs frequency resolution

### See multiple heartbeats through the wall
- 7.3 GHz, detection range up to 3 m
- vital sign monitoring (respiratory cycles, heart rate monitoring)

### High resolution automotive radar to estimate elevation via interferometry [*]
- Stefan Brisken @ ASTYX 
![](assets/IMG_1320.jpg.warped.jpg)
![](assets/IMG_1321.jpg.warped.jpg)
- Put two Tx antennas with vertical offset. Need to have horizontal offset as well due to the size of the antennas
![](assets/IMG_1322.jpg.warped.jpg)
- Use interferometry to find the elevation.
![](assets/IMG_1323.jpg.warped.jpg)
- The elevation information is great feature for DL algorithms
- Design constraints: cost, computational load, power consumption, # channels, packaging constraints
- Very impressive 3D point cloud
![](assets/IMG_1324.jpg.warped.jpg)

### Passive Activity Classification Using Just WiFi Probe Response Signals
- Use wifi signal for monitoring/surveillance.
- Through the wall monitoring as well
- If there is no user on the wifi, then very infrequent handshake so that it does not perform as well as data dense Wifi
- Use a raspberry pi as wifi generator (not relying on connecting to existing Wifi)
- Cls of Doppler Spectrogram with AlexNet
	- Q: seems like the asymmetric features in the different axes of the spectrogram does not matter? 3x3 symmetric kernels seem to work pretty well

	
### Gesture recognition using Doppler, time and range based features
- UCL, collaboration with Project Soli
- Micro-Doppler background info
![](assets/IMG_1325.jpg.warped.jpg)
- Evaluate if keeping the dimension of range will help with cls
![](assets/IMG_1326.jpg.warped.jpg)
- Previously, only micro-Doppler vs time are considered.
- Three different Doppler vs time spectrograms with diff ranges.
- Manually crafted features with classical ML.
![](assets/IMG_1327.jpg.warped.jpg)
![](assets/IMG_1328.jpg.warped.jpg)
- Has not addressed the question of detecting the start and end of the gesture. Cannot deploy without GT.


### GAN-based synthetic radar micro-doppler augmentation for improved human activity recognition
- Sevgi Gurbuz @ Univ of Alabama
- Anchortek radar
- LOS (line of sight); TTW (through the wall)
- eCLEAN, thresholding and convert to grayscale
![](assets/IMG_1329.jpg.warped.jpg)
![](assets/IMG_1330.jpg.warped.jpg)


## Trivias learned at the RadarCon
<!--
#### People
- John Pierro @ Telephonics
- Wolfgang Doerr @ Aptiv
- Euan Ward @ U of Edinburgh
- Thomas Feuillen @ UCL
- Oklahoma Univ has a SOTA radar department mainly because of weather monitoring
- Waymo, Aptiv, Raytheon have great radar staff
-->

#### Hardware
- TI radar
	- provides 3 levels of abstraction: raw data, point cloud and list of tracked objects. Need datacard to extract the raw data
	- at least 5 dim: elevation, dopler, depth, azimuth, SNR
- RadarLog
	- provides raw data, 2D imaging radar
	- RadarLog can work in MIMO mode as well
- ASTYX provides dense point cloud (with adjustable threshold)

#### Radars
- In radar, "detection" means applying the threshold to the ADC. In computer vision, "detection" means drawing bounding boxes around an object.
- **The radar point cloud are usually done after detection and tracking. This is quite different from lidar.**
- Radar imaging
	- Real and imaginary of radar signal: [I and Q](http://www.radartutorial.eu/10.processing/sp06.en.html)
- The direction of arrival (DOA) of all detections in the RD- map are obtained via beamforming (BF). Beamforming requires sensor array calibration, where array responses to targets at various known positions are collected to construct a sensor array calibration matrix.
- The quality of the radar point cloud is mainly determined by the detector and beamforming.
- Multiple user-defined parameters, such as threshold, margin, sizes and shapes of the reference and guard windows determine the performance of the conventional radar signal processing. Automotive radar is required to operate in a variety of significantly different scenes, and therefore, selection of a single optimal set of these parameters is extremely challenging and frequently an impossible task. 
- If radars do not have height information, can we simply discard it and generate birds eye view for 2D bbox (3D localization in CV terms)?




