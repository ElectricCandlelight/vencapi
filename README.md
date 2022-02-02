# vencapi:

Python wrapper for hi3520d hardware encoder API, Examples of hardware are [UrayTech](http://uray.ltd/h-pd-133.html#_pp=0_304_9_-1), [J-tech](https://jtechdigital.com/product/h264-ip-encoder-live-streaming/), [NTI](https://www.networktechinc.com/h264-hdmi-encoder.html) and [Orivision](https://www.orivision.com.cn/c/h264-hdmi-encoder_0017)

# Requirements:

Requests ```pip install requests``` 		https://pypi.org/project/requests/

# Usage:

See [simple_example.py](https://github.com/ElectricCandlelight/vencapi/blob/main/simple_example.py) and [examples.py](https://github.com/ElectricCandlelight/vencapi/blob/main/examples.py)

```python
from vencapi import VencAPI, VencOSD

stream = VencAPI("admin", "admin", "192.168.0.168") #Username, password and the IP of the encoder
osd_1 = VencOSD(stream, 0) #Sets up zone 1

osd_1.hide() #Hide zone 1
```
