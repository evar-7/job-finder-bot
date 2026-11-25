from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Teclado base con las acciones principales del bot."""
    keyboard = [
        [
            InlineKeyboardButton("🔎 Buscar vacantes", callback_data="menu_buscar"),
            InlineKeyboardButton("⚙️ Preferencias", callback_data="menu_preferencias"),
        ],
        [
            InlineKeyboardButton("⭐ Favoritos", callback_data="menu_favoritos"),
            InlineKeyboardButton("📊 Estadísticas", callback_data="menu_estadisticas"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
