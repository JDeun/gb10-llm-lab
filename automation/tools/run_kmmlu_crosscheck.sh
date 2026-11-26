#!/usr/bin/env bash
# Cross-check our own 100-item KMMLU subset against the standard lm-eval-harness implementation.
# The model is served on the GB10; this reaches it through an SSH tunnel on 127.0.0.1:8001.
# Usage: run_kmmlu_crosscheck.sh <output-name> [limit-per-subject]
set -eu
NAME=${1:?output name}
LIMIT=${2:-5}            # 20 subjects x 5 = 100 items, the same size as our own subset
SUBJECTS=kmmlu_accounting,kmmlu_biology,kmmlu_chemistry,kmmlu_civil_engineering,kmmlu_computer_science,kmmlu_criminal_law,kmmlu_economics,kmmlu_education,kmmlu_electrical_engineering,kmmlu_health,kmmlu_korean_history,kmmlu_law,kmmlu_management,kmmlu_math,kmmlu_mechanical_engineering,kmmlu_patent,kmmlu_political_science_and_sociology,kmmlu_psychology,kmmlu_real_estate,kmmlu_taxation
cd "$(dirname "$0")"
OPENAI_API_KEY=none ./.venv/bin/lm_eval \
  --model local-completions \
  --model_args "base_url=http://127.0.0.1:8001/v1/completions,model=crosscheck,tokenizer=nvidia/Qwen3.6-35B-A3B-NVFP4,num_concurrent=4,max_retries=2,tokenized_requests=False" \
  --tasks "$SUBJECTS" \
  --limit "$LIMIT" \
  --output_path "results/$NAME" \
  --log_samples \
  --seed 0
