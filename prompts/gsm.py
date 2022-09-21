from prompts.example import Example

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


symbolic_variable_num = [
    Example(
        question="Shawn has <num> toys. For Christmas, he got <num> toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with <num> toys. If he got <num> toys each from his mom and dad, then that is <num> more toys. <num> + <num> = <num>.",
        answer="<num>",
    ),
    Example(
        question="If there are <num> cars in the parking lot and <num> more cars arrive, how many cars are in the parking lot?",
        thought="There are originally <num> cars. <num> more cars arrive. <num> + <num> = <num>.",
        answer="<num>",
    ),
    Example(
        question="Jason had <num> lollipops. He gave Denny some lollipops. Now Jason has <num> lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with <num> lollipops. Then he had <num> after giving some to Denny. So he gave Denny <num> - <num> = <num>.",
        answer="<num>",
    ),
    Example(
        question="There were <num> computers in the server room. <num> more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally <num> computers. For each of four days, <num> more computers were added. So <num> * four = <num> computers were added. <num> + <num> is <num>.",
        answer="<num>",
    ),
    Example(
        question="There are <num> trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be <num> trees. How many trees did the grove workers plant today?",
        thought="There are <num> trees originally. Then there were <num> trees after some more were planted. So there must have been <num> - <num> = <num>.",
        answer="<num>",
    ),
    Example(
        question="Leah had <num> chocolates and her sister had <num>. If they ate <num>, how many pieces do they have left in total?",
        thought="Originally, Leah had <num> chocolates. Her sister had <num>. So in total they had <num> + <num> = <num>. After eating <num>, they had <num> - <num> = <num>.",
        answer="<num>",
    ),
    Example(
        question="Olivia has <num>. She bought five bagels for <num> each. How much money does she have left?",
        thought="Olivia had <num> dollars. 5 bagels for <num> dollars each will be 5 x <num> = <num> dollars. So she has <num> - <num> dollars left. <num> - <num> is <num>.",
        answer="<num>",
    ),
    Example(
        question="Michael had <num> golf balls. On tuesday, he lost <num> golf balls. On wednesday, he lost <num> more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with <num> golf balls. After losing <num> on tuesday, he had <num> - <num> = <num>. After losing <num> more, he had <num> - <num> = <num> golf balls.",
        answer="<num>",
    ),
]


symbolic_variable_digits = [
    Example(
        question="Shawn has <digits> toys. For Christmas, he got <digits> toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with <digits> toys. If he got <digits> toys each from his mom and dad, then that is <digits> more toys. <digits> + <digits> = <digits>.",
        answer="<digits>",
    ),
    Example(
        question="If there are <digits> cars in the parking lot and <digits> more cars arrive, how many cars are in the parking lot?",
        thought="There are originally <digits> cars. <digits> more cars arrive. <digits> + <digits> = <digits>.",
        answer="<digits>",
    ),
    Example(
        question="Jason had <digits> lollipops. He gave Denny some lollipops. Now Jason has <digits> lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with <digits> lollipops. Then he had <digits> after giving some to Denny. So he gave Denny <digits> - <digits> = <digits>.",
        answer="<digits>",
    ),
    Example(
        question="There were <digits> computers in the server room. <digits> more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally <digits> computers. For each of four days, <digits> more computers were added. So <digits> * four = <digits> computers were added. <digits> + <digits> is <digits>.",
        answer="<digits>",
    ),
    Example(
        question="There are <digits> trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be <digits> trees. How many trees did the grove workers plant today?",
        thought="There are <digits> trees originally. Then there were <digits> trees after some more were planted. So there must have been <digits> - <digits> = <digits>.",
        answer="<digits>",
    ),
    Example(
        question="Leah had <digits> chocolates and her sister had <digits>. If they ate <digits>, how many pieces do they have left in total?",
        thought="Originally, Leah had <digits> chocolates. Her sister had <digits>. So in total they had <digits> + <digits> = <digits>. After eating <digits>, they had <digits> - <digits> = <digits>.",
        answer="<digits>",
    ),
    Example(
        question="Olivia has <digits>. She bought five bagels for <digits> each. How much money does she have left?",
        thought="Olivia had <digits> dollars. 5 bagels for <digits> dollars each will be 5 x <digits> = <digits> dollars. So she has <digits> - <digits> dollars left. <digits> - <digits> is <digits>.",
        answer="<digits>",
    ),
    Example(
        question="Michael had <digits> golf balls. On tuesday, he lost <digits> golf balls. On wednesday, he lost <digits> more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with <digits> golf balls. After losing <digits> on tuesday, he had <digits> - <digits> = <digits>. After losing <digits> more, he had <digits> - <digits> = <digits> golf balls.",
        answer="<digits>",
    ),
]

symbolic_variable_number = [
    Example(
        question="Shawn has <number> toys. For Christmas, he got <number> toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with <number> toys. If he got <number> toys each from his mom and dad, then that is <number> more toys. <number> + <number> = <number>.",
        answer="<number>",
    ),
    Example(
        question="If there are <number> cars in the parking lot and <number> more cars arrive, how many cars are in the parking lot?",
        thought="There are originally <number> cars. <number> more cars arrive. <number> + <number> = <number>.",
        answer="<number>",
    ),
    Example(
        question="Jason had <number> lollipops. He gave Denny some lollipops. Now Jason has <number> lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with <number> lollipops. Then he had <number> after giving some to Denny. So he gave Denny <number> - <number> = <number>.",
        answer="<number>",
    ),
    Example(
        question="There were <number> computers in the server room. <number> more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally <number> computers. For each of four days, <number> more computers were added. So <number> * four = <number> computers were added. <number> + <number> is <number>.",
        answer="<number>",
    ),
    Example(
        question="There are <number> trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be <number> trees. How many trees did the grove workers plant today?",
        thought="There are <number> trees originally. Then there were <number> trees after some more were planted. So there must have been <number> - <number> = <number>.",
        answer="<number>",
    ),
    Example(
        question="Leah had <number> chocolates and her sister had <number>. If they ate <number>, how many pieces do they have left in total?",
        thought="Originally, Leah had <number> chocolates. Her sister had <number>. So in total they had <number> + <number> = <number>. After eating <number>, they had <number> - <number> = <number>.",
        answer="<number>",
    ),
    Example(
        question="Olivia has <number>. She bought five bagels for <number> each. How much money does she have left?",
        thought="Olivia had <number> dollars. 5 bagels for <number> dollars each will be 5 x <number> = <number> dollars. So she has <number> - <number> dollars left. <number> - <number> is <number>.",
        answer="<number>",
    ),
    Example(
        question="Michael had <number> golf balls. On tuesday, he lost <number> golf balls. On wednesday, he lost <number> more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with <number> golf balls. After losing <number> on tuesday, he had <number> - <number> = <number>. After losing <number> more, he had <number> - <number> = <number> golf balls.",
        answer="<number>",
    ),
]


symbolic_variable_numeric = [
    Example(
        question="Shawn has <numeric> toys. For Christmas, he got <numeric> toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with <numeric> toys. If he got <numeric> toys each from his mom and dad, then that is <numeric> more toys. <numeric> + <numeric> = <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="If there are <numeric> cars in the parking lot and <numeric> more cars arrive, how many cars are in the parking lot?",
        thought="There are originally <numeric> cars. <numeric> more cars arrive. <numeric> + <numeric> = <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="Jason had <numeric> lollipops. He gave Denny some lollipops. Now Jason has <numeric> lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with <numeric> lollipops. Then he had <numeric> after giving some to Denny. So he gave Denny <numeric> - <numeric> = <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="There were <numeric> computers in the server room. <numeric> more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally <numeric> computers. For each of four days, <numeric> more computers were added. So <numeric> * four = <numeric> computers were added. <numeric> + <numeric> is <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="There are <numeric> trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be <numeric> trees. How many trees did the grove workers plant today?",
        thought="There are <numeric> trees originally. Then there were <numeric> trees after some more were planted. So there must have been <numeric> - <numeric> = <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="Leah had <numeric> chocolates and her sister had <numeric>. If they ate <numeric>, how many pieces do they have left in total?",
        thought="Originally, Leah had <numeric> chocolates. Her sister had <numeric>. So in total they had <numeric> + <numeric> = <numeric>. After eating <numeric>, they had <numeric> - <numeric> = <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="Olivia has <numeric>. She bought five bagels for <numeric> each. How much money does she have left?",
        thought="Olivia had <numeric> dollars. 5 bagels for <numeric> dollars each will be 5 x <numeric> = <numeric> dollars. So she has <numeric> - <numeric> dollars left. <numeric> - <numeric> is <numeric>.",
        answer="<numeric>",
    ),
    Example(
        question="Michael had <numeric> golf balls. On tuesday, he lost <numeric> golf balls. On wednesday, he lost <numeric> more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with <numeric> golf balls. After losing <numeric> on tuesday, he had <numeric> - <numeric> = <numeric>. After losing <numeric> more, he had <numeric> - <numeric> = <numeric> golf balls.",
        answer="<numeric>",
    ),
]


symbolic_num_seq = [
    Example(
        question="Shawn has <num1> toys. For Christmas, he got <num2> toys each from his mom and dad. How many toys does he have now?",
        thought="Shawn started with <num1> toys. If he got <num2> toys each from his mom and dad, then that is <num3> more toys. <num1> + <num3> = <num4>.",
        answer="<num4>",
    ),
    Example(
        question="If there are <num1> cars in the parking lot and <num2> more cars arrive, how many cars are in the parking lot?",
        thought="There are originally <num1> cars. <num2> more cars arrive. <num1> + <num2> = <num3>.",
        answer="<num3>",
    ),
    Example(
        question="Jason had <num1> lollipops. He gave Denny some lollipops. Now Jason has <num2> lollipops. How many lollipops did Jason give to Denny?",
        thought="Jason started with <num1> lollipops. Then he had <num2> after giving some to Denny. So he gave Denny <num1> - <num2> = <num3>.",
        answer="<num3>",
    ),
    Example(
        question="There were <num1> computers in the server room. <num2> more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        thought="There were originally <num1> computers. For each of four days, <num2> more computers were added. So <num2> * four = <num3> computers were added. <num1> + <num3> is <num4>.",
        answer="<num4>",
    ),
    Example(
        question="There are <num1> trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be <num2> trees. How many trees did the grove workers plant today?",
        thought="There are <num1> trees originally. Then there were <num2> trees after some more were planted. So there must have been <num2> - <num1> = <num3>.",
        answer="<num3>",
    ),
    Example(
        question="Leah had <num1> chocolates and her sister had <num2>. If they ate <num3>, how many pieces do they have left in total?",
        thought="Originally, Leah had <num1> chocolates. Her sister had <num2>. So in total they had <num1> + <num2> = <num4>. After eating <num3>, they had <num4> - <num3> = <num5>.",
        answer="<num5>",
    ),
    Example(
        question="Olivia has <num1>. She bought five bagels for <num2> each. How much money does she have left?",
        thought="Olivia had <num1> dollars. 5 bagels for <num2> dollars each will be 5 x <num2> = <num3> dollars. So she has <num1> - <num3> dollars left. <num1> - <num3> is <num4>.",
        answer="<num4>",
    ),
    Example(
        question="Michael had <num1> golf balls. On tuesday, he lost <num2> golf balls. On wednesday, he lost <num3> more. How many golf balls did he have at the end of wednesday?",
        thought="Michael started with <num1> golf balls. After losing <num2> on tuesday, he had <num1> - <num2> = <num4>. After losing <num3> more, he had <num4> - <num3> = <num5> golf balls.",
        answer="<num5>",
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


gsm_task_id_to_prompt = {
    "test": math_qa_examples_original,
    "gsm_stream": math_qa_examples_original,
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
    "gsmsample_symb_abs_var": symbolic_variable_num,
    "gsmsample_symb_abs_dig": symbolic_variable_digits,
    "gsmsample_symb_abs_number": symbolic_variable_number,
    "gsmsample_symb_abs_numeric": symbolic_variable_numeric,
    "gsmsample_symb_abs_seq": symbolic_num_seq,
}
