from controller import Robot, Keyboard, Motion

timestep=32

robot= Robot()
keyboard = Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')

def startMotion(motion):
    motion.play()
   
def printMessages():
    print("press space to wave")
key = -1

printMessages()

while robot.step(timestep) != -1:

    key = keyboard.getKey()  

    if key == Keyboard.LEFT:
        startMotion(wave)
