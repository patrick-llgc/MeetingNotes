# Slides Photo Conversion Tool
The script `crop.py` converts photos of slides taken at conferences into upright images.


## Usage
Run the following command

```
python crop.py -i /path/to/your/image.png
```

or

```
python crop.py -d /path/to/your/image/directory
```

If the results look weird and you want to know which step went run, run the above command with `--debug` flag.

```
python crop.py -i /path/to/your/image.png --debug
```

This will show you intermediate steps. When an image is presented, press any key to go to the next step.

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