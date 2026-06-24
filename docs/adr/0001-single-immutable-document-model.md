# ADR 0001: Use One Immutable Document Model Across Pipeline Stages

## Status

Accepted

## Context

The parser, layout analysis, translator, image exporter, and DOCX builder all
operate on the same logical document structure. Earlier stage-specific wrappers
contained no distinct data or enforceable invariants and required unnecessary
nesting between stages.

## Decision

The pipeline uses one immutable `Document` model composed of focused nested
dataclasses. Each stage receives a `Document` snapshot and returns a new snapshot
when it enriches or transforms document content. Tuple order is authoritative for
page content, table rows and cells, text runs, headers, and footers.

Stage-specific behavior remains in pipeline components rather than in the model.
New stage-specific result types should be introduced only when a stage develops a
distinct, validated contract that the shared model cannot express.

## Consequences

- Pipeline stages share one stable, format-neutral structural contract.
- Immutable snapshots preserve prior stage output without defensive copying.
- The model does not encode pipeline progress or translation state.
- The type system does not distinguish parsed, laid-out, and translated snapshots;
  stage sequencing remains the responsibility of the pipeline.
