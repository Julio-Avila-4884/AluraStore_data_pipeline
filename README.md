# Telecom ETL Pipeline

Este repositorio incluye archivos de ejemplo para probar el pipeline ETL de telecomunicaciones.

Pipeline ETL desarrollado en Python para la ingesta, transformación y carga de datos de clientes de telecomunicaciones.

El pipeline procesa datos en formato JSON, aplica limpieza y validaciones básicas, y carga el resultado tanto en un archivo CSV final como en una base de datos PostgreSQL.

---

## Tecnologías

- Python 3.11+
- Pandas
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy

---

## Estructura del proyecto
telecom_pipeline/
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
├── data/
│ ├── source/
│ ├── raw/
│ └── final/
├── sql/
│ └── validation.sql/
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## Ejecución

### 1. Levantar dependencias

PostgreSQL se ejecuta en un contenedor Docker.

docker compose up -d

### 2. Ejecutar el pipeline

Desde la raíz del proyecto:

python src/main.py

## Validación de datos

Después de la carga, se pueden ejecutar consultas SQL básicas para validar el contenido de la tabla `telecom_customers`.
Las consultas de ejemplo se encuentran en `sql/validation.sql`.