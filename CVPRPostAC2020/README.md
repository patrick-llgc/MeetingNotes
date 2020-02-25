# [CVPR Post AC Meeting 2020](http://www.cvpr2020-ac-meeting.org/workshop.html)

Time: 2020 Feb 24 (Monday)

Location: Location: Atkinson Auditorium @ UCSD

Live stream on [youtube](https://www.youtube.com/watch?v=9bZT5dzyeS8).

## Session I @ 8:00AM-10:00AM
- 8:00 - 8:12	Justin Johnson	End-to-End View Synthesis from a Single Image
	- Feifei Li's student, UMich
	- [SynSin: End-to-end View Synthesis from a Single Image](https://arxiv.org/abs/1912.08804)
	- Input: 
		- one image
		- transform based on given translation and rotation
	- Challenge: need to know the depth, impainting missing regions
	- Train without depth GT
	- Hallucinating the occluded part
	- Differentiable projection, Z-buffer --> PyTorch3D
	- Similar to depth prediction (SfMLearner)?
	- Next step: self-supervised depth
	![](assets/johnson_umich1.png)
	![](assets/johnson_umich2.png)
- 8:12 - 8:24	Alex Schwing	Chirality Nets for Human Pose Regression
	- UIUC
	- [Chirality Nets for Human Pose Regression](https://papers.nips.cc/paper/9027-chirality-nets-for-human-pose-regression) NIPS 2019
	- seeing the unseen (occlusion), and predict the future
	- Pose regression tasks:
		- concatenation of joint coordinates
		- 2D pose mirroed --> 3D pose mirrored (charality equivariance)
		- Work the charality equivariance into the neural nets
	- Benefits of charality
		- Data efficient
		- Equivariance guarantee
	- Similar to pointNet
	- Will take you down for assymetric tasks
	![](assets/schwing_uiuc.png)
- 8:24 - 8:36	Georgia Gkioxari	Challenges in PyTorch 3D
	- FAIR
	- 2D to 3D: Mesh R-CNN
	- Mask RCNN: more than 500 samples per image
	- Batching in 3D: varying number of vertexes, **hetereogeneous batches**
		- Auxiliary tensor to remember index
		- Padded tensor
		- different batching mode even int he same forward pass
	- Differentiable renderer
	- PyTorch3D is important for any Neural nets with rendering
		- can be useful for 3D MOD
		- [video demo](https://www.youtube.com/watch?v=lG3s_uHJQYY) and [another one](https://www.youtube.com/watch?v=FQugQKz8hwE)
- 8:36 - 8:48	Carl Vondrick	Oops! Predicting Unintentional Action
	- [Oops! Predicting Unintentional Action in Video](https://arxiv.org/abs/1911.11206) CVPR 2020
	- Survivor bias of video Data
	- [Opps! Dataset: failed videos](oops.cs.columbia.edu)
	- What are the perception clues to tell intentionality
	- Self-supervised clue: order, video speed
		- speed of action alters perceptual judgement
	- Video: intentional, transition, unintentional
- 8:48 - 9:00	Hyun Soo Park	HUMBI dataset multiview human expression
	- Univ of Minnesota
	- Multiview data from diverse identities
	- Collect garment, gaze, guesture
	- $1 reward for participants
- 9:00 - 9:12	Rita Cucchiara	Self-attention in Vision and Language
	- Italy
	- Image captioning: RNN --> Transfomer
	- Transformer is a soft dictionary
	- self-attention and cross-attention
- 9:12 - 9:24	Vineeth N Balasubramanian		Zero-shot Task Transfer/Causal Attributions in Neural Networks
	- IIT Hyderabad
	- related to and inspired by Taskconomy
	- Input: task correlation matrix: either crowd sourcing or Taskconomy
	- Zero shot: how to learn models for tasks without Gt, given other tasks with GT
	- Meta Learning to learn a regressor to learn the weights for a new task based on the weight of existing tasks
	- Limitation: output space need to be the same
- 9:24 - 9:36	Roozbeh Mottaghi	Interactive Scene Understanding
	- Allen Institute for AI
	- CV problems: passive/active/interactive
		- passive: fixed dataset
		- active: change dataset to corresponds to the label
		- interactive: no fixed dataset. The dataset depends on your actions. navigation, interactive QA
	- Dataset: AI2Thor, AI2Thor-robo (sim2real dataset, inverted virtual KITTI)
- 9:36 - 9:48	[Philipp Kraehenbuehl](https://www.philkr.net/) Objects as Points	
	- Efficiently Training Video Models [A Multigrid Method for Efficiently Training Video Models](https://arxiv.org/abs/1912.00998)
	- [Learning by Cheating](https://arxiv.org/abs/1912.12294)
	- Tracking objects as points, extremely fast on MOT
- 9:48 - 10:00	David Fouhey	Internet-Scale Hands In Interaction
	- UMich
	- Learn how we interact with the world
	- Large dataset with 100k frames 
	- Ego centric, third person videos

## Session II @ 10:30AM-12:00AM
- 10:30 - 10:42	[Laura Leal-Taixé](https://dvl.in.tum.de/team/lealtaixe/)	Video anonymization
	- TUM
	- Properties:
		- anomynmous: face swapping
		- Create new identities that does not exists
	- Input: background + facial landmarks
	- Without retraining, the identification perf drops to zero.
- 10:42 - 10:54	[Vinay Namboodiri](https://vinaypn.github.io/pubs_short/)	Integrating Vision, Speech and Language
	- IIT Kampur
	- Modify sync to improve lip sync
	- Modify video to improve lip sync in different languages
- 10:54 - 11:06	[Adriana Kovashka](https://people.cs.pitt.edu/~kovashka/publications.htm)	Reasoning about Complex Media from Weak Multi-Modal Supervision
	- University of Pittsburgh
	- Understanding of advertisement
- 11:06 - 11:18	[Amir Zamir](https://cs.stanford.edu/~amirz/)	Perception in the Action Loop
	- student of Silvio Savarese and Jitendra Malik.
	- Datasets: fixed, passive
	- Perception for active agents
	- Having vidual priors helps visual navigation
- 11:18 - 11:30	[Ayellet Tal](https://webee.technion.ac.il/~ayellet/papers.html)	Solving Jigsaw Puzzles
	- Technion
	- Archeologists are solving puzzles
	- Reconstruct an object from a set of non-overlapping and unordered parts (NP-hard)
	- Solving puzzles: take in image patches, then generate a coherent image
	- Boundaries are eroded (for archeology use)
	- Key ideas:
		- Inpaint
		- Learn to classify a pair is neighbor or not
	- Even humans would need to know the maximum margin of erosion to perform well.
- 11:30 - 11:42	Boqing Gong	Long-Tailed Visual Recognition Is A Domain Adaptation Problem
	- Google
	- Current/previous methods assumes that the conditional probability for CAT and TAC are the same (not true for minority classes)
- 11:42 - 11:54	Chen Sun	Speech2Action
	- Google
	- Annotating actions in videos are very costly
	- Use human speech as weak supervision

## Session III @ 1:00PM-3:00PM
- 1:00 - 1:12	Andreras Geiger	Learning Implicit 3D Reconstruction without 3D Supervision
	- Toyota Institute, University of Tubingen, MPI
	- Output representation: 
		- Voxels/Points/Meshes (discretize)
	- Occupancy networks
	- [Differentiable Volumetric Rendering: Learning Implicit 3D Representations without 3D Supervision](https://arxiv.org/abs/1912.07372)
	- No need to store intermediate results
	- [blog](https://autonomousvision.github.io/)
- 1:12 - 1:24	[Hamed Pirsiavash](https://www.csee.umbc.edu/~hpirsiav/)	Adversarial Patches Exploiting Contextual Reasoning in Object Detection
	- Univ of Maryland
	- last layer has receptive field of the entire image. YOLO uses global info
	- conditional reasoning leaves backdoor for adversarial attacks
	- single shot detectors are hard to defend against adversarial patches
	- blinding toward one or multiple object classes
	- Introduce DetGrad-Cam
	- Impossible to detect the patch (the patch can be initialized from a natural image and it does not need to be very random)
- 1:24 - 1:36	Hao Su	SAPIEN: A Simulated Part-based Interactive Environment
	- Simulation environment
- 1:36 - 1:48	[Jun-Yan Zhu](https://people.csail.mit.edu/junyanz/)	Visualizing and Understanding GANs
	- [Seeing What a GAN Cannot Generate](https://arxiv.org/abs/1910.11626) ICCV 2019
	- which neurals are responsible for a feature
	- How to manipulate an existing photo? Reconstruct the image first then manipulate the neurons
- 1:48 - 2:00	Manmohan Chandraker		Physically-Based Learning for Inverse Rendering
	- Inverse rendering via Differentiable rendering layer
- 2:00 - 2:12	Minsu Cho	Composing Neural Features for Visual Correspondence in the Wild
	- Postech
	- Visual correspondence <==> Semantic correspondence
	- Multilayer search strategy for semantic correspondence
	- Exhaustive search vs beam search
- 2:12 - 2:24	Natalia Neverova	Transferring Dense Pose to Animals
	- FAIR in Paris, MPI
	- DensePose (ultimate human parsing)
	- bijective mapping between 3D models of human and other creatures
	- **Temporal consistency** is a good indicator of network performance as well
- 2:24 - 2:36	Octavia Camps	Compact and Interpretable Dynamics-based Video Representations
	- Integrate kalman filter into the representation and keep the representations consistent
- 2:36 - 2:48	Rei Kawakami	Improving Robustness in Recognition: Motion, Open-set, and Multi-task learning
	- Video can help object detection as well -- the motion pattern can help differentiate FPs
- 2:48 - 3:00	Vicente Ordonez	Explicit Compositionality in Language and Vision
	- s


## Session IV @ 3:30PM-5:00PM
- 3:30 - 3:42	Richard Zhang	CNN-Generated Images Are Surprisingly Easy to Spot ... for Now
	- Adobe
	- [Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486) ICML 2019
	- [CNN-generated images are surprisingly easy to spot... for now](https://arxiv.org/abs/1912.11035) CVPR 2020
		-  Our findings suggest the
intriguing possibility that today’s CNN-generated images
share some common systematic flaws, preventing them from
achieving realistic image synthesis.
- 3:42 - 3:54	Sanjeev Koppal	Fast Foveating Cameras, LIDARs and Projectors
- 3:54 - 4:06	Shuran Song	Grasping in the Wild
- 4:06 - 4:18	Subhransu Maji	Dark Ecology: Unraveling Mysteries of Bird Migration using Weather Radar and Machine Learning


