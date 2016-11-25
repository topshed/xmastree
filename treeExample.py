import xmasTree as tree
from time import sleep

# setup our tree with the pins it's connected to:
mytree = tree.XmasTree(21,19,26,20)

mytree.led1_on() # turn on a red LED
sleep(1) # wait one second
mytree.led1_on() # turn on another red LED
# note that the first one turns off!

mytree.yellow_pulse(1,1,5) # make the yellow led glow 5 times

mytree.all_on(2) # turn all the LEDs on
