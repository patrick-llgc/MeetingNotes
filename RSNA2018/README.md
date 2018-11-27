# RSNA 2018 Meeting Notes
- [RSNA 2018 Meeting Notes](#rsna-2018-meeting-notes)
  * [SUNDAY](#sunday)
    + [SSA12](#ssa12)
      - [AI keynotes](#ai-keynotes)
      - [Ian Pan (thyroid)](#ian-pan--thyroid-)
      - [*Rib fracture*](#-rib-fracture-)
      - [Brain stroke detection (CAIDE from Korea)](#brain-stroke-detection--caide-from-korea-)
      - [Liver focal liver lesion (FLL)](#liver-focal-liver-lesion--fll-)
      - [Unirary stone detection](#unirary-stone-detection)
      - [Combining Chest X-ray Datasets (IBM Almaden Research)](#combining-chest-x-ray-datasets--ibm-almaden-research-)
      - [Automatic cls and reporting](#automatic-cls-and-reporting)
      - [Detection of Fracture of distal radius in X-ray](#detection-of-fracture-of-distal-radius-in-x-ray)
  * [MONDAY](#monday)
    + [SSC09](#ssc09)
      - [Keynotes](#keynotes)
      - [Nodule retrieval and matching](#nodule-retrieval-and-matching)
      - [Bone suppression](#bone-suppression)
      - [Lung cancer survival prediction](#lung-cancer-survival-prediction)
      - [Predict ICH from Sinogram](#predict-ich-from-sinogram)
      - [Accelerating annotation with eye trackers](#accelerating-annotation-with-eye-trackers)
      - [Automatically recognition of mislabels](#automatically-recognition-of-mislabels)
      - [Performance with Chest Xray](#performance-with-chest-xray)
      - [Mobile Chest Xray system](#mobile-chest-xray-system)
    + [RSNA challenge recap](#rsna-challenge-recap)
      - [1st place](#1st-place)
      - [3rd](#3rd)
      - [4th](#4th)
      - [5th](#5th)
      - [6th](#6th)
      - [8th](#8th)
    + [SSE14](#sse14)
      - [Classification of lateral and frontal Xray images](#classification-of-lateral-and-frontal-xray-images)
      - [segmentation of kidney](#segmentation-of-kidney)
      - [Liver segmentation with active learning](#liver-segmentation-with-active-learning)


## SUNDAY

### SSA12
[Abstract](./assets/sun/abstract_SSA12.pdf)

#### AI keynotes 
- Detection pipeline
	- two stage: faster rcnn
	- one stage: YOLO, SDD, retinaNet(!)
- AI + Doctor workflow
![](./assets/sun/IMG_0342.jpg.warped.jpeg)

#### Ian Pan (thyroid)
- Predict malignancy of thyroid in US
- 1 transverse + 1 sagittal view for each nodule
- Methodology:
	- Different Arch 
	- Ensemble of models trained on 3 different splits
	- ramdom search for hyperparameter tuning
- Important to do multiple splits for small datasets (CI and smoothing effect)
![](./assets/sun/IMG_0348.jpg)
- github.com/i-pan/thyroid-us

#### *Rib fracture*
- Chenwei Li gave the talk from LinYi Hospital on behalf of Xiaodong Li
- United Imaging
- Architecture: 3D ResUnet, 3 layers
- 100 patients, 726 factures, thin slice <1 mm CT
- GT by consensus
![](./assets/sun/rib_fracture_ct/IMG_0350.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0351.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0352.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0353.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0354.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0355.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0356.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0357.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0358.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0359.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0360.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0361.jpg.warped.jpg)
![](./assets/sun/rib_fracture_ct/IMG_0362.jpg.warped.jpg)


#### Brain stroke detection (CAIDE from Korea)
- Ischemic vs ICH
- ICH has many types
![](./assets/sun/IMG_0364.jpg.warped.jpeg)
- Narrow window width (40/40 for stroke window)
![](./assets/sun/IMG_0365.jpg.warped.jpeg)
- cascaded CNN for cls: both saying no, then no (this is a way to leverage different characteristics of ROC)
![](./assets/sun/IMG_0367.jpg.warped.jpeg)
- Different classes for segmentation
![](./assets/sun/IMG_0369.jpg.warped.jpeg)
![](./assets/sun/IMG_0370.jpg.warped.jpg)
- Narrowed window increases detection results (!need to try)
![](./assets/sun/IMG_0371.jpg.warped.jpeg)

#### Liver focal liver lesion (FLL)
- The author is from [KAIST](https://hansanglee.wordpress.com/)
- Classification of liver nodules
- Generation of **LINA** patches (lesion Information Augmentation) (this is quite interesting! seems like random need more investigation)
![](./assets/sun/IMG_0374.jpg.warped.jpg)
- GAN generated samples based on LINA patches
![](./assets/sun/IMG_0375.jpg.warped.jpg)
- ROC, recall ~0.8-0.85 at FP of 0.1

#### Unirary stone detection
- GrayNet: address generality issue of DL models
- Best solution: large-scale, well-annotated data
- Workaround: 
	- Transfer learning
	- **Learning anatomy before pathology**
	- ImageNet --> GrayNet --> MI DL App
- Weights will soon be published

#### Combining Chest X-ray Datasets (IBM Almaden Research)
- PLCO, NIH, Indiana collection
- Normalizing annotation vocabulary (label) from diff datasets (mapping table listed below)
![](./assets/sun/IMG_0384.jpg.warped.jpeg)
![](./assets/sun/IMG_0386.jpg.warped.jpeg)

#### Automatic cls and reporting
- Extract 14-bit label with LSTM from raw text report
- For the release of reports, ask Ronald Summers at NIH

#### Detection of Fracture of distal radius in X-ray
- 1900 xray images, 1350 negative + 450 positive
- Augmentation rotation: up to 10 degrees
- Used DL GUI to train model




## MONDAY

### SSC09
[Abstract](./assets/mon/abstract_SSC09.pdf)

#### Keynotes
- Ronald Summers from NIH (ChestXray14 initiator)
![](./assets/mon/IMG_0419.jpg.warped.jpg)
- Major directions: Detection, Segmentation, Mapping, Image Synthesis
- Broad scope
	- RECIST labeling (keypoint regression of major/minor axes): used for treatment
- Datasets
	- [Lymph Node CT Datasets](https://wiki.cancerimagingarchive.net/display/Public/CT+Lymph+Nodes#663e5b256e85496ba3eaa26deb1050c3) (176 scans with segmentation masks) 
	- [Pancreas CT Datasets](https://wiki.cancerimagingarchive.net/display/Public/Pancreas-CT): 82 scans
	- ChestXray14
	- Deep Lesion
- Ionizing radiation (CT, Mammo, X-ray) vs Non-ionizing (US, MRI)
	
	
#### Nodule retrieval and matching
- Ke Yan from NIH
- DeepLesion dataset
	- "Bookmasks" marked by radiologists to highlight abnormal lesions in their daily work
- Weakly labels
	- Annotaed 2k, predicted pseudo label for others (?)
- Triplet loss (!need to look closer)
![](./assets/mon/IMG_0427.jpg.warped.jpg)
![](./assets/mon/IMG_0428.jpg.warped.jpg)
- Intra patient lesion matching and inter-patient lesion retrieval 
![](./assets/mon/IMG_0431.jpg.warped.jpg)

#### Bone suppression
- Generate bone-only and tissue-only images from one single DR image
![](./assets/mon/IMG_0433.jpg.warped.jpg)
![](./assets/mon/IMG_0434.jpg.warped.jpg)
- Conventional methods: dual energy imaging
![](./assets/mon/IMG_0435.jpg.warped.jpg)
- GT: Dual Energy image 461 cases of DE DR
![](./assets/mon/IMG_0437.jpg.warped.jpg)
- Architecture: predict coarse image first, then use smaller receptive field to focus on details
![](./assets/mon/IMG_0436.jpg.warped.jpg)
- **Predict bone image, then subtract it to keep fine details**
![](./assets/mon/IMG_0438.jpg.warped.jpg)
![](./assets/mon/IMG_0439.jpg.warped.jpg)
- SSIM > 0.98 for tissue only images
![](./assets/mon/IMG_0440.jpg.warped.jpg)
- Foreign objects not excluded. Only produce bone-only image
- Did not use ResNet, see paper DDSR

#### Lung cancer survival prediction
- Yiwen Xu from Dana-Farber
- Multiple images in a sequence. This is like time series: video action classification
- Input: seed point, bbox in CT, 1, 3, 6 month after therapy
- 2.5 D: not necessarily the immediate scans. Use **larger spacings** (!)
- More follow-ups leads to better prediction
![](./assets/mon/IMG_0441.jpg.warped.jpg)
- We cannot just concat images from different time points into channels and predict. Then the network will learn that if a timepoint is missing, the patient is dead. Now every time point is processed by a CNN first, then use a RNN to aggregate the results. 
![](./assets/mon/IMG_0442.jpg.warped.jpg)


#### Predict ICH from Sinogram
![](./assets/mon/IMG_0443.jpg.warped.jpg)
- 720 cases (~6k slices)
- Reverse generation of sinogram based on CT images (lossy conversion as Radon is not the inverse of CT recon)
- two windows: full window and ICH window (!need to try)
	- ICH: W/L = 50/100
- ICH window > full window (more information is not necessarily better. Need more information)

#### Accelerating annotation with eye trackers
- Paul Murphy@UCSD Radiology
- Tobii 4c device, cost about $150 as of 2018/11/26
![](./assets/mon/IMG_0447.jpg.warped.jpg)
- annotation error ~1cm
- Precision drop toward the edge

#### Automatically recognition of mislabels
- Train model first
- Manually flip the label
- Rank mislabeled data by ranking the scores
- Auto-fix the label (why not flag suspicious results for doctors to verify?)
- Loss function: cross entropy + influence function
- Influence function: [ICML2017 best paper](https://arxiv.org/pdf/1703.04730.pdf) **(needs to read!)**
![](./assets/mon/IMG_0451.jpg.warped.jpg)
![](./assets/mon/IMG_0452.jpg.warped.jpg)
![](./assets/mon/IMG_0453.jpg.warped.jpg)
![](./assets/mon/IMG_0454.jpg.warped.jpg)
![](./assets/mon/IMG_0455.jpg.warped.jpg)
![](./assets/mon/IMG_0456.jpg.warped.jpg)
![](./assets/mon/IMG_0457.jpg.warped.jpg)

#### Performance with Chest Xray
- Qure.ai from India
- opacity (focal or diffuse)
- any abnormality
- Tested classifier on follow-up chest xrays
- Detect early symptoms in chest xray (that are missed by doctors on DR but later identified in CT)
![](./assets/mon/IMG_0460.jpg.warped.jpg)

#### Mobile Chest Xray system
- RadiSen company
- visualization with GradCAM or GradCAM++
- Used GAN to generate image for domain adaptation
![](./assets/mon/IMG_0463.jpg.warped.jpg)

### RSNA challenge recap
- Last year bone age challenge, this year pneumonia
- Ron Summers, head of AI lab at NIH
- Challenges in de-identifying the patients: manual inspection twice to remove identifiers in the images
![](./assets/mon/IMG_0468.jpg.warped.jpg)
![](./assets/mon/IMG_0469.jpg.warped.jpg)

#### 1st place
- Classifier + detector
- More than 10 models in the ensemble!
- [source code](https://github.com/i-pan/kaggle-rsna18)
![](./assets/mon/IMG_0474.jpg.warped.jpg)
![](./assets/mon/IMG_0476.jpg.warped.jpg)
![](./assets/mon/IMG_0478.jpg.warped.jpg)
![](./assets/mon/IMG_0479.jpg.warped.jpg)
![](./assets/mon/IMG_0480.jpg.warped.jpg)
![](./assets/mon/IMG_0481.jpg.warped.jpg)
![](./assets/mon/IMG_0482.jpg.warped.jpg)

#### 3rd
- Philips Cheng from USC
- simple ensemble of 2 retinaNets (single stage), very clean
- shrink bbox by 17% increases leaderboard score
- [source code](https://github.com/pmcheng/rsna-pneumonia)
![](./assets/mon/IMG_0485.jpg.warped.jpg)
![](./assets/mon/IMG_0486.jpg.warped.jpg)
![](./assets/mon/IMG_0487.jpg.warped.jpg)
![](./assets/mon/IMG_0488.jpg.warped.jpg)

#### 4th
- 16 bit + layer6
- They did not know the test set was annotated by 3 truthers, but they seem to have analyzed the statistics after stage 1
- intersection of 3 detectors (yolo, faster, mask rcnn)
- filtered by classifier
![](./assets/mon/IMG_0490.jpg.warped.jpg)
![](./assets/mon/IMG_0491.jpg.warped.jpg)
![](./assets/mon/IMG_0492.jpg.warped.jpg)
![](./assets/mon/IMG_0493.jpg.warped.jpg)
![](./assets/mon/IMG_0494.jpg.warped.jpg)

#### 5th
- Imsight (靓影)
- one month intern's work
![](./assets/mon/IMG_0495.jpg.warped.jpg)
- majority voting of multiple detectors
![](./assets/mon/IMG_0496.jpg.warped.jpg)
- filtered by classifier

#### 6th 
- DeepRadiology
![](./assets/mon/IMG_0497.jpg.warped.jpg)
- [CoupleNet](https://arxiv.org/pdf/1708.02863.pdf), similar to R-FCN and R-CNN, but uses local and global contexts
![](./assets/mon/IMG_0498.jpg.warped.jpg)
- Grouped bboxes from ensemble of models based on IoU
![](./assets/mon/IMG_0500.jpg.warped.jpg)

#### 8th
- Filipe Kitamura (北村？) From Brazil
- RetinaNet with ResNet backbone
- Modified anchor box ratio
![](./assets/mon/IMG_0502.jpg.warped.jpg)
- Shrank bbox size by 16%
![](./assets/mon/IMG_0503.jpg.warped.jpg)
![](./assets/mon/IMG_0504.jpg.warped.jpg)


### SSE14
#### Classification of lateral and frontal Xray images
- Misclassification scores are all over the place, not robust

#### segmentation of kidney
- Used scouting to zoom into the VOI
![](./assets/mon/IMG_0506.jpg.warped.jpg)
![](./assets/mon/IMG_0507.jpg.warped.jpg)
- Implementation of dice score improved performance quite a lot
- Impressive UNet activation visualization

#### Liver segmentation with active learning
- active learning
- Use open dataset, evaluate on institutional data. Identify worse performing cases, then relabel.
![](./assets/mon/IMG_0509.jpg.warped.jpg)
![](./assets/mon/IMG_0510.jpg.warped.jpg)
![](./assets/mon/IMG_0511.jpg.warped.jpg)
![](./assets/mon/IMG_0512.jpg.warped.jpg)
![](./assets/mon/IMG_0513.jpg.warped.jpg)
![](./assets/mon/IMG_0514.jpg.warped.jpg)
![](./assets/mon/IMG_0517.jpg.warped.jpg)
![](./assets/mon/IMG_0518.jpg.warped.jpg)