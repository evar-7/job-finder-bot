from typing import Any


def obtener_usuario(telegram_id: int) -> dict[str, Any] | None:
    """
    Consulta y devuelve el perfil de un estudiante en la colección 'usuarios'
    a partir de su telegram_id.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")


def actualizar_preferencias(
    telegram_id: int,
    puesto: str | None = None,
    tecnologias: list[str] | None = None,
    salario_minimo: float | int | None = None,
) -> bool:
    """
    Actualiza las preferencias de búsqueda del usuario en MongoDB usando operadores
    como $set (y/o $push/$addToSet según la lógica acordada).

    Retorna True si el documento fue actualizado correctamente.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")


def agregar_alerta(telegram_id: int, alerta: dict[str, Any]) -> bool:
    """
    Agrega una nueva alerta configurada por el usuario a su arreglo 'alertas'
    en la colección 'usuarios'.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")


def eliminar_alerta(telegram_id: int, criterio_alerta: Any) -> bool:
    """
    Elimina una alerta específica del arreglo 'alertas' del usuario usando $pull.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")


def eliminar_cuenta_o_historial(telegram_id: int, solo_historial: bool = False) -> bool:
    """
    Si solo_historial es True, limpia alertas/favoritos/preferencias del usuario;
    si es False, elimina el documento del usuario de la colección 'usuarios' con delete_one.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")


def obtener_estadisticas() -> dict[str, Any]:
    """
    Ejecuta pipelines de agregación (aggregate con $unwind, $group, $sort, etc.)
    sobre la colección 'vacantes' para devolver métricas como el Top de tecnologías
    más demandadas o distribución por modalidad/ubicación.
    """
    raise NotImplementedError("Pendiente de implementar en services/usuarios_service.py")
