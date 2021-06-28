# habi.com test

Rest api para consultar 

## Technical specifications


### Software requirements
* Python 3.9
* Django
* Django REST framework
* flake8
* MySql

### Project execution

El proyecto se puede instalar facilmente usando docker-compose

```bash
# Ejecutar
 docker-compose up -d
```

La documentacion wsagger se puede ver en:

[http://localhost:72/swagger-docs]

### Run Tests

Los test pueden ser ejecutados con

```bash
python manage.py test
```

## Disclaimers

- No se tienen en cuenta consideraciones de seguridad para las variables de acceso a la bd, ni para el acceso a los servicios expuestos.

## Punto dos.

### Modelo modificado

![alt text](https://github.com/yeisonlegarda/habi_backend_test/blob/main/CambiosModelo.PNG?raw=true)

el modelo en sql es [https://github.com/yeisonlegarda/habi_backend_test/blob/main/proposedModel.sql]

Se agrega la tabla  user_like_property esto debido a que es una relación muchos a muchos entre usuarios y properties indicando
que usuarios dieron like a un inmueble, teniendo el histórico, no se considera un borrado lógico en caso de que el usuario de
"dislike" a un inmueble, adicionalmente, al modelo que se encontraba se realiza un único cambio para tener el estado actual
en la tabla de inmuebles esto con el fin de no consultarlo desde el histórico, pues consultándolo desde el histórico requiere
hacer un subquery en la consulta para filtrar por este campo y a muchos mas dados va a hacer la consulta lenta.
