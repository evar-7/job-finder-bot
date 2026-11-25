from datetime import datetime, timezone
from typing import Any


def normalizar_vacante(raw_item: dict[str, Any]) -> dict[str, Any]:
    """
    Transforma un registro crudo (por ejemplo, del JSON de prueba)
    al esquema estándar de la colección 'vacantes' en JobFinder.
    """
    raise NotImplementedError("Pendiente de implementar en database/seed_vacantes.py")


def cargar_vacantes_desde_json(ruta_archivo: str) -> list[dict[str, Any]]:
    """
    Lee el archivo JSON con vacantes y devuelve la lista de documentos normalizados.
    """
    raise NotImplementedError("Pendiente de implementar en database/seed_vacantes.py")


def insertar_vacantes(vacantes: list[dict[str, Any]], evitar_duplicados: bool = True) -> int:
    """
    Inserta los documentos en la colección 'vacantes' de MongoDB Atlas.
    Retorna la cantidad de documentos insertados.
    """
    raise NotImplementedError("Pendiente de implementar en database/seed_vacantes.py")


if __name__ == "__main__":
    # Ejemplo de uso local
    raise NotImplementedError("Ejecución directa pendiente de implementar.")
