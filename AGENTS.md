# Project agent contract

This repository uses one independent subagent per paper.

- A paper-reading agent receives exactly one `paper_id` and must stop after completing that paper.
- It may write only `readings/<paper_id>.json` and `readings/<paper_id>.md`.
- It writes the Markdown file first and publishes the schema-valid JSON file last. A partial JSON file must never appear at the final path.
- It must read and follow `prompts/deep-read.md` and `schemas/deep-read.schema.json`.
- It must read the verified local PDF in full, including references, appendix, and supplementary material when present.
- Abstracts, search snippets, reviews, and automatic metrics cannot substitute for PDF reading.
- Every substantive judgment needs a physical PDF page, section, and short evidence anchor.
- Missing facts remain explicit missing values. Do not infer author intent without textual or layout evidence.
- Catalog, acquisition, schema, prompt, validation, and aggregate files are owned by the primary agent.
- Never edit another paper's reading files.
