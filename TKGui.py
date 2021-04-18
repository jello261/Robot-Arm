import tkinter as tk
from robotArm import RobotArm
#from pyPS4Controller.controller import Controller

def main():
    window = tk.Tk()
    display(window)
    

def display(window):
    robotArm = RobotArm()
    homeButton = tk.Button(text="Home", command=lambda :robotArm.home())
    #ps3conButton = tk.Button(text="PS3 Controller", command=lambda :self.PS3(True))

    #buttons to open and close claw
    clawOpen = tk.Button(text="Open Claw", command=lambda :robotArm.openClaw())
    clawClose = tk.Button(text="Close Claw", command=lambda :robotArm.closeClaw())

    #entry and labels for the base and arms
    baseLabel = tk.Label(text="Base rotaion 0-90 130-650")
    base = tk.Entry(width=10)

    xarmLabel = tk.Label(text="First Arm 180-600")
    xarm = tk.Entry(width=10)

    sxarmLabel = tk.Label(text="Second Arm 400-700")
    sxarm = tk.Entry(width=10)

    #buttons to move the base and arms
    moveBase = tk.Button(text="Move Base", command=lambda :robotArm.baseMover(base))
    moveXarm = tk.Button(text="Move First Arm", command=lambda :robotArm.xarmMover(xarm))
    moveSXarm = tk.Button(text="Move Second Arm", command=lambda :robotArm.sxarmMover(sxarm))

    #display Buttons and entry's
    clawOpen.grid(row=0 ,column=0)
    clawClose.grid(row=0 ,column=1)

    baseLabel.grid(row=1,column=0)
    xarmLabel.grid(row=1, column=1)
    sxarmLabel.grid(row=1, column=2)

    base.grid(row=2, column=0)
    xarm.grid(row=2 ,column=1)
    sxarm.grid(row=2, column=2)

    moveBase.grid(row=3, column=0)
    moveXarm.grid(row=3, column=1)
    moveSXarm.grid(row=3, column=2)

    homeButton.grid(row=4, column=0)
    #aps3conButton.grid(row=4, column=1)

    window.mainloop()

main()
