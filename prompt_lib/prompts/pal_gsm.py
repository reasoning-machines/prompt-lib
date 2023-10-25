from dataclasses import dataclass


@dataclass
class Example:
    question: str
    answer: str
    thought: str

eg_1_solution_string = """
def solution():
    \"\"\"Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?\"\"\"
    toys_initial = 5
    mom_toys = 2
    dad_toys = 2
    total_received = mom_toys + dad_toys
    total_toys = toys_initial + total_received
    result = total_toys
    return result
"""


eg_2_solution_string = """
def solution():
    \"\"\"If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?\"\"\"
    cars_initial = 3
    cars_arrived = 2
    total_cars = cars_initial + cars_arrived
    result = total_cars
    return result
"""

eg_3_solution_string = """
def solution():
    \"\"\"Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?\"\"\"
    jason_lollipops_initial = 20
    jason_lollipops_after = 12
    denny_lollipops = jason_lollipops_initial - jason_lollipops_after
    result = denny_lollipops
    return result
"""

eg_4_solution_string = """
def solution():
    \"\"\"There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?\"\"\"
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between monday and thursday
    computers_added = computers_per_day * num_days
    computers_total = computers_initial + computers_added
    result = computers_total
    return result
"""

eg_5_solution_string = """
def solution():
    \"\"\"There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?\"\"\"
    trees_initial = 15
    trees_after = 21
    trees_added = trees_after - trees_initial
    result = trees_added
    return result
"""

eg_6_solution_string = """
def solution():
    \"\"\"Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?\"\"\"
    leah_chocolates = 32
    sister_chocolates = 42
    total_chocolates = leah_chocolates + sister_chocolates
    chocolates_eaten = 35
    chocolates_left = total_chocolates - chocolates_eaten
    result = chocolates_left
    return result
"""

eg_7_solution_string = """
def solution():
    \"\"\"Olivia has $23. She bought five bagels for $3 each. How much money does she have left?\"\"\"
    money_initial = 23
    bagels = 5
    bagel_cost = 3
    money_spent = bagels * bagel_cost
    money_left = money_initial - money_spent
    result = money_left
    return result
"""


eg_8_solution_string = """
def solution():
    \"\"\"Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?\"\"\"
    golf_balls_initial = 58
    golf_balls_lost_tuesday = 23
    golf_balls_lost_wednesday = 2
    golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
    result = golf_balls_left
    return result
"""


pal_gsm = [
    Example(
        question="Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?",
        answer=eg_1_solution_string,
        thought="",
    ),
    Example(
        question="If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?",
        answer=eg_2_solution_string,
        thought="",
    ),
    Example(
        question="Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?",
        answer=eg_3_solution_string,
        thought="",
    ),
    Example(
        question="There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?",
        answer=eg_4_solution_string,
        thought="",
    ),
    Example(
        question="There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?",
        answer=eg_5_solution_string,
        thought="",
    ),
    Example(
        question="Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?",
        answer=eg_6_solution_string,
        thought="",
    ),
    Example(
        question="Olivia has $23. She bought five bagels for $3 each. How much money does she have left?",
        answer=eg_7_solution_string,
        thought="",
    ),
    Example(
        question="Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?",
        answer=eg_8_solution_string,
        thought="",
    ),
]


pal_maths_task_id_to_prompt = {
    "gsm_pal": pal_gsm,
    "gsmtrainmistakes_pal": pal_gsm,
    "gsmhard_pal": pal_gsm,
    "svamp_pal": pal_gsm,
    "mawpsaddsub_pal": pal_gsm,
    "mawpsmultiarith_pal": pal_gsm,
    "mawpssingleeq_pal": pal_gsm,
    "mawpssingleop_pal": pal_gsm,
    "asdiv_pal": pal_gsm,
}