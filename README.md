# Real Estate API

Una API completa para la gestión de propiedades inmobiliarias desarrollada con Django REST Framework.

## Tabla de Contenidos
- [Características](#características)
- [Diagrama de Base de Datos](#diagrama-de-base-de-datos)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Configuración del Entorno](#configuración-del-entorno)
- [Uso](#uso)
- [Documentación de la API](#documentación-de-la-api)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modelos](#modelos)
- [Endpoints de la API](#endpoints-de-la-api)
- [Despliegue](#despliegue)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características

- Gestión completa de propiedades inmobiliarias
- Filtrado por tipo de propiedad, ubicación, precio, etc.
- Autenticación de usuarios
- API RESTful completa
- Documentación detallada con Swagger/OpenAPI
- Soporte para Docker
- Optimización de consultas con serializers específicos

## Diagrama de Base de Datos

El siguiente diagrama muestra la estructura de la base de datos del proyecto:

![image](https://github.com/user-attachments/assets/dd799a89-98db-4e3e-9193-fb9a2dd98098)

El siguiente diagrama muestra el flujo de Trabajo de la Aplicación:

![image](https://github.com/user-attachments/assets/dab2961a-a476-4ed0-a498-1e16bdf281e4)



## Tecnologías Utilizadas

- **Backend:**
  - Django 5.1
  - Django REST Framework 3.14
  - Msql
  - 
-
- **Frontend (opcional):**
  - HTMl
  - bootstrap@5.3.0
  - Templates de Django (para interfaz básica)

## Instalación

### Opción 1: Instalación Local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/real-estate-api.git
   cd real-estate-api
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar variables de entorno:
   Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Opción 2: Instalación con Docker

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/hollrojm/real_estate_project.git
   cd real-estate-api
   ```

2. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```

## Configuración del Entorno



```
# Django settings
DEBUG=True
SECRET_KEY='django-insecure-qv_$1o3u!$7qdx#v5g!58xnv0gpgr%8ff5_=_w!9=ech=q!zd#'
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_ENGINE=django.db.backends.mysql
DB_NAME='real_estate_db'
DB_USER= 
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306


```

## Uso

### Endpoints Principales

- `GET /api/properties/`: Listar todas las propiedades
- `POST /api/properties/`: Crear una nueva propiedad
- `GET /api/properties/{id}/`: Obtener detalles de una propiedad
- `PUT /api/properties/{id}/`: Actualizar una propiedad
- `DELETE /api/properties/{id}/`: Eliminar una propiedad
- `GET /api/properties/ages/`: Obtener tipos de antigüedad disponibles
- `GET /api/locations/by_department/?department=nombre`: Obtener ciudades y distritos de un departamento

### Autenticación

La API requiere autenticación para todos los endpoints. Utiliza el esquema de autenticación por token:

```bash
# Obtener token (requiere usuario previamente creado)
curl -X POST http://localhost:8000/api-token-auth/ -d "username=usuario&password=contraseña"

# Usar el token en las solicitudes
curl -H "Authorization: Token tu-token-aquí" http://localhost:8000/api/properties/
```



Estas interfaces proporcionan información detallada sobre todos los endpoints, parámetros, respuestas y modelos.

## Estructura del Proyecto

```
real_estate_project/
├── api/                      # App para la API REST
│   ├── serializers.py        # Serializers para la API
│   ├── urls.py               # URLs de la API
│   └── views.py              # ViewSets de la API
├── core/                     # Modelos y lógica de negocio
│   ├── admin.py              # Configuración del admin
│   └── models.py             # Modelos de datos
├── docs/                     # Documentación
│   └── diagrama_bd.png       # Diagrama de la base de datos
├── frontend/                 # Frontend (opcional)
├── real_estate_project/      # Configuración del proyecto
│   ├── settings.py           # Configuración de Django
│   └── urls.py               # URLs principales
├── .env.example              # Ejemplo de variables de entorno
├── docker-compose.yml        # Configuración de Docker Compose
├── Dockerfile                # Configuración de Docker
├── manage.py                 # Script de gestión de Django
└── requirements.txt          # Dependencias del proyecto
```

## Modelos

El proyecto incluye los siguientes modelos principales:

- **Property**: Propiedades inmobiliarias
- **PropertyType**: Tipos de propiedades (Casa, Apartamento, etc.)
- **TransactionType**: Tipos de transacciones (Venta, Arriendo)
- **Owner**: Propietarios de las propiedades
- **OwnerType**: Tipos de propietarios (Inmobiliaria, Particular)
- **Location**: Ubicaciones (Departamento, Ciudad, Distrito)

## Endpoints de la API

### Propiedades

- `GET /api/properties/`: Listar propiedades
- `POST /api/properties/`: Crear propiedad
- `GET /api/properties/{id}/`: Detalles de propiedad
- `PUT /api/properties/{id}/`: Actualizar propiedad
- `PATCH /api/properties/{id}/`: Actualizar parcialmente
- `DELETE /api/properties/{id}/`: Eliminar propiedad
- `GET /api/properties/ages/`: Tipos de antigüedad

### Ubicaciones

- `GET /api/locations/`: Listar ubicaciones
- `POST /api/locations/`: Crear ubicación
- `GET /api/locations/{id}/`: Detalles de ubicación
- `PUT /api/locations/{id}/`: Actualizar ubicación
- `DELETE /api/locations/{id}/`: Eliminar ubicación
- `POST /api/locations/find_or_create/`: Buscar o crear ubicación
- `GET /api/locations/by_department/?department=nombre`: Filtrar por departamento

### Propietarios

- `GET /api/owners/`: Listar propietarios
- `POST /api/owners/`: Crear propietario
- `GET /api/owners/{id}/`: Detalles de propietario
- `PUT /api/owners/{id}/`: Actualizar propietario
- `DELETE /api/owners/{id}/`: Eliminar propietario

### Tipos de Propietarios

- `GET /api/owner_types/`: Listar tipos de propietarios
- `POST /api/owner_types/`: Crear tipo de propietario
- `GET /api/owner_types/{id}/`: Detalles de tipo de propietario
- `PUT /api/owner_types/{id}/`: Actualizar tipo de propietario
- `DELETE /api/owner_types/{id}/`: Eliminar tipo de propietario

### Tipos de Propiedades

- `GET /api/property_types/`: Listar tipos de propiedades
- `POST /api/property_types/`: Crear tipo de propiedad
- `GET /api/property_types/{id}/`: Detalles de tipo de propiedad
- `PUT /api/property_types/{id}/`: Actualizar tipo de propiedad
- `DELETE /api/property_types/{id}/`: Eliminar tipo de propiedad

### Tipos de Transacciones

- `GET /api/transaction_types/`: Listar tipos de transacciones
- `POST /api/transaction_types/`: Crear tipo de transacción
- `GET /api/transaction_types/{id}/`: Detalles de tipo de transacción
- `PUT /api/transaction_types/{id}/`: Actualizar tipo de transacción
- `DELETE /api/transaction_types/{id}/`: Eliminar tipo de transacción



### Despliegue en Producción

Para un entorno de producción, considera:

1. Configurar `DEBUG=False` y crear un  archivo `.env`
2. Establecer `ALLOWED_HOSTS` con los dominios válidos
3. Usar una base de datos PostgreSQL
4. Configurar un servidor web como Nginx como proxy inverso
5. Usar Gunicorn como servidor WSGI

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add some amazing feature'`)
4. Envía tu rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
