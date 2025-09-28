#!/bin/bash
# Script de inicio para EasyPanel

# Obtener el puerto de la variable de entorno o usar 8000 por defecto
PORT=${PORT:-8000}

# Ejecutar la aplicación con uvicorn
exec uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1