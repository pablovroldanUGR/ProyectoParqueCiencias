import paramiko
import os
import filetype

# IP del host a enviar y puerto SSH
host = "192.168.56.110"
port = 22

# Credenciales de acceso
username = "rpi"
password = "admin"

#Directorio al que se van a pasar las fotos
DirectorioRemoto = "/home/rpi/fotos"

#Configurar conexion SSH
client = paramiko.SSHClient()

try:

    #Abrir conexion SSH
    client.connect(host, port, username, password, look_for_keys=False)

    #Abrir conexion SFTP
    sftp = client.open_sftp()

    for archivo in os.listdir("."):
        if filetype.is_image(archivo):
            rutaLocal = archivo
            rutaRemota = DirectorioRemoto + "/" + archivo

            print("Archivo " + rutaLocal + " transferido")
            print("Nueva ruta: " + rutaRemota)
            print("-----------Enviando-------------")

            sftp.put(rutaLocal, rutaRemota)

    client.close()

except Exception as e:
    print(f"Error: {e}")