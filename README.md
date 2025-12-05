# API con Litestar y PostgreSQL

API REST para gestión de biblioteca que permite administrar usuarios, libros y préstamos. Incluye autenticación JWT y documentación interactiva (Swagger/Scalar).

## Requisitos

- [uv](https://github.com/astral-sh/uv)
- PostgreSQL

## Inicio rápido

```bash
uv sync                      # Instala las dependencias
cp .env.example .env         # Configura las variables de entorno (ajusta según sea necesario)
uv run alembic upgrade head  # Aplica las migraciones de la base de datos
uv run litestar --reload     # Inicia el servidor de desarrollo
# Accede a http://localhost:8000/schema para ver la documentación de la API
```

## Variables de entorno

Crea un archivo `.env` basado en `.env.example`:

- `DEBUG`: Modo debug (True/False)
- `JWT_SECRET_KEY`: Clave secreta para tokens JWT
- `DATABASE_URL`: URL de conexión a PostgreSQL (formato: `postgresql+psycopg://usuario:contraseña@host:puerto/nombre_bd`). Recuerda crear la base de datos antes de ejecutar la aplicación con `createdb nombre_bd`.

## Estructura del proyecto

```
app/
├── controllers/     # Endpoints de la API (auth, book, loan, user)
├── dtos/            # Data Transfer Objects
├── repositories/    # Capa de acceso a datos
├── models.py        # Modelos SQLAlchemy (User, Book, Loan)
├── db.py            # Configuración de base de datos
├── config.py        # Configuración de la aplicación
└── security.py      # Autenticación y seguridad
migrations/          # Migraciones de Alembic
```

## Crear una copia privada de este repositorio

Para crear una copia privada de este repositorio en tu propia cuenta de GitHub, conservando el historial de commits, sigue estos pasos:

- Primero, crea un repositorio privado en tu cuenta de GitHub. Guarda la URL del nuevo repositorio.
- Luego, ejecuta los siguientes comandos en tu terminal, reemplazando `<URL_DE_TU_REPOSITORIO_PRIVADO>` con la URL de tu nuevo repositorio privado:

  ```bash
  git clone https://github.com/dialvarezs/learning-vue-bd2-2025 # Clona el repositorio
  cd learning-vue-bd2-2025
  git remote remove origin                                      # Elimina el origen remoto existente
  git remote add origin <URL_DE_TU_REPOSITORIO_PRIVADO>         # Agrega el nuevo origen remoto
  git push -u origin main                                       # Sube la rama principal al
  ```
# Cambios Realizados - Tarea 2

### Descripción General

Esta tarea implementó funcionalidades avanzadas para el sistema de gestión de biblioteca, incluyendo:

- Sistema de categorías con relaciones many-to-many
- Sistema de reseñas de libros
- Gestión avanzada de inventario
- Sistema completo de préstamos con estados y multas
- Métodos de búsqueda y filtrado en repositorios
- Base de datos inicial con datos de ejemplo

| Punto | Requisito | Estado | Observaciones |
|-------|-----------|--------|---------------|
| 1 | Crear modelo Category con relación many-to-many a Book | ✅ Cumplido 
| 2 | Crear modelo Review para reseñas de libros | ✅ Cumplido 
| 3 | Actualizar modelo Book con inventario y descripción | ✅ Cumplido 
| 4 | Actualizar modelo User con email y datos adicionales | ✅ Cumplido 
| 5 | Actualizar modelo Loan con fechas y estado | ✅ Cumplido 
| 6 | Implementar métodos en BookRepository | ✅ Cumplido 
| 7 | Implementar métodos en LoanRepository | ✅ Cumplido
| 8 | Crear base de datos inicial (initial_data.sql) | ✅ Cumplido 


**Para cargar los datos iniciales:**

```bash
psql -U tu_usuario -d tu_base_de_datos -f initial_data.sql
```