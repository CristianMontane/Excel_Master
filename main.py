from fastapi import FastAPI
from typing import List, Dict

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Disponibilidad",
    description="API simple para consultar disponibilidad de franjas horarias",
    version="1.0.0"
)

# Datos de ejemplo para las franjas disponibles
franjas_disponibles = [
    {
        "dia": "martes",
        "hora_inicio": "13:00",
        "hora_fin": "14:00",
        "disponible": True,
        "descripcion": "Franja disponible de 1 a 2 PM"
    },
    {
        "dia": "miércoles", 
        "hora_inicio": "13:00",
        "hora_fin": "14:00",
        "disponible": True,
        "descripcion": "Franja disponible de 1 a 2 PM"
    },
    {
        "dia": "jueves",
        "hora_inicio": "10:00", 
        "hora_fin": "11:00",
        "disponible": True,
        "descripcion": "Franja disponible de 10 a 11 AM"
    },
    {
        "dia": "viernes",
        "hora_inicio": "15:00",
        "hora_fin": "16:00", 
        "disponible": False,
        "descripcion": "Franja ocupada"
    }
]

@app.get("/")
def read_root():
    """Endpoint raíz con información básica de la API"""
    return {
        "mensaje": "API de Disponibilidad funcionando correctamente",
        "version": "1.0.0",
        "endpoints_disponibles": [
            "/disponibilidad - Consultar todas las franjas",
            "/disponibilidad/libres - Solo franjas disponibles", 
            "/docs - Documentación interactiva"
        ]
    }

@app.get("/disponibilidad")
def consultar_disponibilidad():
    """Consultar todas las franjas horarias (disponibles y ocupadas)"""
    return {
        "mensaje": "Consulta de disponibilidad realizada",
        "total_franjas": len(franjas_disponibles),
        "franjas": franjas_disponibles
    }