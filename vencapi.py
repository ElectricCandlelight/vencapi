import time
import requests
import threading

class VencAPI:
    def __init__(self, username, password, host, output_id=0):
        self.username = username
        self.password = password
        self.host = host
        self.output_id = output_id
        self.url= "http://{}:{}@{}/".format(username, password, host)

    def reboot(self):
        command = self.url + "reboot"
        requests.get(command)

    def reset(self):
        command = self.url + "reset"
        requests.get(command)
    
    def status(self):
        command = self.url + "get_status"
        requests.get(command)


class VencOSD:
    def __init__(self, VencAPI, osd_id):
        self.url = VencAPI.url + "set_osd?enc_chn={}&osd_chn={}".format(VencAPI.output_id, osd_id)

    def show(self):
        command = self.url + "&enable=1"
        requests.get(command)
        
    def hide(self):
        command = self.url + "&enable=0"
        requests.get(command)

    def x_pos(self, x_val):
        command = self.url + "&x={}".format(x_val)
        requests.get(command)

    def y_pos(self, y_val):
        command = self.url + "&y={}".format(y_val)
        requests.get(command)

    def text(self, text):
        command = self.url + "&txt={}".format(text)
        requests.get(command)
    
    def alpha(self, alpha_val):
        command = self.url + "&alpha={}".format(alpha_val)
        requests.get(command)
    
    def font_size(self, size):
        command = self.url + "&font_size={}".format(size)
        requests.get(command)

    def text_colour(self, colour):
        command = self.url + "&color={}".format(colour)
        requests.get(command)

    def background(self, colour):
        command = self.url + "&bcolor={}".format(colour)
        requests.get(command)

    def set_osd(self, enable=None, x=None, y=None, alpha=None, font_size=None, colour=None, bcolour=None, txt=None):
        command = self.url
        if enable is not None:
            command = command + "&enable={}".format(enable)
        if x is not None:
            command = command + "&x={}".format(x)
        if y is not None:
            command = command + "&y={}".format(y) 
        if alpha is not None:
            command = command + "&alpha={}".format(alpha)
        if font_size is not None:
            command = command + "&font_size={}".format(font_size) 
        if colour is not None:
            command = command + "&color={}".format(color) 
        if bcolour is not None:
            command = command + "&bcolor={}".format(bcolor)
        if txt is not None:
            command = command + "&txt={}".format(txt)
        requests.get(command)


class VencSequence:
    def __init__(self):
        self.stopped = False
    
    def sequence(self, func_seq):
        self.stopped = False
        seq_thread = threading.Thread(target=self.sequence_thread_handler, args=(func_seq,), daemon=True)
        seq_thread.start()

    def sequence_thread_handler(self, func_seq):
        while not self.stopped:
            for packed_func in func_seq:
                if not self.stopped:
                    def unpack_func(func_name, sleep, *args):
                        if not args:
                            func_name()
                        elif type(args[0]) is dict:
                            func_name(**args[0])
                        else:
                            func_name(args[0])
                        time.sleep(sleep)
                    unpack_func(packed_func[0], packed_func[1], *packed_func[2:])

    def sequence_stop(self):
        self.stopped = True
        
