# Soluciones LeetCode
Bienvenido a mi repositorio de soluciones para problemas de **LeetCode**.

Aquí encontrarás mis implementaciones y explicaciones para diversos problemas de algoritmos y estructuras de datos. El objetivo es mejorar mis habilidades de programación y documentar todo lo que iré resolviendo.

## Estructura del repositorio
```
study_plan
   ├── src
   │   ├── categoria_1
   │   │   ├── problema_1.py
   │   │   ├── problema_2.py
   │   ├── categoria_2
   │   │   ├── problema_3.py
   │   │   ├── problema_4.py
   ├── tests
   │   ├── categoria_1
   │   │   ├── test_problema_1.py
   │   │   ├── test_problema_2.py
   │   ├── categoria_2
   │   │   ├── test_problema_3.py
   │   │   ├── test_problema_4.py
   ├── requirements.txt
   ├── pytest.ini
```
- Cada carpeta corresponde a un plan de estudios diferente.
- Dentro del plan de estudios, habrá una carpeta `src` con los problemas resueltos (separados por categorías), una carpeta `tests` con los tests correspondientes y archivos de dependencias o configuraciones para el entorno de desarrollo (`requirements.txt`, `pytest.ini`, etc.).
- Los scripts incluyen el enunciado del problema y la solución en código.
- En cada categoría se proporcionan test propios para verificar la validez de las soluciones.

## Tecnologías utilizadas
A medida que resuelva diferentes problemas, iré añadiendo las tecnologías utilizadas. Por ahora, he usado:
- Python
    - Pytest
    - Pandas

## Cómo probar el repositorio
1. Clona el repositorio:
    ```bash
    git clone https://github.com/rafaroldan93/soluciones-leetcode
    ```
2. Navega a la carpeta del plan de estudios que deseas probar:
    ```bash
    cd study_plan
    ```
3. Inicia un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows
    pip install -r requirements.txt
    ```
4. Para probar los scripts puedes:
    - Ejecutar los scripts individualmente directamente:
     ```bash
     python src/categoría/problema.py
     ```
    - Ejecutar los tests:
     ```bash
     pytest -v
     ```

## Recursos útiles

- [Página principal de LeetCode](https://leetcode.com)
- [Documentación oficial de Python en español](https://docs.python.org/es/3.13/)