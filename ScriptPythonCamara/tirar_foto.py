#Documentación en https://picamera.readthedocs.io/en/release-1.13/recipes1.html

from picamera import PiCamera
from datetime import datetime
from time import sleep
import os

home_dir = os.environ['/home/parqueciencias']	# Dirección del home
cam = PiCamera()								# Crear el objeto cámara
cam.resolution = (4608, 2592)					# Fijar la resolución
cam.annotate(<Metadatos de la foto>)


cam.start_preview()

time.sleep(2)
for filename in camera.capture_continuous(f"{home_dir}/img{counter:02d}.jpg"): #Tira una foto cada segundo hasta un máximo de 100
    time.sleep(1)