### Archivos del código

**src/**: Contendrá el código fuente principal de tu aplicación.

`main.py`: Archivo principal que inicia la aplicación.

**camera/**: Contendrá el código relacionado con la cámara.

`camera_module.py`: Contendrá la lógica para interactuar con la cámara.

**gui/**: Contendrá el código relacionado con la interfaz gráfica de usuario (GUI).

`buttons.py`: Contendrá la lógica para manejar eventos de botones.

`display.py`: Contendrá la lógica para la pantalla HDMI.

**peripherals/**: Contendrá el código relacionado con los dispositivos periféricos como los motores.

`motors.py`: Contendrá la lógica para controlar los motores.

**utils/**: Contendrá módulos de utilidad compartidos por varias partes de la aplicación.

`helpers.py`: Contendrá funciones y utilidades comunes utilizadas en todo el proyecto.

### Archivos adicionales:

`requirements.txt`: Se puede incluir las dependencias de tu proyecto aquí para facilitar la instalación.

`README.md`: Un archivo de documentación para describir tu proyecto y proporcionar información sobre cómo ejecutarlo.

### ¿Por que se usa __init__.py?
Archivo de inicialización para marcar la carpeta como un paquete de Python.

Recordar que Python busca módulos en los directorios que contienen un archivo __init__.py. Por lo tanto, gracias a estos archivos, los directorios camera, gui, peripherals, y utils se consideran paquetes y sus módulos pueden ser importados de esta manera.
- `from camera import camera_module` importa el módulo camera_module del paquete camera.
- `from gui import buttons, display` importa los módulos buttons y display del paquete gui.
- `from peripherals import motors` importa el módulo motors del paquete peripherals.
- `from utils import helpers` importa el módulo helpers del paquete utils.

El archivo `__init__.py` no tiene por qué tener contenido dentro, se puede dejar vacío. 