# Slides Photo Conversion Tool
The script `crop.py` converts photos of slides taken at conferences into upright images.


## Recommended Usage
1. Process whole jpg or png folder in batch
```
python crop.py -d /path/to/your/image/directory
```
2. Manually delete unsatisfactory crops
3. Manually adjust the crops in batch
```
python crop.py -d /path/to/your/image/directory --mode manual
```


## General Usage
Run the following command

```
python crop.py -i /path/to/your/image.png
```

or

```
python crop.py -d /path/to/your/image/directory
```

If the results are wrong or the script does not do a good job cropping automatically, run the above command with `--mode manual` flag to select the four anchor points manually for perspective transformation.

```
python crop.py -i /path/to/your/image.png --mode manual
```

If the results look weird and you want to know which step went run, run the above command with `--debug` flag. This will show you intermediate steps. When an image is presented, press any key to go to the next step.

```
python crop.py -i /path/to/your/image.png --debug
```

## Example
### Light themed
Example original image
![](./assets/orig.jpg)


Example converted image
![](./assets/warped.jpg)

### Dark themed
Before conversion
![](./assets/orig_dark.jpg)

After conversion
![](./assets/warped_dark.jpg)


### Manual selection of anchor points
Before conversion
![](./assets/manual_orig.jpg)

Manual mark
![](./assets/manual_orig_mark.jpg)

After conversion
![](./assets/manual_orig_mark_warped.jpg)