from controller import Robot, Keyboard, Motion

timestep=32

robot= Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')
forward = Motion('../../motions/Forwards50.motion')
backward = Motion('../../motions/Backwards.motion')
sideStepLeft = Motion('../../motions/SideStepLeft.motion')
sideStepRight = Motion('../../motions/SideStepRight.motion')

def startMotion(motion):
    motion.play()
   
def printMessages():
    print("press space to wave")
    print('press up to move forward')
    print('press down to move backward')
    print('press left for side step left')
    print('press right for side step right')
     
key = -1

printMessages()

while robot.step(timestep) != -1:

    key = keyboard.getKey()  

    if key == Keyboard.LEFT:
        startMotion(sideStepLeft)
    elif key == Keyboard.RIGHT:
        startMotion(sideStepRight)
    elif key == Keyboard.UP:
        startMotion(forward)
    elif key == Keyboard.DOWN:
        startMotion(backward)
    elif key == Keyboard.SPACE:
        startMotion(wave)