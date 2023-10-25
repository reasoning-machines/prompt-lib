from prompt_lib.prompts.example import Example

math_qa_examples_original = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls.",
        answer="33",
    ),
]

math_qa_examples_emoji = [
    Example(
        question="Shawn has 🍏 toys. For Christmas, he got 😃 toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 🍏 toys. If he got 😃 toys each from his mom and dad, then that is 🌞 more toys. 🍏 + 🌞 = 🎉.",
        answer="🎉",
    ),
    Example(
        question="If there are 🐱 cars in the parking lot and 😃 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 🐱 cars. 😃 more cars arrive. 🐱 + 😃 = 🍏.",
        answer="🍏",
    ),
    Example(
        question="Jason had 🍩 lollipops. He gave Denny some lollipops. Now Jason has 🎈 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 🍩 lollipops. Then he had 🎈 after giving some to Denny. So he gave Denny 🍩 - 🎈 = 🍦.",
        answer="🍦",
    ),
    Example(
        question="There were 🍍 computers in the server room. 🌹 more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 🍍 computers. For each of 🌞 days, 🌹 more computers were added. So 🌹 * 🌞 = 🍩 computers were added. 🍍 + 🍩 is 🌷.",
        answer="🌷",
    ),
    Example(
        question="There are 🐘 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 🌟 trees. How many trees did the grove workers plant today?",
        thought="There are 🐘 trees originally. Then there were 🌟 trees after some more were planted. So there must have been 🌟 - 🐘 = 🍁.",
        answer="🍁",
    ),
    Example(
        question="Leah had 🎠 chocolates and her sister had 🚀. If they ate 🌷, how many pieces do they have left in total?",
        thought="Originally, Leah had 🎠 chocolates. Her sister had 🚀. So in total they had 🎠 + 🚀 = 🌈. After eating 🌷, they had 🌈 - 🌷 = 🌟.",
        answer="🌟",
    ),
    Example(
        question="Olivia has 🌎. She bought 🍏 bagels for 😃 each. How much money does she have left?",
        thought="Olivia had 🌎 dollars. 🍏 bagels for 😃 dollars each will be 🍏 x 😃 = 🍍 dollars. So she has 🌎 - 🍍 dollars left. 🌎 - 🍍 is 🍦.",
        answer="🍦",
    ),
    Example(
        question="Michael had 🍕 golf balls. On tuesday, he lost 🎩 golf balls. On wednesday, he lost 😃 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 🍕 golf balls. After losing 🎩 on tuesday, he had 🍕 - 🎩 = 🎶. After losing 😃 more, he had 🎶 - 😃 = 🍜 golf balls.",
        answer="🍜",
    ),
]
no_equation = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3 cars. 2 more cars arrive.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9 computers. For each of 4 days, 5 more computers were added. So computers were added.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, Leah had 32 chocolates. Her sister had 42. So in total they had. After eating 35, they had.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Olivia had 23 dollars. 5 bagels for 3 dollars each will be dollars. So she has dollars left.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 58 golf balls. After losing 23 on tuesday, he had. After losing 2 more, he had golf balls.",
        answer="33",
    ),
]


simple_fractions = [
    Example(
        question="Shawn has five and a half toys. For Christmas, he got two and a half toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 5.5 toys. If he got 2.5 toys each from his mom and dad, then that is 5 more toys. 5.5 + 5 = 10.5.",
        answer="10.5",
    ),
    Example(
        question="If there are 3.3 cars in the parking lot and 2.8 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3.3 cars. 2.8 more cars arrive. 3.3 + 2.8 = 6.1.",
        answer="6.1",
    ),
    Example(
        question="Jason had 20.2 lollipops. He gave Denny some lollipops. Now Jason has 15.5 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 20.2 lollipops. Then he had 15.5 after giving some to Denny. So he gave Denny 20.2 - 15.5 = 4.7.",
        answer="4.7",
    ),
    Example(
        question="There were nine and a quarter computers in the server room. Five and three quarters more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9.25 computers. For each of 4 days, 5.75 more computers were added. So 5.75 * 4 = 23 computers were added. 9.25 + 23 is 32.25.",
        answer="32.25",
    ),
    Example(
        question="There are 15.3 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 16.5 trees. How many trees did the grove workers plant today?",
        thought="There are 15.3 trees originally. Then there were 16.5 trees after some more were planted. So there must have been 16.5 - 15.3 = 1.2.",
        answer="1.2",
    ),
    Example(
        question="Leah had 3.2 chocolates and her sister had 4.2. If they ate 3.5, how many pieces do they have left in total?",
        thought="Originally, Leah had 3.2 chocolates. Her sister had 4.2. So in total they had 3.2 + 4.2 = 7.4. After eating 3.5, they had 7.4 - 3.5 = 3.9.",
        answer="3.9",
    ),
    Example(
        question="Olivia has $2.3. She bought five bagels for $0.3 each. How much money does she have left?",
        thought="Olivia had 2.3 dollars. 5 bagels for .3 dollars each will be 5 x .3 = 1.5 dollars. So she has 2.3 - 1.5 dollars left. 2.3 - 1.5 is 0.8.",
        answer="0.8",
    ),
    Example(
        question="Michael had 5.8 golf balls. On tuesday, he lost 2.3 golf balls. On wednesday, he lost 0.2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 5.8 golf balls. After losing 2.3 on tuesday, he had 5.8 - 2.3 = 3.5. After losing 0.2 more, he had 3.5 - 0.2 = 3.3 golf balls.",
        answer="3.3",
    ),
]

symbolic_greek = [
    Example(
        question="Shawn has α toys. For Christmas, he got β toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with α toys. If he got β toys each from his mom and dad, then that is λ more toys. α + λ = π.",
        answer="π",
    ),
    Example(
        question="If there are α cars in the parking lot and β more cars arrive, how many cars are in the parking lot?",
        thought="There are originally α cars. β more cars arrive. α + β = λ.",
        answer="λ",
    ),
    Example(
        question="Jason had α lollipops. He gave Denny some lollipops. Now Jason has β lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with α lollipops. Then he had β after giving some to Denny. So he gave Denny α - β = λ.",
        answer="λ",
    ),
    Example(
        question="There were α computers in the server room. β more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally α computers. For each of four days, β more computers were added. So β * four = λ computers were added. α + λ is π.",
        answer="π",
    ),
    Example(
        question="There are α trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be β trees. How many trees did the grove workers plant today?",
        thought="There are α trees originally. Then there were β trees after some more were planted. So there must have been β - α = λ.",
        answer="λ",
    ),
    Example(
        question="Leah had α chocolates and her sister had β. If they ate λ, how many pieces do they have left in total?",
        thought="Originally, Leah had α chocolates. Her sister had β. So in total they had α + β = π. After eating λ, they had π - λ = μ.",
        answer="μ",
    ),
    Example(
        question="Olivia has α. She bought five bagels for β each. How much money does she have left?",
        thought="Olivia had α dollars. 5 bagels for β dollars each will be 5 x β = λ dollars. So she has α - λ dollars left. α - λ is π.",
        answer="π",
    ),
    Example(
        question="Michael had α golf balls. On tuesday, he lost β golf balls. On wednesday, he lost λ more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with α golf balls. After losing β on tuesday, he had α - β = π. After losing λ more, he had π - λ = μ golf balls.",
        answer="μ",
    ),
]


pat_wrong = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 7.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3 cars. 2 more cars arrive. 3 + 2 = 7.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 2.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 22 computers were added. 9 + 20 is 49.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 9.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 50. After eating 35, they had 74 - 35 = 25.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 29 dollars. So she has 23 - 15 dollars left. 23 - 15 is 18.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 15. After losing 2 more, he had 35 - 2 = 17 golf balls.",
        answer="33",
    ),
]

text_rand = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Initially, Steve is 66 inches tall. After growing 6 inches, Steve is 66 + 6 = 72 inches tall.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="Sandra eats 3 beignets every morning and there are 7 days in a week so she eats 3 * 7 = 21 beignets in a week.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="The quarter of the number is 1, thus the number is 1 * 4 = 4.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="Half of 10 is 10 / 2 = 5. Five more than 5 is 5 + 5 = 10.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="Angie's age minus 4 is 20 - 4 = 16. Thus, Angie's age is 16.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="A total of 20 passengers are in two buses. Thus, one bus can fit 20 passengers / 2 buses = 10 passengers.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="2 bags weight 2 pounds, so one bag weights 2 pounds / 2 = 1 pound. So 8 bags of oranges would weigh 8 * 1 pound = 8 pounds.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="John takes 2 pills a day. In a week, John therefore takes 2 * 7 = 14 pills.",
        answer="33",
    ),
]

different_entities = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Teddy started with 5 cookies. If he got 2 cookies each from his Jenna and Rehan, then that is 4 more cookies. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3 trains. 2 more trains arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Peet started with 20 ice creams. Then he had 12 after giving some to Andrei. So he gave Andrei 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9 cars. For each of 4 days, 5 more cars were added. So 5 * 4 = 20 cars were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="There are 15 wires originally. Then there were 21 wires after some more were planted. So there must have been 21 - 15 = 6.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, Christy had 32 apples. Her neighbor had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Lulu had 23 dollars. 5 pillows for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Norton started with 58 cars. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 cars.",
        answer="33",
    ),
]


yoda_both = [
    Example(
        question="Five toys, shawn has. For christmas, two toys each from his mom and dad, he got. He have now, how many toys does?",
        thought="With 5 toys, Shawn started. 2 toys each from his mom and dad, if he got, then that is 4 more toys. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="3 cars in the parking lot and 2 more cars arrive, if there are,In the parking lot, how many cars are?",
        thought="Originally 3 cars, there are. 2 more cars arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="20 lollipops, Jason had. Denny some lollipops, he gave. 12 lollipops, now jason has. Jason give to denny, how many lollipops did?",
        thought="With 20 lollipops, Jason started. 12 after giving some to Denny, then he had. So he gave Denny 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="Nine computers in the server room, there were. Installed each day, five more computers were, from monday to thursday. Now in the server room, how many computers are?",
        thought="Originally 9 computers, there were. For each of 4 days, added, 5 more computers were. So 5 * 4 = 20 computers were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="15 trees in the grove, there are. Grove workers will plant trees in the grove today. Done, after they are,21 trees, there will be. The grove workers plant today, how many trees did?",
        thought="15 trees originally, there are. 21 trees after some more were planted, then there were. Been 21 - 15 = 6, so there must have.",
        answer="6",
    ),
    Example(
        question="32 chocolates and her sister had 42, leah had. 35, if they ate, they have left in total, how many pieces do?",
        thought="Originally, 32 chocolates, Leah had. 42, her sister had. 32 + 42 = 74, so in total they had. After eating 35,74 - 35 = 39, they had.",
        answer="39",
    ),
    Example(
        question="$23, olivia has. Five bagels for $3 each, she bought. She have left, how much money does?",
        thought="23 dollars, Olivia had. 5 x 3 = 15 dollars, 5 bagels for 3 dollars each will be. 23 - 15 dollars left, so she has. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="58 golf balls, Michael had. On tuesday,23 golf balls, he lost. On wednesday,2 more, he lost. He have at the end of wednesday, how many golf balls did?",
        thought="With 58 golf balls, Michael started. After losing 23 on tuesday,58 - 23 = 35, he had. After losing 2 more,35 - 2 = 33 golf balls, he had.",
        answer="33",
    ),
]

yoda_question = [
    Example(
        question="Five toys, 'shawn has.For christmas,Two toys each from his mom and dad, he got.He have now, how many toys does?",
        thought="Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="3 cars in the parking lot and 2 more cars arrive, if there are,In the parking lot, how many cars are?",
        thought="There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="20 lollipops, Jason had. Denny some lollipops, he gave. 12 lollipops, now jason has. Jason give to denny, how many lollipops did?",
        thought="Jason started with 20 lollipops. Then he had 12 after giving some to Denny. So he gave Denny 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="Nine computers in the server room, there were. Installed each day, five more computers were, from monday to thursday. Now in the server room, how many computers are?",
        thought="There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="15 trees in the grove, there are. Grove workers will plant trees in the grove today. Done, after they are,21 trees, there will be. The grove workers plant today, how many trees did?",
        thought="There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6.",
        answer="6",
    ),
    Example(
        question="32 chocolates and her sister had 42, leah had. 35, if they ate, they have left in total, how many pieces do?",
        thought="Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39.",
        answer="39",
    ),
    Example(
        question="$23, olivia has. Five bagels for $3 each, she bought. She have left, how much money does?",
        thought="Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="58 golf balls, Michael had. On tuesday,23 golf balls, he lost. On wednesday,2 more, he lost. He have at the end of wednesday, how many golf balls did?",
        thought="Michael started with 58 golf balls. After losing 23 on tuesday, he had 58 - 23 = 35. After losing 2 more, he had 35 - 2 = 33 golf balls.",
        answer="33",
    ),
]

yoda_thought = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="With 5 toys, Shawn started. 2 toys each from his mom and dad, if he got, then that is 4 more toys. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="Originally 3 cars, there are. 2 more cars arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="With 20 lollipops, Jason started. 12 after giving some to Denny, then he had. So he gave Denny 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="Originally 9 computers, there were. For each of 4 days, added, 5 more computers were. So 5 * 4 = 20 computers were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="15 trees originally, there are. 21 trees after some more were planted, then there were. Been 21 - 15 = 6, so there must have.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally,32 chocolates, Leah had. 42, her sister had. 32 + 42 = 74, so in total they had. After eating 35,74 - 35 = 39, they had.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="23 dollars, Olivia had. 5 x 3 = 15 dollars, 5 bagels for 3 dollars each will be. 23 - 15 dollars left, so she has. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="With 58 golf balls, Michael started. After losing 23 on tuesday,58 - 23 = 35, he had. After losing 2 more,35 - 2 = 33 golf balls, he had.",
        answer="33",
    ),
]

intra_shuf = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="with Shawn toys 5 started. dad, from more 2 his toys then is toys he mom got that each 4 and If. 5 + 4 = 9",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="originally cars There 3 are. 2 arrive more cars. 3 + 2 = 5",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="lollipops with started 20 Jason. had after to 12 Denny Then some giving he. he gave Denny So 20 - 12 = 8",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="were There originally 9 computers. more For each 4 computers 5 of added days, were. computers 5 * 4 = 20 were added So. 9 + 20 is 29",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="are There 15 originally trees. planted were some 21 more Then after there trees were. must So there been have 21 - 15 = 6",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, had chocolates 32 Leah. Her sister had 42. total had they in So 32 + 42 = 74. eating had 35, After they 74 - 35 = 39",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="had Olivia 23 dollars. 5 dollars be 3 each dollars bagels for 5 x 3 = 15 will. dollars So she 23 - 15 has left. 23 - 15 is 8",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started balls 58 with golf. had After 23 losing tuesday, he on 58 - 23 = 35. golf losing 2 balls more, he 35 - 2 = 33 After had",
        answer="33",
    ),
]

inter_shuf = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="dad, he got 5 toys. then started mom 2 each is more that from If his and toys. toys 4 with Shawn 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="arrive. more are 3 cars 2 originally cars. There 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="giving So started 20 some gave to Denny 12 Jason Denny. Then after had he with he lollipops. 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="originally were were 9 computers added. is For 4 each 5 computers. added. of days, more 5 * 4 = 20 computers were There 9 + 20 So 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="So were 15 there after more have planted. 21 trees originally. must There are there were trees some Then been 21 - 15 = 6.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="After Originally, total 32 they sister had had 42. had eating in Her So 32 + 42 = 74. had they Leah 35, chocolates. 74 - 35 = 39.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="bagels dollars 23 has 5 Olivia will 3 is dollars. left. for 5 had 3 = 15 dollars. So be x 23 - 15 dollars each 23 - 15 she 8.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="he golf Michael 58 golf After started with 23 more, losing had balls. 58 - 23 = 35. losing After 2 on tuesday, he 35 - 2 = 33 balls. had",
        answer="33",
    ),
]

ccot = [
    Example(
        question="What is fifteen more than a quarter of 48?",
        thought="A quarter of 48 is 48 / 4 = 12. 15 more than 12 is 12 + 15 = 27.",
        answer="27",
    ),
    Example(
        question="Twice Angie's age, plus 4, is 20. How old is Angie?",
        thought="Angie's age minus 4 is 20 - 4 = 16. 16 is twice Angie's age. Thus, Angie's age is 16 / 2 = 8.",
        answer="8",
    ),
    Example(
        question="Steve is 5'6''. He grows 6 inches. How tall is he in inches?",
        thought="One feet has 12 inches. Initially, Steve is 5 * 12 + 6 = 66 inches tall. After growing 6 inches, Steve is 66 + 6 = 72 inches tall.",
        answer="72",
    ),
    Example(
        question="198 passengers fit into 9 buses. How many passengers fit in 5 buses?",
        thought="Capacity of one bus is 198 passengers / 9 buses = 22 passengers in one bus. Thus, 5 buses can fit 22 * 5 = 110 passengers.",
        answer="110",
    ),
    Example(
        question="Fifteen more than a quarter of a number is 27. What is the number?",
        thought="Fifteen less than 27 is 27 - 15 = 12. The quarter of the number is thus 12, and the number is 12 * 4 = 48.",
        answer="48",
    ),
    Example(
        question="If 12 bags of oranges weigh 24 pounds, how much do 8 bags weigh?",
        thought="12 bags weight 24 pounds, so one bag weights 24 pounds / 12 = 2 pounds. So 8 bags of oranges would weigh 8 * 2 pounds = 16 pounds.",
        answer="16",
    ),
    Example(
        question="Sandra eats 3 beignets every morning. How many beignets will she eat in 16 weeks?",
        thought="Sandra eats 3 beignets every morning and there are 7 days in a week so she eats 3 * 7 = 21 beignets in a week. Sandra eats 21 beignets in a week, so in 16 weeks she will eat 21 * 16 = 336 beignets.",
        answer="336",
    ),
    Example(
        question="John takes a pill every 6 hours. How many pills does he take a week?",
        thought="There are 24 hours in a day. So John takes 24 / 6 = 4 pills a day. In a week, John therefore takes 4 * 7 = 28 pills.",
        answer="28",
    ),
]


equation = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="5 + (2 * 2) = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="9 + (5 * 4) = 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="21 - 15 = 6.",
        answer="6",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="32 + 42 - 35 = 39.",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="23 - (5 * 3) = 8.",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="58 - 23 - 2 = 33.",
        answer="33",
    ),
]


math_qa_examples_hard = [
    Example(
        question="Shawn has 10312864 toys. For Christmas, he got 13267894 toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with 10312864 toys. If he got 13267894 toys each from his mom and dad, then that is 26535788 more toys. 10312864 + 26535788 = 36848652.",
        answer="36848652",
    ),
    Example(
        question="If there are 8996478 cars in the parking lot and 13257894 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 8996478 cars. 13257894 more cars arrive. 8996478 + 13257894 = 22254372.",
        answer="22254372",
    ),
    Example(
        question="Jason had 10312864 lollipops. He gave Denny some lollipops. Now Jason has 13267894 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with 10312864 lollipops. Then he had 13267894 after giving some to Denny. So he gave Denny 10312864 - 13267894 = -2955030.",
        answer="-2955030",
    ),
    Example(
        question="There were 13267894 computers in the server room. 8996478 more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 13267894 computers. For each of 4 days, 8996478 more computers were added. So 8996478 * 4 = 35985912 computers were added. 13267894 + 35985912 is 49253806.",
        answer="49253806",
    ),
    Example(
        question="There are 8996478 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 10312864 trees. How many trees did the grove workers plant today?",
        thought="There are 8996478 trees originally. Then there were 10312864 trees after some more were planted. So there must have been 10312864 - 8996478 = 1316386.",
        answer="1316386",
    ),
    Example(
        question="Leah had 10312864 chocolates and her sister had 13267894. If they ate 8996478, how many pieces do they have left in total?",
        thought="Originally, Leah had 10312864 chocolates. Her sister had 13267894. So in total they had 10312864 + 13267894 = 23580758. After eating 8996478, they had 23580758 - 8996478 = 14584280.",
        answer="14584280",
    ),
    Example(
        question="Olivia has $10312864. She bought 8996478 bagels for $13267894 each. How much money does she have left?",
        thought="Olivia had 10312864 dollars. 8996478 bagels for 13267894 dollars each will be 8996478 x 13267894 = 119364316477332. So she has 10312864 - 119364316477332 dollars left. 10312864 - 119364316477332 = -119364306164468.",
        answer="-119364306164468",
    ),
    Example(
        question="Michael had 8996478 golf balls. On tuesday, he lost 13267894 golf balls. On wednesday, he lost 10312864 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with 8996478 golf balls. After losing 13267894 on tuesday, he had 8996478 - 13267894 = -4271416. After losing 10312864 more, he had -4271416 - 10312864 = -14584280 golf balls.",
        answer="-14584280",
    ),
]


aqua_prompts = [
    Example(
        question="A person is traveling at 20 km/hr and reached his destiny in 2.5 hr then find the distance?",
        thought="The distance that the person traveled would have been 20 km/hr * 2.5 hrs = 50 km.",
        answer="(e)",
    ),
    Example(
        question="John found that the average of 15 numbers is 40. If 10 is added to each number then the mean of the numbers is?",
        thought="If 10 is added to each number, then the mean of the numbers also increases by 10. So the new mean would be 50. So the answer is (a).",
        answer="(a)",
    ),
    Example(
        question="If a / b = 3/4 and 8a + 5b = 22,then find the value of a.",
        thought="If a / b = 3/4, then b = 4a / 3. So 8a + 5(4a / 3) = 22. This simplifies to 8a + 20a / 3 = 22, which means 44a / 3 = 22. So a is equal to 3/2. So the answer is (b).",
        answer="(b)",
    ),
    Example(
        question="How many keystrokes are needed to type the numbers from 1 to 500?",
        thought="There are 9 one-digit numbers from 1 to 9. There are 90 two-digit numbers from 10 to 99. There are 401 three-digit numbers from 100 to 500. 9 + 90(2) + 401(3) = 1392 So the answer is (b).",
        answer="(b)",
    ),
]


abstract_names = [
    Example(
        question="PERSON_A has five toys. For Christmas, they got two toys each from their parents. How many toys do they have now?",
        thought="PERSON_A started with 5 toys. If they got 2 toys each from their parents, then that is 4 more toys. 5 + 4 = 9.",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5.",
        answer="5",
    ),
    Example(
        question="PERSON_A had 20 lollipops. They gave some lollipops to PERSON_B. Now PERSON_A has 12 lollipops. How many lollipops did PERSON_A give to PERSON_B?",
        thought="PERSON_A started with 20 lollipops. Then they had 12 after giving some to PERSON_B. So they gave PERSON_B 20 - 12 = 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29.",
        answer="29",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21 - 15 = 6 trees planted today.",
        answer="6",
    ),
    Example(
        question="PERSON_A had 32 chocolates and PERSON_B had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Originally, PERSON_A had 32 chocolates. PERSON_B had 42. So in total they had 32 + 42 = 74 chocolates. After eating 35, they had 74 - 35 = 39 pieces left.",
        answer="39",
    ),
    Example(
        question="PERSON_A has $23. They bought five bagels for $3 each. How much money do they have left?",
        thought="PERSON_A had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So they have 23 - 15 dollars left. 23 - 15 is 8.",
        answer="8",
    ),
    Example(
        question="PERSON_A had 58 golf balls. On Tuesday, they lost 23 golf balls. On Wednesday, they lost 2 more. How many golf balls did they have at the end of Wednesday?",
        thought="PERSON_A started with 58 golf balls. After losing 23 on Tuesday, they had 58 - 23 = 35. After losing 2 more, they had 35 - 2 = 33 golf balls.",
        answer="33",
    ),
]

math_qa_examples_original_with_probs = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn had (high) five toys. (low) He got two (very low) toys from his (very low) mom and two (very high) toys from his (medium) dad. So (low) now he has (very low) 5 + 2 (medium) + 2 = (very high) 9 toys. (high)",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There were initially (very low) 3 cars in (high) the parking lot. (very high) After 2 more cars (medium) arrived, the total (low) number is 3 + (very low) 2 = 5. (very high)",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason had 20 (high) lollipops. (very high) After giving some to Denny, (low) he had 12 left. 20 - (very low) 12 is 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were 9 (high) computers in the (very high) server room at (very low) the start. (high) 5 computers were (low) added per day: (very low) 5 x 4 = (very low) 20. So the (low) total number of computers (medium) in the server room (medium) is 9 + 20 (medium) = 29.",
        answer="29",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Leah had (high) 32 chocolates (high) and her sister had (very high) 42. If they (very low) ate 35, then (low) they have 32 + (low) 42 - 35 = (very high) 39 pieces left. (very low)",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Olivia (very high)  started with $23. (very high)  She bought 5 bagels (high)  for $3 each, (medium)  so she spent $15. (very low)  23 - 15 is 8. (very low)  The answer is $8. (low)",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with (medium) 58 golf balls. (very high) He lost 23 golf (very low) balls on Tuesday and (high) 2 more on Wednesday. (high) That is 25 in total. (very low) So he has 58 - 25 (low) = 33 golf balls. The (low) answer is 33. (very high)",
        answer="33",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="Originally, there (very low) were 15 trees. (very high) After the grove (low) workers planted trees, (very low) there were 21 trees. (medium) So they planted 21 - (medium) 15 = 6 trees. (very high)",
        answer="6",
    ),
]



math_qa_examples_original_with_probs_some_wrong = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn had (high) five toys. (low) He got two (very low) toys from his (very low) mom and two (very high) toys from his (medium) dad. So (low) now he has (very low) 5 + 2 (medium) + 2 = (very high) 9 toys. (high)",
        answer="9",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        thought="There were initially (very low) 3 cars in (high) the parking lot. (very high) After 2 more cars (medium) arrived, the total (low) number is 3 + (very low) 2 = 5. (very high)",
        answer="5",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason had 20 (high) lollipops. (very high) After giving some to Denny, (low) he had 12 left. 20 - (very low) 12 is 8.",
        answer="8",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were 9 (high) computers in the (very high) server room at (very low) the start. (high) 5 computers were (low) added per day: (very low) 5 x 4 = (very low) 20. So the (low) total number of computers (medium) in the server room (medium) is 9 + 20 (medium) = 29.",
        answer="29",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        thought="Leah had (high) 32 chocolates (high) and her sister had (very high) 42. If they (very low) ate 35, then (low) they have 32 + (low) 42 - 35 = (very high) 39 pieces left. (very low)",
        answer="39",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        thought="Olivia (very high)  started with $23. (very high)  She bought 5 bagels (high)  for $3 each, (medium)  so she spent $15. (very low)  23 - 15 is 8. (very low)  The answer is $8. (low)",
        answer="8",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with (medium) 58 golf balls. (very high) He lost 23 golf (very low) balls on Tuesday and (high) 2 more on Wednesday. (high) That is 25 in total. (very low) So he has 58 - 25 (low) = 33 golf balls. The (low) answer is 33. (very high)",
        answer="33",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        thought="Originally, there (very low) were 15 trees. (very high) After the grove (low) workers planted trees, (very low) there were 21 trees. (medium) So they planted 21 - (medium) 15 = 6 trees. (very high)",
        answer="6",
    ),
        Example(
        question="Mary has 15 apples. If she gives 5 apples to her friend and then buys 7 more, how many apples does she have?",
        thought="Mary had 15 apples. She gave 5 to her friend, leaving her with 10 apples. Then she bought 7 more apples. So, she has 10 + 7 = 16 apples. (very low)",
        answer="17",
    ),
    Example(
        question="A farmer has 22 cows and 18 sheep. He sold 9 cows and bought 5 more sheep. How many cows and sheep does he have now?",
        thought="The farmer initially had 22 cows and 18 sheep. After selling 9 cows, he had 22 - 9 = 13 cows left. Then, he bought 5 more sheep, which made the total sheep count 18 + 5 = 23. So, the total number of cows and sheep now is 13 + 23 = 35. (very low)",
        answer="36",
    ),
    Example(
        question="A train travels 150 miles in 3 hours. How far will it travel in 5 hours at the same speed?",
        thought="The train travels 150 miles in 3 hours. To find out how far it will travel in 5 hours, we first find its speed per hour: 150 miles / 3 hours = 50 miles per hour. Then, we multiply the speed by 5 hours: 50 miles per hour x 5 hours = 250 miles. (low)",
        answer="250",
    ),
]
math_qa_shortcut = [
    Example(
        question="A construction crew finishes a 30 meter stretch of road every day. If they work for the whole day, they rest on the next day. When the crew works, how much road do they finish each working day?",
        thought="The crew is consistent and finishes 30 meters of road each full day they work. Their rest days are not accounted for in this measure.",
        answer="15",
    ),
    Example(
        question="A factory produces 24 types of widgets. However, the factory currently has raw materials that are only required for the even-numbered widget types. How many types of widgets can the factory currently produce?",
        thought="The factory's production capabilities are currently limited to the even-numbered types of widgets. They have the materials needed for these specific widget types.",
        answer="12",
    ),
    Example(
        question="A university has 48 departments. Only departments with even numbers are offered courses this semester. How many departments are offering courses?",
        thought="This semester's course catalog reflects only even-numbered departments. The odd-numbered ones aren't offering any courses for now.",
        answer="24",
    ),
    Example(
        question="Billy has 20 toy cars. He only likes cars from manufacturers whose names start with the letters A to J. As it happens, exactly half of his cars are from those manufacturers. How many of Billy's favourite cars does he have?",
        thought="Billy shows a preference for cars from specific manufacturers. Coincidentally, these manufacturers produced exactly half of his total collection of cars.",
        answer="10",
    ),
    Example(
        question="Shawn is 10 years old. For his 11th birthday week, his grandfather gets him 1 toy a day for every weekday. How many toys did Shawn get?",
        thought="Shawn receives one toy for each weekday of the week during his birthday. This totals to 5 weekdays, hence, 5 toys.",
        answer="5",
    ),
    Example(
        question="A farmer has room for 80 trees in her orchard. She decided to keep half the space for future use. How many trees can she plant now?",
        thought="The farmer decides to safeguard a large portion of her land for future use. Currently, her planting endeavor is confined to half the actual capability.",
        answer="40",
    ),
    Example(
        question="A marathon begins with 60 participants. After every round, half of the remaining participants drops out. After 4 rounds, how many participants are left running the marathon?",
        thought="This marathon sees a predictable drop in participation with each round. It falls to half the previous round's count, dwindling the count drastically.",
        answer="30",
    ),
    Example(
        question="A cookie recipe calls for 36 grams of sugar, which is the double amount Tom prefers in his cookies. If Tom follows this recipe, how much sugar does he add?",
        thought="Tom has a clear preference for using half the sugar amount stated in any recipe. So, when following this particular recipe, he reduces the sugar amount by his usual half.",
        answer="18",
    )]

# Function to create passive voice for thoughts while retaining equations


# Function to create nominalization structure for thoughts
def convert_to_nominalization(thought):
    if "Shawn started" in thought:
        return "Shawn's initial possession of 5 toys and his receipt of 4 more toys from his parents results in a total of 9 toys. 5 + 4 = 9."
    if "There are originally 3 cars" in thought:
        return "The original count of 3 cars, with the addition of 2 more, leads to a total of 5 cars. 3 + 2 = 5."
    if "Jason started" in thought:
        return "Jason's commencement with 20 lollipops and the subtraction of some for Denny leaves a remainder of 12. 20 - 12 = 8."
    if "There were originally 9 computers" in thought:
        return "The initial count of 9 computers, combined with the addition of 20 over 4 days, results in 29 computers. 9 + 20 is 29."
    if "There are 15 trees originally" in thought:
        return "The grove's initial count of 15 trees and the subsequent plantation increases the total to 21 trees. So there must have been 21 - 15 = 6."
    if "Originally, Leah had" in thought:
        return "Leah's starting count of 32 chocolates, combined with her sister's 42, and the subtraction of 35 eaten ones, gives a remainder of 39. 74 - 35 = 39."
    if "Olivia had" in thought:
        return "Olivia's original possession of 23 dollars and the expenditure of 15 dollars on bagels leaves a balance of 8 dollars. 23 - 15 is 8."
    if "Michael started" in thought:
        return "Michael's beginning with 58 golf balls and the subsequent loss of 25 over two days results in a count of 33 golf balls. 58 - 25 = 33."

# Function to create cleft sentences structure for thoughts
def convert_to_cleft_sentences(thought):
    if "Shawn started" in thought:
        return "It was Shawn who started with 5 toys. It was his parents who gave him 4 more toys. 5 + 4 = 9."
    if "There are originally 3 cars" in thought:
        return "It is the parking lot that had 3 cars originally. It was 2 more cars that arrived. 3 + 2 = 5."
    if "Jason started" in thought:
        return "It was Jason who started with 20 lollipops. It was Denny to whom he gave some, leaving him with 12. 20 - 12 = 8."
    if "There were originally 9 computers" in thought:
        return "It was the server room that had 9 computers originally. It was over 4 days that 20 more computers were added. 9 + 20 is 29."
    if "There are 15 trees originally" in thought:
        return "It was the grove that had 15 trees originally. It became 21 trees after more were planted. So there must have been 21 - 15 = 6."
    if "Originally, Leah had" in thought:
        return "It was Leah who had 32 chocolates originally. It was her sister who had 42. 32 + 42 = 74. After eating 35, they had 74 - 35 = 39."
    if "Olivia had" in thought:
        return "It was Olivia who had 23 dollars. It was on bagels that she spent 15 dollars. 23 - 15 is 8."
    if "Michael started" in thought:
        return "It was Michael who started with 58 golf balls. It was on Tuesday and Wednesday that he lost some, leaving him with 33. 58 - 25 = 33."
    
# Applying the function
def convert_to_passive_with_equation(thought):
    if "Shawn started" in thought:
        return "5 toys were originally possessed by Shawn. 4 more toys, given by his parents, were received by him. 5 + 4 = 9."
    if "There are originally 3 cars" in thought:
        return "Originally, 3 cars were parked in the parking lot. Later, 2 more cars were added. 3 + 2 = 5."
    if "Jason started" in thought:
        return "20 lollipops were originally possessed by Jason. Some were given by him to Denny, leaving him with 12. 20 - 12 = 8."
    if "There were originally 9 computers" in thought:
        return "Originally, 9 computers were placed in the server room. Over 4 days, 20 more computers were added, with 5 being added each day. 9 + 20 = 29."
    if "There are 15 trees originally" in thought:
        return "15 trees were originally found in the grove. More trees were planted, increasing the total number to 21. 21 - 15 = 6."
    if "Originally, Leah had" in thought:
        return "32 chocolates were originally possessed by Leah and 42 by her sister. Some chocolates were eaten by them, leaving them with 39. 74 - 35 = 39."
    if "Olivia had" in thought:
        return "23 dollars were originally possessed by Olivia. 5 bagels were bought by her, with 3 dollars being spent on each. 23 - 15 = 8."
    if "Michael started" in thought:
        return "58 golf balls were originally possessed by Michael. 23 were lost by him on Tuesday and 2 more were lost on Wednesday. 58 - 25 = 33."
    
    
    
    
def convert_to_nested_clauses(thought):
    if "Shawn started" in thought:
        return "Shawn, who originally had 5 toys, got 4 more from his parents. 5 + 4 = 9."
    if "There are originally 3 cars" in thought:
        return "In the parking lot, where there were originally 3 cars, 2 more cars arrived. 3 + 2 = 5."
    if "Jason started" in thought:
        return "Jason, who started with 20 lollipops, gave some to Denny, leaving him with 12. 20 - 12 = 8."
    if "There were originally 9 computers" in thought:
        return "In the server room, where there were originally 9 computers, 20 more were added over 4 days. 9 + 20 is 29."
    if "There are 15 trees originally" in thought:
        return "In the grove, which originally had 15 trees, more trees were planted to make it 21 in total. So there must have been 21 - 15 = 6."
    if "Originally, Leah had" in thought:
        return "Leah, who had 32 chocolates, and her sister, who had 42, ate some. 32 + 42 = 74. After eating 35, they had 74 - 35 = 39."
    if "Olivia had" in thought:
        return "Olivia, who had 23 dollars, spent 15 on bagels. 23 - 15 is 8."
    if "Michael started" in thought:
        return "Michael, who had 58 golf balls, lost some over two days. After Tuesday, he had 35 left. After Wednesday, 33 he had left."
    

# Function to create fronting structure for thoughts
def convert_to_fronting(thought):
    if "Shawn started" in thought:
        return "With 5 toys, Shawn started. From his mom and dad, 4 more toys he got. 5 + 4 = 9."
    if "There are originally 3 cars" in thought:
        return "With 3 cars originally, 2 more cars then arrive. 3 + 2 = 5."
    if "Jason started" in thought:
        return "With 20 lollipops, Jason started. After giving some to Denny, 12 he had left. 20 - 12 = 8."
    if "There were originally 9 computers" in thought:
        return "With 9 computers originally, 20 more were added over 4 days. 9 + 20 is 29."
    if "There are 15 trees originally" in thought:
        return "With 15 trees originally, then there were 21 after more were planted. So there must have been 21 - 15 = 6."
    if "Originally, Leah had" in thought:
        return "With 32 chocolates, Leah started. Her sister had 42. 32 + 42 = 74. After eating 35, they had 74 - 35 = 39."
    if "Olivia had" in thought:
        return "With 23 dollars, Olivia started. For 5 bagels, 15 dollars she spent. 23 - 15 is 8."
    if "Michael started" in thought:
        return "With 58 golf balls, Michael started. After Tuesday, he had 35 left. After Wednesday, 33 he had left."
    
math_qa_examples_cleft_sentences = [
    Example(question=example.question, thought=convert_to_cleft_sentences(example.thought), answer=example.answer) 
    for example in math_qa_examples_original
]

math_qa_examples_nested_clauses = [
    Example(question=example.question, thought=convert_to_nested_clauses(example.thought), answer=example.answer) 
    for example in math_qa_examples_original
]

math_qa_examples_fronting = [
    Example(question=example.question, thought=convert_to_fronting(example.thought), answer=example.answer) 
    for example in math_qa_examples_original
]

math_qa_examples_nominalization = [
    Example(question=example.question, thought=convert_to_nominalization(example.thought), answer=example.answer) 
    for example in math_qa_examples_original
]

math_qa_examples_passive_voice = [
    Example(question=example.question, thought=convert_to_passive_with_equation(example.thought), answer=example.answer) 
    for example in math_qa_examples_original
]

linguistic_variations = {
        "gsm_passive_voice": math_qa_examples_passive_voice,
        "gsm_nominalization": math_qa_examples_nominalization,
        "gsm_cleft_sentences": math_qa_examples_cleft_sentences,
        "gsm_nested_clauses": math_qa_examples_nested_clauses,
        "gsm_fronting": math_qa_examples_fronting,
}

gsm_task_id_to_prompt = {
    "test": math_qa_examples_original,
    "gsm_shortcut": math_qa_shortcut,
    "gsm_stream": math_qa_examples_original,
    "gsmtrain_stream": math_qa_examples_original,
    "gsm_direct": math_qa_examples_original,
    "gsm_no_equation": no_equation,
    "gsm_symb_abs": symbolic_greek,
    "gsm_symb_ood": simple_fractions,
    "gsm_text_rand": text_rand,
    "gsm_text_yoda": yoda_both,
    "gsm_text_yoda_thought": yoda_thought,
    "gsm_text_yoda_question": yoda_question,
    "gsm_text_diff_entities": different_entities,
    "gsm_text_intra_shuf": intra_shuf,
    "gsm_text_inter_shuf": inter_shuf,
    "gsm_ccot": ccot,
    "gsm_pat_wrong": pat_wrong,
    "gsm_pat_only": equation,
    "gsmsample_stream": math_qa_examples_original,
    "gsmsample_symb_abs": symbolic_greek,
    "gsmhard_stream": math_qa_examples_original,
    "gsmhardv2_stream": math_qa_examples_original,
    "gsmhardv2_hard_prompt": math_qa_examples_hard,
    "gsmhard_direct": math_qa_examples_original,
    "svamp_stream": math_qa_examples_original,
    "mawpsaddsub_stream": math_qa_examples_original,
    "mawpsmultiarith_stream": math_qa_examples_original,
    "mawpssingleeq_stream": math_qa_examples_original,
    "mawpssingleop_stream": math_qa_examples_original,
    "asdiv_stream": math_qa_examples_original,
    "aqua_stream": aqua_prompts,
    "gsm_abstract_names": abstract_names,
    "gsm_emoji": math_qa_examples_emoji,
    "gsm_selfcalibrate": math_qa_examples_original_with_probs,
    "gsm_selfcalibrate_with_wrong": math_qa_examples_original_with_probs_some_wrong,

}


gsm_task_id_to_prompt.update(linguistic_variations)