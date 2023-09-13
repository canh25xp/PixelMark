# PixelMark
Use for marking pixel coordinate
Tested on Ubuntu 22.04.3 LTS
## Requirement
opencv-python
```bash
pip install opencv-python
```
## Usage
1. Put images in the input folders. The files structure should be as follow
```
.
├── input
│   └── cccdc_back_1.jpg
├── output
│   ├── cccdc_front_1.jpg
│   └── cccdc_front_1.txt
└── pixelMark.py
```
2. Run pixelMark.py
```
python pixelMark.py
```
3. Use mouse scroll to zoom in and out. Left click to mark a point
4. Press any key to finish and save result to output
