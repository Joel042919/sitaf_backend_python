# SITAF Backend Inteligencia Artificial (FastAPI / Python)

Este microservicio se encarga exclusivamente de las tareas de Machine Learning e Inteligencia Artificial para el SITAF, correspondientes al **Módulo 3**.

## Requisitos Previos
- **Python 3.9+**
- **pip**

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install fastapi uvicorn pydantic scikit-learn
   # (añade cualquier otra dependencia si se agregó al requirements.txt)
   ```

## Ejecución

Para iniciar el servidor de desarrollo, ejecuta:
```bash
uvicorn main:app --reload
```

El microservicio correrá en `http://localhost:8000`.

## Endpoints (Documentación Automática)
FastAPI genera documentación automática de la API. Una vez que el servidor esté corriendo, puedes visitar:
- [http://localhost:8000/docs](http://localhost:8000/docs) (Interfaz Swagger)

## Funcionalidades (Endpoints)
- `POST /predict/stock`: Devuelve predicciones de demanda futura.
- `POST /detect/anomaly`: Evalúa transacciones de medicamentos y retorna un score de riesgo.
- `POST /predict/expiration_risk`: Analiza los medicamentos e identifica posibles caducidades prioritarias.

Nota para el equipo: Este servicio es consumido directamente por **Spring Boot**, no por el Frontend.
