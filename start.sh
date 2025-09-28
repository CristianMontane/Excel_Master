#!/bin/bash

# Script de inicio para Easy Panel
# Este script se ejecuta cuando el contenedor se inicia

echo "🚀 Iniciando FastAPI App para Easy Panel..."
echo "📅 Fecha: $(date)"
echo "🌐 Puerto: 8000"
echo "📋 Endpoints disponibles:"
echo "   - / (raíz)"
echo "   - /disponibilidad"
echo "   - /disponibilidad/libres"
echo "   - /docs (documentación)"

# Ejecutar la aplicación
exec uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1