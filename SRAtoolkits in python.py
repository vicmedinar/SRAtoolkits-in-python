import os
import shutil

#from setuptools.config.expand import read_files

#descargar secuencia usandon sratoolkit
# ID de la secuencia
secuencia_id = "SRR10832365" #modificar con ID de interes
comando = f"fasterq-dump {secuencia_id}  " #comando para descarga dos archivos fastq (forward y reverse)
os.system(comando)

#mover archivos a carpeta
# Ruta del archivo de origen
archivo_origen = r"C:\Users\Vistor\SRR10832365_1.fastq"
archivo_origen2 = r"C:\Users\Vistor\SRR10832365_2.fastq"
# Ruta de destino
directorio_destino = r"C:\Users\Vistor\Desktop\victor\maestria Nacional\programacion para biologos\ensayo\tareas\entregable #1\SRA"
# Mover el archivo
try:
    shutil.move(archivo_origen, directorio_destino)
    shutil.move(archivo_origen2, directorio_destino)
    print(f"El archivo ha sido movido a: {directorio_destino}")
except Exception as e:
    print(f"Hubo un error al mover el archivo: {e}")
