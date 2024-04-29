from solucion_p1 import process_class #importamos la funcion

def create_email(nombre, apellido):
    
    '''La función recibirá el nombre y apellido de cada alumno/a y 
       devolverá una dirección de correo en el dominio de Educación Navarra.
        Parámetros:
            - tendremos dos str con el nombre y el apellido de cada alumno/a.
        Salida:
            -la función devolveremos un str con el email resultante.
    '''
# llama la funcion para leer los datos del archivo y almacenarlo 
#en la variable alumnado
alumnado = process_class("class.csv")
dominio = '@educacion.navarra.es'
for alumno in alumnado:
    nombre = alumno["Nombre"]
    apellido = alumno["Apellido"]
    email_resultante = nombre[0] + apellido[:5] + dominio
    print(f"{nombre} {apellido}: {email_resultante}")