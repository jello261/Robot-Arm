import tkinter as tk
from robotArm import RobotArm
#from pyPS4Controller.controller import Controller

def main():
    window = tk.Tk()
    robotArm = RobotArm()
    display(window, robotArm)
    

def display(window, robotArm):
    
    homeButton = tk.Button(text="Home", command=lambda :robotArm.home())
    #ps3conButton = tk.Button(text="PS3 Controller", command=lambda :self.PS3(True))

    #buttons to open and close claw
    clawOpen = tk.Button(text="Open Claw", command=lambda :robotArm.openClaw())
    clawClose = tk.Button(text="Close Claw", command=lambda :robotArm.closeClaw())

    #entry and labels for the base and arms
    baseLabel = tk.Label(text="Base rotaion 0-180")
    base = tk.Entry(width=10)

    xarmLabel = tk.Label(text="First Arm 0-180")
    xarm = tk.Entry(width=10)

    sxarmLabel = tk.Label(text="Second Arm 0-180")
    sxarm = tk.Entry(width=10)

    txarmLabel = tk.Label(text="Thrid Arm 0-180")
    txarm = tk.Entry(width=10)

    xLabel = tk.Label(text="X Point")
    x = tk.Entry(width=10)
    
    yLabel = tk.Label(text="Y Point")
    y = tk.Entry(width=10)

    phiLabel = tk.Label(text="Angle of the last arm")
    phi = tk.Entry(width=10)

    #buttons to move the base and arms
    moveBase = tk.Button(text="Move Base", command=lambda :robotArm.baseMover(base))
    moveXarm = tk.Button(text="Move First Arm", command=lambda :robotArm.xarmMover(xarm))
    moveSXarm = tk.Button(text="Move Second Arm", command=lambda :robotArm.sxarmMover(sxarm))
    moveTXarm = tk.Button(text="Move Thrid Arm", command=lambda :robotArm.txarmMover(txarm))
    moveKin = tk.Button(text="Move arm to X, Y Potions", command=lambda :robotArm.inverseKiematics(x, y, phi))

    #display Buttons and entry's
    clawOpen.grid(row=0 ,column=0)
    clawClose.grid(row=0 ,column=1)

    baseLabel.grid(row=1,column=0)
    xarmLabel.grid(row=1, column=1)
    sxarmLabel.grid(row=1, column=2)
    txarmLabel.grid(row=1, column=3)

    base.grid(row=2, column=0)
    xarm.grid(row=2 ,column=1)
    sxarm.grid(row=2, column=2)
    txarm.grid(row=2, column=3)

    moveBase.grid(row=3, column=0)
    moveXarm.grid(row=3, column=1)
    moveSXarm.grid(row=3, column=2)
    moveTXarm.grid(row=3, column=3)

    xLabel.grid(row=4, column=0)
    yLabel.grid(row=4, column=1)
    phiLabel.grid(row=4, column=2)

    x.grid(row=5, column=0)
    y.grid(row=5, column=1)
    phi.grid(row=5, column=2)

    moveKin.grid(row=5, column=3)

    homeButton.grid(row=7, column=0)
    #aps3conButton.grid(row=4, column=1)

    window.mainloop()

main()
