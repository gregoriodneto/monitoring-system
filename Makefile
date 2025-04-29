build:
	docker build -t monitoring-system .

up:
	docker compose up -d --build

test:
	docker exec monitoring-system bash -c "export PYTHONPATH=/app && pytest /app/tests"