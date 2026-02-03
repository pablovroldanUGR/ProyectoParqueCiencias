# Proyecto Parque de las Ciencias

Proyecto para el **Parque de las Ciencias** cuyo objetivo es llevar una **cámara a las capas altas de la atmósfera** mediante una sonda.

La misión consiste en enviar un dispositivo capaz de realizar un **time‑lapse** (por ejemplo, **1 foto por segundo**) y **transmitir las imágenes en tiempo real** a un ordenador en tierra utilizando una **SIM de datos** (p. ej. vía **SFTP** o **WhatsApp/Telegram**).

---

## 🎯 Objetivos del proyecto

* Capturar imágenes de la atmósfera a gran altitud.
* Realizar un time‑lapse configurable.
* Enviar las fotografías en tiempo real a tierra.
* Minimizar consumo energético y peso.
* Garantizar funcionamiento en condiciones extremas de temperatura.

---

## Propuestas evaluadas

### 🔹 Propuesta 1: Uso de un teléfono móvil

Utilizar un **móvil** y desarrollar una **APK** que:

* Tome una fotografía cada *X* segundos.
* Envíe las imágenes a un ordenador en tierra usando la SIM.

**Ventajas**

* Hardware ya integrado en el móvil.
* Mejor software de posprocesado de imágenes.
* Cámara de mayor calidad.

**Desventajas**

* No tolera bien temperaturas bajas.
* Conectividad limitada por la antena del móvil.
* Desarrollo de APK desde cero.
* Difícil gestión remota (requiere *root*).
* Solución poco profesional.
* Alto consumo de batería.

---

### 🔹 Propuesta 2: Raspberry Pi + módulos externos

Utilizar una **Raspberry Pi** con:

* Módulo de cámara.
* Módulo SIM.
* Script en **Python/C++** para capturar y enviar imágenes.

**Ventajas**

* Bajo consumo energético.
* Enfoque más profesional.
* Programación flexible en Python/C++.
* Acceso remoto sencillo (Linux + SSH).
* Posibilidad de usar antenas externas de mayor alcance.

**Desventajas**

* Requiere búsqueda y montaje de módulos de hardware.
* Cámara de menor calidad frente a un móvil.
* Software de procesado de imágenes más limitado.

---

## Decisión final

Se elige **Raspberry Pi Zero 2 W** por:

* Compatibilidad con cámaras de hasta **12 MP**.
* **Bajo consumo** energético.
* Rango de funcionamiento aproximado de **−20 °C a 70 °C**, ideal para el proyecto.

### Componentes necesarios

* Raspberry Pi Zero 2 W
* Módulo de cámara
* Módulo SIM con antena
* (Opcional) Módulo GPS

---

## Hardware seleccionado

### Raspberry Pi Zero 2 W

* Precio aproximado: **~20 €**
* Producto: [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)

**Enlaces de compra**

* [Raspipc](https://www.raspipc.es/1956?src=raspberrypi)
* [Reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_zero_2_w_4x_1_ghz_512_mb_ram_wlan_bt-313902?country=es&CCTYPE=private&LANGUAGE=es)
* [Tiendatec](https://www.tiendatec.es/raspberry-pi/gama-raspberry-pi/1735-raspberry-pi-zero-2-w.html?src=raspberrypi)

---

### Cámaras compatibles

#### 🔸 Raspberry Pi Camera Module 3 (12 MP)

* Precio aproximado: **~30 €**
* Producto: [Camera Module 3](https://www.raspberrypi.com/products/camera-module-3/)

**Enlaces de compra**

* [Raspipc](https://www.raspipc.es/2014?src=raspberrypi)
* [Tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1984-camara-oficial-raspberry-pi-v3-12mpx-5056561803241.html?src=raspberrypi)
* [Reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_camara_12mp_76_v3-339256)

---

#### 🔸 Raspberry Pi HQ Camera (12.3 MP)

* Precio aproximado: **~55 €**
* Producto: [HQ Camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/)

**Enlaces de compra**

* [Reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_camara_12mp_75_-276919)
* [Raspipc](https://www.raspipc.es/index.php?ver=tienda&accion=verArticulo&idProducto=1808&src=raspberrypi)
* [Tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1195-camara-hq-oficial-raspberry-pi-montura-cs-c-5056561800127.html?src=raspberrypi)

**Objetivos compatibles (gran angular ~6 mm)**

* Precio aproximado: **~30 €**
* [Reichelt](https://www.reichelt.com/es/es/shop/producto/raspberry_pi_-_lente_de_camara_de_6mm_gran_angular-276922)
* [Raspipc](https://www.raspipc.es/1810)
* [Tiendatec](https://www.tiendatec.es/raspberry-pi/camaras/1192-lente-fija-4mm-montura-cs-para-camara-hq-raspberry-pi-8472496016568.html)

---

## Otros aspectos a tener en cuenta 
* Garantizar el funcionamiento en remoto utilizando un watchdog para poder "encender" el dispositivo en remoto
