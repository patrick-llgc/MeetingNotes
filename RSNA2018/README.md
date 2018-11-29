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
  * [TUESDAY](#tuesday)
      - [CT spine fracture detection](#ct-spine-fracture-detection)
      - [Using GAN to generate chest DR image](#using-gan-to-generate-chest-dr-image)
      - [GAN generate ICH slices](#gan-generate-ich-slices)
      - [ICH segmentation](#ich-segmentation)
      - [Brain tumor segmentation](#brain-tumor-segmentation)
      - [Femoral Neck Fracture Detection](#femoral-neck-fracture-detection)
      - [Classification of DR with meta data](#classification-of-dr-with-meta-data)
      - [@ideas: Gan with attention in differentiator](#-ideas--gan-with-attention-in-differentiator)
  * [WEDNESDAY](#wednesday)
    + [SSK02](#ssk02)
      - [Breast density](#breast-density)
      - [cancer detection for Mammo screening](#cancer-detection-for-mammo-screening)
      - [Mammo detection reader study](#mammo-detection-reader-study)
      - [GAN to insert and remove lesion from mammo](#gan-to-insert-and-remove-lesion-from-mammo)
      - [million mammo](#million-mammo)
      - [Mammo detection](#mammo-detection)
      - [CAD for tomo](#cad-for-tomo)
      - [Tomo DBT vs mammo](#tomo-dbt--vs-mammo)
      - [breast density estimation](#breast-density-estimation)


Disclaimer: These are my personal notes on deep learning related talks when I attended RSNA 2018. If you are the author and find any mentioning of your work undesirable, please let me know by filing an issue in the repo or contact me at `pliu_AT_12sigma.ai`.

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
- Imsight (视见科技)
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

## TUESDAY
Kheiron (喀戎), a UK-based company, has an impressive demo of breast generated by GAN. **They have a publication on [ArXiv](https://arxiv.org/pdf/1807.03401.pdf).**

#### CT spine fracture detection
- SSG08-03
- Karen Cheng from UCSD, Peter Chang, director of medical AI lab at UCI
- Sagittal bine reconstruction
- Two stages: 3d mask rcnn for detection, followed by 3d resnet for classification
- 3d mask rcnn: actually hybrid 2.5 d. Feedi multiple layers, instead of multiple channels, then perform 3d convolution as well.
![](./assets/tue/IMG_0528.jpg.warped.jpg)
![](./assets/tue/IMG_0529.jpg.warped.jpg)
![](./assets/tue/IMG_0530.jpg.warped.jpg)
![](./assets/tue/IMG_0531.jpg.warped.jpg)

#### Using GAN to generate chest DR image 
- SSG06-07
- [Sliced Wasserstein GAN](https://arxiv.org/pdf/1803.11188.pdf)
- NIH dataset, downsized to 512 x 512
- Demo: https://courses.engr.illinois.edu/ece544na/fa2018/check/
- Radiologists favor GAN 30% of the time
- Checkerboard artifact sometimes visible. Radio-opaque legends not sharp.
![](./assets/tue/IMG_0532.jpg.warped.jpg)

#### GAN generate ICH slices 
- SSG06-08
- CAIDE
- Generate 2d ICH slices. Feed image label pair. No need to label again.
- conditional GAN (cGAN) similar to [this lung nodule synthesis paper](https://arxiv.org/pdf/1806.04051.pdf)
- cGAN: In an unconditioned generative model, there is no control on modes of the data being generated. In the Conditional GAN (cGAN), the generator learns to generate a fake sample with a specific condition or characteristics (such as a label associated with an image or more detailed tag) rather than a generic sample from unknown noise distribution. A good summary can be found [here](http://www1.idc.ac.il/toky/seminarIP-18/Presentations/10b_raaz.pdf).

#### ICH segmentation
- SSJ18-03
- 95 cases with ICH, one scan for one patient was included
- 60/5/30 for train/valid/test
- two thresholds:
	- High threshold: high specificity
	- Low threshold: high sensitivity
	- different post processing technique
![](./assets/tue/IMG_0539.jpg.warped.jpg)
![](./assets/tue/IMG_0540.jpg.warped.jpg)
![](./assets/tue/IMG_0542.jpg.warped.jpg)

#### Brain tumor segmentation 
- SSJ18-06
- Train on coarse tumor first, then finetune with added small tumor. Similar to curriculum learning
![](./assets/tue/IMG_0543.jpg.warped.jpg )

#### Femoral Neck Fracture Detection
- Generation of training data with DRR
![](./assets/tue/IMG_0546.jpg.warped.jpg) 
- The GAN generated images look rather distorted. Does it even help with classification task?
![](./assets/tue/IMG_0547.jpg.warped.jpg) 

#### Classification of DR with meta data
- feeding meta data to model for DR classification. 
	- Concat category data to fc layer
![](./assets/tue/IMG_0548.jpg.warped.jpg)
- The idea is worth trying, but results are not promising
![](./assets/tue/IMG_0549.jpg.warped.jpg)

#### @ideas: Gan with attention in differentiator
- Can we identify what looks weird in the generated image and use the more location-specific loss to guide the generator?


## WEDNESDAY
### SSK02
#### Breast density
- studies published recently
![](./assets/wed/IMG_0551.jpeg.warped.jpg)
- poor intra-reader and inter-reader correlation in the qualitative assessment in human reading
- AI performs better in the hetero and scattered cases

#### cancer detection for Mammo screening
- CAD does not really help prior to DL. How about now?
![](./assets/wed/IMG_0552.jpeg.warped.jpg)
![](./assets/wed/IMG_0553.jpeg.warped.jpg)
- commercial product named transpara
- hybrid case: 1 FP per 50 images, semi-automatic
![](./assets/wed/IMG_0554.jpeg.warped.jpg)
- Better ROC
![](./assets/wed/IMG_0556.jpeg.warped.jpg)
![](./assets/wed/IMG_0557.jpeg.warped.jpg)
![](./assets/wed/IMG_0558.jpeg.warped.jpg)
- No really increase of reading time overall; reduces time for easy cases, but increases time for hard cases
![](./assets/wed/IMG_0559.jpeg.warped.jpg)

#### Mammo detection reader study
- Jung Yin Huh, medical director for Lunit
- Beautiful GUI!
![](./assets/wed/IMG_0560.jpeg.warped.jpg)
![](./assets/wed/IMG_0563.jpeg.warped.jpg)
- 2nd reader study: 80k patients (we need more data!)
- Comments from the audience: Use of inexperienced reader will accentuate the importance of the tool

#### GAN to insert and remove lesion from mammo
- Dr. Anton Becker; anton.becker@usz.ch
- paper on [ArXiv](https://arxiv.org/pdf/1811.07767.pdf)
- zero-sum game: saddle point optimization problem
- cycle GAN, image to image translation
![](./assets/wed/IMG_0567.jpeg.warped.jpg)
![](./assets/wed/IMG_0568.jpeg.warped.jpg)

#### million mammo
- Hari Trevidi vs Peter Chang
- 7-8 per 1000 cancer rate
- 50%+ get at least one false recall in 10 years
- what is the relevant clinical questions we want to answer?
![](./assets/wed/IMG_0572.jpeg.warped.jpg)
- classify definitively negative cases (so 0 is positive, only 1 and 2 are 
- Mask RCNN network. Downsize images of mammogram not recommended 
- specificity 99.7%. only 0.3% of patient will be missed.
![](./assets/wed/IMG_0574.jpeg.warped.jpg)
- How did they arrive at this number?

#### Mammo detection
- Dr. Watanabe
- CureMetrix, evaluation of product cmAssist AI-CAD
![](./assets/wed/IMG_0575.jpeg.warped.jpg)
![](./assets/wed/IMG_0576.jpeg.warped.jpg)
- neuScore returned by the product
![](./assets/wed/IMG_0579.jpeg.warped.jpg)
![](./assets/wed/IMG_0580.jpeg.warped.jpg)
![](./assets/wed/IMG_0581.jpeg.warped.jpg)

#### CAD for tomo
- Lunit
- Background
![](./assets/wed/IMG_0582.jpeg.warped.jpg)
![](./assets/wed/IMG_0583.jpeg.warped.jpg)
![](./assets/wed/IMG_0584.jpeg.warped.jpg)
- Purpose
![](./assets/wed/IMG_0585.jpeg.warped.jpg)
- Methods
![](./assets/wed/IMG_0587.jpeg.warped.jpg)
![](./assets/wed/IMG_0588.jpeg.warped.jpg)
![](./assets/wed/IMG_0589.jpeg.warped.jpg)
- Architecture: transfer learning from tomo
![](./assets/wed/IMG_0590.jpeg.warped.jpg)
![](./assets/wed/IMG_0591.jpeg.warped.jpg)
![](./assets/wed/IMG_0592.jpeg.warped.jpg)
- Result:
![](./assets/wed/IMG_0594.jpeg.warped.jpg)
![](./assets/wed/IMG_0595.jpeg.warped.jpg)
![](./assets/wed/IMG_0596.jpeg.warped.jpg)
- Sample comparison with DBT only vs Mammo+DBT
![](./assets/wed/IMG_0598.jpeg.warped.jpg)
![](./assets/wed/IMG_0599.jpeg.warped.jpg)
![](./assets/wed/IMG_0601.jpeg.warped.jpg)
![](./assets/wed/IMG_0602.jpeg.warped.jpg)

- sensitivity of calc is about the same between Synthetic mammo is about the same as tomo
- trained on 2d thin slices of tomo and deployed on 3d slice by slice

#### Tomo(DBT) vs mammo
- DeepHealth
- Background
- Tomo has way passed the hype
![](./assets/wed/IMG_0603.jpeg.warped.jpg)
![](./assets/wed/IMG_0604.jpeg.warped.jpg)
![](./assets/wed/IMG_0605.jpeg.warped.jpg)
![](./assets/wed/IMG_0606.jpeg.warped.jpg)
- 3D is similar to action recognition
- Methods:Published at MICCAI-2017 on [ArXiv](https://arxiv.org/pdf/1707.06978.pdf)
![](./assets/wed/IMG_0607.jpeg.warped.jpg)
![](./assets/wed/IMG_0608.jpeg.warped.jpg)
![](./assets/wed/IMG_0609.jpeg.warped.jpg)
![](./assets/wed/IMG_0610.jpeg.warped.jpg)
![](./assets/wed/IMG_0611.jpeg.warped.jpg)
- Trend: RSNA is better for publication of reader studies

#### breast density estimation
- BR258-SD-WEA5
- Constance D. Lehman, MD,PhD from MGH and Havard
- DL model and the consensus has the highest agreement
![](./assets/wed/IMG_0615.jpeg.warped.jpg)