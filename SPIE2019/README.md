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
