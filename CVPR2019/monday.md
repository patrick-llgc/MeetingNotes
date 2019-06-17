## 06/17/2019 (Monday)


### Killian Weingerger@Cornell
- 3D object detection without expensive lidar (stereo vs lidar)
- [Pseudo-lidar]() (mimic lidar with depth map from mono or stereo)
- You cannot apply conv map on depth map: front depth maps are ill suited for convnets
- Change of representation leads to huge boost
- However depth are inaccurate! Disparity are optimized in the wrong way
	- conv map on disparity map is a wrong thing
	- for objects that are far away, pixel difference means different things!
	- Solution: don't estimate disparity, estimate depth!
	- Stereo depth network: optimizes depth cube (in unit of meters)
- Use sparse lidar measurement to correct wrong estimation
	- Affinity is correct
	- Correct the whole object (locally linear depth correction)
- [Pseudo lidar++](https://deeplearn.org/arxiv/80511/pseudo-lidar++:-accurate-depth-for-3d-object-detection-in-autonomous-driving)


### Alex Kendal@Cambridge+Wayve
- Nvidia weather in 2016
- Turn log-tail distribution to normal tail distribution
- How to get more human guidance in an exploration setting? --> simulation
- Q: Sim2real problem --> how to learn a proper representation?
	- zero shot sim2real: [Learning to Drive from Simulation without Real World Labels](https://arxiv.org/abs/1812.03823)
- Interpretation/Verification of DL representation
	- [Real Time Image Saliency for Black Box Classifiers](https://arxiv.org/abs/1705.07857)
	- [Interpretable Explanations of Black Boxes by Meaningful Perturbation](https://arxiv.org/abs/1704.03296)
- What metric to optimize?
	- We care about minority cases more
- Difference with Go and Dota:
	- Games states are easy, but action space are huge
	- autonomous driving: state space is huge, but action space is simple

### Trevor Darrell@BAIR
- 3D tracking
- occlusion aware 3D tracking
- [Joint Monocular 3D Vehicle Detection and Tracking](https://arxiv.org/abs/1811.10742)
- [Monocular Plan View Networks for Autonomous Driving](https://arxiv.org/abs/1905.06937)
- Explainable/causal driving policies
	- [Interpretable Learning for Self-Driving Cars by Visualizing Causal Attention](https://arxiv.org/abs/1703.10631)
- Localization
	- [Accurate Visual Localization for Automotive Applications](https://arxiv.org/abs/1905.03706)

### Raquel Urtason@Uber ATG
- Redundancy
- Disadvantage of traditional engineering stack
	- hard to propagate uncertainty
	- computation not shared between modules
	- Each module is trained separately to optimize diff objectives
- Not all actors influence dirving behavior
	- Most critial object need to be evlauated separately
	- Multi-sensor fusion: Liang et al, CVPR 2019
	- Xiong et al, CVPR 2019 oral, UPSnet, UPSNet ([A Unified Panoptic Segmentation Network]())
- Luo et al, CVPR2018 oral (prediction of waypoint in the future)
- Intention net: CoRL 2018
	- stopped vs park
- Human showcase their intent, indicator/turn signal detection (ICRA2019)
- Perception/prediction/planning
	- Zheng, oral at CVPR 2019
- AI in HD maps
	- Liang et al, CVPR 2019 (Convolutional Recurrent Network for Road Boundary Extractio)
- detection of construction elements
- AI for localization
	- VLAD for image retrieval
- AI for simulation
	- capture the world and simulate sensor input
	- separate static scenes and dynamic objects
	- real lidar and simulated lidar look almost the same

## Perception, Prediction, Data Collection for Autonomous Cars (from Lyft Level 5)
- ds