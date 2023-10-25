from prompt_lib.prompts.example import Example

startegy_examples = [
    Example(
        question="Do hamsters provide food for any animals?",
        thought="Hamsters are prey animals. Prey are food for predators. Thus, hamsters provide food for some animals.",
        answer="yes",
    ),
    Example(
        question="Could Brooke Shields succeed at University of Pennsylvania?",
        thought="Brooke Shields went to Princeton University. Princeton University is about as academically rigorous as the University of Pennsylvania. Thus, Brooke Shields could also succeed at the University of Pennsylvania.",
        answer="yes",
    ),
    Example(
        question="Yes or no: Hydrogen's atomic number squared exceeds number of Spice Girls?",
        thought="Hydrogen has an atomic number of 1. 1 squared is 1. There are 5 Spice Girls. Thus, Hydrogen's atomic number squared is less than 5.",
        answer="no",
    ),
    Example(
        question="Yes or no: Is it common to see frost during some college commencements?",
        thought="College commencement ceremonies can happen in December, May, and June. December is in the winter, so there can be frost. Thus, there could be frost at some commencements.",
        answer="yes",
    ),
    Example(
        question="Yes or no: Could a llama birth twice during War in Vietnam (1945-46)?",
        thought="The War in Vietnam was 6 months. The gestation period for a llama is 11 months, which is more than 6 months. Thus, a llama could not give birth twice during the War in Vietnam.",
        answer="no",
    ),
    Example(
        question="Yes or no: Would a pear sink in water?",
        thought="The density of a pear is about 0.6 g/cm^3, which is less than water. Objects less dense than water float. Thus, a pear would float.",
        answer="no",
    ),
]

strategy_examples_abstract = [
    Example(
        question="Do ANIMAL_1 provide food for any ANIMAL_2?",
        thought="ANIMAL_1 are PREY ANIMAL_2. PREY are food for predators. Thus, ANIMAL_1 provide food for some ANIMAL_2.",
        answer="yes",
    ),
    Example(
        question="Could PERSON_1 succeed at SCHOOL_1?",
        thought="PERSON_1 went to SCHOOL_2. SCHOOL_2 is about as academically rigorous as SCHOOL_1. Thus, PERSON_1 could also succeed at SCHOOL_1.",
        answer="yes",
    ),
    Example(
        question="Yes or no: ELEMENT_1's ATOMIC_PROPERTY squared exceeds number of MUSIC_BAND_1?",
        thought="ELEMENT_1 has an ATOMIC_PROPERTY of VALUE_1. VALUE_1 squared is VALUE_2. There are VALUE_3 MUSIC_BAND_1. Thus, ELEMENT_1's ATOMIC_PROPERTY squared is less than VALUE_3.",
        answer="no",
    ),
    Example(
        question="Yes or no: Is it common to see WEATHER_ELEMENT_1 during some EVENT_1?",
        thought="EVENT_1 can happen in MONTH_1, MONTH_2, and MONTH_3. MONTH_1 is in the SEASON_1, so there can be WEATHER_ELEMENT_1. Thus, there could be WEATHER_ELEMENT_1 at some EVENT_1.",
        answer="yes",
    ),
    Example(
        question="Yes or no: Could a ANIMAL_1 give birth twice during EVENT_1 (YEAR_1-YEAR_2)?",
        thought="The EVENT_1 was DURATION_1. The gestation period for a ANIMAL_1 is DURATION_2, which is more than DURATION_1. Thus, a ANIMAL_1 could not give birth twice during the EVENT_1.",
        answer="no",
    ),
    Example(
        question="Yes or no: Would a FRUIT_1 FLOAT in LIQUID_1?",
        thought="The density of a FRUIT_1 is about VALUE_1, which is less than LIQUID_1. Objects less dense than LIQUID_1 float. Thus, a FRUIT_1 would FLOAT.",
        answer="no",
    ),
]

startegy_examples_wrong = [
    Example(
        question="Do hamsters provide food for any animals?",
        thought="Hamsters are domestic animals. Domestic animals are pets, not food. Thus, hamsters provide food for some animals.",
        answer="yes",
    ),
    Example(
        question="Could Brooke Shields succeed at University of Pennsylvania?",
        thought="Brooke Shields went to a local community college. A community college is less academically rigorous than the University of Pennsylvania. Thus, Brooke Shields could also succeed at the University of Pennsylvania.",
        answer="yes",
    ),
    Example(
        question="Yes or no: Hydrogen's atomic number squared exceeds number of Spice Girls?",
        thought="Hydrogen has an atomic number of 2. 2 squared is 4. There are 5 Spice Girls. Thus, Hydrogen's atomic number squared is less than 5.",
        answer="no",
    ),
    Example(
        question="Yes or no: Is it common to see frost during some college commencements?",
        thought="College commencement ceremonies typically happen in December, May, and June. December is in the summer, so there cannot be frost. Thus, there could be frost at some commencements.",
        answer="yes",
    ),
    Example(
        question="Yes or no: Could a llama birth twice during War in Vietnam (1945-46)?",
        thought="The War in Vietnam was 6 months. The gestation period for a llama is 2 months, which is less than 6 months. Thus, a llama could not give birth twice during the War in Vietnam.",
        answer="no",
    ),
    Example(
        question="Yes or no: Would a pear sink in water?",
        thought="The density of a pear is about 0.6 g/cm^3, which is less than water. Objects more dense than water float. Thus, a pear would float.",
        answer="no",
    ),
]
strategy_ccot = [
    Example(
        question="Can hamsters serve as food for other animals?",
        thought="Hamsters -> prey animals. Prey -> food for predators.",
        answer="yes",
    ),
    Example(
        question="Could Brooke Shields succeed at University of Pennsylvania?",
        thought="Brooke Shields -> Princeton graduate. Princeton -> similar rigor to University of Pennsylvania.",
        answer="yes",
    ),
    Example(
        question="Is Hydrogen's atomic number squared more than the number of Spice Girls?",
        thought="Hydrogen's atomic number -> 1. 1 squared -> 1. Number of Spice Girls -> 5.",
        answer="no",
    ),
    Example(
        question="Is frost a common sight during some college commencements?",
        thought="Commencement ceremonies -> occur in December. December -> winter season can have frost.",
        answer="yes",
    ),
    Example(
        question="Could a llama give birth twice during the War in Vietnam (1945-46)?",
        thought="War in Vietnam duration -> 6 months. Llama's gestation period -> 11 months.",
        answer="no",
    ),
    Example(
        question="Would a pear sink in water?",
        thought="Pear's density -> less than water's density. Less dense objects -> float in water.",
        answer="no",
    ),
]
strategy_task_id_to_prompt = {
    "strategy_stream": startegy_examples,
    "strategy_stream_abstract": strategy_examples_abstract,
    "strategy_stream_wrong": startegy_examples_wrong,
    "strategy_stream_ccot": strategy_ccot,
}
