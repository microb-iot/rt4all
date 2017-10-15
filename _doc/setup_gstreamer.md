### Install gstreamer
```python
sudo apt-get install gstreamer1.0-libav
```
### Test own camera
```python
gst-launch-1.0 v4l2src ! videoconvert ! autovideosink
``` 

### Start stream
```python
gst-launch-1.0 -v v4l2src device="/dev/video0" ! videoconvert ! videoscale ! video/x-raw,format=I420,framerate=25/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000
```

### Connect to stream
```python
gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
```
