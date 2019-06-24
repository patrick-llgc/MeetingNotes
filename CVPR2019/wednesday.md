## 06/19/2019 (Wednesday)

## Motion and tracking
- Use siamese network for tracking
- **Note** [Deeper and Wider Siamese Networks for Real-Time Visual Tracking](https://arxiv.org/abs/1901.01660)
	- ResNet causes performance drop. Why?
	- SiamDW: redesign residual blocks for tracking
- Modeling games with GNN (with inherent insensitivity to permutation)
- Detection and pose tracking
![](assets/wednesday/IMG_1765.jpg.warped.jpg)
- [SiamFC: Fully-Convolutional Siamese Networks for Object Tracking](https://arxiv.org/abs/1606.09549) (ECCV 2016)
- [Graph Convolutional Tracking](http://nlpr-web.ia.ac.cn/mmc/homepage/jygao/gct_cvpr2019.html)

## Recognition
- **Notes** Mask Scoring R-CNN --> can be adapted to object detection
	- mask Iou is low, but mask score is high
	- regress iou head for predicting mask iou
	- this improves high quality segmenation
![](assets/wednesday/IMG_1775.jpg.warped.jpg)
- Adaptive NMS: Refining Pedestrian Detection in a Crowd
![](assets/wednesday/IMG_1776.jpg.warped.jpg)
- Locating Objects Without Bounding Boxes
- Few-shot learning with localization in realistic settings **Note**
	- three parameter free techniques
	- Batch folding **Note**
![](assets/wednesday/IMG_1777.jpg.warped.jpg)

## posters
- noise aware unsupervised deep lidar stereo fusion
- an attention based recurrent neural network for vehicle tailgate recognition
- superdepth: monocular 
- ROI-10D: Monocular Lifting of 2d detection to 6d pose and metric shape
- TASCNet Learning to fuse things and stuff
- PackNet SfM
- SPIGAN previleged adversarial learning from simulation
- pointnetlk robust and efficient point cloud registration using pointnet
- pedestrian detection with autoregressive network passes
- grid r-cnn
- multi-task multi-sensor fusion for 3D object detection
- leveraging crowd-sourced gps data for road extraction from satellite imagery
- triangulation learning network: from monocular to stereo 3d object detection
- joint manifold deffusion for combining prediction on decoupled observation
- siamese cascaded region proposal networks for real-time visual tracking
- rules of the road: predicting driving behavior with a convolutional model of semantic interaction

### Morning session
