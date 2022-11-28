from prompt_lib.prompts.example import Example
humaneval = [
    Example(
        question= "\ndef fix_spaces(text):\n    \"\"\"\n    Given a string text, replace all spaces in it with underscores, \n    and if a string has more than 2 consecutive spaces, \n    then replace all consecutive spaces with - \n    \n    fix_spaces(\"Example\") == \"Example\"\n    fix_spaces(\"Example 1\") == \"Example_1\"\n    fix_spaces(\" Example 2\") == \"_Example_2\"\n    fix_spaces(\" Example   3\") == \"_Example-3\"\n    \"\"\"\n",
        answer="    new_text = \"\"\n    i = 0\n    start, end = 0, 0\n    while i < len(text):\n        if text[i] == \" \":\n            end += 1\n        else:\n            if end - start > 2:\n                new_text += \"-\"+text[i]\n            elif end - start > 0:\n                new_text += \"_\"*(end - start)+text[i]\n            else:\n                new_text += text[i]\n            start, end = i+1, i+1\n        i+=1\n    if end - start > 2:\n        new_text += \"-\"\n    elif end - start > 0:\n        new_text += \"_\"\n    return new_text\n",
        thought="",
    ),
    Example(
        question="\n\ndef same_chars(s0: str, s1: str):\n    \"\"\"\n    Check if two words have the same characters.\n    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')\n    True\n    >>> same_chars('abcd', 'dddddddabc')\n    True\n    >>> same_chars('dddddddabc', 'abcd')\n    True\n    >>> same_chars('eabcd', 'dddddddabc')\n    False\n    >>> same_chars('abcd', 'dddddddabce')\n    False\n    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')\n    False\n    \"\"\"\n",
        answer="    return set(s0) == set(s1)\n",
        thought="",
    )
]

humaneval_task_id_to_prompt = {
    "humaneval_stream": humaneval
}