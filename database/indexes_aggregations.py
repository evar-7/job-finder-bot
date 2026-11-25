from typing import Any


def crear_indices() -> list[str]:
    """
    Crea los índices en 'vacantes' y 'usuarios' (por ejemplo: índice de texto
    en campos descriptivos/título, índice compuesto o TTL) y devuelve sus nombres.
    """
    raise NotImplementedError("Pendiente de implementar en database/indexes_aggregations.py")


def consultar_uso_indice(filtro: dict[str, Any]) -> dict[str, Any]:
    """
    Ejecuta explain('executionStats') sobre una consulta en 'vacantes' para verificar
    si utiliza los índices creados y qué métricas de escaneo arroja.
    """
    raise NotImplementedError("Pendiente de implementar en database/indexes_aggregations.py")


def pipeline_top_tecnologias(limite: int = 5) -> list[dict[str, Any]]:
    """
    Aggregation pipeline con $unwind, $group y $sort para obtener el Top N de
    tecnologías más solicitadas en las vacantes.
    """
    raise NotImplementedError("Pendiente de implementar en database/indexes_aggregations.py")


def pipeline_vacantes_por_ubicacion_o_modalidad() -> list[dict[str, Any]]:
    """
    Aggregation pipeline con $group y $sort para agrupar vacantes por ubicación
    o modalidad y ordenar resultados.
    """
    raise NotImplementedError("Pendiente de implementar en database/indexes_aggregations.py")
