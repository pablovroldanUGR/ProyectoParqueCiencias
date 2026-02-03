import paramiko
import os

# IP del host a enviar y puerto SSH
host = "192.168.1.106"
port = 22

# Credenciales de acceso
username = "rpi"
password = "admin"

#Directorio al que se van a pasar las fotos
DirectorioRemoto = "/home/rpi/fotos"

#Configurar conexion SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

try:

    #Abrir conexion SSH
    client.connect(host, port, username, password)

    #Abrir conexion SFTP
    sftp = client.open_sftp()

    for archivo in os.listdir("."):
        if os.is_file(archivo)
            rutaLocal = os.cu archivo
            rutaRemota = DirectorioRemoto + "/" + archivo

        print(rutaLocal)
        print(rutaRemota)

except Exception as e:
    print(f"Error: {e}")