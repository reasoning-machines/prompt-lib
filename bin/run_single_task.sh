#!/bin/bash
set -u

declare -a TASK_TO_RUN=$1

declare -a SEEDS=(0)

# model name should be one of `text-davinci-002` (GPT-3) or `code-davinci-002` (CODEX)
MODEL_NAME="code-davinci-002"

if [ "${MODEL_NAME}" == "text-davinci-002" ]; then
    REQ_PER_MIN=1600000
elif [ "${MODEL_NAME}" == "code-davinci-002" ]; then
    REQ_PER_MIN=16   # code-davinci-002 has a much lower throughput
else
    echo "Invalid model name"
    exit 1
fi

mkdir -p logs

MAX_TOKENS=600
TEMP=0.0

NUM_QUESTIONS_PER_THREAD=500

for TASK in "${TASK_TO_RUN[@]}"; do

    for SEED in "${SEEDS[@]}"; do

        echo "Running $TASK with seed $SEED"
        ARGS=(--task_id ${TASK}
            --num_prompt_examples -1  # -1 means use all examples in the prompt
            --name "${TASK}_${MODEL_NAME}_s${SEED}"  # name of the run
            --model_name "${MODEL_NAME}"
            --max_tokens ${MAX_TOKENS}
            --max_requests_per_min ${REQ_PER_MIN}
            --seed ${SEED}   # decides order of examples in the prompt
            --num_questions_per_thread ${NUM_QUESTIONS_PER_THREAD}  # number of questions to ask per thread
            --temperature ${TEMP}  # temperature for sampling
            --num_inference_examples 3
            # --is_debug # if set, wandb logging is disabled
            ) 

        if [[ ! "${TASK}" == *"direct"* ]]; then
            ARGS+=("--cot_task")
        fi
        echo "python3 run.py ${ARGS[@]}"
        python -u prompt-lib/prompt_lib/run_inference.py  "${ARGS[@]}" > logs/"${TASK}_${MODEL_NAME}_s${SEED}.log" 2>&1

    done
done

