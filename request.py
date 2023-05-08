import requests


def get_oauth2_password_token(client_id, client_secret, username, password, token_url):
    data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
        "scope": "read write",  # Opcional, ajusta según las necesidades de tu aplicación
    }

    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        token_info = response.json()
        return token_info["access_token"]
    else:
        print(f"Error al obtener el token: {response.status_code} - {response.text}")
        return None


# Reemplaza los valores con la información de tu aplicación y API
client_id = "qCG7tiau6qQyHsJj32WaB0g0pPFkDAhYdWrEljTV"
client_secret = "GltmfnhWK1X6prGa76Z4wZmLqu64mpSc9cun34kC9f3tjQGl7djdqaSzOTqy0fYDQHhRVirZGV8yyj0Mt22hEZ6FnO948CYiVESZYPxhu0UC5LqqvlaHjhsrBGDhowmK"
username = "carlos"
password = "abc123."
token_url = "https://localhost:8000/oauth2/token"

access_token = get_oauth2_password_token(
    client_id, client_secret, username, password, token_url
)

if access_token:
    print(f"Token obtenido: {access_token}")
else:
    print("No se pudo obtener el token.")
