# Workshop

## [Joint Workshop on Long-Term Visual Localization, Visual Odometry and Geometric and Learning-based SLAM](https://www.youtube.com/watch?v=ZCTxPJPCfF0&feature=youtu.be)
- Daniel Cremers
	- [video and slides](http://cvpr20.com/event/keynote-17/)
	- Startup Artisense: cheap senseors (camera, IMU, GPS) to reconstruct the world
	- Erwin Kruppa in 1913: 5 pts solution
	- Keypoint based methods vs direct method
		- How to deploy DL approaches to boost direct SLAM
	![](assets/sunday/sunday_022.jpg)
	- LSD SLAM: large scale direct SLAM
		- Pose and 3D alternatingly
		- How to do photometric adjustment simultaneously? --> DSO, as second gen of LSD
	- DSO: Direct Sparse Odometry (1% drift): better than ORB-SLAM
		![](assets/sunday/sunday_021.jpg)
	- DL is not SOTA in early works (2017 and 2018)
	- DVSO (deep virtual stereo odometry) (ECCV 2018), mono DVSO on par with St. DSO. Very little scale drift.
	- [D3VO](https://github.com/patrick-llgc/Learning-Deep-Learning/blob/master/paper_notes/d3vo.md)
	- on par with stereo VIO, much crisper than mono DSO
	![](assets/sunday/sunday_020.jpg)
	- [Gasuss Newton Net for multi-weather localization]() ICRA 2020
	- Genealizes quite well. Train on sunny/rainy, and test on sunny/overcast
	![]()
	- Q&A: How to compensate for photo consistency loss when the assumption breaks?
		- predict affine transformation
		- predict a mask where it fails and downweigh
		- predict the changes with nueral network (sunny/rainy)
	- He promotes hybrid approaches
		- Deep learning predicts depth from single image
		- Optimization is powerful and accurate when it is applicable
		- It would be stupid not to use old knowledge
- From SLAM to spatial AI, Andrew Davison
	- Startup SLAMCORE: 
		- robust localization
		- dense mapping
		- semantic undertanding
	- Build semantic maps simultaneously
- Geometric reasoning in Machine vision using only 2D supervision
	- Simon Lucey, Argo
	- Mono image --> CNN --> 3xP + 6 DoF pose
	![](assets/sunday/sunday_007.jpg)
	- Pacal 3D
		- But 3D groundtruth labeling is tedious and difficult (with 3D dictionary)
		- Using simulation will lead to the sim2real gap. 
		- 3D supervision may not capture all the corner cases (limo, etc)
	- Structure from category: lifting chair from 2d to 3d. Much like structure from motion.
	- Just annotate 2D, and 3D structure can be learned inherently.
- Visual slam with deep learning
	- Tomasz Malisiewicz
	- [SuperPoint](https://github.com/patrick-llgc/Learning-Deep-Learning/blob/master/paper_notes/superpoint.md)
		- powerful fully conv design
		- No patches, simultaneous location and descriptor output
		- real time with GPU
		- **No deconv layers, but rather classification** (64+1 dustbin)
		- 15-30 deg rotation during training
	- [Deep ChArUco](https://arxiv.org/abs/1812.03247): detects Charuco patterns in the dark
	- [SuperPoint VO](https://arxiv.org/abs/1812.03245): self improving VO
	- [SuperGlue](https://arxiv.org/abs/1911.11763): get better than motion-guided matching without any motion model.
		- requires both sets of local features; a paradigm shift in matching
		- works better with superpoint and naive matching, in wide baseline matching
	- Quo vadis visual SLAM?
		- multi-user SLAM
		- integrating object recognition into the front end 
- SLAM with plane and objects
	- Sichao Yang, @Facebook, CMU
	- point-based methods 
		- Works well in normal condition (Orb-slam, DSO)
		- too sparse to detect car in driving
		- challenging for low-texture place	
	- Background
		- optimization method: decoupled (regress pose, then detect) and tightly coupled
		- object representation: no shape prior (cuboid, sphere, ellipsoid), weak prior (skeleton) and accurate prior (3D cad)
			- if not 100% sure if the object matches the 3D CAD, it is hard to use silouette loss. We could use shape encoder to adjust the 3D instances. 
		- optimization cost
	- **Single view detection, and multiview for optimization**
		- [CubeSLAM: Monocular 3D Object SLAM](https://arxiv.org/abs/1806.00557)
		- **Tracking with keypoint within object (maybe w/ optical flow)**. Much better than bbox based approach.
		- Fixed object size assumption.
		- For indoor environment looks fabulous. Do not need explicit loop closure to get good performance. 
		- Dense map just reproject the image onto the plane. --> Can we do the same for moving cars?
		- **Dynamic object SLAM**
- Tracking without vision
	- Jakob Engel
	- TLIO: tight learned inertial odo
	- Why useful? low power, privacy
	- IMU measures the rotaitonal velocity and linear acc. Integrating rotational velocity and double-integrating linear acc.
	- conventional VIO
	![](assets/monday/monday_12.jpg)
	- long term drift of IMU is huge. Can we replace vision with another source of information?
		- attach to the foot or wrist and
		- ML to learn how people move
			- RIDI (robust IMU double integration)
	- TLIO motion model learning: use network to odometry (only displacement vector) in 1s from IMU input, used together with EKF
- [Upgrading optical flow to scene flow](http://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_Upgrading_Optical_Flow_to_3D_Scene_Flow_Through_Optical_Expansion_CVPR_2020_paper.pdf)
	- [youtube talk](https://youtu.be/aOkLGcspoyY?t=24046)
	- Deva Ramanan@CMU, Argo AI
	- optical flow vs scene flow
	![](assets/monday/monday_13.jpg)
	![](assets/monday/monday_14.jpg)
	- Scale changes reveal relative detph
		- Now eliminates 1 DoF, we know the direction of the 3D scene flow
	- Depth uncertainty
		- uncertainty through discretization
		- Stitching depth map based on confidence score
	![](assets/monday/monday_15.jpg)
- [Monocular 3D](https://youtu.be/aOkLGcspoyY?t=28052	)
	- Xiaoming Liu@MSU
	- Monocular [image based](https://github.com/patrick-llgc/Learning-Deep-Learning/blob/master/paper_notes/m3d_rpn.md) and [video based](kinematic 3d object detection in monocular video) (under review) 3D object detection 
	- kinematic 3D object detection with mono videos
	![](assets/monday/monday_16.jpg)
	![](assets/monday/monday_17.jpg)
	- use a 3D kalman filter to limit constraints
	![](assets/monday/monday_18.jpg)
	![](assets/monday/monday_19.jpg)
	- Video based 2D/3D object detection
		- physical model constrained only to move in the direction of orientation
		- Self-balancing IoU that encourages higher conf for better IoU (localization)
		![](assets/monday/monday_21.jpg)
		- overall architecture
		![](assets/monday/monday_22.jpg)
	- limitation in mono3D is mainly due to poor localization (at lower IoU threshold, recall is higher)
	![](assets/monday/monday_23.jpg)


## [Safe Artificial Intelligence for Automated Driving](https://sites.google.com/view/saiad2020/home?authuser=0)
- [conference page with videos and slides](http://cvpr20.com/safe-artificial-intelligence-for-automated-driving/)

## [Learning and understanding single image depth estimation in the wild](https://sites.google.com/view/cvpr-2020-depth-from-mono/home/talks-slides?authuser=0)
All talks and slides are uploaded.

## [Visual Recognition for Images, Video, and 3D](http://s9xie.github.io/Tutorials/CVPR2020/)
All talks and slides are uploaded.


## [All About Self-Driving](http://www.allaboutselfdriving.com/)
- Hardware
	- Ultrasound: only one measurement, spherical distance, can use cross-echo to boost performance.
	- microphone: provide early alert to sirens, background noise signature, limited geometry with beam forming
- End to end vs traditional stck
	- Maps/Sensors --> Perception --> Prediction --> Planning --> Control
	- Interpretable intermediate representation
- 3D Perception:
	- Lidar: 
		- 3d voxel: keeps metric space, but large sparsity, and computation grows cubically
		- range view: compact, panorama range for lidar. Efficiently processable by 2D CNN. Hard to incorporate prior knowledge
		- BEV: also sparse, can use 2D conv efficiently
		- point set: preserve point location; harder to learn; irregular memory access and dynamic kernel computation
		![](assets/sunday/sunday_018.jpg)
	- Sparse convolution, sparse block convolution; use road map mask and object mask to speed up computation
	- One stage (real time, but less accurate) and two stage
		- PIXOR
	- Mono3D:
		- Lift to 3D at output: unsatisfactory
		- Lift to 3D at input: pseudo-lidar
		- Lift to 3D at feature map: OFT, can work without depth estimation. Reason depth in feature map
	- Fusion lidar/camera
		- Fusion in Cascade: F-pointnet, can be hard for occluded object
		- Fusion at output: safety from redundancy, mono3D + lidar3D
		- Fusion at input: pointpainting, limited exploitation of camera data
		- Fusion at Feature: PointFusion, ContFuse; more robust to small calib errors; more computation cost
	- Radar
	![](assets/sunday/sunday_016.jpg)
	![](assets/sunday/sunday_017.jpg)
	- HD maps
		- Geometric correction by subtracting ground height
		- raster map (CheuffeurNet)
		- Lane graph (vector net)
	![](assets/sunday/sunday_015.jpg)
	![](assets/sunday/sunday_014.jpg)
	![](assets/sunday/sunday_013.jpg)
	- Detecting the unknown by projecting to an semantic-agnostic space
	![](assets/sunday/sunday_012.jpg)
- Prediction
	- tradditional
		- Unroll the tracker's state with a kinematic model (linear motion model, constant turn rate, etc)
		- Maneuver-based, classify first
	- Using neural network for prediction, with HD map
	![](assets/sunday/sunday_011.jpg)
	- Joint perception and prediction
		- [Fast and Furious]()
		- [IntentNet]()
	- Predicting each object individually may lead to collision
	- Using social pooling to extract social vector to model interaction
	- Trajectory uncertainty and multi-modality
	- mixture of Gaussian, occupancy grid, **trajectory sets** (coverNet; seems most promising), Auto-regressive (R2P2, trajectron; slow, compounding error)
	![](assets/sunday/sunday_010.jpg)
	- Use prior knowledge in precise multimodal prediction; less off road/map behavior
	- Scene-coherent sampling: social auto-regressive methods, using states of other actors when unrolling. Alternatively, ILVM (implicit latent variable model for scene-consistency motion forecasting) can be used for parallel sampling.
	![](assets/sunday/sunday_001.jpg)
- Motion planning and control
	- Route, behavior, trajectory planning
	- Route planning: A*, Dijkstra algorithm
	- Behavior planning: reduce complexity in trajectory planning
		- State machine: hard to generalize
		- Optimal driving corridor
	![](assets/sunday/sunday_009.jpg)
	- Trajectory planning: 
		- Continuous optimization (variable execution time, problematic for safety-critical applications)
		![](assets/sunday/sunday_009.jpg)
		- Sampling based methods (suboptimal solution)
	- Control
		- Path following
		- Model predictive control
	- Learned joint planning and control
- Building HD Maps
	- Human annotation is extremely tedious. 
	- Using DL to help automate the process
- Localization within HD Maps
	- GNSS, camera, lidar, IMU, wheel odo
	- topological maps (openstreetmaps)
	- challenges: sensor noise, dynamic objects, degenerate geometry, environment changes (construction site)
	- minimal (3 DoF lat, long, yaw) vs complete 6 DoF
	- Localization as State Space Estimation
	- Bayesian filter: Usually not tractable in practice
		![](assets/sunday/sunday_004.jpg)
		![](assets/sunday/sunday_002.jpg)
		![](assets/sunday/sunday_003.jpg)
		- Kalman filter: efficient, compact, but gaussian-like and unimodal (single hypothesis tracking)
		- Particle filter: non-parametric, any distribution, supports multi-modal, but may suffer from mode collapse due to insufficient sampling
		- Histogram filter: any distribution, multi-modal, avoids unimodal collapse, but memory intensive
	- Existing methods: (6 methods)
		- RTK: need direct satellite LoS
		- Semantic matching: light weight maps, cannot achieve cm level 
		- geometric alignment: lidar to 3D HD map: need a good initialization; storage of detailed HD Map is expensive; can degenerate in tunnels
		- Camera to lidar matching: map with Lidar, match with camera; cm accuracy;
		- place recognition: image retrieval; not cm level accuracy
		- Lidar reflectance matching: need good initialization; can be robust to outliers, and can be implemented efficiently; vulnerable to lidar mis-calibration
	- Recent methods: 
		- [learn to localize with lidar to HD map matching](http://openaccess.thecvf.com/content_CVPR_2019/papers/Wei_Learning_to_Localize_Through_Compressed_Binary_Maps_CVPR_2019_paper.pdf) (CVPR 2019): main drawback is the large storage space of HD Map. Learn compressed representation with DL. (3 orders of magnitude less space, with marginal degradation in accuracy.)
	- Global localization
		- Initialization, and recovery
		- Challenges: the same place can be different, weather, time of day, season, etc
		- Pose regression/retrieval-based


## [A Comprehensive Tutorial on Video Modeling](https://bryanyzhu.github.io/videomodeling.github.io/)
- Human activity understanding in videos
	- Controlled collection vs In the wild
	- Trimmed and untrimmed: are there irrelavant information in video?
	- Single person vs multi-person
	- **Temporal action detection**: automatic highlight extraction 
		- Input: untrimmed video
		- output: start and end timestamps, and action labels
		- Strongly supervised vs weekly supervised
	- Action segmentation:
		- Similar to temporal detection
		- output: action segmentation per frame. 
	- Online vs offline
	- Modeling longer timespan
		- RNN or 3D CNN: but still intractable to model longer sequence
		- one solution: temporal segment network: model from sparse sampling
		- attention vs graph conv
			- to address regular conv (computation efficiency)
			- non-local CNN
			- ST-GCN (spatial-temporal graph conv networks)
	- Efficiency:
		- pseudo-3D conv
		- Decoupled 3D conv
- Recent SOTA (2014-2020)
	![](assets/sunday/sunday_005.jpg)
	- DeepVideo by Karpathy: fovea and context streams
	- Two stream methods: spatial stream + temporal stream (single frame + optical flow)
		- But optical flow calculation and loading I/O slows down training and inference
	- 3D CNN
		- C3D
		- I3D (inflating and boostraping)
		- P3D: factorize 3x3x3 into simpler kernels
		- non-local
		- slow-fast (cf. two stream models. slow-fast models two temporal speeds, not spatial and temporal modeling)
		- X3D: improved slimmed slow-fast
	- Other works:
		- Directly inferencing video codec
		- draw inspiration from optical flow, and use CNN to learn optical flow on the side 
		- [TSM: Temporal Shift Module for Efficient Video Understanding](http://openaccess.thecvf.com/content_ICCV_2019/papers/Lin_TSM_Temporal_Shift_Module_for_Efficient_Video_Understanding_ICCV_2019_paper.pdf): temporal shift, suitable for video object detection and edge deployment. 
- Decord: An Efficient Video Reader for Deep Learning
	- Decoding videos to frames
		- takes 10x more space
		- I/O bottleneck
		- Data storage is huge!
	- Random access > sequential read.
	- CPU or GPU loading.
	- pythonic
	- Can be used in many DL frameworks, including pytorch.

	
## [SCALABILITY IN AUTONOMOUS DRIVING](https://sites.google.com/view/cvpr20-scalability) ([video on youtube](https://www.youtube.com/watch?v=XvTS57jJQF8&feature=youtu.be))
- Scaling data and data scaling (with simulation and GAN)
	- Paul Newman, Oxbotica & University of Oxford
	- The four questions of AD
	![](assets/monday/monday_01.jpg)
	- Simulator: lidar data is easy to simulate
	- Experience: drive around the same scene again and again. Self-labeling source via localization + Map: We know where we are, and we know where to look
		- Open-loop Maps are free
		- Copy road markers to 2D images
		- Vision + geometry: depth groundtruth
		- This needs to have fully labeled video, and need highly precise localization (< 0.1 deg for YPR)
	![](assets/monday/monday_02.jpg)
	- Data synthesis. Generate scenes with semantic maps, learning to in-paint
		- cycleGAN: not necessarily easy to train, need to tune
		![](assets/monday/monday_03.jpg)
		![](assets/monday/monday_04.jpg)
		![](assets/monday/monday_05.jpg)
		![](assets/monday/monday_06.jpg)
		- Use semantic map to modulate what to manipulate
		- class swapping (tree to and from building)
- Andrej Karpathy
	- Tesla Autopilot
	- Navigate on Autopilot
	- Stops on Autopilot
	![](assets/monday/monday_07.jpg)
	- Vision based approach
		- No lidar, no HD maps (self-built minimalistic HD maps)
	- For Chinese market
	![](assets/monday/monday_08.jpg) 
	![](assets/monday/monday_09.jpg) 
	- Driving with HD map can be a burden: need to maintain HD Maps	
	![](assets/monday/monday_11.jpg) 
	- Corner cases
	![](assets/monday/monday_10.jpg) 
	
	
	
	