# Bot de Telegram y Backend API para la Recomendación de Empleos de LinkedIn

Solución de software desarrollada en **Python** con **MongoDB Atlas** (`BuscadorEmpleos`) para ayudar a estudiantes universitarios y recién graduados a buscar vacantes de empleo, gestionar preferencias y favoritos, y consultar estadísticas del mercado laboral mediante un bot interactivo de Telegram.

## Arquitectura general

- **Interfaz:** Telegram Bot API (`python-telegram-bot`) con comandos y botones interactivos.
- **Lógica / Backend:** Módulos en Python separados por responsabilidades (`bot/`, `services/`, `database/`, `config/`).
- **Persistencia NoSQL:** MongoDB Atlas (`JobFinder`) con las colecciones `usuarios` y `vacantes`, soportando documentos embebidos, referencias por `ObjectId`, índices y *aggregation pipelines*.

## Estructura del repositorio

```text
job-finder-bot/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config/
│   └── database.py
├── database/
│   ├── seed_vacantes.py
│   └── indexes_aggregations.py
├── services/
│   ├── vacantes_service.py
│   └── usuarios_service.py
└── bot/
    ├── handlers.py
    └── keyboards.py
