from vencapi import VencAPI, VencOSD

stream = VencAPI("admin", "admin", "192.168.0.168")
osd_1 = VencOSD(stream, 0) 

osd_1.hide()

