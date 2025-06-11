FROM python:3.12-slim

WORKDIR /app

# Copiar solo requerimientos primero para cachear mejor
COPY requerimientos.txt /app/

# Instalar setuptools antes de instalar requerimientos
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requerimientos.txt

# Copiar el resto del proyecto
COPY TecnoStore /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
