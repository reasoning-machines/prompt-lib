### Structure of a prompt

* A prompt is a list of examples, where each example is an instantiation of the following:

```py
@dataclass
class Example:
    question: str
    answer: str
    thought: str
```

* Depending on the task, we need several special symbols to determine the exact format of the prompt. These symbols are passed to the inference script as options:

* The `question_prefix` is the prefix to the question. For example, `# Q: `.

* The `answer_prefix` is the prefix to the answer string. For example, `let's think step by step:\n`. This is prefix to the chain.

* The `final_answer_prefix` is the prefix to the actual answer, usually something like "The answer is". The difference arises for CoT setups, where the answer contains an explanation followed by the actual answer.

* The `intra_example_sep` is the separator between the question and the answer. For example, `\n`.

* The `inter_example_sep` is the separator between two examples. For example, `\n\n`.


- See `make_prompt` in `prompt_lib/prompts/utils.py` for more details.


### Structure of a prompt

- The prompt has the following structure (for two questions)

```txt
{question_prefix}{question_1}{intra_example_sep}{answer_prefix}{thought_1}{final_answer_prefix}{answer_1}{inter_example_sep}{question_prefix}{question_2}{intra_example_sep}{answer_prefix}{thought_2}{final_answer_prefix}{answer_2}{inter_example_sep}
```

- Note that the prompt ends with `inter_example_sep`. During inference, the prompt is extended as follows:


```txt
{question_prefix}{question_1}{intra_example_sep}{answer_prefix}{thought_1}{final_answer_prefix}{answer_1}{inter_example_sep}{question_prefix}{question_2}{intra_example_sep}{answer_prefix}{thought_2}{final_answer_prefix}{answer_2}{inter_example_sep}{question_prefix}{question_3}{intra_example_sep}{answer_prefix}
```


- *NOTE*: During inference, the prompt is extended with the given question, and everything up until answer_prefix is added by the inference script.
Thus, your task file should only contain raw question without any prompt-specific prefixes.

- The question will be simply attached to the prompt, so make sure that the last inter_prompt_sep is present in the prompt.


### Example

Consider a prompt with two examples:

```py
[
    Example(
        question="!a & a & (a ^ c & d | !b)",
        answer="false",
        thought="false & expr is false",
    ),
    Example(
        question="a & b | a & c",
        answer="a & (b | c)",
        thought="a & (b | c) is the same as a & b | a & c",
    ),
]
```

* The special symbols are:

```
QUESTION_PREFIX="# Q: "
ANSWER_PREFIX="Let's think step by step:\n"
FINAL_ANSWER_PREFIX="Answer"
INTRA_EXAMPLE_SEP="\n"
INTER_EXAMPLE_SEP="\n\n"
```


The prompt will be:

```txt
# Q: !a & a & (a ^ c & d | !b)
Let's think step by step:
false & expr is false
Answer: false

# Q: a & b | a & c
Let's think step by step:
a & (b | c) is the same as a & b | a & c
Answer: a & (b | c)

```

For a new question, say `a & b | a & c`, the prompt will be extended by the inference script to:

```txt
# Q: !a & a & (a ^ c & d | !b)
Let's think step by step:
false & expr is false
Answer: false

# Q: a & b | a & c
Let's think step by step:
a & (b | c) is the same as a & b | a & c
Answer: a & (b | c)

# Q: a & b | a & c
```
