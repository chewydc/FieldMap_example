import json
from transform import transform_api_response

def load_field_map(file_path: str) -> dict:
    """
    Carga el archivo JSON que contiene el mapeo de campos.
    :param file_path: Ruta al archivo JSON.
    :return: El diccionario de mapeo de campos.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Ejemplo de respuesta de API (lista de objetos)
    api_response = [
        {"id": 12345, "name": "John Doe", "email": "johndoe@example.com", "extra_field": "This will be discarded"},
        {"id": 67890, "name": "Jane Smith", "email": "janesmith@example.com",
         "extra_field": "This will also be discarded"}
    ]

    # Cargar el mapeo de campos desde el archivo JSON
    field_map = load_field_map("field_map.json")

    # Transformar los datos
    transformed_data = transform_api_response(api_response, field_map)

    # Mostrar los datos transformados
    print("Transformed Data:", json.dumps(transformed_data, indent=2))

if __name__ == "__main__":
    main()
