from  gpiozero import OutputDevice, InputDevice
from time import sleep

class XmasTree(): # define our xmas tree as a Python class

# When we create a new tree, we set the pins that it uses.
# Each pin is a 'node' that is used to control 2 LEDs. Each LED
# uses 2 nodes: one is the anode, the other the cathode

    def __init__(self, node1, node2, node3, node4):
        self.anode = InputDevice(node1)
        self.cathode = InputDevice(node2)
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4

# A function to turn off any LED which is on.

    def all_off(self):
        self.anode.close()
        self.cathode.close()

# A function to turn on an LED
# We pass in anode and cathode values

    def gen_on(self,anode, cathode):
        self.all_off()
        self.anode = OutputDevice(anode)
        self.cathode = OutputDevice(cathode)
        self.anode.value = True
        self.cathode.value = False

# A function for each of the LEDs
# It just calls the gen_on() and passes in
# the correct anode and acthode values

    def red1_on(self):
        self.gen_on(self.node4, self.node3)

    def red2_on(self):
        self.gen_on(self.node3, self.node4)

    def red3_on(self):
        self.gen_on(self.node4, self.node2)

    def red4_on(self):
        self.gen_on(self.node2, self.node4)

    def red5_on(self):
        self.gen_on(self.node1, self.node2)

    def red6_on(self):
        self.gen_on(self.node2, self.node1)

    def yellow_on(self):
        self.gen_on(self.node3, self.node1)

    def all_on(self,time):
        t = 0.001
        for p in range(int((time/t)/7)):
            self.red1_on()
            sleep(t)
            self.red2_on()
            sleep(t)
            self.red3_on()
            sleep(t)
            self.red4_on()
            sleep(t)
            self.red5_on()
            sleep(t)
            self.red6_on()
            sleep(t)
            self.yellow_on()
            sleep(t)


mytree = XmasTree(21,19,26,20)
time = 0.1

mytree.all_on(5)

'''while True:
    mytree.red1_on()
    sleep(time)
    mytree.red2_on()
    sleep(time)
    mytree.red3_on()
    sleep(time)
    mytree.red4_on()
    sleep(time)
    mytree.red5_on()
    sleep(time)
    mytree.red6_on()
    sleep(time)
    mytree.yellow_on()
    sleep(time)'''
