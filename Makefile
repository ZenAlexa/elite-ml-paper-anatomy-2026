PYTHON ?= python3

.PHONY: catalog hydrate resolve resolve-preprints acquire acquire-preprints measure measure-preprints sample validate aggregate cohort lexical index blueprint checkpoint checkpoint-figures next next-icml

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

sample:
	$(PYTHON) scripts/build_analysis_sample.py

validate:
	uv run --with jsonschema $(PYTHON) scripts/validate.py

aggregate:
	$(PYTHON) scripts/aggregate.py

cohort:
	$(PYTHON) scripts/cohort_analysis.py

lexical:
	$(PYTHON) scripts/lexical_analysis.py

index:
	$(PYTHON) scripts/build_reading_index.py

blueprint:
	$(PYTHON) scripts/build_iclr_blueprint.py

checkpoint:
	$(PYTHON) scripts/aggregate.py
	$(PYTHON) scripts/cohort_analysis.py --bootstrap-replicates 5000
	$(PYTHON) scripts/lexical_analysis.py
	$(PYTHON) scripts/checkpoint_analysis.py --target 250
	$(PYTHON) scripts/checkpoint_design_taxonomy.py --target 250
	$(PYTHON) scripts/checkpoint_limitation_taxonomy.py --target 250
	$(PYTHON) scripts/render_checkpoint_figures.py --target 250
	$(PYTHON) scripts/build_reading_index.py
	$(PYTHON) scripts/build_iclr_blueprint.py

checkpoint-figures:
	$(PYTHON) scripts/render_checkpoint_figures.py --target 250

next:
	$(PYTHON) scripts/next_batch.py --limit 3

next-icml:
	$(PYTHON) scripts/next_batch.py --conference ICML --source any --limit 3
