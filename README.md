# Generador_Entradas
Este repositorio sirve para generar entradas con codigos qr existentes standar para cualquier joda que quieras hacer, asi no permitis pasar a cualquier desconcido a que te rompa las pelotas en tu joda. El mismo se ejecuta con Python3 por lo que su utilizacion es por de mas decir que mas simple que tu vieja.
Para utilizar el generador de entradas se debe descargar la libreria Pillow la cual puede instalar con el siguiente comando

pip install Pillow

Para ejecutar el archivo se debe utilizar el siguiente comando:

Python3 generator.py

Antes de la ejecucion del programa se debe verificar que las imagenes de los codigos QR esten situados en la carpeta correspondiente(CodigosQR, si no te diste cuenta consulta un medico(?), debido a que si no existe ninguno no se generará ninguna entrada. El formato de la imagen QR es el siguiente.

nombre-apellido.formato

Si no se respeta el formato se incorporará el caracter separador al nombre del invitado.

Una vez finalizado el archivo se generará automaticamente una carpeta con las entradas generadas las cuales son archivos jpg con el nombre y apellido que se establecio en la imagen QR
