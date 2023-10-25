from prompt_lib.prompts.example import Example

sports_examples_original = [
      
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Jamal Murray is a basketball player. Being perfect from the line is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Joao Moutinho is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Jonas Valanciunas is a basketball player. Beating the buzzer is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Sam Darnold is a American football player. Passing the puck is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Kyle Palmieri is a hockey player. Being called for slashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Carson Wentz is an American football player. Pick and roll is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Malcolm Brogdon is a basketball player. Banking the shot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Draymond Green is an basketball player. Throwing a touchdown is part of football, not basketball.",
    answer = "no"),
]

abstract_person = [
  
Example(question = "Is the following sentence plausible? 'PERSON was perfect from the line.'",
    thought = "PERSON is a basketball player. Being perfect from the line is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON caught the screen pass in the NFC championship.'",
    thought = "PERSON is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON beat the buzzer.'",
    thought = "PERSON is a basketball player. Beating the buzzer is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON passed the puck.'",
    thought = "PERSON is a American football player. Passing the puck is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON was called for slashing.'",
    thought = "PERSON is a hockey player. Being called for slashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON set the pick and roll.'",
    thought = "PERSON is an American football player. Pick and roll is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON banked the shot in.'",
    thought = "PERSON is a basketball player. Banking the shot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON threw a touchdown.'",
    thought = "PERSON is an basketball player. Throwing a touchdown is part of football, not basketball.",
    answer = "no"),
]

abstract_sport = [
  
Example(question = "Is the following sentence plausible? 'Jamel Murray was perfect from the line.'",
    thought = "Jamal Murray is a SPORT1 player. Being perfect from the line is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Joao Moutinho is a SPORT2 player. The NFC championship is part of SPORT3, not SPORT2.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Jonas Valanciunas is a SPORT1 player. Beating the buzzer is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Sam Darnold is a SPORT3 player. Passing the puck is part of SPORT4, not SPORT3.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Kyle Palmieri is a SPORT4 player. Being called for slashing is part of SPORT4.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Carson Wentz is an SPORT3 player. Pick and roll is part of SPORT1, not SPORT3.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Malcolm Brogdon is a SPORT1 player. Banking the shot in is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Draymond Green is an SPORT1 player. Throwing a touchdown is part of SPORT3, not SPORT1.",
    answer = "no"),
]

abstract_person_sport = [
  
Example(question = "Is the following sentence plausible? 'PERSON was perfect from the line.'",
    thought = "PERSON is a SPORT1 player. Being perfect from the line is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON caught the screen pass in the NFC championship.'",
    thought = "PERSON is a SPORT3 player. The NFC championship is part of SPORT2, not SPORT3.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON beat the buzzer.'",
    thought = "PERSON is a SPORT1 player. Beating the buzzer is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON passed the puck.'",
    thought = "PERSON is a SPORT2 player. Passing the puck is part of SPORT4, not SPORT2.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON was called for slashing.'",
    thought = "PERSON is a SPORT4 player. Being called for slashing is part of SPORT4.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON set the pick and roll.'",
    thought = "PERSON is an SPORT2 player. Pick and roll is part of SPORT1, not SPORT2.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON banked the shot in.'",
    thought = "PERSON is a SPORT1 player. Banking the shot in is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON threw a touchdown.'",
    thought = "PERSON is an SPORT1 player. Throwing a touchdown is part of SPORT2, not SPORT1.",
    answer = "no"),
]

abstract_person_activity_sport = [
  
Example(question = "Is the following sentence plausible? 'PERSON was involved in ACTIVITY.'",
    thought = "PERSON is a SPORT1 player. Being ACTIVITY is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON does ACTIVITY.'",
    thought = "PERSON is a SPORT2 player. The ACTIVITY is part of SPORT3, not SPORT2.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON finishes ACTIVITY.'",
    thought = "PERSON is a SPORT1 player. ACTIVITY is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON performs ACTIVITY.'",
    thought = "PERSON is a SPORT3 player. ACTIVITY is part of SPORT4, not SPORT3.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON was seen doing ACTIVITY.'",
    thought = "PERSON is a SPORT4 player. Being ACTIVITY is part of SPORT4.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON complete ACTIVITY.'",
    thought = "PERSON is an SPORT3 player. ACTIVITY is part of SPORT1, not SPORT3.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'PERSON executes ACTIVITY.'",
    thought = "PERSON is a SPORT1 player. ACTIVITY is part of SPORT1.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'PERSON carries out ACTIVITY.'",
    thought = "PERSON is an SPORT1 player. ACTIVITY is part of SPORT3, not SPORT1.",
    answer = "no"),
]

ood = [
  
Example(question = "Is the following sentence plausible? 'Adair Foster was juggling the paper cups.'",
    thought = "Adair Foster is a basketball player. Juggling the paper cups is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Scottie Colby caught the hot potato in the NFC championship.'",
    thought = "Scottie Colby is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Chas Jase beat the buzzer.'",
    thought = "Chas Jase is a basketball player. Beating the pillow is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Denny Dillan passed the soda.'",
    thought = "Denny Dillan is a American football player. Passing the soda is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Myron Storm was called for trashing.'",
    thought = "Myron Storm is a hockey player. Being called for trashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Cliff Kristopher set the tick and floor.'",
    thought = "Cliff Kristopher is an American football player. Tick and floor is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Celestine Holden banked the pot in.'",
    thought = "Celestine Holden is a basketball player. Banking the pot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Peter Abraham threw a tantrum.'",
    thought = "Peter Abraham is an basketball player. Throwing a tantrum is part of football, not basketball.",
    answer = "no"),
]

wrong = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Jamal Murray is a soccer player. Being perfect from the line is part of soccer.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Joao Moutinho is a basketball player. The NFC championship is part of American football, not basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Jonas Valanciunas is an American football player. Beating the buzzer is part of American football.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Sam Darnold is a basketball player. Passing the puck is part of American football, not basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Kyle Palmieri is an American football player. Being called for slashing is part of American football.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Carson Wentz is a hockey player. Pick and roll is part of football, not hockey.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Malcolm Brogdon is a hockey player. Banking the shot in is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Draymond Green is an American football player. Throwing a touchdown is part of hockey, not American football.",
    answer = "no"),
]


no_pat = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Jamal Murray is a basketball player. Being perfect from the line is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Joao Moutinho and the NFC championship are not both part of American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Beating the buzzer, Jonas Valanciunas, and basketball player are related.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Both are a part of different sports.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Being called for slashing is Ice hockey too.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "One of them is related to American football player, the other to basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "They seem to be related.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "The person and the activity are unrelated to each other.",
    answer = "no"),
]

only_pat = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Both are a part of the same sport.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Both are a part of different sports.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Both are a part of the same sport.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Both are a part of different sports.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Both are a part of the same sport.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Both are a part of different sports.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Both are a part of the same sport.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Both are a part of different sports.",
    answer = "no"),
]

text_random = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Sam Darnold is a American football player. Passing the puck is part of hockey, not American football.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Draymond Green is an basketball player. Throwing a touchdown is part of football, not basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Carson Wentz is an American football player. Pick and roll is part of basketball, not football.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Jamal Murray is a basketball player. Being perfect from the line is part of basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Joao Moutinho is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Malcolm Brogdon is a basketball player. Banking the shot in is part of basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Jonas Valanciunas is a basketball player. Beating the buzzer is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Kyle Palmieri is a hockey player. Being called for slashing is part of hockey.",
    answer = "no"),
]


text_shuf_intra = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "is a player Jamal basketball Murray. from line Being perfect part is the basketball of",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Moutinho player is soccer a Joao. NFC American soccer of championship The not is part football,",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "is a Valanciunas Jonas basketball player. part buzzer basketball the Beating of is",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "a Sam player football is Darnold American. of hockey, puck the football American is Passing part not",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Palmieri player hockey a is Kyle. called Being of part slashing hockey for is",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "football Carson is American player Wentz an. roll and not basketball, part is Pick football of",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "player basketball Brogdon Malcolm a is. the Banking shot in of basketball part is",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "an is Draymond player basketball Green. Throwing football, a of touchdown part not is basketball",
    answer = "no"),
]

text_shuf_inter = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "perfect player. basketball. a Murray part basketball is of Being Jamal is the from line",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "American soccer. Moutinho not soccer Joao is part player. NFC The football, a championship is of",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Valanciunas of player. the basketball Jonas Beating is buzzer is part a basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "football is puck the hockey, player. not football. Darnold part a American of American Passing Sam is",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "hockey. of Palmieri slashing Kyle Being a player. called part hockey is is for",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "is football not football. Carson Pick roll basketball, and part Wentz American an of player. is",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "player. is of a in Brogdon basketball Banking shot the basketball. part Malcolm is",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "of an a is touchdown football, Green basketball Draymond basketball. not player. is part Throwing",
    answer = "no"),
]

yoda = [
  
Example(question = "Is the following sentence plausible? 'Perfect from the line Jamal Murray was.'",
    thought = "A basketball player Jamal Murray is. Perfect from the line is part of basketball being.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'The screen pass in the nfc championship Joao Moutinho caught.'",
    thought = "A soccer player Joao Moutinho is. Part of American football the nfc championship is, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'The buzzer Jonas Valanciunas beat.'",
    thought = "A basketball player Jonas Valanciunas is. The buzzer is part of basketball beating.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Passed the puck, Sam darnold did.'",
    thought = "An American football player Sam darnold is. Part of hockey passing the puck is, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Called for slashing Kyle Palmieri was.'",
    thought = "A hockey player Kyle Palmieri is. Called for slashing is part of hockey being.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'The pick and roll Carson Wentz set.'",
    thought = "An American football player Carson Wentz is. Part of basketball pick and roll is, not football.",
    answer = "no"),
Example(question = "is the following sentence plausible? In 'Malcolm Brogdon banked the shot.'",
    thought = "A basketball player Malcolm Brogdon is. In is part of basketball banking the shot.",
    answer = "yes"),
Example(question = "is the following sentence plausible? A touchdown 'Draymond Green threw.'",
    thought = "An basketball player Draymond Green is. A touchdown is part of football throwing, not basketball.",
    answer = "no"),
]

yoda_thought = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "A basketball player Jamal Murray is. Perfect from the line is part of basketball being.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "A soccer player Joao Moutinho is. Part of American football the nfc championship is, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "A basketball player Jonas Valanciunas is. The buzzer is part of basketball beating.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "An American football player Sam darnold is. Part of hockey passing the puck is, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "A hockey player Kyle Palmieri is. Called for slashing is part of hockey being.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "An American football player Carson Wentz is. Part of basketball pick and roll is, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "A basketball player Malcolm Brogdon is. In is part of basketball banking the shot.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "An basketball player Draymond Green is. A touchdown is part of football throwing, not basketball.",
    answer = "no"),
]

ccot = [
Example(question = "Is the following sentence plausible? 'Jamel Murray was perfect from the line.'",
    thought = "Jamal Murray -> basketball. perfect from the line -> basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Joao Moutinho -> soccer. NFC championship -> American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Jonas Valanciunas -> basketball. beating the buzzer -> basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Sam Darnold -> American football. passing the puck -> hockey.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Kyle Palmieri -> hockey. called for slashing -> hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Carson Wentz is -> American football. pick and roll -> basketball.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Malcolm Brogdon -> basketball. banking the shot in -> basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Draymond Green -> basketball. throwing a touchdown -> football.",
    answer = "no"),
]

different_player = [
  
Example(question = "Is the following sentence plausible? 'Jamal Murray was perfect from the line.'",
    thought = "Adair Foster is a basketball player. Being perfect from the line is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Scottie Colby is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Chas Jase is a basketball player. Beating the buzzer is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Sam Darnold passed the puck.'",
    thought = "Denny Dillan is a American football player. Passing the puck is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Kyle Palmieri was called for slashing.'",
    thought = "Myron Storm is a hockey player. Being called for slashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Carson Wentz set the pick and roll.'",
    thought = "Cliff Kristopher is an American football player. Pick and roll is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible? 'Malcolm Brogdon banked the shot in.'",
    thought = "Celestine Holden is a basketball player. Banking the shot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible? 'Draymond Green threw a touchdown.'",
    thought = "Peter Abraham is an basketball player. Throwing a touchdown is part of football, not basketball.",
    answer = "no"),
]


different_player_different_activity = [
Example(question = "Is the following sentence plausible ? 'Jamal Murray was perfect from the line.'",
    thought = "Adair Foster is a basketball player. Juggling the paper cups is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible ? 'Joao Moutinho caught the screen pass in the NFC championship.'",
    thought = "Scottie Colby is a soccer player. The NFC championship is part of American football, not soccer.",
    answer = "no"),
Example(question = "Is the following sentence plausible ? 'Jonas Valanciunas beat the buzzer.'",
    thought = "Chas Jase is a basketball player. Beating the pillow is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible ? 'Sam Darnold passed the puck.'",
    thought = "Denny Dillan is a American football player. Passing the soda is part of hockey, not American football.",
    answer = "no"),
Example(question = "Is the following sentence plausible ? 'Kyle Palmieri was called for slashing.'",
    thought = "Myron Storm is a hockey player. Being called for trashing is part of hockey.",
    answer = "yes"),
Example(question = "Is the following sentence plausible ? 'Carson Wentz set the pick and roll.'",
    thought = "Cliff Kristopher is an American football player. Tick and floor is part of basketball, not football.",
    answer = "no"),
Example(question = "Is the following sentence plausible ? 'Malcolm Brogdon banked the shot in.'",
    thought = "Celestine Holden is a basketball player. Banking the pot in is part of basketball.",
    answer = "yes"),
Example(question = "Is the following sentence plausible ? 'Draymond Green threw a touchdown.'",
    thought = "Peter Abraham is an basketball player. Throwing a tantrum is part of football, not basketball.",
    answer = "no"),
]

# Redefining the function to convert the sports "thought" sentences into passive voice
def convert_sports_to_passive(thought):
    # Split the thought into sentences
    sentences = thought.split('. ')
    # Convert each sentence to passive
    for i, sentence in enumerate(sentences):
        if "Jamal Murray is a basketball player" in sentence:
            sentences[i] = "Basketball is the game played by Jamal Murray"
        elif "Joao Moutinho is a soccer player" in sentence:
            sentences[i] = "Soccer is the game played by Joao Moutinho"
        elif "Jonas Valanciunas is a basketball player" in sentence:
            sentences[i] = "Basketball is the game played by Jonas Valanciunas"
        elif "Sam Darnold is a American football player" in sentence:
            sentences[i] = "American football is the game played by Sam Darnold"
        elif "Kyle Palmieri is a hockey player" in sentence:
            sentences[i] = "Hockey is the game played by Kyle Palmieri"
        elif "Carson Wentz is an American football player" in sentence:
            sentences[i] = "American football is the game played by Carson Wentz"
        elif "Malcolm Brogdon is a basketball player" in sentence:
            sentences[i] = "Basketball is the game played by Malcolm Brogdon"
        elif "Draymond Green is an basketball player" in sentence:
            sentences[i] = "Basketball is the game played by Draymond Green"
    
    # Join the sentences back
    passive_thought = '. '.join(sentences)
    return passive_thought

# Re-applying the passive voice function

# Function to create nominalization for sports thoughts
def convert_sports_to_nominalization(thought):
    if "Jamal Murray is a basketball player." in thought:
        return "Jamal Murray's identification as a basketball player and the association of being perfect from the line with basketball make it plausible."
    if "Joao Moutinho is a soccer player." in thought:
        return "Joao Moutinho's recognition as a soccer player and the NFC championship's link to American football make it implausible."
    if "Jonas Valanciunas is a basketball player." in thought:
        return "Jonas Valanciunas's status as a basketball player and the act of beating the buzzer being part of basketball confirm its plausibility."
    if "Sam Darnold is a American football player." in thought:
        return "Sam Darnold's association with American football and the act of passing the puck being linked to hockey make it implausible."
    if "Kyle Palmieri is a hockey player." in thought:
        return "Kyle Palmieri's identification as a hockey player and the call for slashing being a hockey term confirm its plausibility."
    if "Carson Wentz is an American football player." in thought:
        return "Carson Wentz's recognition as a football player and the pick and roll being a basketball move make it implausible."
    if "Malcolm Brogdon is a basketball player." in thought:
        return "Malcolm Brogdon's status as a basketball player and the act of banking the shot being part of basketball confirm its plausibility."
    if "Draymond Green is an basketball player." in thought:
        return "Draymond Green's association with basketball and the act of throwing a touchdown being a football term make it implausible."
    
# Applying the function


# Function to create cleft sentences for sports thoughts
def convert_sports_to_cleft(thought):
    if "Jamal Murray is a basketball player." in thought:
        return "It is Jamal Murray who is a basketball player. It is being perfect from the line that is part of basketball."
    if "Joao Moutinho is a soccer player." in thought:
        return "It is Joao Moutinho who is a soccer player. It is the NFC championship that is part of American football, not soccer."
    if "Jonas Valanciunas is a basketball player." in thought:
        return "It is Jonas Valanciunas who is a basketball player. It is beating the buzzer that is part of basketball."
    if "Sam Darnold is a American football player." in thought:
        return "It is Sam Darnold who is an American football player. It is passing the puck that is part of hockey, not American football."
    if "Kyle Palmieri is a hockey player." in thought:
        return "It is Kyle Palmieri who is a hockey player. It is being called for slashing that is part of hockey."
    if "Carson Wentz is an American football player." in thought:
        return "It is Carson Wentz who is an American football player. It is pick and roll that is part of basketball, not football."
    if "Malcolm Brogdon is a basketball player." in thought:
        return "It is Malcolm Brogdon who is a basketball player. It is banking the shot in that is part of basketball."
    if "Draymond Green is an basketball player." in thought:
        return "It is Draymond Green who is a basketball player. It is throwing a touchdown that is part of football, not basketball."
    
# Applying the function

# Function to create nested clauses for sports thoughts
def convert_sports_to_nested(thought):
    if "Jamal Murray is a basketball player." in thought:
        return "Since Jamal Murray is a basketball player, being perfect from the line, which is part of basketball, makes it plausible."
    if "Joao Moutinho is a soccer player." in thought:
        return "While Joao Moutinho is a soccer player, the fact that the NFC championship, which is part of American football and not soccer, makes it implausible."
    if "Jonas Valanciunas is a basketball player." in thought:
        return "Given that Jonas Valanciunas is a basketball player, beating the buzzer, which is part of basketball, confirms its plausibility."
    if "Sam Darnold is a American football player." in thought:
        return "Because Sam Darnold is an American football player, the act of passing the puck, which is linked to hockey and not American football, makes it implausible."
    if "Kyle Palmieri is a hockey player." in thought:
        return "Given that Kyle Palmieri is a hockey player, being called for slashing, which is part of hockey, confirms its plausibility."
    if "Carson Wentz is an American football player." in thought:
        return "While Carson Wentz is an American football player, the pick and roll move, which is part of basketball and not football, makes it implausible."
    if "Malcolm Brogdon is a basketball player." in thought:
        return "Given that Malcolm Brogdon is a basketball player, banking the shot in, which is part of basketball, confirms its plausibility."
    if "Draymond Green is an basketball player." in thought:
        return "Although Draymond Green is a basketball player, the act of throwing a touchdown, which is a football term and not a basketball one, makes it implausible."
    
# Applying the function

# Function to create fronting for sports thoughts
def convert_sports_to_fronting(thought):
    if "Jamal Murray is a basketball player." in thought:
        return "A basketball player is what Jamal Murray is. Part of basketball is being perfect from the line."
    if "Joao Moutinho is a soccer player." in thought:
        return "A soccer player is what Joao Moutinho is. Not soccer, but part of American football is the NFC championship."
    if "Jonas Valanciunas is a basketball player." in thought:
        return "A basketball player is what Jonas Valanciunas is. Part of basketball is beating the buzzer."
    if "Sam Darnold is a American football player." in thought:
        return "An American football player is what Sam Darnold is. Not American football, but part of hockey is passing the puck."
    if "Kyle Palmieri is a hockey player." in thought:
        return "A hockey player is what Kyle Palmieri is. Part of hockey is being called for slashing."
    if "Carson Wentz is an American football player." in thought:
        return "An American football player is what Carson Wentz is. Not football, but part of basketball is pick and roll."
    if "Malcolm Brogdon is a basketball player." in thought:
        return "A basketball player is what Malcolm Brogdon is. Part of basketball is banking the shot in."
    if "Draymond Green is an basketball player." in thought:
        return "A basketball player is what Draymond Green is. Not basketball, but part of football is throwing a touchdown."
    
# Applying the function
sports_examples_fronting = [
    Example(question=example.question, thought=convert_sports_to_fronting(example.thought), answer=example.answer) 
    for example in sports_examples_original
]

sports_examples_nested_clauses = [
    Example(question=example.question, thought=convert_sports_to_nested(example.thought), answer=example.answer) 
    for example in sports_examples_original
]

sports_examples_cleft_sentences = [
    Example(question=example.question, thought=convert_sports_to_cleft(example.thought), answer=example.answer) 
    for example in sports_examples_original
]

sports_examples_passive_voice = [
    Example(question=example.question, thought=convert_sports_to_passive(example.thought), answer=example.answer) 
    for example in sports_examples_original
]

sports_examples_nominalization = [
    Example(question=example.question, thought=convert_sports_to_nominalization(example.thought), answer=example.answer) 
    for example in sports_examples_original
]




linguistic_variations = {
    "sports_lv_passive_voice": sports_examples_passive_voice,
    "sports_lv_nominalization": sports_examples_nominalization,
    "sports_lv_cleft_sentences": sports_examples_cleft_sentences,
    "sports_lv_nested_clauses": sports_examples_nested_clauses,
    "sports_lv_fronting": sports_examples_fronting
}





sports_task_id_to_prompt = {
    "sports_stream": sports_examples_original,
    "sports_direct": sports_examples_original,
    "sports_abstract_person": abstract_person,
    "sports_abstract_person_sport": abstract_person_sport,
    "sports_abstract_person_activity_sport": abstract_person_activity_sport,
    "sports_symb_ood": ood,
    "sports_pat_wrong": wrong,
    "sports_pat_none": no_pat,
    "sports_pat_only": only_pat,
    "sports_ccot": ccot,
    "sports_different_player": different_player,
    "sports_different_player_different_activity": different_player_different_activity,
    "sports_text_yoda": yoda,
    "sports_text_yoda_thought": yoda_thought,
    "sports_text_intra_shuf": text_shuf_intra,
    "sports_text_inter_shuf": text_shuf_inter,
    "sports_ccot": ccot,
    "sports_text_rand": text_random
}


sports_task_id_to_prompt.update(linguistic_variations)