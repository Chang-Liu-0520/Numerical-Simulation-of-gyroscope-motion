from visual import rate
from gyroscope import Gyroscope
from show import Show
from control import Control

def main():
    dt = 0.0001 # the unit time to calculate
    Nsteps = 20 # steps to refresh the screen
    gyro = Gyroscope()
    show = Show() # create the screen to show the movement of gyroscope
    control = Control(gyro) # create a screen to control gyroscope
    while True:
        rate(100) # refresh the screen 100 times one second
        for i in range(Nsteps):
            gyro.go(dt) # let the gyroscope go 
        x,y,z = gyro.GetPos()
        angle = gyro.GetRotationVel() * dt * Nsteps
        show.update(x,y,z,angle) # update the position and angle of the gyroscope
        control.ShowEnergy() # show total energy of gyroscope

main()