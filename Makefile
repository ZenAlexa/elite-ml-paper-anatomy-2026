PYTHON ?= python3

.PHONY: catalog hydrate resolve resolve-preprints acquire acquire-preprints measure measure-preprints validate aggregate lexical

catalog:
	$(PYTHON) scripts/build_catalog.py

hydrate: catalog
	$(PYTHON) scripts/hydrate_catalog.py

resolve: hydrate
	$(PYTHON) scripts/resolve_pdf_sources.py

resolve-preprints:
	$(PYTHON) scripts/resolve_preprint_sources.py

acquire: resolve
	$(PYTHON) scripts/acquire_pdfs.py

acquire-preprints: resolve-preprints
	$(PYTHON) scripts/acquire_preprints.py

measure:
	$(PYTHON) scripts/measure_pdfs.py

measure-preprints:
	$(PYTHON) scripts/measure_pdfs.py --preprints

validate:
	uv run --with jsonschema $(PYTHON) scripts/validate.py

aggregate:
	$(PYTHON) scripts/aggregate.py

lexical:
	$(PYTHON) scripts/lexical_analysis.py
