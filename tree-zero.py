from  gpiozero import OutputDevice, InputDevice
from time import sleep

class XmasTree():

    def __init__(self):
        #self.A = InputDevice(21)
        #self.B = InputDevice(19)
        self.anode = InputDevice(26)
        self.cathode = InputDevice(20)

    def all_off(self):
        #self.A.close()
        #self.B.close()
        #self.C.close()
        #self.D.close()
        self.anode.close()
        self.cathode.close()

    def gen_on(self,an, cath):
        self.all_off()
        self.anode = OutputDevice(an)
        self.cathode = OutputDevice(cath)
        self.anode.value = True
        self.cathode.value = False

    def red1_on(self):
        self.all_off()
        self.C = OutputDevice(26)
        self.D = OutputDevice(20)
        self.C.value = True
        self.D.value = False

    def red2_on(self):
        self.all_off()
        self.C = OutputDevice(26)
        self.D = OutputDevice(20)
        self.C.value = False
        self.D.value = True

    def red3_on(self):
        self.all_off()
        self.B = OutputDevice(19)
        self.D = OutputDevice(20)
        self.B.value = False
        self.D.value = True

    def red4_on(self):
        self.all_off()
        self.B = OutputDevice(19)
        self.D = OutputDevice(20)
        self.B.value = True
        self.D.value = False

    def red5_on(self):
        self.all_off()
        self.B = OutputDevice(19)
        self.A = OutputDevice(21)
        self.B.value = True
        self.A.value = False

    def red6_on(self):
        self.all_off()
        self.B = OutputDevice(19)
        self.A = OutputDevice(21)
        self.A.value = True
        self.B.value = False

    def yellow_on(self):
        self.all_off()
        self.C = OutputDevice(26)
        self.A = OutputDevice(21)
        self.C.value = True
        self.A.value = False

mytree = XmasTree()
time = 0.1
while True:
    mytree.gen_on(20,26)
    sleep(time)
    mytree.gen_on(26,20)
    sleep(time)
    mytree.gen_on(19,20)
    sleep(time)

    '''mytree.red3_on()
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
