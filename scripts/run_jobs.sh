#!/bin/bash

declare -a TASKS=("gsm_symb_abs" "gsm_symb_ood" "gsm_no_equation" "gsm_stream" "gsm_direct" "sports_stream" "sports_direct" "date_stream" "date_direct")

declare -a SEEDS=(1 2)

for SEED in "${SEEDS[@]}"; do
    for TASK in "${TASKS[@]}"; do
        echo "Running $TASK with seed $SEED"
        python -u query_alpa_with_text_file.py --task_id ${TASK} \
            --num_examples 4 \
            --name "${TASK}_s${SEED}" \
            --timeout 3000 \
            --seed ${SEED} --cot_task >logs/${TASK}.log 2>&1 &
    done
done
