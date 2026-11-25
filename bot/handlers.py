from datetime import datetime, timezone
from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import main_menu_keyboard
from config.database import get_collections


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Registra al estudiante si no existe en 'usuarios' y muestra el menú base."""
    if not update.effective_user or not update.message:
        return

    telegram_user = update.effective_user
    collections = get_collections()
    usuarios_col = collections["usuarios"]

    # Inserta el perfil solo si el telegram_id aún no está registrado
    usuarios_col.update_one(
        {"telegram_id": telegram_user.id},
        {
            "$setOnInsert": {
                "telegram_id": telegram_user.id,
                "nombre": telegram_user.full_name or "Estudiante",
                "preferencias": {
                    "puesto": "",
                    "tecnologias": [],
                    "salario_minimo": None,
                },
                "alertas": [],
                "favoritos": [],
                "creado_en": datetime.now(timezone.utc),
            }
        },
        upsert=True,
    )

    mensaje = (
        f"¡Hola, {telegram_user.first_name}! 👋\n\n"
        "Soy tu asistente para explorar vacantes de empleo y tendencias del mercado laboral.\n"
        "Elige una opción del menú para comenzar:"
    )

    await update.message.reply_text(mensaje, reply_markup=main_menu_keyboard())


async def menu_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja los botones iniciales falta conectar los servicios."""
    query = update.callback_query
    if not query:
        return

    await query.answer()

    respuestas_temporales = {
        "menu_buscar": "🔎 Módulo de búsqueda en construcción (próximamente con filtros de MongoDB).",
        "menu_preferencias": "⚙️ Módulo de preferencias en construcción.",
        "menu_favoritos": "⭐ Módulo de vacantes favoritas en construcción.",
        "menu_estadisticas": "📊 Módulo de estadísticas en construcción (pipelines de agregación).",
    }

    texto = respuestas_temporales.get(query.data or "", "Opción no reconocida.")
    await query.edit_message_text(text=texto, reply_markup=main_menu_keyboard())
