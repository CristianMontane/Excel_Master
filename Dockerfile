# Usamos una imagen base oficial de Python
# Python 3.12 es estable y compatible con FastAPI
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
# Todo nuestro código estará en esta carpeta
WORKDIR /app

# Copiamos el archivo de dependencias primero
# Esto permite que Docker use cache si las dependencias no cambian
COPY requirements.txt .

# Instalamos las dependencias
# --no-cache-dir evita que se guarden archivos temporales innecesarios
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo nuestro código al contenedor
COPY . .

# Exponemos el puerto 8000 (puerto estándar de FastAPI)
EXPOSE 8000

# Comando para ejecutar la aplicación
# uvicorn es el servidor que ejecutará nuestra API
# --host 0.0.0.0 permite conexiones desde cualquier IP
# --port 8000 especifica el puerto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]