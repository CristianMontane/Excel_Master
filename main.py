from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI()


# Modelos Pydantic para validación de datos
class ConsultaDisponibilidad(BaseModel):
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None

class NuevaCita(BaseModel):
    cliente_nombre: str
    fecha: date
    hora: str
    tipo_descarga: str
    observaciones: Optional[str] = None

class ReprogramarCita(BaseModel):
    cita_id: str
    nueva_fecha: date
    nueva_hora: str
    motivo: Optional[str] = None

class CancelarEntrega(BaseModel):
    cita_id: str
    motivo: Optional[str] = None

# Endpoint 1: Consultar disponibilidad de franjas
@app.get("/disponibilidad")
async def consultar_disponibilidad():
    """
    Consulta la disponibilidad de franjas horarias para agendar citas
    """
    return {
        "mensaje": "La disponibilidad es de martes a jueves",
        "franjas_disponibles": [
            {"dia": "martes", "horarios": ["09:00", "14:00", "16:00"]},
            {"dia": "miércoles", "horarios": ["10:00", "15:00", "17:00"]},
            {"dia": "jueves", "horarios": ["09:30", "13:00", "15:30"]}
        ],
        "status": "success"
    }

# Endpoint 2: Agendar una nueva cita de descarga
@app.post("/agendar-cita")
async def agendar_cita(cita: NuevaCita):
    """
    Agenda una nueva cita de descarga
    """
    # Simulación de validación
    if cita.fecha.weekday() not in [1, 2, 3]:  # martes, miércoles, jueves
        raise HTTPException(
            status_code=400, 
            detail="Las citas solo se pueden agendar de martes a jueves"
        )
    
    # Generar ID ficticio para la cita
    cita_id = f"CITA_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    return {
        "mensaje": "Tu cita ha sido agendada con éxito",
        "cita_id": cita_id,
        "detalles": {
            "cliente": cita.cliente_nombre,
            "fecha": cita.fecha.strftime("%Y-%m-%d"),
            "hora": cita.hora,
            "tipo_descarga": cita.tipo_descarga
        },
        "status": "success"
    }

# Endpoint 3: Reprogramar una cita programada
@app.put("/reprogramar-cita")
async def reprogramar_cita(reprogramacion: ReprogramarCita):
    """
    Reprograma una cita ya existente
    """
    # Simulación de validación
    if reprogramacion.nueva_fecha.weekday() not in [1, 2, 3]:
        raise HTTPException(
            status_code=400, 
            detail="Las citas solo se pueden reprogramar de martes a jueves"
        )
    
    return {
        "mensaje": f"Tu cita {reprogramacion.cita_id} ha sido reprogramada con éxito",
        "nueva_fecha": reprogramacion.nueva_fecha.strftime("%Y-%m-%d"),
        "nueva_hora": reprogramacion.nueva_hora,
        "motivo": reprogramacion.motivo,
        "status": "success"
    }

# Endpoint 4: Cancelar una entrega
@app.delete("/cancelar-entrega")
async def cancelar_entrega(cancelacion: CancelarEntrega):
    """
    Cancela una entrega programada
    """
    return {
        "mensaje": f"La entrega {cancelacion.cita_id} ha sido cancelada exitosamente",
        "motivo": cancelacion.motivo,
        "fecha_cancelacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"
    }

# Endpoint de salud para verificar que la API está funcionando
@app.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado de la API
    """
    return {
        "mensaje": "API funcionando correctamente",
        "timestamp": datetime.now().isoformat(),
        "status": "healthy",
    }

# Endpoint raíz
@app.get("/")
async def root():
    """
    Endpoint raíz con información básica de la API
    """
    return {
        "mensaje": "Bienvenido al Sistema de Gestión de Citas",
        "version": "1.0.0",
        "endpoints_disponibles": [
            "GET /disponibilidad - Consultar disponibilidad",
            "POST /agendar-cita - Agendar nueva cita",
            "PUT /reprogramar-cita - Reprogramar cita",
            "DELETE /cancelar-entrega - Cancelar entrega",
            "GET /health - Estado de la API"
        ]
    }

