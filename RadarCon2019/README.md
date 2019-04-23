# Radar Concerence 2019
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
- [Slides](assets/T-15 Radar Detection, Performance Analysis, and CFAR.pdf) 
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


### Misc
#### People
<!--
- John Pierro @ Telephonics
- Wolfgang Doerr @ Aptiv
- Euan Ward @ U of Edinburgh
- Thomas Feuillen @ UCL-->

#### Stuff
- TI radar
	- provides 3 levels of abstraction: raw data, point cloud and list of tracked objects. Need datacard to extract the raw data
	- at least 5 dim: elevation, dopler, depth, azimuth, SNR
- RadarLog
	- provides raw data, 2D imaging radar