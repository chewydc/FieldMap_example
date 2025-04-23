# 🛠️ API Field Mapping Example
Este proyecto es un ejemplo de cómo transformar la respuesta de una API utilizando un archivo de configuración externo (JSON) que define cómo deben procesarse los campos.

## 📁 Estructura del proyecto

```
project/
│
├── main.py                   # Script principal que carga datos de ejemplo y aplica la transformación
├── transform.py              # Función que aplica el mapeo de campos
├── field_map.json            # Archivo JSON con el mapeo de campos y configuración
```

## ⚙️ ¿Cómo funciona?

### 1. `field_map.json` define:

- Qué claves conservar.
- Cuáles renombrar.
- Cuáles son obligatorias.
- Cuáles descartar.

### 2. `transform.py` contiene la función `transform_api_response(data, field_map)` que aplica las reglas definidas.

### 3. `main.py`:

- Carga un ejemplo de respuesta de API.
- Carga el mapeo desde field_map.json.
- Ejecuta la transformación y muestra el resultado.

## 📌 Ejemplo de field_map.json
```
{
  "id": {"new_key": "user_id", "required": true},
  "name": {"required": true},
  "email": {"new_key": "contact_email", "required": false}
}
```
En este ejemplo:
- "id" será renombrado a "user_id" y es obligatorio.
- "name" se mantiene igual y es obligatorio.
- "email" se renombra si existe, pero no es obligatorio.
- Cualquier otro campo será descartado.

## ✅ Requisitos
- Python 3.7 o superior
- No requiere librerías externas

## 🚀 Ejecutar
```
python main.py
```
