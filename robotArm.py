import time
import math
import Adafruit_PCA9685


class RobotArm():
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.speed = .0005
        self.setcheck(False)

    def openClaw(self):
        print("open")
        self.pwm.set_pwm(3,0,self.clawMin)

    def closeClaw(self):
        print("close")
        self.pwm.set_pwm(3,0,self.clawMax)
        
    def baseMover(self, input):
        if self.check():
            #Thanks Josh for helping calculate the degrees
            x = int(2.888888889 * int(input.get()) + 130)
            y = self.get_basePos()
            if x < self.get_basePos():
                for a in range(x, self.get_basePos()):
                    y -= 1
                    self.pwm.set_pwm(4,0,(y))
                    time.sleep(self.speed)
            else:
                for a in range(self.get_basePos(), x):
                    self.pwm.set_pwm(4,0,(a + 1))
                    time.sleep(self.speed)
            self.set_basePos(x)
        else:
            print("You must home the robot first")
        
    #First X arm mover
    def xarmMover(self, input):
        if self.check():    
            xone = self.get_xarmOne()
            xtwo = self.get_xarmTwo()
            xangle = self.get_xangle()

            angle = int(input.get())
            rangle = 180 - angle

            #Thanks Josh for helping calculate the degrees 
            xMove = int(((26/9) * angle + 130))
            
            if xangle < angle:
                for i in range(xone, xMove):
                    xtwo -= 1
                    xone += 1
                    self.pwm.set_pwm(5,0,xone)
                    self.pwm.set_pwm(6,0,xtwo)
                    time.sleep(self.speed)
            else:
                for i in range( xMove , xone):
                    xtwo += 1
                    xone -= 1
                    self.pwm.set_pwm(5,0,xone)
                    self.pwm.set_pwm(6,0,xtwo)
                    time.sleep(self.speed)
            
            self.set_xangle(angle)
            self.set_xarmOne(xone)
            self.set_xarmTwo(xtwo)
        else:
            print("You must home the robot first")
        
    #Second X arm mover 
    def sxarmMover(self, input):
        if self.check():    
            xone = self.get_sxarmOne()
            xtwo = self.get_sxarmTwo()
            xangle = self.get_sxangle()

            angle = int(input.get())
            rangle = 180 - angle

            #Thanks Josh for helping calculate the degrees 
            xMove = int(((26/9) * angle + 130))
            #FIX 
            if xangle < angle:
                for i in range(xone, xMove):
                    xtwo -= 1
                    xone += 1
                    self.pwm.set_pwm(7,0,xone)
                    self.pwm.set_pwm(8,0,xtwo)
                    time.sleep(self.speed)
            else:
                for i in range( xMove , xone):
                    xtwo += 1
                    xone -= 1
                    self.pwm.set_pwm(7,0,xone)
                    self.pwm.set_pwm(8,0,xtwo)
                    time.sleep(self.speed)

            self.set_sxangle(angle)
            self.set_sxarmOne(xone)
            self.set_sxarmTwo(xtwo)
        else:
            print("You must home the robot first")

    #Third X arm mover
    # FIX
    def txarmMover(self, input):
        if self.check():    
            xone = self.get_txarmOne()
            xtwo = self.get_txarmTwo()
            xangle = self.get_txangle()

            angle = int(input.get())
            rangle = 180 - angle

            #Thanks Josh for helping calculate the degrees 
            xMove = int(((26/9) * angle + 130))
            
            if xangle < angle:
                for i in range(xone, xMove):
                    xtwo -= 1
                    xone += 1
                    self.pwm.set_pwm(9,0,xone)
                    self.pwm.set_pwm(10,0,xtwo)
                    time.sleep(self.speed)
            else:
                for i in range( xMove , xone):
                    xtwo += 1
                    xone -= 1
                    self.pwm.set_pwm(9,0,xone)
                    self.pwm.set_pwm(10,0,xtwo)
                    time.sleep(self.speed)

            self.set_txangle(angle)
            self.set_txarmOne(xone)
            self.set_txarmTwo(xtwo)
        else:
            print("You must home the robot first")


    def inverseKiematics(self, x, y, phiangle):
        #Length of links in cm
        a1 = 16.4688
        a2 = 15.7952
        a3 = 13.3698

        # Desired Position of End effector
        px = x
        py = y

        phi = phiangle
        phi = math.radians(phi)

        # Equations for Inverse kinematics
        wx = px - a3* math.cos(phi)
        wy = py - a3* math.sin(phi)

        delta = wx**2 + wy**2
        c2 = (delta -a1**2 -a2**2)/(2*a1*a2)
        s2 = math.sqrt(1-c2**2)  # elbow down
        theta_2 = math.atan2(s2, c2)

        s1 = ((a1+a2*c2)*wy - a2*s2*wx)/delta
        c1 = ((a1+a2*c2)*wx + a2*s2*wy)/delta
        theta_1 = math.atan2(s1,c1)
        theta_3 = phi-theta_1-theta_2
        if(theta_1 < 0 ):
            theta_1 = theta_1* -1

        self.xarmMover(round(math.degrees(theta_1)))
        self.sxarmMover(round(math.degrees(theta_2)))
        self.txarmMover(round(math.degrees(theta_3)))
        

    #homeing method
    def home(self):
        #4 is base
        self.pwm.set_pwm(4,0,130)
        #5 & 6 is first arm
        self.pwm.set_pwm(5,0,390)
        self.pwm.set_pwm(6,0,390)
        #7 & 8 is second arm
        self.pwm.set_pwm(7,0,390)
        self.pwm.set_pwm(8,0,390)
        #9 & 10 is third arm
        self.pwm.set_pwm(9,0,390)
        self.pwm.set_pwm(10,0,390)
        #11 wrist join
        self.pwm.set_pwm(11,0,130)
        #12 claw open/close        
        self.pwm.set_pwm(12,0,130)
        #set all 
        self.set_basePos(0)

        self.set_xangle(90)
        self.set_xarmOne(390)
        self.set_xarmTwo(390)

        self.set_sxangle(90)
        self.set_sxarmOne(390)
        self.set_sxarmTwo(390)

        self.set_txangle(90)
        self.set_txarmOne(390)
        self.set_txarmTwo(390)

        print("Homed")
        self.setcheck(True)
    

    #change the home state 
    def setcheck(self, bool):
        self.state = bool
    
    #Check if the Robot has been homed
    def check(self):
        return self.state

    #Set methods
    def set_basePos(self, basePos):
        self.basePos = basePos 
    
    def set_xangle(self, xangle):
        self.xangle = xangle
    def set_xarmOne(self, xarmOne):
        self.xarmOne = xarmOne
    def set_xarmTwo(self, xarmTwo):
        self.xarmTwo = xarmTwo
    
    def set_sxangle(self, sxangle):
        self.sxangle = sxangle
    def set_sxarmOne(self, sxarmOne):
        self.sxarmOne = sxarmOne
    def set_sxarmTwo(self, sxarmTwo):
        self.sxarmTwo = sxarmTwo

    def set_txangle(self, txangle):
        self.txangle = txangle
    def set_txarmOne(self, txarmOne):
        self.txarmOne = txarmOne
    def set_txarmTwo(self, txarmTwo):
        self.txarmTwo = txarmTwo

    #Get methods
    def get_basePos(self):
        return self.basePos
    
    def get_xangle(self):
        return self.xangle
    def get_xarmOne(self):
        return self.xarmOne
    def get_xarmTwo(self):
        return self.xarmTwo
    
    def get_sxangle(self):
        return self.sxangle
    def get_sxarmOne(self):
        return self.sxarmOne
    def get_sxarmTwo(self):
        return self.sxarmTwo

    def get_txangle(self):
        return self.txangle
    def get_txarmOne(self):
        return self.txarmOne
    def get_txarmTwo(self):
        return self.txarmTwo

