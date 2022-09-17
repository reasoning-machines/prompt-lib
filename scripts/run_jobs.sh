#!/bin/bash
set -u



declare -a DATE_TASKS=("date_stream" "date_symb_ood" "date_symb_abs" "date_pat_wrong" "date_pat_none" "date_pat_only" "date_text_rand" "date_text_yoda_thought" "date_text_yoda_both" "date_text_inter_shuf" "date_text_intra_shuf" "date_ccot")

declare -a SPORTS_TASKS=("sports_stream" "sports_abstract_person" "sports_abstract_person_sport" "sports_abstract_person_activity_sport" "sports_symb_ood" "sports_pat_wrong" "sports_pat_none" "sports_pat_only" "sports_different_player" "sports_different_player_different_activity" "sports_text_yoda" "sports_text_yoda_thought" "sports_text_intra_shuf" "sports_text_inter_shuf" "sports_ccot")


declare -a GSM_TASKS=("gsm_stream" "gsm_no_equation" "gsm_symb_abs" "gsm_symb_ood" "gsm_text_rand" "gsm_text_yoda" "gsm_text_yoda_thought" "gsm_text_yoda_question" "gsm_text_diff_entities" "gsm_text_intra_shuf" "gsm_text_inter_shuf" "gsm_ccot")

declare -a ALL_TASKS=("date_pat_wrong" "date_pat_only" "date_pat_none" "sports_pat_wrong" "sports_pat_none" "sports_pat_only" "gsm_no_equation" "gsm_pat_wrong" "gsm_pat_only")

declare -a SEEDS=(0 1)

REQ_PER_MIN=16

for TASK in "${ALL_TASKS[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        echo "Running $TASK with seed $SEED"
        python -u query_alpa_with_text_file.py --task_id ${TASK} \
            --num_examples 0 \
            --name "${TASK}_codex_s${SEED}" \
            --timeout 1440 \
            --model_name "code-davinci-002" \
             --max_requests_per_min ${REQ_PER_MIN} --cot_task \
            --seed ${SEED} > logs/${TASK}.log 2>&1 
    done
    wait
done