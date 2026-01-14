# VSCodeHelpers

Una colección curada de snippets, plantillas y configuraciones para VS Code, diseñada para aumentar la productividad de los desarrolladores. Incluye snippets de código listos para usar en varios lenguajes de programación, facilitando la escritura de código limpio, eficiente y consistente.

## Características

### Snippets

- **Snippets organizados por lenguaje**: Soporte para Java, JavaScript, Python y Markdown.
- **Categorías especializadas**: Incluye snippets para frameworks populares como Spring (Java), Django (Python), Express (Node.js), y más.
- **Instalación automática**: Script Python para instalar todos los snippets de manera sencilla.
- **Archivos de prueba**: Ejemplos de uso en cada lenguaje soportado.

### Configuraciones

La carpeta `settings` contiene diferentes archivos de configuración de VS Code, cada uno diseñado para un estilo de programación o flujo de trabajo específico. Puedes cambiar entre ellos para adaptar el editor a tus necesidades sin instalar extensiones adicionales.

## Lenguajes y Frameworks Soportados

- **Java**:
  - Core (arrays, clases, colecciones, excepciones, I/O, switches, funciones avanzadas)
  - JSP (bases, condicionales, CRUD, formularios, includes, enlaces, bucles, mensajes, tablas)
  - PicoCLI (básicos, opciones, prompts, subcomandos)
  - Spring (querys, componentes, configuración, excepciones, Thymeleaf)

- **JavaScript**:
  - Core (arrays, básicos, clases, colecciones, comentarios, excepciones, I/O, switches)
  - Node.js (child_process, events, fs, http, os, path, readline)
  - Express
  - React

- **TypeScript**:
  - Core (arrays, básicos, clases, colecciones, comentarios, excepciones, I/O, switches)
  - React

- **Python**:
  - Core (básicos, clases, colecciones, comentarios, excepciones, funciones, I/O, bucles)
  - Click (básicos, echo/colors, opciones, subcomandos)
  - Django
  - Numpy
  - Pandas

- **Markdown**:
  - Formateo, encabezados, enlaces y medios, listas, tablas y código

- **Svelte**

## Instalación

### Opción 1: Instalación Automática (Recomendada)

Ejecuta el script `add-snippets.py` para instalar todos los snippets automáticamente en tu configuración de VS Code:

```bash
python add-snippets.py
```

Este script copiará los archivos `.code-snippets` a la carpeta de snippets de usuario de VS Code.

### Opción 2: Instalación Manual

1. Abre VS Code.
2. Ve a `Archivo > Preferencias > Snippets de Usuario`.
3. Selecciona el lenguaje correspondiente (Java, JavaScript, Python, Markdown).
4. Copia y pega el contenido de los archivos `.code-snippets` relevantes desde la carpeta `snippets/` de este repositorio.

## Uso

Una vez instalados los snippets:

1. Abre un archivo en el lenguaje deseado en VS Code.
2. Escribe el prefijo del snippet (definido en cada archivo `.code-snippets`).
3. Presiona `Tab` o `Enter` para expandir el snippet.

Por ejemplo, en un archivo Java, escribe `class` y presiona `Tab` para insertar una plantilla de clase básica.

## Estructura del Proyecto

```
VSCodeHelpers/
├── add-snippets.py          # Script para instalación automática
├── LICENSE                  # Licencia del proyecto
├── README.md                
├── docs/                    # Carpeta de documentación por idiomas (en, es)
├── settings/                # Carpeta con settings para vscode
└── snippets/                # Carpeta principal de snippets
    ├── java/
    │   ├── core/
    │   ├── jsp/
    │   ├── picocli/
    │   └── spring/
    ├── javascript/
    │   ├── core/
    │   ├── node/
    │   └── react/
    ├── typecript/
    │   ├── core/
    │   └── react/
    ├── markdown/
    └── python/
        ├── click/
        ├── core/
        └── django/
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas agregar nuevos snippets o mejorar los existentes:

1. Forkea el repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nuevo-snippet`).
3. Agrega tus cambios y actualiza los archivos de prueba si es necesario.
4. Envía un Pull Request.

Asegúrate de seguir las convenciones de nomenclatura y formato de los archivos `.code-snippets`.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

Creado por [Tu Nombre] - Siéntete libre de contactarme para preguntas o sugerencias.