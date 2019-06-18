# 2019 CVPR
## 06/25/2019 (Saturday)

- ICML last day
- CARLA AD challenge. agents are dockerized and submitted to evaluation systems.

#### Aurora
- "fuel the rockers": Building rockers vs ladders to the moon
- Learn from Demonstration, mimic human behavior (imitation learning)
- failure modes
	- radar in a tunnel
	- lidar in a snowstorm
	- camera at dusk/night
- decision making: non-compliance
- Why other to use imitation learning when you have simulation/RL learning.
	- Global exploration is extremely hard. Mimic good behaving drivers
- Statistical learning assumptions breaks in sequential setting (IID does not hold)
	- no training data in recovery mode
	- DAggr (Dataset Aggregation), learn by expert intervention

	
## 06/26/2019 (Sunday)
### Tutorial: Learning Representations via Graph-structured Networks
- Learnable Spatial Propagation Networks - Sifei Liu and Ming-Hsuan Yang
- **Note** Good paper on depth propagation from [Baidu](https://arxiv.org/pdf/1810.02695.pdf)
- Non-Local vs spatial propagation (less connections)
- 1D SPN (ECCZV2016), 2D SPN, unstructured SPN
- 1D: each row/column in image as a single
	- FIR: conv, IIR: long range
- **NOte**: read up on this page later https://xiaolonw.github.io/graphnn/

### Workshop on Autonomous Driving -- Beyond Single-Frame Perception
- Lyft: Kumar hockey stick growth
- Incorporate knowledge into driving (static/dynamic objects)
![](assets/sunday/IMG_1534.jpg.warped.jpg)
![](assets/sunday/IMG_1535.jpg.warped.jpg)
- Geometric Map (camera + lidar) vs Visual Geometric Map (SfM)
- Two 9's accuracy with CV, but 4s's with human curation


### Workshop: CARLA
- Drago@Waymo
- What is the input representation for powering realsunday/sunday/IMGistic agents?
	- realistic perception (CARLA)
	- box world (ChauffeurNet)
- Is pure imitation sufficient? 
	- DAGGER: not good in practice
	- ChauffeurNet solution: synthesize perturbation, 
![](assets/sunday/IMG_1538.jpg.warped.jpg)
- What is the metric for success?
- How to model non-average agent
- **Note**: RL may be good for ego car, but imitation is needed for agent modeling
- Google is going to open source a huge dataset in July
![](assets/sunday/IMG_1536.jpg.warped.jpg)

#### Andrej Karpathy
- Autonomous driving stack and AI
![](assets/sunday/IMG_1555.jpg.warped.jpg)
- Data collection pipeline
![](assets/sunday/IMG_1556.jpg.warped.jpg)
![](assets/sunday/IMG_1559.jpg.warped.jpg)
![](assets/sunday/IMG_1560.jpg.warped.jpg)
- 30-40 different tasks. each task has additonal sub-tasks.
- Architecture considerations
	- every single task have network: expenseive in inference, no feature sharing, potential overfitting, but decoupled functinality
	- Single backbone with multiple head: cheaper in test, but fight for capacity, sometimes. fully coupled functionality.
	- Partially shared backbone? backbone used during training but not in testing
	- Temporal component: unrolled hybrid architecture
![](assets/sunday/IMG_1561.jpg.warped.jpg)
![](assets/sunday/IMG_1562.jpg.warped.jpg)
![](assets/sunday/IMG_1563.jpg.warped.jpg)
![](assets/sunday/IMG_1564.jpg.warped.jpg)
![](assets/sunday/IMG_1565.jpg.warped.jpg)
![](assets/sunday/IMG_1566.jpg.warped.jpg)

- Loss considerations
	- more than 200 losses in total!
	- How to do weighting factor $\lambda$ saerch?
	- Tasks have different scale, importance, difficulty, have more data, more noise, etc...
	- Single task: early stopping. But how about multiple loss?
![](assets/sunday/IMG_1567.jpg.warped.jpg)
![](assets/sunday/IMG_1568.jpg.warped.jpg)
![](assets/sunday/IMG_1569.jpg.warped.jpg)
- Team assignment
	- How can multiple task owners iterate on one neural network?
	- big problem: reproducibility: track workflow
![](assets/sunday/IMG_1572.jpg.warped.jpg)
![](assets/sunday/IMG_1573.jpg.warped.jpg)
![](assets/sunday/IMG_1575.jpg.warped.jpg)
![](assets/sunday/IMG_1576.jpg.warped.jpg)
![](assets/sunday/IMG_1578.jpg.warped.jpg)
- Make each increment buildable, use distributed training for fast testing
![](assets/sunday/IMG_1579.jpg.warped.jpg)
![](assets/sunday/IMG_1580.jpg.warped.jpg)
![](assets/sunday/IMG_1582.jpg.warped.jpg)
![](assets/sunday/IMG_1583.jpg.warped.jpg)
- **Note**: You can only develop as fast as you can evaluate. The team can only move as fast as your evaluation allows. So it is critical to have 
- Jitter over time indicate uncertainty implicitly. Use uncertainty, but not exactly Bayesian networks, but cheap approximation to that.
- Oversample "boat on trailer" 

### Hearsay at Poster section
- Dilated point convolution, sparse sample nearest neighors
- Domain adaptation: use video, train on those frames that it does not work well.
- Generic 3D object proposal generation: run 2D mask rcnn at low threshold, then use consistency to find the objects. 

### Video Classification and Detection
- Inflating filters in the temporal domain
- slowFast network

### Workshop: Vision for All Seasons: Bad Weather and Nighttime
#### How to evaluate each sensor degrades with increasingly adverse weather 
- DENSE project 
- From Mario Bijelic Daimler AG
![](assets/sunday/IMG_1584.jpg.warped.jpg)
![](assets/sunday/IMG_1585.jpg.warped.jpg)
![](assets/sunday/IMG_1586.jpg.warped.jpg)
- gated imager: only from a certain depth
- snowdust disturbs lidar a lot. Can simulate fog in clear data.
![](assets/sunday/IMG_1587.jpg.warped.jpg)
![](assets/sunday/IMG_1588.jpg.warped.jpg)
![](assets/sunday/IMG_1589.jpg.warped.jpg)
![](assets/sunday/IMG_1590.jpg.warped.jpg)

#### Gated imaging in adverse weather
- only collect relfected signal in a certain distance range
- good for condition such as fog (rid of back scatter from other depth slices) or night
- active illumination with: NIR (no color)
- frames per second? --> 120 fps, little motion blur
- single illumination and multiple collection?
- distance bins? usually 3, but overlapping, how thick?
- Estimate depth from multiple slides
![](assets/sunday/IMG_1591.jpg.warped.jpg)
![](assets/sunday/IMG_1592.jpg.warped.jpg)
![](assets/sunday/IMG_1593.jpg.warped.jpg)

#### [fastDraw: Predict lane lines](FastDraw: Addressing the Long Tail of Lane Detection by Adapting a Sequential Prediction Network)
- conventional methods
![](assets/sunday/IMG_1593.jpg.warped.jpg)
![](assets/sunday/IMG_1596.jpg.warped.jpg)
- Assume RNN to be Markov
![](assets/sunday/IMG_1597.jpg.warped.jpg)
![](assets/sunday/IMG_1599.jpg.warped.jpg)
![](assets/sunday/IMG_1600.jpg.warped.jpg)
- Style transfer to translate image into other weather conditions, Convert dashed to continuous lines, etc
- With augmentation, both in-domain and out-of-domain 
![](assets/sunday/IMG_1601.jpg.warped.jpg)
- [Tusimple data challenge](https://github.com/TuSimple/tusimple-benchmark/blob/master/doc/lane_detection/readme.md) for lane detection

#### [Heavy rain image restoration](https://arxiv.org/pdf/1904.05050.pdf)
- Rain streak removal algorithm: but only good camera can capture rain streaks
![](assets/sunday/IMG_1602.jpg.warped.jpg)
![](assets/sunday/IMG_1603.jpg.warped.jpg)
![](assets/sunday/IMG_1604.jpg.warped.jpg)
![](assets/sunday/IMG_1605.jpg.warped.jpg)
- Accumulated rain streaks
- Fog model formula: what is N?
- Run google vision API to classify

#### Learn a common representation
![](assets/sunday/IMG_1606.jpg.warped.jpg)
![](assets/sunday/IMG_1607.jpg.warped.jpg)
![](assets/sunday/IMG_1608.jpg.warped.jpg)
![](assets/sunday/IMG_1609.jpg.warped.jpg)
![](assets/sunday/IMG_1610.jpg.warped.jpg)

#### Illuminition in bad weather
- [Srinivasa Narasimhan](http://www.cs.cmu.edu/~srinivas/) from CMU
- Enhance physics/sensors
- people tend to drive fast in fog, due to bad perception of speed -- Nature 1998
- MILD database: 25% bad weather in Manhattan
- Defogged photo can also reveal 3D structure
- radar + camera fusion in his phd thesis
- How to illuminate in poor visibility?
	- Why we don't use high beam in fog/rain 
	![](assets/sunday/IMG_1611.jpg.warped.jpg)
	![](assets/sunday/IMG_1612.jpg.warped.jpg)
	- try to minimize diffuse volume
	- Scan with narrow beam very fast
- Combine velodyne puck with kinect depth: light sheet depth imaging
- Epilolar geometry: dense depth measurement at 50 m
- light curtains: obstacle avoidance without computation (see through fog, smoke, etc). (more common in Confocal imaging in microscopy)
![](assets/sunday/IMG_1613.jpg.warped.jpg)
- programmable headlight: 1M light points x 1000 fps. only illuminate objects of interest (beam intensity without glare)
![](assets/sunday/IMG_1615.jpg.warped.jpg)
- better visibility through snow/rain (smartly avoiding snow flakes/rain drops)
![](assets/sunday/IMG_1617.jpg.warped.jpg)

#### 3D detection across weathers, conditions, and locations: algorithms and benchmarks
- Daniel Cremers @ MTU
- SLAM: BA (bundle adjustment)
![](assets/sunday/IMG_1619.jpg.warped.jpg)
- But Kruppa is misleding:
	- Why only two images? why only points?
![](assets/sunday/IMG_1621.jpg.warped.jpg)
- min reproj error of key points only vs photometric error: all pixels contribute to the photometric error. Color consistency is the key
- DSO is much better than ORB-SLAM
- SLAM: GPS is not robust: multi-path in urban canyon, NA in tunnel
- Q: How to incorporate IMU or GPS signal? ICRA 2018: visual-inertial DSO. Integrate these measurement in the loss function. But the main challenge is the synchronization of measurement.
![](assets/sunday/IMG_1623.jpg.warped.jpg)
![](assets/sunday/IMG_1624.jpg.warped.jpg)
- Deep network end-to-end, but how to incorporate the existing knowledge?
- Yang et al ECCV 2018, use monocular, but estimates stereo disparity map
	- Depth from a single image with conventional method usually lead to inaccurate scale, but DNN is good at it
- Scene understanding: Build a 
- Relocalization: you have a map, localize yourself inside the map.
	- Gauss-newton loss, Von Stumberg, arxiv 2019

#### NuTonomy Talk on Nusences and 3D object detection
![](assets/sunday/IMG_1625.jpg.warped.jpg)
![](assets/sunday/IMG_1626.jpg.warped.jpg)
![](assets/sunday/IMG_1627.jpg.warped.jpg)
![](assets/sunday/IMG_1628.jpg.warped.jpg)
![](assets/sunday/IMG_1629.jpg.warped.jpg)
![](assets/sunday/IMG_1630.jpg.warped.jpg)
![](assets/sunday/IMG_1631.jpg.warped.jpg)

#### Panel discussion
- How to measure the adversity of environment (data quality as well)? And measure algorithm performance degradation a a function of the harsh-ness of environment.