# Pcasillas
Programa de casillas con viewset
#intall vitualenv
ejecutar pip install virtualenv 
#crear entorno virtual
ejecutar el siguiente comando en el directoreo donde se creara
python -m virtualenv env
#entrar al env con el siguiente comando desde windows
env\Scripts\activate
#instalar los siguientes paquetes
pip install django 
pip install django-rest-framework
pip install django-cors-headers
pip install django-filter
pip install psycopg2
pip install pycparser
pip install pytz
pip install django-rest-auth
#clonar el repositorio 
#modificar el archivo de settings dentro de la carpeta pcasillas3_1 con las bases de datos
#salir de la carpeta pcasillas3_1
#ejecutar 
python manage.py makemigrate
python manage.py migrate 
python manage.py shell
#el ultimo comando abrida una shell para crear al super usuario
copiar el contenido del .txt de super usuario y pegar en la shell 
salir usando exit()
#hacerlo correr con 
python manage.py 0.0.0.0:8000
si todo salio bien ingresar a tu "IP:8000/admin"
##############################################################################################
######################################frontend###############################################
#installar yay
#ingresar a frontend_casilas/frontend
ejecurtar yay install 
ejecutar yay run dev --host para que este enta red 
