from math import sin,cos,pi,sqrt

class Gyroscope:
    def __init__(self):   
        # The analysis is in terms of Lagrangian mechanics.
        # The Lagrangian variables: theta, the angle of nutation, phi, the angle of procession, psi, the angle of rotation
        # initial value of theta,phi,psi,and the velocity and accelerate of them
        global r,M,g,Rrotor,I1,I3
        self.theta = 0.3*pi
        self.phi = -pi/2
        self.theta_vel = 0
        self.phi_vel = 0
        self.psi_vel = 30
        self.theta_a = 0
        self.phi_a = 0
        self.psi_a = 0
        r = 0.5 # distance from support to center of mass
        M = 1. # mass of gyroscope (massless shaft)
        g = 9.8  #gravitational acceleration
        Rrotor = 0.4 # radius of gyroscope rotor
        I3 = 0.5*M*Rrotor**2 # moment of inertia of gyroscope about its own axis
        I1 = M*r**2 + .5*I3 # moment of inertia about a line through the support, perpendicular to the axis
        
    def go(self,dt):
        # Calculate accelerations of the Lagrangian coordinates:
        self.theta_a = sin(self.theta)*cos(self.theta)*self.phi_vel**2+(
            M*g*r*sin(self.theta)-I3*(self.psi_vel+self.phi_vel*cos(self.theta))*self.phi_vel*sin(self.theta))/I1
        self.phi_a = (I3/I1)*(self.psi_vel+self.phi_vel*cos(self.theta))*self.theta_vel/sin(self.theta)-2*cos(self.theta)*self.theta_vel*self.phi_vel/sin(self.theta)
        self.psi_a = self.phi_vel*self.theta_vel*sin(self.theta)-self.phi_a*cos(self.theta)
        # Update velocities of the Lagrangian coordinates:
        self.theta_vel += self.theta_a*dt
        self.phi_vel += self.phi_a*dt
        self.psi_vel += self.psi_a*dt
        # Update Lagrangian coordinates:
        self.theta += self.theta_vel*dt
        self.phi += self.phi_vel*dt

    def GetPos(self):
        # return the position as x, y, z
        x = sin(self.theta)*sin(self.phi)
        y = cos(self.theta)
        z = sin(self.theta)*cos(self.phi)
        return x,y,z

    def GetPower(self):
        # calculate and return the total energy
        K = .5*I1*(self.theta_vel**2+(self.phi_vel*sin(self.theta))**2)+.5*I3*(self.psi_vel+self.phi_vel*cos(self.theta))**2
        U = M*g*r*cos(self.theta)
        return K+U
    
    def GetRotationVel(self):
        # return the velocity of rotation
        return self.psi_vel
    
    def SetNutation(self,nutation):
        # set the angle of nutation
        self.theta = nutation
    
    def SetRotationVel(self,rotation_vel):
        # set the velocity of rotation
        self.psi_vel = rotation_vel