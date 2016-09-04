# Numerical-Simulation-of-gyroscope-motion
This contains several python scripts used to simulate the motion of gyroscope. In GUI, user can set the nutation angle, rotation velocity and the total energy of gyroscope. This folder also contain two Python library that are used

##Gyroscope.py
This script build a class of gyroscope, that calculate the motion using Largrange equation of gyroscope
###Property:
Weight, size, inertia, initial nutation angle(theta), procession angle(phi), rotaton angle(psi), and nutation velocity, procession velocity, rotation velocity;
###go Method:
Used nutation angle, procession angle and rotation angle as generalized coordinates, and used Largrange equation ot calculate the motion after dt step.
###GetPos Method: 
Performed coordinate transformation, which change nutation angle, procession angle and rotation angle as x,y,z in cartesian coordinate of Vpython
###GetPower Method: 
Used velocity of nutation, procession, rotation to obtain the kinetic energy of gyroscope, used nutation angle to get the potential energy of gyroscope, and returen the total power
###return_rotation_vel method: 
return the velocity of rotation;
###SetNutation method: 
change the nutation angle
###SetRotation Vel: 
change the rotation velocity

##show.py
This model used third library: VPython to show the results
###initial method: 
initialization build the basic image to show
###gyro property:
this is the frame of gyroscope to show
###tip property: 
this is the trajectory of the gyroscope top
###update method:
used new value from gyroscope class to update the new position of gyro and tip

##control.py
This model use third library: wxpython to design control panel, it can change the initial nutation angle and rotation velocity of the gyroscope. It also show the total energy of the gyroscope

##main.py
This script used models above to start simulation
