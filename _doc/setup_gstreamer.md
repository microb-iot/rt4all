### Instalar gstreamer
```python
sudo apt-get install gstreamer1.0-libav
```
### Probar camara
```python
gst-launch-1.0 v4l2src ! videoconvert ! autovideosink
``` 

### Comenzar stream
```python
gst-launch-1.0 -v v4l2src device="/dev/video0" ! videoconvert ! videoscale ! video/x-raw,format=I420,framerate=25/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000
```

### Conectar a stream
```python
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
```

### Instalar pygst
```python
sudo apt-get install python-gst-1.0
sudo apt-get install python-gst-1.0-dbg
sudo apt-get install python-gst0.10
```