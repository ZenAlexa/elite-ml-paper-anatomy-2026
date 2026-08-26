PYTHON ?= python3

.PHONY: catalog hydrate resolve acquire measure validate aggregate

catalog:
	$(PYTHON) scripts/build_catalog.py

hydrate: catalog
	$(PYTHON) scripts/hydrate_catalog.py

resolve: hydrate
	$(PYTHON) scripts/resolve_pdf_sources.py

acquire: resolve
	$(PYTHON) scripts/acquire_pdfs.py

measure:
	$(PYTHON) scripts/measure_pdfs.py

validate:
	$(PYTHON) scripts/validate.py

aggregate:
	$(PYTHON) scripts/aggregate.py
