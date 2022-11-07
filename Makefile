#!make

export
tests:
	pytest
docker-up:
	docker-compose up -d
docker-down:
	docker-compose down -v --remove-orphans
run-local:
	uvicorn ixpandit.main:app
fmt:
	black . && isort . && flake8 .