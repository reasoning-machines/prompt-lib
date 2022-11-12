#!/bin/bash
set -u


# model name should be one of `text-davinci-002` (GPT-3) or `code-davinci-002` (CODEX)
MODEL_NAME="code-davinci-002"

if [ "${MODEL_NAME}" == "text-davinci-002" ]; then
    REQ_PER_MIN=1600000
elif [ "${MODEL_NAME}" == "code-davinci-002" ]; then
    REQ_PER_MIN=16  # code-davinci-002 has a much lower throughput
else
    echo "Invalid model name"
    exit 1
fi

NUM_QUESTIONS_PER_THREAD=200
MAX_TOKENS=600

QUESTION_PREFIX="# Q: "
ANSWER_PREFIX="# solution using Python:\n"
FINAL_ANSWER_PREFIX=""
INTRA_EXAMPLE_SEP="\n\n"
INTER_EXAMPLE_SEP="\n\n\n"

EVAL_FUNC="get_acc_from_python_thoughts"

TEMP=0.0
NUM_EXAMPLES=-1

declare -a ALL_TASKS=("gsm_quco" "gsmhard_quco" "svamp_quco" "mawpsaddsub_quco" "mawpsmultiarith_quco" "mawpssingleeq_quco" "mawpssingleop_quco" "asdiv_quco")

declare -a ALL_TASKS=("fiveexamples_quco")

declare -a SEEDS=(0)

# declare -a ALL_TASKS=("humaneval_stream")

for TASK in "${ALL_TASKS[@]}"; do

    for SEED in "${SEEDS[@]}"; do

        echo "Running $TASK with seed $SEED"
        ARGS=(--task_id ${TASK}
            --num_examples ${NUM_EXAMPLES} # -1 means use all examples in the prompt
            --name "${TASK}_${MODEL_NAME}_s${SEED}"  # name of the run
            --timeout 1440  # timeout in minutes
            --model_name "${MODEL_NAME}"
            --max_requests_per_min ${REQ_PER_MIN}
            --seed ${SEED}   # decides order of examples in the prompt
            --num_questions_per_thread ${NUM_QUESTIONS_PER_THREAD}  # number of questions to ask per thread
            --max_tokens ${MAX_TOKENS}
            --question_prefix "${QUESTION_PREFIX}"
            --answer_prefix "${ANSWER_PREFIX}"
            --final_answer_prefix "${FINAL_ANSWER_PREFIX}"
            --intra_example_sep "${INTRA_EXAMPLE_SEP}"
            --inter_example_sep "${INTER_EXAMPLE_SEP}"
            --wandb_project "pal"
            --eval_function "${EVAL_FUNC}"
            --temperature ${TEMP}
            )  # number of tokens in completion


        echo "python3 run.py ${ARGS[@]}"
        python -u prompt-lib/query_openai.py "${ARGS[@]}"
    done
done

