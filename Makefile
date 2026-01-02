PYTHON = .venv/bin/python
APP = app.main:app

dev:
	$(PYTHON) -m uvicorn $(APP) --reload
