# SPIE Medical Imaging 2019
## Sunday
### Deep Learning Session 1
#### AI + Medical Imaging in China: Present and Future
- Presenter Dr. Shiyuan Li from Changzheng Hospital in China
- High quality medical services are needed
	- Aging population
- Pain point of Medical Imaging in China
	- Inaccurate diagnosis
	- Scarcity of supply: 20% annual growth rate of data, 4.1% of radiologists
	- Low efficiency
- AI + Medicine
	- Disease detection
	- Lesion quantification
	- Malignancy diagnosis
	- Therapeutic evaluation
- Compared with US, China has way too many medical imaging AI company, but not enough new drug discovery, patient management, etc. 
- Usage:
	- lung nodule: daily use
	- fracture and ICH: ER
- Iterative AI model
	- Refinement using hospital data
	- False positives gradually reduce to acceptable levels
- AI tool for measuring intracerebral hemorrhage (ICH)
	- x ml --> y ml
- Bone Age analysis
	- Parents height, child's height and weight, evaluates the status of the child's growth (too over-weight? ahead of the growth curve)
	- Shows the growth curve (height/weight vs age), and the child's position (a single point) in the curves
- Large medical imaging database
	- National Database of ultrasound
	- National radiology database
- CFDA
	- Class II: assistive diagnostic suggestion/recommendation, regulated by local provincial FDA
	- Class III: give definitive diagnostic suggestion/recommendation, regulated by CFDA

#### Impact of imprinted labels on deep learning classification of AP and PA thoracic radiographs
- PA: Size of hard shadow, visual cues: scapula/clavicle positions
- a CNN classifier to classify AP/PA
- 2000 images, may contain foreign objects, 65:20:15 splits
- Wording of imprinted labels: portable, AP, Erect, semi erect
- 97% ROC AUC for images with labels, 95% ROC AUC for images without labels
- Q&A:
	- Only DR is used
	- AP often contain more foreign objects
	- No CAM is used to visualize, this is the next step

#### Deep learning method for tumor segmentation in breast DCE-MRI
- previous methods: fuzzy c-means (Zhang et al), watershed
- 2D vs 3D methods: U-Net used
- data: slices with tumors
- 3D U-Net has fewer false positives
- Q&A:
	- Test: how about false positives in healthy regions? ROI is specified by doctors. This is only for segmentation.
	- Patient split: yes

	
### Deep Learning Session 2
#### Optic disc segmentation in fundus images 
- MWSSIDOR, open dataset, 1200 images
- ROI abstracted from fundus images with RetinaNet
- Segmentation done with U-Net

#### Learning cross-protocol radiomics and deep feature standardization from CT images of texture phantoms
- Standardize features across scanners
- Texture phantom scanned by various scanners
- Classify scanned texture to learn features stable across scanners
- Domain adversarial training with gradient reverse layer to forget about domain

#### A data interpretation approach for deep learning-based prediction models
- Model interpretability
	- Radiomics vs deep learning
- CNN is **ruthless** in finding discriminative features. Here is a cool story [from the Pentagon](https://www.analyticsvidhya.com/blog/2018/03/essentials-of-deep-learning-visualizing-convolutional-neural-networks/).
- Scheme 1: modify input images to examine CNN models wrt changes in ROI (occlusion test)
	- 4x4 grid: keep information inside one grid, but mask all other 15 girds (This does not quite make sense)
- Scheme 2: CAM based methods
- Notes: not very convincing


### Breast III and Heart
#### Visual evidence for interpreting diagnostic decision of deep neural network in computer-aided diagnosis
- Deep learning has limited interpretability
- Solution: CAM (class activation map) or gradCAM
- Inspired by Radiologists' interpretation: BI-RADS
- Margin interpretation + shape interpretation
	- Interpretation loss
	- Consistency loss
	- Extra supervision loss
- Note: the losses are too complicated to replicate

#### U-Net inspired architecture ensembles for left atrial segmentation
- Ensemble of 15 different U-Net based on different feature extractors (ResNet, DenseNet, SENet, etc)
- Some individual model has wide error bars
- The ensemble model does not have clear efficiency over some of the good performing models