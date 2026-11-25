# Bot de Telegram y Backend API para la Recomendación de Empleos de LinkedIn

Solución de software desarrollada en **Python** con **MongoDB Atlas** (`BuscadorEmpleos`) para ayudar a estudiantes universitarios y recién graduados a buscar vacantes de empleo, gestionar preferencias y favoritos, y consultar estadísticas del mercado laboral mediante un bot interactivo de Telegram.

## Arquitectura general

- **Interfaz:** Telegram Bot API (`python-telegram-bot`) con comandos y botones interactivos.
- **Lógica / Backend:** Módulos en Python separados por responsabilidades (`bot/`, `services/`, `database/`, `config/`).
- **Persistencia NoSQL:** MongoDB Atlas (`JobFinder`) con las colecciones `usuarios` y `vacantes`, soportando documentos embebidos, referencias por `ObjectId`, índices y *aggregation pipelines*.

## Configuración del entorno con Telegram y MongoDB Atlas:

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd <carpeta-del-proyecto>
   ```

2. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

   > *(Opcional)* Si tienen algún otro proyecto de Python y prefieren aislar los paquetes de esos proyectos, pueden crear y activar un entorno virtual antes de instalar:
   > ```bash
   > python -m venv .venv
   > # En Windows:
   > .venv\Scripts\activate
   > # En macOS / Linux:
   > source .venv/bin/activate
   > ```

3. **Configurar las variables de entorno:**
   Crear archivo `.env` tomando como plantilla `.env.example`:

   ```bash
   cp .env.example .env
   ```

   Abrir `.env` y completar las credenciales de prueba:

   ```env
   TELEGRAM_TOKEN=token_de_botfather
   MONGO_URI=mongodb+srv://USUARIO:CONTRASEÑA@NOMBRE_DEL_CLUSTER.mongodb.net/?retryWrites=true&w=majority
   DB_NAME=Jobfinder
   ```

   > **Nota:** Verificar con `git status` que `.env` esté ignorado por Git para no subirlo al repositorio.

4. **Ejecutar el bot y probar la conexión:**

   ```bash
   python main.py
   ```

   * En la terminal se debería ver el mensaje de confirmación de conexión exitosa a MongoDB Atlas y que el bot está esperando mensajes.

   * Abrir bot en Telegram, escribir `/start` y comprobar que responda con el menú principal y registre el usuario en la colección `usuarios` dentro de `Jobfinder`.
   

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
```
