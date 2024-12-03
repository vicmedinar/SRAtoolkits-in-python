import os
import shutil

#descargar secuencia usandon sratoolkit
# ID de la secuencia
secuencia_id = "" #modificar con ID de interes
comando = f"fasterq-dump {secuencia_id}  " #comando para descarga dos archivos fastq (forward y reverse)
os.system(comando)

#mover archivos a carpeta
# Ruta del archivo de origen
archivo_origen = r"C:\ruta\al\archivo1.fastq" #modificar con la ruta al archivo.fastq 1
archivo_origen2 = r"C:\ruta\al\archivo2.fastq" #modificar con la ruta al archivo.fastq 2
# Ruta de destino
directorio_destino = r"C:\ruta\de\destino" #modificar con la ruta de destino para los archivos .fastq
# Mover el archivo
try:
    shutil.move(archivo_origen, directorio_destino)
    shutil.move(archivo_origen2, directorio_destino)
    print(f"El archivo ha sido movido a: {directorio_destino}")
except Exception as e:
    print(f"Hubo un error al mover el archivo: {e}")
