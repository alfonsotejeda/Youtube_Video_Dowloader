"""
dowlader.py

Este módulo proporciona funcionalidades para descargar archivos desde diferentes fuentes.
Incluye funciones para manejar descargas HTTP y FTP, así como para gestionar errores comunes
durante el proceso de descarga.

Funciones:
----------
- download_http(url, destino): Descarga un archivo desde una URL HTTP y lo guarda en el destino especificado.
- download_ftp(servidor, ruta_remota, destino): Descarga un archivo desde un servidor FTP y lo guarda en el destino especificado.
- manejar_error(error): Maneja los errores que pueden ocurrir durante el proceso de descarga.

Ejemplos:
---------
Ejemplo de descarga HTTP:
>>> download_http('http://example.com/archivo.zip', '/ruta/al/destino/archivo.zip')

Ejemplo de descarga FTP:
>>> download_ftp('ftp.example.com', '/ruta/remota/archivo.zip', '/ruta/al/destino/archivo.zip')
"""
