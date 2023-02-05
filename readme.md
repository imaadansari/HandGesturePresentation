# Hand Gesture Presentation

This python based application helps users to give presentation using hand gestures
making presentations easier and more interactive.

----------------------------------------

## Installation
First install all the necessary libraries.
```sh
pip install numpy opencv-python mediapipe
```
----------------------------------------

## How to use?

1) Import all your slides in /slides and resize.
- Name the slides in order. eg "1.png,2.png...etc"
- Run resize.py
```sh
python resize.py
``` 

2) Run main.py
```sh
python main.py
```
- Use pinky finger to move to next slide.
- Use thumb to move to previous slide.
- Use index and middle-finger together as a pointer.
- Use index finger to draw annotations.
- Use index, middle and ring finger to undo annotations.
- Refer to /screenshots for visual guide.
