# Usar Python 3.12 slim como imagen base (más ligera)
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements.txt primero (para aprovechar el cache de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY main.py .

# Crear un usuario no-root para mayor seguridad
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

# Exponer el puerto 8000 (estándar para FastAPI)
EXPOSE 8000

# Variables por defecto para puerto y workers (se pueden sobrescribir en runtime)
ENV PORT=8000 \
    WORKERS=1

# Comando para ejecutar la aplicación
# Usar uvicorn con configuraciones optimizadas para producción
# Ejecutar Uvicorn respetando el puerto inyectado por la plataforma y pasando proxy headers
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers ${WORKERS} --proxy-headers"]