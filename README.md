# Ixpandit - Challenge

### Tecnologias
-   FastAPI (con server-side rendering usando Jinja2)
- Bootstrap y un poquito de JS Vanilla (practicamente nada jaja)
- HTTPX para hacer peticiones HTTP asincronas
- Pytest para los tests

## Instalacion
```sh
# Dentro del archivo Makefile estan los comandos por si no tienen Make instalado
# En Ubuntu viene instalado por defecto

# Con Docker
make docker-up

# Sin Docker (con una version de Python > 3.8)
python -m pip install virtualenv
python -m virtualenv env_ixpandit
- Linux/Mac: source env_ixpandit/bin/activate
- Windows: cd env_ixpandit/Scripts && activate

pip install -r requirements.txt

- Con Make: make run-local
- Sin Make: uvicorn ixpandit.main:app --reload
```

## Otros comandos
- make docker-down: eliminar el container y el volumen
- make fmt: formatear el proyecto con Flake8, Black e ISort (se instalan por aparte para no sobrecargar el requirements)
- make tests: correr los tests

## Contacto
- Wpp: https://wa.me/543874829183
- Mail: facundo.padilla@outlook.com
- LinkedIn: https://www.linkedin.com/in/facundopadilla
