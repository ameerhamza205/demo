<!-- uvicorn core.asgi.application --port 8000 --workers 4 --log-level debug --reload -->
uvicorn core.asgi:application --port 8000 --workers 4 --log-level debug --reload
