#!/bin/bash
set -u

declare -a GSM_TASKS=("gsm_stream" "gsm_direct" "gsm_no_equation" "gsm_symb_abs" "gsm_symb_ood" "gsm_text_rand" "gsm_text_yoda_thought" "gsm_text_diff_entities" "gsm_text_intra_shuf" "gsm_text_inter_shuf" "gsm_ccot" "gsm_pat_wrong" "gsm_pat_only")

declare -a DATE_TASKS=("date_stream" "date_direct" "date_symb_ood" "date_symb_abs" "date_pat_wrong" "date_pat_none" "date_pat_only" "date_text_rand" "date_text_yoda_thought" "date_text_inter_shuf" "date_text_intra_shuf" "date_ccot")

declare -a SPORTS_TASKS=("sports_stream" "sports_direct" "sports_abstract_person" "sports_abstract_person_sport" "sports_abstract_person_activity_sport" "sports_symb_ood" "sports_pat_wrong" "sports_pat_none" "sports_pat_only" "sports_ccot" "sports_different_player" "sports_different_player_different_activity" "sports_text_yoda_thought" "sports_text_intra_shuf" "sports_text_inter_shuf" "sports_ccot" "sports_text_rand")

declare -a SORTING_TASKS=("sorting_stream" "sorting_direct" "sorting_pat_none" "sorting_pat_wrong" "sorting_symb_abs" "sorting_symb_ood" "sorting_verbose")

declare -a ABS_TASKS=("gsm_symb_abs" "date_symb_abs" "sports_abstract_person" "sports_abstract_person_sport" "sports_abstract_person_activity_sport" "sorting_symb_abs")

declare -a OOD_TASKS=("gsm_symb_ood" "date_symb_ood" "sports_symb_ood" "sorting_symb_ood")

declare -a PAT_TASKS=("gsm_no_equation" "gsm_pat_wrong" "gsm_pat_only" "date_pat_wrong" "date_pat_none" "date_pat_only" "sports_pat_wrong" "sports_pat_none" "sports_pat_only" "sorting_pat_none" "sorting_pat_wrong")

declare -a CCOT_TASKS=("gsm_ccot" "date_ccot" "sports_ccot")

declare -a TEXT_RAND_TASKS=("date_text_rand" "gsm_text_rand" "sports_text_rand")

declare -a TEXT_INTRA_SHUF=("gsm_text_intra_shuf" "date_text_intra_shuf" "sports_text_intra_shuf")

declare -a TEXT_INTER_SHUF=("gsm_text_inter_shuf" "date_text_inter_shuf" "sports_text_inter_shuf")

declare -a YODA_TASKS=("gsm_text_yoda_thought" "date_text_yoda_thought" "sports_text_yoda_thought")

declare -a ALL_TASKS=("test")

declare -a SEEDS=(0 1 2)

# model name should be one of `text-davinci-002` (GPT-3) or `code-davinci-002` (CODEX)
MODEL_NAME="code-davinci-002"

if [ "${MODEL_NAME}" == "text-davinci-002" ]; then
    REQ_PER_MIN=1600000
elif [ "${MODEL_NAME}" == "code-davinci-002" ]; then
    REQ_PER_MIN=16
else
    echo "Invalid model name"
    exit 1
fi

for TASK in "${ALL_TASKS[@]}"; do

    for SEED in "${SEEDS[@]}"; do

        echo "Running $TASK with seed $SEED"
        ARGS=(--task_id ${TASK}
            --num_examples 0
            --name "${TASK}_${MODEL_NAME}_s${SEED}"
            --timeout 1440
            --model_name "${MODEL_NAME}"
            --max_requests_per_min ${REQ_PER_MIN}
            --seed ${SEED})
        if [[ ! "${TASK}" == *"direct"* ]]; then
            ARGS+=("--cot_task")
        fi
        echo "python3 run.py ${ARGS[@]}"
        python -u query_openai.py "${ARGS[@]}"
    done
done
