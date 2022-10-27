#!/bin/bash
set -u

declare -a DATE_TASKS=("date_stream" "date_symb_ood" "date_symb_abs" "date_pat_wrong" "date_pat_none" "date_pat_only" "date_text_rand" "date_text_yoda_thought" "date_text_yoda_both" "date_text_inter_shuf" "date_text_intra_shuf" "date_ccot")

declare -a SPORTS_TASKS=("sports_stream" "sports_abstract_person" "sports_abstract_person_sport" "sports_abstract_person_activity_sport" "sports_symb_ood" "sports_pat_wrong" "sports_pat_none" "sports_pat_only" "sports_different_player" "sports_different_player_different_activity" "sports_text_yoda" "sports_text_yoda_thought" "sports_text_intra_shuf" "sports_text_inter_shuf" "sports_ccot" "sports_text_rand")

declare -a GSM_TASKS=("gsm_stream" "gsm_no_equation" "gsm_symb_abs" "gsm_symb_ood" "gsm_text_rand" "gsm_text_yoda" "gsm_text_yoda_thought" "gsm_text_yoda_question" "gsm_text_diff_entities" "gsm_text_intra_shuf" "gsm_text_inter_shuf" "gsm_ccot")

declare -a ALL_TASKS=("sorting_stream" "sorting_pat_none" "sorting_pat_wrong" "sorting_symb_abs" "sorting_symb_ood" "sorting_verbose")

declare -a ALL_TASKS=("gsmsample_stream" "gsmsample_symb_abs" "gsmsample_symb_abs_var" "gsmsample_symb_abs_dig" "gsmsample_symb_abs_number" "gsmsample_symb_abs_numeric" "gsmsample_symb_abs_seq")

declare -a ALL_TASKS=("date_text_yoda_thought" "gsm_text_yoda_thought" "sports_text_yoda_thought" "sports_different_player" "sports_different_player_different_activity")

declare -a OOD_TASKS=("gsm_symb_ood" "date_symb_ood" "sports_symb_ood")

declare -a CCOT_TASKS=("gsm_ccot" "date_ccot" "sports_ccot")

declare -a RAND_TASKS=("date_text_rand" "gsm_text_rand" "sports_text_rand")

declare -a ALL_TASKS=(${RAND_TASKS[@]})


declare -a SEEDS=(1 2)

REQ_PER_MIN=16
MODEL_NAME="code-davinci-002"

for TASK in "${ALL_TASKS[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        echo "Running $TASK with seed $SEED"
        python -u query_alpa_with_text_file.py --task_id ${TASK} \
            --num_examples 0 \
            --name "${TASK}_${MODEL_NAME}_s${SEED}" \
            --timeout 1440 \
            --model_name "${MODEL_NAME}" \
            --max_requests_per_min ${REQ_PER_MIN} --cot_task \
            --seed ${SEED} >logs/${TASK}_${MODEL_NAME}_s${SEED}.log 2>&1
    done
    wait
done

#
