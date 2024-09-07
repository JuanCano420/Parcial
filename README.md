# PQR Cotizaciones - Guía de Ejecución

## Requerimientos

- **Python 3.x**
- **Entorno virtual** (venv)
- **Librerías especificadas en `requirements.txt`**

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/JuanCano420/Parcial
    ```

2. **Crear y activar el entorno virtual:**

    - **En Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    - **En Linux/MacOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Instalar las dependencias:**

    Asegúrate de que el entorno virtual esté activado, luego instala las dependencias listadas en `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para ejecutar el programa, usa el siguiente comando mientras estás en el directorio raíz del proyecto (donde se encuentra el directorio `app`):

```bash
python app/main.py
