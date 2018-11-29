## wed/NESDAY
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
- paper on [ArXiv]()
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
- Methods:Published at MICCAI-2017
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