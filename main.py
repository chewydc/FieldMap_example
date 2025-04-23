from transformer import transform_data_list

api_response = [
    {
        "id": 1,
        "name": "Juan Pérez",
        "email": "juan@example.com",
        "password": "123456",
        "created_at": "2024-04-01T12:00:00Z",
        "last_login": "2024-04-21T10:00:00Z"
    },
    {
        "id": 2,
        "email": "ana@example.com",
        "created_at": "2024-04-10T08:30:00Z"
    }
]

if __name__ == "__main__":
    transformed = transform_data_list(api_response, "field_map.json")
    print(transformed)
