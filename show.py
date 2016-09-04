from visual import *

class Show:# create the initial scene and create the initial value 
    def __init__(self):
        scene.width=800
        scene.height=800
        scene.title='Nutating Gyroscope'       
        Lshaft = 1. # length of gyroscope shaft
        Rshaft = 0.03 # radius of gyroscope shaft
        Rrotor = 0.4 # radius of gyroscope rotor
        Drotor = 0.1 # thickness of gyroscope rotor
        hpedestal = Lshaft # height of pedestal
        wpedestal = 0.1 # width of pedestal
        tbase = 0.05 # thickness of base
        wbase = 3*wpedestal # width of base
        top = vector(0,0,0) # top of pedestal
        theta = 0.3*pi  # initial polar angle of shaft (from vertical)
        phi = -pi/2. # initial azimuthal angle
        self.gyro=frame(axis=(sin(theta)*sin(phi),cos(theta),sin(theta)*cos(phi)))
        # create the frame that contain shaft and rotor and move together
        shaft = cylinder(axis=(Lshaft,0,0), radius=Rshaft, color=color.green,
                 material=materials.marble, frame=self.gyro)  
        rotor = cylinder(pos=(Lshaft/2 - Drotor/2, 0, 0),
                 axis=(Drotor, 0, 0), radius=Rrotor, color=color.gray(0.7),
                 material = materials.emissive, frame=self.gyro)
        pedestal = box(pos=top-vector(0,hpedestal/2.,0),
                height=hpedestal, length=wpedestal, width=wpedestal,
                color=(0.4,0.4,0.55))
        base = box(pos=top-vector(0,hpedestal+tbase/2.,0),
                 height=tbase, length=wbase, width=wbase,
                 color=pedestal.color)
        # create the pedestal and the base
        self.tip = sphere(pos=self.gyro.pos + self.gyro.axis * Lshaft, color=color.red,
               radius=0.001*shaft.radius, make_trail=True,
               interval=5, retain=250)
        # create the tip that show the trail of the shaft
        self.tip.trail_object.radius = 0.2*shaft.radius
    def update(self,x,y,z,rotation):
        # to update the position and angle of the gyroscope
        self.gyro.axis = vector(x,y,z)
        self.gyro.rotate(angle = rotation)
        self.tip.pos = self.gyro.pos + self.gyro.axis * 1.