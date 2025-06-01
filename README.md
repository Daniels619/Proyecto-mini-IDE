# Mini IDE Web

## Datos del Estudiante y Curso
[Aquí va tu información personal]
- Nombre del estudiante: 
- Materia: 
- Profesor: 
- Semestre: 

## Estructura del Proyecto

### 1. `app.py`
Este archivo es el punto de entrada principal de la aplicación:
- Implementa el servidor web usando Flask
- Define las rutas y endpoints de la API:
  - `/`: Ruta principal que muestra la interfaz web
  - `/analizar-lexico`: Endpoint para realizar análisis léxico
  - `/analizar-sintactico`: Endpoint para realizar análisis sintáctico
  - `/turing`: Endpoint para ejecutar la máquina de Turing
- Maneja las peticiones HTTP y coordina la comunicación entre componentes

### 2. `lexer.py`
Implementa el analizador léxico del lenguaje:
- Divide el código fuente en tokens
- Identifica y clasifica elementos del lenguaje como:
  - Palabras clave
  - Símbolos y operadores
  - Identificadores
  - Números
- Detecta tokens no permitidos y errores léxicos

### 3. `parser.py`
Implementa el analizador sintáctico:
- Analiza la estructura gramatical del código
- Verifica que las asignaciones sean válidas
- Detecta errores sintácticos como:
  - Uso de estructuras de control no permitidas
  - Símbolos prohibidos
  - Asignaciones incorrectas
- Genera mensajes de error detallados

### 4. `turing.py`
Implementa la máquina de Turing:
- Procesa las instrucciones del lenguaje
- Ejecuta las operaciones de asignación
- Simula el comportamiento de una máquina de Turing básica
- Maneja el estado de las variables y operaciones

### 5. `templates/`
Directorio que contiene las plantillas HTML:
- Archivos de interfaz web
- Formularios y elementos visuales
- Estilos y diseño de la aplicación

## Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema (versión 3.6 o superior)

2. Instala las dependencias necesarias:
```bash
pip install flask
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre tu navegador web y visita:
```
http://localhost:5000
```

## Lenguaje Personalizado

### Tokens
El analizador léxico reconoce los siguientes tipos de tokens:

1. **Palabras Clave**:
   - if, else, while, for, return (No permitidas en este lenguaje)

2. **Símbolos**:
   - Paréntesis: ( )
   - Llaves: { }
   - Operadores: +, -, *, /, =

3. **Identificadores**:
   - Nombres de variables válidos según las reglas de Python

4. **Números**:
   - Valores numéricos enteros

5. **Símbolos No Permitidos**:
   - Punto y coma (;)
   - Dos puntos (:)

### Gramática
El lenguaje sigue estas reglas sintácticas:

1. Cada línea debe contener una asignación válida
2. La asignación debe usar un solo operador '='
3. No se permiten estructuras de control (if, while, for, etc.)
4. No se permiten los símbolos ';' ni ':'
5. Los comentarios son permitidos usando '#'

### Manejo de Errores
El analizador detecta los siguientes tipos de errores:

1. Uso de símbolos no permitidos (;, :)
2. Uso de estructuras de control no permitidas
3. Asignaciones inválidas
4. Nombres de variables inválidos
5. Valores de asignación faltantes

## Ejemplos

### Código Válido
```
variable = 42
nombre = valor
resultado = 10
x = y
```

### Código Inválido
```
if x = 5          # Error: uso de estructura de control
variable = 42;    # Error: uso de punto y coma
for i in range:   # Error: uso de estructura de control y dos puntos
variable          # Error: falta operador de asignación
= 42             # Error: falta identificador
variable ==  42   # Error: asignación inválida
```

## Características Adicionales
- Interfaz web interactiva
- Análisis léxico y sintáctico en tiempo real
- Resaltado de errores
- Soporte para comentarios 

## Nombre el estudiante y datos de la materia y profesor

- Nombre del alumno: Alvarez Castro Logan Daniel

- Materia: LENGUAJES Y AUTOMATAS I

- Docente: Kevin David Molina Gomez

- Sistema educativo: Tecnológico Nacional De México

- Campus: TecNM Campus Minatitlán

- Carrera: Ingeniería En Sistemas Computacionales

- Grupo:  15:00 – 16:00hrs.

- Fecha de entrega: 30 de mayo de 2025
