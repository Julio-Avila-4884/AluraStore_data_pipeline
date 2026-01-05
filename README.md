# AluraStore ETL Pipeline

Pipeline ETL desarrollado en Python para la ingesta, transformación y carga de datos de ventas de una cadena de tiendas ficticia llamada **AluraStore**.

El pipeline procesa datos de **4 tiendas diferentes**, cada una representada por un archivo CSV independiente, aplica limpieza y normalización, y genera un dataset final listo para análisis.

Este proyecto tiene fines **educativos y de portafolio**, enfocado en prácticas reales de Data Engineering a nivel Junior.

---

## Contexto del dataset

- Cada archivo CSV representa una tienda distinta:
  - `sample_tienda_1.csv` → Tienda 1
  - `sample_tienda_2.csv` → Tienda 2
  - `sample_tienda_3.csv` → Tienda 3
  - `sample_tienda_4.csv` → Tienda 4

- El precio no contiene separadores (`.` o `,`) y se interpreta como **peso colombiano**
- La fecha de compra tiene formato `dd/mm/yyyy`
- Incluye coordenadas (`lat`, `lon`) para posibles análisis geográficos

---

## Tecnologías utilizadas

- Python 3.11+
- Pandas

---

## Estructura del proyecto

```text
alura_store_pipeline/
├── src/
│   ├── ingest.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── data/
│   ├── source/
│   ├── raw/
│   └── final/
├── requirements.txt
└── README.md

## Ejecución del pipeline

Desde la raíz del proyecto, con el entorno virtual activo:

```bash
python src/main.py
