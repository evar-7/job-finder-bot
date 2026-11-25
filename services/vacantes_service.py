from typing import Any


def buscar_vacantes(
    palabra_clave: str | None = None,
    tecnologias: list[str] | None = None,
    salario_minimo: float | int | None = None,
    ubicacion: str | None = None,
    limite: int = 10,
) -> list[dict[str, Any]]:
    """
    Busca vacantes en la colección 'vacantes' aplicando filtros y operadores de MongoDB
    (por ejemplo: $text/$regex, $in, $gte).

    Retorna una lista de documentos/diccionarios de vacantes listos para formatear en el bot.
    """
    raise NotImplementedError("Pendiente de implementar en services/vacantes_service.py")


def obtener_vacante_por_id(vacante_id: str) -> dict[str, Any] | None:
    """
    Obtiene una vacante específica a partir de su ObjectId en formato string.

    Retorna el documento encontrado o None si el ID no es válido o no existe.
    """
    raise NotImplementedError("Pendiente de implementar en services/vacantes_service.py")


def agregar_favorito(telegram_id: int, vacante_id: str) -> bool:
    """
    Guarda la referencia (ObjectId) de una vacante en el arreglo 'favoritos'
    del documento del usuario en la colección 'usuarios' (evitando duplicados).

    Retorna True si se agregó o ya estaba guardada, False en caso de error.
    """
    raise NotImplementedError("Pendiente de implementar en services/vacantes_service.py")


def eliminar_favorito(telegram_id: int, vacante_id: str) -> bool:
    """
    Elimina la referencia (ObjectId) de una vacante del arreglo 'favoritos'
    del usuario mediante $pull.

    Retorna True si se completó la operación, False en caso contrario.
    """
    raise NotImplementedError("Pendiente de implementar en services/vacantes_service.py")


def obtener_favoritos(telegram_id: int) -> list[dict[str, Any]]:
    """
    Consulta los ObjectId en 'favoritos' del usuario y recupera los documentos
    correspondientes desde la colección 'vacantes'.

    Retorna la lista de vacantes favoritas del usuario.
    """
    raise NotImplementedError("Pendiente de implementar en services/vacantes_service.py")
