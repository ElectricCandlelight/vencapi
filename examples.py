from vencapi import VencAPI, VencOSD, VencSequence
import time

output0 = VencAPI("admin", "admin", "192.168.0.168")
zone1 = VencOSD(output0, 0) #Set up zones
zone2 = VencOSD(output0, 1)  
zone3 = VencOSD(output0, 2)  
zone4 = VencOSD(output0, 3)  

#changing one setting at a time
zone1.show() #Display zone1
zone1.hide()
zone1.text("change the text in zone1")
zone1.x_pos(10)
zone1.y_pos(10)
zone1.alpha(64) #OSD transparency [0-128]
zone1.font_size(50) #Range 8-72
zone1.text_colour(0) #Not sure what value it is expecting here
zone1.background(0)

#Change multiple settings at one time
zone1.set_osd(enable=1, x=20, y=20, alpha=64, font_size=72, colour=0, bcolour=0, txt="Zone1")

#Don't need to specify all arguments. can pick just the ones you need 
zone1.set_osd(x=20, y=20) 

#How to set up a sequence
""" For each action you want to perfrom surrond it with [] 
    specify the function name and how long you want to 
    wait before chaning to next command  """
osd_seq = VencSequence() #Set up new sequence
osd_seq.sequence([[zone1.show, 30], [zone1.hide, 30]]) #This will show zone1 for 30 seconds then hide it for 30 seconds
osd_seq.sequence_stop() #Stops the loop

#Using set_osd with sequence
osd_seq2 = VencSequence()
kofi = {"enable":1, "x":20, "y":20, "txt":"kofi.com/1030jh"} #Store all the setting you want to change in a dict
change = {"enable":1, "x":400, "y":400, "txt":"Move and change text"}
osd_seq2.sequence([[zone1.set_osd, 10, kofi], [zone1.set_osd, 10, change]])

time.sleep(70)

output0.stop_stream()