
import paramiko
import os
import re
from datetime import datetime

def ObtenerArchivosRegionales(ruta):
    ruta = ruta
# ---------- CONEXIÓN SFTP ----------
    HOST = "ftp-transfer.falabella.tech"
    PORT = 1224
    USERNAME = "shiftuc_sodclprd_ftp"
    PASSWORD = "zg}]s{F[sM"

    REMOTE_DIR = "/shiftuc_sodclprd_ftp/incoming"

# ---------- RUTA LOCAL BASE ----------
   # RUTA_BASE_LOCAL = ruta

# ---------- FECHA DINÁMICA (dd-mm-yyyy) ----------
    #fecha_hoy = datetime.now().strftime("%d-%m-%Y")

# ---------- RUTA FINAL ----------
   # LOCAL_DIR = os.path.join(RUTA_BASE_LOCAL)
    #os.makedirs(LOCAL_DIR, exist_ok=True)

# ---------- CONEXIÓN ----------
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

# ---------- FILTRO DE ARCHIVOS ----------
    patron = re.compile(r"^Regional \d+\.xlsx$", re.IGNORECASE)

    sftp.chdir(REMOTE_DIR)

    for archivo in sftp.listdir():
        if patron.match(archivo):
            local_path = os.path.join(ruta, archivo)
            sftp.get(archivo, local_path)

    sftp.close()
    transport.close()