# python-toolkit

Utilidades reutilizables para mis proyectos de Python.

## Requisitos

- Python 3.14 o superior
- [uv](https://docs.astral.sh/uv/)

## Instalación

Desde la carpeta del proyecto donde quieres usar la librería:

```bash
uv add git+https://github.com/jhon-elen/python-toolkit.git
```

## Uso

### StopWatch

Mide cuánto tarda un bloque de código, en segundos.

```python
from python_toolkit.stop_watch import StopWatch

start = StopWatch.start()
# ... tu código ...
print(StopWatch.duration(start))  # ej.: 0.123
```

### @timed

Decorador que imprime cuánto tardó una función. Solo funciona con funciones `async`.

```python
from python_toolkit.stop_watch import timed

@timed
async def fetch_data():
    ...
```
