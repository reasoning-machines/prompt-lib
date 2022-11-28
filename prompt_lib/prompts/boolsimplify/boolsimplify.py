from prompt_lib.prompts.example import Example

boolsimplify_examples = [
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
    Example(
        question="a & b | a & b",
        answer="a & b",
        thought="expr | expr is the same as expr",
    ),
    Example(
        question="(a | !a) | ((b & !c | c & !b) & (a | !a) | (b & !c | c & !b))",
        answer="true",
        thought="true | expr is true",
    ),
]

bool_simplify_taskid_to_prompt = {
    "boolsimplify_stream": boolsimplify_examples,
    "boolsimplify_txt": "prompt_lib/prompts/boolsimplify/boolsimplify.txt"
}