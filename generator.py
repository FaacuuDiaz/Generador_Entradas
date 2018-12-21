from PIL import Image,ImageDraw,ImageFont
import os

codigos = os.listdir(os.getcwd()+'/CodigosQR')
if len(codigos)==0:
	print('No hay codigos qr para generar las entradas')
	print('Revisar que la carpeta que contiene los codigos QR no este vacia')
	exit(-1)

if "entradas_generadas" not in os.listdir(os.getcwd()):
	os.mkdir("entradas_generadas")

if len(os.listdir(os.getcwd()+'/ImagenesFondo')) > 1:
	cant=0
	print("Elegi el numero de la Imagen que queres en el fondo de las entradas")
	for i in os.listdir(os.getcwd()+'/ImagenesFondo'):
		print(str(cant)+'-'+i.split('.')[0])
		cant+=1
	
	id_imgFondo=int(input())
	img_fondo=os.listdir(os.getcwd()+'/ImagenesFondo')[id_imgFondo]
else:
	img_fondo=os.listdir(os.getcwd()+'/ImagenesFondo')[0]		

print('Queres agregar algun titulo a la entrada?')
print('s/n')
res=input()
header=''
if(res.lower() == 's'):
	header = input('Ingrese el nombre del titulo de la entrada\n')

cant=0
print("Elegi el numero del tipo de Fuente que queres en las imagenes")
for i in os.listdir(os.getcwd()+'/Fuentes'):
	print(str(cant)+'-'+i.split('.')[0])
	cant+=1

id_fuente=int(input())
print('Queres otro tipo de fuente para el nombre y apellido?')
print('s/n')
respuesta=input()
if respuesta.lower() == "s":
	cant=0
	print("Elegi el numero del tipo de Fuente que queres en los nombres")
	for i in os.listdir(os.getcwd()+'/Fuentes'):
		print(str(cant)+'-'+i.split('.')[0])
		cant+=1
	nombre_fuente=int(input())
	nom_fuente = os.listdir(os.getcwd()+'/Fuentes')[nombre_fuente]
	fuente = os.listdir(os.getcwd()+'/Fuentes')[id_fuente]
	path = os.getcwd()+'/Fuentes/'+fuente
	path_nombre = os.getcwd()+'/Fuentes/'+nom_fuente
elif respuesta.lower() != 's' and respuesta.lower() != 'n':
	print('se debe seleccionar al menos una opcion valida')
	exit(-1)
else:	
	fuente = os.listdir(os.getcwd()+'/Fuentes')[id_fuente]
	path = os.getcwd()+'/Fuentes/'+fuente
	path_nombre = path


for qr in codigos:
	#try:
	nombre,apellido = qr.split('.')[0].split('-')

	"""Carga de la imagen de fondo de la entrada y de la imagen QR"""
	imagen = Image.open(os.getcwd()+'/ImagenesFondo/'+img_fondo)
	qr_imagen = Image.open(os.getcwd()+'/CodigosQR/'+qr)
	"""imagen QR reducida a un tamaño (X,Y)"""
	qr_imagen = qr_imagen.resize((170,170))
	"""imagen de fondo de entrada reducida a un tamaño (X,Y)"""
	reducida = imagen.resize((600,700))
	"""Pegado de la imagen QR a la imagen de la entrada"""
	reducida.paste(qr_imagen,(410,280))
	"""Configuraciones para poder realizar la incorporacion del texto a la imagen"""
	draw = ImageDraw.Draw(reducida)
	font = ImageFont.truetype(path,80) #los parametros son el path de la fuente y el tamaño de la fuente
	font2 = ImageFont.truetype(path_nombre,50)
	font3 = ImageFont.truetype(path_nombre,30)
	font_header = ImageFont.truetype(path,70)
	"""Textos que se ingresaran en la entrada"""
	draw.text((0, 5), header, font=font_header, fill="white")
	draw.text((20, 600), "EN LA RE PERA", font=font, fill="white")
	draw.text((50, 270), nombre+'\n'+apellido, font=font2, fill="white")
	draw.text((410, 225), "Codigo de\nEntrada", font=font3, fill="white")
	"""Almacenamiento de la entrada generada con el nombre y apellido del invitado en la carpeta predeterminada"""
	reducida.save(os.getcwd()+'/entradas_generadas/'+nombre+'-'+apellido+".jpg")
	#except:
	#    print("No ha sido posible cargar la imagen")
