# ProyectoParqueCiencias
Proyecto del parque de las ciencias para llevar una cámara a las capas altas de la atmósfera 

Se quiere mandar con una sonda un dispositivo capaz de hacer un time lapse (una foto por segundo...) y que envíe en tiempo real dichas fotos a un ordenador que esté en tierra conectándose con una sim (p ej. por SFTP o Whatsapp/Telegram...)

Propuesta 1:
  Utilizar un móvil y desarrollar una APK para hacer una foto cada X segundos y mandarla a un ordenador en tierra con la sim
  
  Ventajas:
    - Hardware ya incluido dentro del móvil
    - Mejor software de posprocesado de fotos
    - Mejor cámara

  Desventajas:
    - No aguanta bien el frío
    - Conexión limitada por la antena del móvil
    - Empezar a programar APKs desde cero
    - Dificultad para gestionar el móvil en remoto (necesita root)
    - Poco profesional
    - Consume mucha batería

Propuesta 2:
  Utilizar una raspberry con módulos de sim y cámara y ejecutar un script de python que se encargue de hacer la foto cada X segundos y mandarla a un ordenador en tierra con la sim

  Ventajas:
    - Consume poca batería
    - Mas profesional
    - Programación en Python/C++
    - Facil de acceder en remoto (linux directamente con ssh)
    - Se le puede instalar una mejor antena

  Desventajas:
    - Hay que buscar y montar los módulos de hardware
    - Peor cámara
    - Peor software para procesar fotos


Decisión final:
  Usar Raspberry pi zero 2w por su compatibilidad con cámaras de hasta 12MP y su bajo consumo. Puede funcionar de -20 grados a 70 grados (es ideal para el proecto). Necesitaremos un módulo de cámara, un módulo de sim (con una antena) y opcionalmente un módulo GPS.
  Raspberry pi zero 2w: [pi zero 2w](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) ~20€
  
      Enlaces de compra: [raspipc](https://www.raspipc.es/1956?src=raspberrypi) , [reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_zero_2_w_4x_1_ghz_512_mb_ram_wlan_bt-313902?utm_campaign=&track_id=&country=es&CCTYPE=private&LANGUAGE=es) , [tiendatec](https://www.tiendatec.es/raspberry-pi/gama-raspberry-pi/1735-raspberry-pi-zero-2-w.html?src=raspberrypi)

  Cámaras compatibles: 
    - Raspberry camera module 3 (12MP): [pi camera module 3](https://www.raspberrypi.com/products/camera-module-3/) ~30€
        Enlaces de compra: [raspipc](https://www.raspipc.es/2014?src=raspberrypi) , [tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1984-camara-oficial-raspberry-pi-v3-12mpx-5056561803241.html?src=raspberrypi) , [reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_camara_12mp_76_v3-339256)
    - Raspberry pi HQ camera (12.3MP): [pi HQ camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/) ~55€
      Enlaces de compra: [reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_camara_12mp_75_-276919) , [raspipc](https://www.raspipc.es/index.php?ver=tienda&accion=verArticulo&idProducto=1808&src=raspberrypi) , [tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1195-camara-hq-oficial-raspberry-pi-montura-cs-c-5056561800127.html?src=raspberrypi)
      Enlaces de compra de objetivos (gran angulares 6mm): ~30€ [reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_lente_de_camara_de_6mm_gran_angular-276922) , [raspipc](https://www.raspipc.es/1810) , [tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1192-lente-fija-4mm-montura-cs-para-camara-hq-raspberry-pi-8472496016568.html)
