from prompts.example import Example

sports_examples_original = [
      
Example(question = "Is the following sentence plausible? ``Jamal Murray was perfect from the line.''",
    thought = "Jamal Murray is a basketball player. Being perfect from the line is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? ``Joao Moutinho caught the screen pass in the NFC championship.''",
    thought = "Joao Moutinho is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? ``Jonas Valanciunas beat the buzzer.''",
    thought = "Jonas Valanciunas is a basketball player. Beating the buzzer is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? ``Sam Darnold passed the puck.''",
    thought = "Sam Darnold is a American football player. Passing the puck is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? ``Kyle Palmieri was called for slashing.''",
    thought = "Kyle Palmieri is a hockey player. Being called for slashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? ``Carson Wentz set the pick and roll.''",
    thought = "Carson Wentz is an American football player. Pick and roll is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? ``Malcolm Brogdon banked the shot in.''",
    thought = "Malcolm Brogdon is a basketball player. Banking the shot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? ``Draymond Green threw a touchdown.''",
    thought = "Draymond Green is an basketball player. Throwing a touchdown is part of football, not basketball.",
    answer = "no"),
]


sports_task_id_to_prompt = {
    "sports_stream": sports_examples_original,
    "sports_direct": sports_examples_original,

}
