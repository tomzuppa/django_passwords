django_passwords/
│── manage.py                # Comando para ejecutar Django
│── .gitignore               # Archivos que no se suben al repo
│── .env                     # Variables de entorno (API Keys, DB settings)
│── README.md                # Documentación del proyecto
│── database/                 # 📌 Nueva carpeta para base de datos y backups
│   ├── db.sqlite3            # Base de datos SQLite (solo en desarrollo)
│   ├── backup.sql            # Backup de base de datos (si lo necesitas)
│── config/                   # 📌 Nueva carpeta para configuraciones modulares
│   ├── __init__.py
│   ├── base.py               # Configuración base (común a todos los entornos)
│   ├── development.py        # Configuración de desarrollo
│   ├── production.py         # Configuración de producción
│── webchecklist/             # 📌 Proyecto Django principal
│   ├── __init__.py
│   ├── asgi.py               # Configuración para ASGI
│   ├── wsgi.py               # Configuración para WSGI
│   ├── urls.py               # URLs globales del proyecto
│   ├── settings.py           # (Opcional: si no lo moviste a config/)
│   ├── templates/            # 📌 Plantillas globales (si las usas)
│── secureapp/                # 📌 Aplicación Django
│   ├── __init__.py
│   ├── admin.py              # Panel de administración de Django
│   ├── apps.py               # Configuración de la app
│   ├── forms.py              # Formularios (si los usas)
│   ├── models.py             # Modelos de base de datos
│   ├── tests.py              # Pruebas unitarias
│   ├── views.py              # Lógica de vistas
│   ├── urls.py               # URLs específicas de la app
│   ├── migrations/           # Migraciones de la base de datos
│   ├── templates/            # 📌 Plantillas de la app
│   │   ├── secureapp/        # Convención: nombre de la app aquí dentro
│   │       ├── login.html
│   │       ├── dashboard.html
│   ├── static/               # 📌 Archivos estáticos específicos de la app
│   │   ├── secureapp/        # Convención: prefijo con nombre de la app
│   │       ├── css/
│   │       ├── js/
│   │       ├── img/
│── static/                   # 📌 Archivos estáticos globales
│   ├── css/
│   ├── js/
│   ├── img/
│── media/                    # 📌 Archivos subidos por usuarios (si los manejas)
│   ├── user_uploads/