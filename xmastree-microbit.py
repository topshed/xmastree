from microbit import *
import music

jingle = [
 'e:2','e:2','e:4',
 'e:2','e:2','e:4',
 'e:2','g:2','c','d',
 'e:8',
 'f:2','f:2','f:3',
 'f:1','f:2','e:2',
 'e:2','e:1','e:1',
 'e:2','d:2','d:2',
 'e:2','d:4','g:4',
 'e:2','e:2','e:4',
 'e:2','e:2','e:4',
 'e:2','g:2','c','d',
 'e:8','f:2','f:2','f:2',
 'f:2','f:2','e:2',
 'e:2','e:1','e:1',
 'g:2','g:2','f:2',
 'd:2', 'c:4'
]

perms = [[0,0,0,0],
         [0,0,0,1],
         [0,0,1,0],
         [0,0,1,1],
         [0,1,0,0],
         [0,1,0,1],
         [0,1,1,0],
         [0,1,1,1],
         [1,0,0,0],
         [1,0,0,1],
         [1,0,1,0],
         [1,0,1,1],
         [1,1,0,0],
         [1,1,0,1],
         [1,1,1,0],
         [1,1,1,1]]       
         
         

music.play(jingle,wait=False,loop=True)  
display.scroll("merry christmas",wait=False,loop=True)
while True:
    for x in range(10):
        for x in perms:

            pin0.write_digital(x[0])
            pin1.write_digital(x[1])
            pin2.write_digital(x[2])
            pin3.write_digital(x[3])
            print(x)
            sleep(100)