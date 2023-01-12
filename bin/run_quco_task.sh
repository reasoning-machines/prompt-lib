#!/bin/bash
set -u


MODEL_NAME="code-davinci-002"

NUM_QUESTIONS_PER_THREAD=200
MAX_TOKENS=600

QUESTION_PREFIX="# Q: "
ANSWER_PREFIX="# solution using Python:\n"
FINAL_ANSWER_PREFIX=""
INTRA_EXAMPLE_SEP="\n"
INTER_EXAMPLE_SEP="\n\n"

EVAL_FUNC="get_acc_from_python_thoughts"

TEMP=0.0
num_prompt_examples=-1


declare -a ALL_TASKS=("$@")




declare -a SEEDS=(0 1 2)

# declare -a ALL_TASKS=("humaneval_stream")

for SEED in "${SEEDS[@]}"; do
    for TASK in "${ALL_TASKS[@]}"; do
        echo "Running $TASK with seed $SEED"
        ARGS=(--task_id ${TASK}
            --num_prompt_examples ${num_prompt_examples} # -1 means use all examples in the prompt
            --name "${TASK}_${MODEL_NAME}_s${SEED}"  # name of the run
            --model_name "${MODEL_NAME}"
            --seed ${SEED}   # decides order of examples in the prompt
            --num_questions_per_thread ${NUM_QUESTIONS_PER_THREAD}  # number of questions to ask per thread
            --max_tokens ${MAX_TOKENS}
            --question_prefix  "${QUESTION_PREFIX}"
            --answer_prefix "${ANSWER_PREFIX}"
            --final_answer_prefix "${FINAL_ANSWER_PREFIX}"
            --intra_example_sep "${INTRA_EXAMPLE_SEP}"
            --inter_example_sep "${INTER_EXAMPLE_SEP}"
            --wandb_project "pal"
            --eval_function "${EVAL_FUNC}"
            --temperature ${TEMP}
            )  # number of tokens in completion


        echo "python3 run.py ${ARGS[@]}"
        python -u prompt-lib/prompt_lib/run_inference.py  "${ARGS[@]}" > logs/"${TASK}_${MODEL_NAME}_s${SEED}.log" 2>&1
        # python -u prompt-lib/query_openai.py "${ARGS[@]}"

    done
done

