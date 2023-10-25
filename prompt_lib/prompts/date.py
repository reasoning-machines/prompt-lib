from prompt_lib.prompts.example import Example

date_examples_original = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/05/2015.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 03/12/2002. So the date 24 hours later will be 03/13/2002.",
        answer="03/13/2002",
    ),
]


future_dates = [
    Example(
        question="It is 4/30/3069 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 04/30/3069. 24 hours later is one day after today, which would be 04/31/3069.",
        answer="04/31/3069",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/3043, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after 06/01/3043 is 06/02/3043, so today is 06/02/3043. 10 days before today is 05/23/3043.",
        answer="05/23/3043",
    ),
    Example(
        question="The first day of 3130 is a Tuesday, and today is the first Monday of 3130. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 3130 was Tuesday, then 01/01/3130 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/3130.",
        answer="01/07/3130",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 3101. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on 02/28/3101. Today is her 16-year old birthday, so today is 02/28/3117. So yesterday was 02/27/3117.",
        answer="02/27/3117",
    ),
    Example(
        question="3115 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 3115 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/3115 is 12/30/3114, so today is 12/30/3114. So one week from today will be 01/05/3115.",
        answer="01/05/3115",
    ),
    Example(
        question="Jane thought today is 3/11/3102, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 03/12/3102. So the date 24 hours later will be 03/13/3102.",
        answer="03/13/3102",
    ),
]

abstract_date = [
    Example(
        question="It is DATE today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is DATE. 24 hours later is one day after today, which would be DATE.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on DATE, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after DATE is DATE, so today is DATE. 10 days before today is 05/23/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then DATE was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on DATE. Today is her 16-year old birthday, so today is DATE. So yesterday was 02/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before DATE is DATE, so today is DATE. So one week from today will be 01/05/2015.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is DATE, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is DATE. So the date 24 hours later will be 03/13/2002.",
        answer="03/13/2002",
    ),
]


pat_wrong = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 04/19/1969. 24 hours later is one day after today, which would be 03/20/1969.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/12/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2009.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 03/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 02/05/2015.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 03/12/2002. So the date 24 hours later will be 04/13/2002.",
        answer="03/13/2002",
    ),
]

pat_none = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 04/19/1969.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="10 days before today is 05/23/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="So the date 24 hours later will be 03/13/2002.",
        answer="03/13/2002",
    ),
]

pat_only = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today = 04/19/1969. 24 hours = 1 day. 04/19/1969 + 1 = 04/20/1969.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="06/01/1943 + 1 day = 06/02/1943. Today = 06/02/1943. Today - 10 days = 05/23/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="First day of 2019 = 01/01/2019. 01/01/2019 = Tuesday. Today = first monday. Tuesday - Monday = 6 days. So Today 01/01/2019 + 6 days = 01/07/2019.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="Last day of February = 28th. 16-year old birthday => +16 years. Today = 02/28/2001 + 16 years = 02/28/2017. Yesterday = 02/28/2017 - 1 = 02/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="36 hours = 2 days. 2 days before = 01/01/2015 - 2 = 12/30/2014. Today = 12/30/2014. Today + 1 week = 01/05/2015.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today = 03/12/2002. 24 hours = 1 day. 3/12/2002 + 1 day = 03/13/2002.",
        answer="03/13/2002",
    ),
]

random_thought = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so today is 02/28/2017. So yesterday was 02/27/2017.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="Today is 03/12/2002. So the date 24 hours later will be 03/13/2002.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/05/2015.",
        answer="03/13/2002",
    ),
]

yoda_thought = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="04/19/1969, today is. Later is one day after today, 24 hours, 04/20/1969, which would be.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="06/02/1943, one day after 06/01/1943 is, 06/02/1943, so today is. 05/23/1943, 10 days before today is.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="Tuesday, if the first day of 2019 was, a tuesday, then 01/01/2019 was. The first monday, today is, six days later, would be. 01/07/2019, so today is.",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The 28th, the last day of february is, Born on 02/28/2001, so jane was. Her 16-year old birthday, today is,02/28/2017, so today is. 02/27/2017, so yesterday was.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="Coming in 36 hours, if 2015 is, coming in 2 days, then it is. 12/30/2014, 2 days before 01/01/2015 is, 12/30/2014, so today is. 01/05/2015, so one week from today will be.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="03/12/2002, today is. Later will be 03/13/2002, so the date 24 hours.",
        answer="03/13/2002",
    ),
]

yoda_both = [
    Example(
        question="4/19/1969 today it is. The date 24 hours later in MM/DD/YYYY what is?",
        thought="04/19/1969, today is. Later is one day after today, 24 hours, 04/20/1969, which would be.",
        answer="04/20/1969",
    ),
    Example(
        question="Scheduled to be on 06/01/1943 the concert was, delayed by one day to today but was. The date 10 days ago in MM/DD/YYYY what is?",
        thought="06/02/1943, one day after 06/01/1943 is, 06/02/1943, so today is. 05/23/1943, 10 days before today is.",
        answer="05/23/1943",
    ),
    Example(
        question="A tuesday the first day of 2019 is, the first monday of 2019 and today is. The date today in MM/DD/YYYY what is?",
        thought="Tuesday, if the first day of 2019 was, a tuesday, then 01/01/2019 was. The first monday, today is, six days later, would be. 01/07/2019, so today is.",
        answer="01/07/2019",
    ),
    Example(
        question="Born on the last day of feburary in 2001 jane was. Her 16-year-old birthday today is. The date yesterday in MM/DD/YYYY what is?",
        thought="The 28th, the last day of february is, Born on 02/28/2001, so jane was. Her 16-year old birthday, today is,02/28/2017, so today is. 02/27/2017, so yesterday was.",
        answer="02/27/2017",
    ),
    Example(
        question="Coming in 36 hours 2015 is. The date one week from today in MM/DD/YYYY what is? Yes, hrrrm.",
        thought="Coming in 36 hours, if 2015 is, coming in 2 days, then it is. 12/30/2014, 2 days before 01/01/2015 is, 12/30/2014, so today is. 01/05/2015, so one week from today will be.",
        answer="01/05/2015",
    ),
    Example(
        question="Today is 3/11/2002 jane thought, in fact mar 12 but today is, 1 day later which is. The date 24 hours later in MM/DD/YYYY what is?",
        thought="03/12/2002, today is. Later will be 03/13/2002, so the date 24 hours.",
        answer="03/13/2002",
    ),
]

inter_shuf = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="later is 04/19/1969. 24 day after which would be today, hours Today 04/20/1969. one is",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="today today days One 05/23/1943. 06/01/1943 06/02/1943, 06/02/1943. is is 10 is so day before after",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="01/01/2019 today monday, would Tuesday, 2019 first is Tuesday. day of later. then So was 01/07/2019. first be days Today the a six was is If the",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="last was her 16-year is 02/28/2001. So of so 02/27/2017. is birthday, is The February on yesterday was old today Today 02/28/2017. so day born 28th, the Jane",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="in 2015 one hours, 01/01/2015 36 so it days. today 12/30/2014, then 2 week 2 is 12/30/2014. is be days in is 01/05/2015. So from today coming coming before is will If",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="later So date Today 03/13/2002. hours 24 is 03/12/2002. the be will",
        answer="03/13/2002",
    ),
]

intra_shuf = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today 04/19/1969 is. 24 after one which later be would hours 04/20/1969 day today, is",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="is 06/02/1943, so today 06/02/1943 day 06/01/1943 One is after. 10 today days is before 05/23/1943",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="was Tuesday the day was 2019 first If then 01/01/2019 of Tuesday, a. days Today six later is monday, be would first the. today So 01/07/2019 is",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="last day Jane February on was The of 28th, born is so the 02/28/2001. Today today is birthday, old so 02/28/2017 16-year is her. 02/27/2017 yesterday So was",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="days 2015 is then coming 36 If it hours, coming is in 2 in. 2 is 12/30/2014, days 01/01/2015 so 12/30/2014 is today before. from week will So 01/05/2015 be today one",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="03/12/2002 Today is. the hours later 24 be will So date 03/13/2002",
        answer="03/13/2002",
    ),
]

brief = [
    Example(
        question="It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 04/19/1969. 24 hours (one day) later is 04/20/1969.",
        answer="04/20/1969",
    ),
    Example(
        question="The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="Today is 06/02/1943 (one day after 06/01/1943). 10 days before today is 05/23/1943.",
        answer="05/23/1943",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="01/01/2019 was a Tuesday (first day of 2019). Today is the first monday, 01/07/2019. (six days later).",
        answer="01/07/2019",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="Jane was born on 02/28/2001. So today is 02/28/2017 and yesterday was 02/27/2017.",
        answer="02/27/2017",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="2015 is coming in 2 days (36 hours). So today is 12/30/2021, and one week from today will be 01/05/2015.",
        answer="01/05/2015",
    ),
    Example(
        question="Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is 03/12/2002. So the date 24 hours later will be 03/13/2002.",
        answer="03/13/2002",
    ),
]


date_examples_abstract_one = [
    Example(
        question="It is DATE1 today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is DATE1. 24 hours later is one day after today, which would be DATE2.",
        answer="DATE2",
    ),
    Example(
        question="The concert was scheduled to be on DATE1, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after DATE1 is DATE2, so today is DATE2. 10 days before today is DATE3.",
        answer="DATE3",
    ),
    Example(
        question="The first day of Y1 is a D1, and today is the first D2 of Y1. What is the date today in MM/DD/YYYY?",
        thought="If the first day of Y1 was D1, then 01/01/Y1 was a D1. Today is the first D2, would be six days later. So today is DATE1.",
        answer="DATE1",
    ),
    Example(
        question="Jane was born on the last day of M1 in Y1. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of M1 is the D1, so Jane was born on DATE1. Today is her 16-year old birthday, so today is DATE2. So yesterday was DATE3.",
        answer="DATE3",
    ),
    Example(
        question="Y1 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If Y1 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/Y1 is DATE1, so today is DATE1. So one week from today will be DATE2.",
        answer="DATE2",
    ),
    Example(
        question="Jane thought today is DATE1, but today is in fact DATE2, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is DATE2. So the date 24 hours later will be DATE3.",
        answer="DATE3",
    ),
]
date_examples_abstract_two = [
    Example(
        question="It is [DATE1] today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [DATE1]. 24 hours later is one day after today, which would be [DATE2].",
        answer="[DATE2]",
    ),
    Example(
        question="The concert was scheduled to be on [DATE1], but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after [DATE1] is [DATE2], so today is [DATE2]. 10 days before today is [DATE3].",
        answer="[DATE3]",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then [DATE1] was a Tuesday. Today is the first monday, would be six days later. So today is [DATE2].",
        answer="[DATE2]",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on [DATE1]. Today is her 16-year old birthday, so today is [DATE2]. So yesterday was [DATE3].",
        answer="[DATE3]",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before [DATE1] is [DATE2], so today is [DATE2]. So one week from today will be [DATE3].",
        answer="[DATE3]",
    ),
    Example(
        question="Jane thought today is [DATE1], but today is in fact 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [DATE2]. So the date 24 hours later will be [DATE3].",
        answer="[DATE3]",
    ),
]
date_examples_abstract_three = [
    Example(
        question="It is [DATE_1] today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [DATE_1]. 24 hours later is one day after today, which would be [DATE_2].",
        answer="[DATE_2]",
    ),
    Example(
        question="The concert was scheduled to be on [DATE_1], but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after [DATE_1] is [DATE_2], so today is [DATE_2]. 10 days before today is [DATE_3].",
        answer="[DATE_3]",
    ),
    Example(
        question="The first day of [YEAR] is a Tuesday, and today is the first Monday of [YEAR]. What is the date today in MM/DD/YYYY?",
        thought="If the first day of [YEAR] was Tuesday, then 01/01/[YEAR] was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/[YEAR].",
        answer="01/07/[YEAR]",
    ),
    Example(
        question="[NAME] was born on the last day of Feburary in [YEAR]. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so [NAME] was born on 02/28/[YEAR]. Today is her 16-year old birthday, so today is 02/28/[YEAR2]. So yesterday was 02/27/[YEAR2].",
        answer="02/27/[YEAR2]",
    ),
    Example(
        question="[YEAR] is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If [YEAR] is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/[YEAR] is 12/30/[YEAR], so today is 12/30/[YEAR]. So one week from today will be 01/05/[YEAR].",
        answer="01/05/[YEAR]",
    ),
    Example(
        question="[NAME] thought today is [DATE_1], but today is in fact [DATE_2], which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [DATE_2]. So the date 24 hours later will be [DATE_3].",
        answer="[DATE_3]",
    ),
]

date_examples_abstract_four = [
    Example(
        question="It is <date1> today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is <date1>. 24 hours later is one day after today, which would be <date2>.",
        answer="<date2>",
    ),
    Example(
        question="The concert was scheduled to be on <date1>, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after <date1> is <date2>, so today is <date2>. 10 days before today is <date3>.",
        answer="<date3>",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then <date1> was a Tuesday. Today is the first monday, would be six days later. So today is <date2>.",
        answer="<date2>",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on <date1>. Today is her 16-year old birthday, so today is <date2>. So yesterday was <date3>.",
        answer="<date3>",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before <date1> is <date2>, so today is <date2>. So one week from today will be <date3>.",
        answer="<date3>",
    ),
    Example(
        question="Jane thought today is <date1>, but today is in fact <date2>, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is <date2>. So the date 24 hours later will be <date3>.",
        answer="<date3>",
    ),
]


date_abstract_hash = [
    Example(
        question="It is #### today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is ####. 24 hours later is one day after today, which would be ######.",
        answer="######",
    ),
    Example(
        question="The concert was scheduled to be on ####, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after #### is #####, so today is #####. 10 days before today is #######.",
        answer="#######",
    ),
    Example(
        question="The first day of #### is a Tuesday, and today is the first Monday of ####. What is the date today in MM/DD/YYYY?",
        thought="If the first day of #### was Tuesday, then ###### was a Tuesday. Today is the first monday, would be six days later. So today is ######.",
        answer="######",
    ),
    Example(
        question="Jane was born on the last day of #### in ####. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of #### is the ###, so Jane was born on #####. Today is her 16-year old birthday, so today is #####. So yesterday was ######.",
        answer="######",
    ),
    Example(
        question="#### is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If #### is coming in 36 hours, then it is coming in 2 days. 2 days before ##### is ######, so today is ######. So one week from today will be #######.",
        answer="#######",
    ),
    Example(
        question="Jane thought today is ####, but today is in fact ####, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is ####. So the date 24 hours later will be #####.",
        answer="#####",
    ),
]


date_examples_single_hash = [
    Example(
        question="It is # today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is #. 24 hours later is one day after today, which would be #.",
        answer="#",
    ),
    Example(
        question="The concert was scheduled to be on #, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after # is #, so today is #. 10 days before today is #.",
        answer="#",
    ),
    Example(
        question="The first day of # is a Tuesday, and today is the first Monday of #. What is the date today in MM/DD/YYYY?",
        thought="If the first day of # was Tuesday, then # was a Tuesday. Today is the first monday, would be six days later. So today is #.",
        answer="#",
    ),
    Example(
        question="Jane was born on the last day of # in #. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of # is the #, so Jane was born on #. Today is her 16-year old birthday, so today is #. So yesterday was #.",
        answer="#",
    ),
    Example(
        question="# is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If # is coming in 36 hours, then it is coming in 2 days. 2 days before # is #, so today is #. So one week from today will be #.",
        answer="#",
    ),
    Example(
        question="Jane thought today is #, but today is in fact #, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is #. So the date 24 hours later will be #.",
        answer="#",
    ),
]

date_examples_ampersand = [
    Example(
        question="It is % today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is %. 24 hours later is one day after today, which would be %.",
        answer="%",
    ),
    Example(
        question="The concert was scheduled to be on %, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after % is %, so today is %. 10 days before today is %.",
        answer="%",
    ),
    Example(
        question="The first day of % is a Tuesday, and today is the first Monday of %. What is the date today in MM/DD/YYYY?",
        thought="If the first day of % was Tuesday, then % was a Tuesday. Today is the first monday, would be six days later. So today is %.",
        answer="%",
    ),
    Example(
        question="Jane was born on the last day of Feburary in %. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on %. Today is her 16-year old birthday, so today is %. So yesterday was %.",
        answer="%",
    ),
    Example(
        question="% is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If % is coming in 36 hours, then it is coming in 2 days. 2 days before % is %, so today is %. So one week from today will be %.",
        answer="%",
    ),
    Example(
        question="Jane thought today is %, but today is in fact %, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is %. So the date 24 hours later will be %.",
        answer="%",
    ),
]


date_abstract_blanks = [
    Example(
        question="It is _____ today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is _____. 24 hours later is one day after today, which would be _____.",
        answer="____",
    ),
    Example(
        question="The concert was scheduled to be on _____, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after _____ is _____, so today is _____. 10 days before today is _____.",
        answer="____",
    ),
    Example(
        question="The first day of _____ is a Tuesday, and today is the first Monday of _____. What is the date today in MM/DD/YYYY?",
        thought="If the first day of _____ was Tuesday, then _____ was a Tuesday. Today is the first monday, would be six days later. So today is _____.",
        answer="____",
    ),
    Example(
        question="Jane was born on the last day of Feburary in _____. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on _____. Today is her 16-year old birthday, so today is _____. So yesterday was _____.",
        answer="____",
    ),
    Example(
        question="_____ is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If _____ is coming in 36 hours, then it is coming in 2 days. 2 days before _____ is _____, so today is _____. So one week from today will be _____.",
        answer="____",
    ),
    Example(
        question="Jane thought today is _____, but today is in fact _____, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is _____. So the date 24 hours later will be _____.",
        answer="____",
    ),
]


date_abstract_xyz = [
    Example(
        question="It is [x] today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [x]. 24 hours later is one day after today, which would be [y].",
        answer="[y]",
    ),
    Example(
        question="The concert was scheduled to be on [x], but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after [x] is [y], so today is [y]. 10 days before today is [z].",
        answer="[z]",
    ),
    Example(
        question="The first day of [x] is a Tuesday, and today is the first Monday of [x]. What is the date today in MM/DD/YYYY?",
        thought="If the first day of [x] was Tuesday, then [y] was a Tuesday. Today is the first monday, would be six days later. So today is [z].",
        answer="[z]",
    ),
    Example(
        question="Jane was born on the last day of Feburary in [x]. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on [y]. Today is her 16-year old birthday, so today is [z]. So yesterday was [a].",
        answer="[a]",
    ),
    Example(
        question="[x] is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If [x] is coming in 36 hours, then it is coming in 2 days. 2 days before [y] is [z], so today is [z]. So one week from today will be [a].",
        answer="[a]",
    ),
    Example(
        question="Jane thought today is [x], but today is in fact one day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [y]. So the date 24 hours later will be [z].",
        answer="[z]",
    ),
]




date_abstract_sym = [
    Example(
        question="It is [SYM] today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [SYM]. 24 hours later is one day after today, which would be [SYM].",
        answer="[SYM]",
    ),
    Example(
        question="The concert was scheduled to be on [SYM], but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after [SYM] is [SYM], so today is [SYM]. 10 days before today is [SYM].",
        answer="[SYM]",
    ),
    Example(
        question="The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?",
        thought="If the first day of 2019 was Tuesday, then [SYM] was a Tuesday. Today is the first monday, would be six days later. So today is [SYM].",
        answer="[SYM]",
    ),
    Example(
        question="Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of February is the 28th, so Jane was born on [SYM]. Today is her 16-year old birthday, so today is [SYM]. So yesterday was [SYM].",
        answer="[SYM]",
    ),
    Example(
        question="2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before [SYM] is [SYM], so today is [SYM]. So one week from today will be [SYM].",
        answer="[SYM]",
    ),
    Example(
        question="Jane thought today is [SYM], but today is in fact [SYM], which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [SYM]. So the date 24 hours later will be [SYM].",
        answer="[SYM]",
    ),
]


date_abstract_xyz_v2 = [
    Example(
        question="It is [X] today. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [X]. 24 hours later is one day after today, which would be [Y].",
        answer="[Y]",
    ),
    Example(
        question="The concert was scheduled to be on [X], but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?",
        thought="One day after [X] is [Y], so today is [Y]. 10 days before today is [Z].",
        answer="[Z]",
    ),
    Example(
        question="The first day of [X] is a Tuesday, and today is the first Monday of [X]. What is the date today in MM/DD/YYYY?",
        thought="If the first day of [X] was Tuesday, then [Y] was a Tuesday. Today is the first monday, would be six days later. So today is [Z].",
        answer="[Z]",
    ),
    Example(
        question="Jane was born on the last day of [X] in [Y]. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?",
        thought="The last day of [X] is the [Y], so Jane was born on [Z]. Today is her 16-year old birthday, so today is [A]. So yesterday was [B].",
        answer="[B]",
    ),
    Example(
        question="[X] is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?",
        thought="If [X] is coming in 36 hours, then it is coming in 2 days. 2 days before [Y] is [Z], so today is [Z]. So one week from today will be [A].",
        answer="[A]",
    ),
    Example(
        question="Jane thought today is [X], but today is in fact [Y], which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?",
        thought="Today is [Y]. So the date 24 hours later will be [Z].",
        answer="[Z]",
    ),
]

# Function to create passive voice for date thoughts
def convert_date_to_passive(thought):
    if "Today is 04/19/1969." in thought:
        return "04/19/1969 is the date today. 24 hours later, which is one day after today, would be recognized as 04/20/1969."
    if "One day after 06/01/1943 is 06/02/1943," in thought:
        return "06/02/1943 is the date which comes one day after 06/01/1943. 10 days before this date, 05/23/1943 is identified."
    if "If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday." in thought:
        return "01/01/2019 was identified as a Tuesday based on the information that the first day of 2019 was a Tuesday. Being the first Monday, today would be recognized as six days later, which is 01/07/2019."
    if "The last day of February is the 28th, so Jane was born on 02/28/2001." in thought:
        return "02/28/2001 is identified as the date of Jane's birth, based on the information that she was born on the last day of February. Given that today is her 16-year-old birthday, 02/28/2017 is identified as today. This means 02/27/2017 was the date yesterday."
    if "If 2015 is coming in 36 hours, then it is coming in 2 days." in thought:
        return "12/30/2014 is identified as today based on the information that 2015 is coming in 2 days. Thus, 01/05/2015 is recognized as the date one week from today."
    if "Today is 03/12/2002." in thought:
        return "03/12/2002 is the date recognized as today. The date 24 hours later is identified as 03/13/2002."
    
# Applying the function


# Function to create nominalization for date thoughts
def convert_date_to_nominalization(thought):
    if "Today is 04/19/1969." in thought:
        return "The date's recognition as 04/19/1969 and the addition of 24 hours, which equates to one day, results in the identification of 04/20/1969 as the next day."
    if "One day after 06/01/1943 is 06/02/1943," in thought:
        return "The identification of 06/02/1943 as the day following 06/01/1943 leads to the conclusion that 05/23/1943 is the date 10 days prior."
    if "If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday." in thought:
        return "With 01/01/2019's identification as a Tuesday, the calculation of six days later confirms the date as 01/07/2019, which is a Monday."
    if "The last day of February is the 28th, so Jane was born on 02/28/2001." in thought:
        return "Jane's birth on 02/28/2001, identified as the last day of February, and the recognition of today as her 16-year-old birthday, confirms 02/28/2017 as today and 02/27/2017 as yesterday."
    if "If 2015 is coming in 36 hours, then it is coming in 2 days." in thought:
        return "The deduction of today as 12/30/2014, based on 2015's arrival in 2 days, results in the identification of 01/05/2015 as the date one week later."
    if "Today is 03/12/2002." in thought:
        return "03/12/2002's identification as today leads to the conclusion that 03/13/2002 is the date 24 hours later."
    
# Applying the function

# Function to create cleft sentences for date thoughts
def convert_date_to_cleft(thought):
    if "Today is 04/19/1969." in thought:
        return "It is today that is recognized as 04/19/1969. And it is one day later, which translates to 24 hours, that would be 04/20/1969."
    if "One day after 06/01/1943 is 06/02/1943," in thought:
        return "It is 06/02/1943 that is the day after 06/01/1943. And it is 05/23/1943 that stands as the date 10 days prior."
    if "If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday." in thought:
        return "It was on 01/01/2019 that Tuesday was identified. And it is 01/07/2019 that represents today, which is six days later and a Monday."
    if "The last day of February is the 28th, so Jane was born on 02/28/2001." in thought:
        return "It is 02/28/2001 that is identified as Jane's birthdate, being the last day of February. And it is 02/28/2017 that stands as today, given her 16-year-old birthday, making 02/27/2017 the date for yesterday."
    if "If 2015 is coming in 36 hours, then it is coming in 2 days." in thought:
        return "It is 12/30/2014 that is recognized as today, deducing from 2015's arrival in 2 days. And it is 01/05/2015 that would be the date one week later."
    if "Today is 03/12/2002." in thought:
        return "It is 03/12/2002 that is recognized as today. And it is 03/13/2002 that would be the date 24 hours later."
    
# Applying the function


# Function to create nested clauses for date thoughts
def convert_date_to_nested_clauses(thought):
    if "Today is 04/19/1969." in thought:
        return "Given that today is 04/19/1969, and considering that 24 hours later is one day after today, we can deduce that the date would be 04/20/1969."
    if "One day after 06/01/1943 is 06/02/1943," in thought:
        return "Given that 06/02/1943 is the day that comes after 06/01/1943, and considering that we want to know the date 10 days prior, it is evident that the date is 05/23/1943."
    if "If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday." in thought:
        return "Given that 01/01/2019 was a Tuesday, and considering that today is said to be the first Monday, it is evident that today, which is six days later, is 01/07/2019."
    if "The last day of February is the 28th, so Jane was born on 02/28/2001." in thought:
        return "Given that 02/28/2001, which is the last day of February, is when Jane was born, and considering that today is her 16-year-old birthday, it is evident that today is 02/28/2017, making yesterday 02/27/2017."
    if "If 2015 is coming in 36 hours, then it is coming in 2 days." in thought:
        return "Given that 2015 is arriving in 2 days, which means in 36 hours, and considering that we want to know the date one week from today, it becomes clear that today is 12/30/2014, leading to the date one week later as 01/05/2015."
    if "Today is 03/12/2002." in thought:
        return "Given that today is 03/12/2002, and considering that we are looking for the date 24 hours later, it is evident that the date will be 03/13/2002."
    
# Applying the function

# Function to create fronting for date thoughts
def convert_date_to_fronting(thought):
    if "Today is 04/19/1969." in thought:
        return "04/19/1969 is the date today. 24 hours later, or one day after, would be the date 04/20/1969."
    if "One day after 06/01/1943 is 06/02/1943," in thought:
        return "06/02/1943, that's the date one day after 06/01/1943. 10 days prior to this, the date would be 05/23/1943."
    if "If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday." in thought:
        return "01/01/2019, that was a Tuesday. Six days after this, which is the first Monday, the date is 01/07/2019."
    if "The last day of February is the 28th, so Jane was born on 02/28/2001." in thought:
        return "02/28/2001, that's the date when Jane was born. 16 years later, which is her birthday today, the date is 02/28/2017. This means yesterday was 02/27/2017."
    if "If 2015 is coming in 36 hours, then it is coming in 2 days." in thought:
        return "12/30/2014, that's the date today if 2015 is coming in 2 days. A week later from this date would be 01/05/2015."
    if "Today is 03/12/2002." in thought:
        return "03/12/2002, that's the date today. 24 hours later, the date would be 03/13/2002."
    
date_examples_nested_clauses = [
    Example(question=example.question, thought=convert_date_to_nested_clauses(example.thought), answer=example.answer) 
    for example in date_examples_original
]

date_examples_fronting = [
    Example(question=example.question, thought=convert_date_to_fronting(example.thought), answer=example.answer) 
    for example in date_examples_original
]

date_examples_nominalization = [
    Example(question=example.question, thought=convert_date_to_nominalization(example.thought), answer=example.answer) 
    for example in date_examples_original
]

date_examples_cleft_sentences = [
    Example(question=example.question, thought=convert_date_to_cleft(example.thought), answer=example.answer) 
    for example in date_examples_original
]

date_examples_passive_voice = [
    Example(question=example.question, thought=convert_date_to_passive(example.thought), answer=example.answer) 
    for example in date_examples_original
]

linguistic_variation_date = {
    "date_lv_passive_voice": date_examples_passive_voice,
    "date_lv_nominalization": date_examples_nominalization,
    "date_lv_cleft_sentences": date_examples_cleft_sentences,
    "date_lv_nested_clauses": date_examples_nested_clauses,
    "date_lv_fronting": date_examples_fronting,
}




date_task_id_to_prompt = {
    "date_stream": date_examples_original,
    "date_direct": date_examples_original,
    "date_symb_ood": future_dates,
    "date_symb_abs": abstract_date,
    "date_symb_abs_v1": date_examples_abstract_one,
    "date_symb_abs_v2": date_examples_abstract_two,
    "date_symb_abs_v3": date_examples_abstract_three,
    "date_symb_abs_v4": date_examples_abstract_four,
    
    "date_symb_hash": date_abstract_hash,
    "date_symb_single_hash": date_examples_single_hash,
    "date_symb_ampersand": date_examples_ampersand,
    "date_symb_blanks": date_abstract_blanks,
    
    "date_symb_xyz": date_abstract_xyz,
    "date_symb_xyz_v2": date_abstract_xyz_v2,
    
    "date_symb_sym": date_abstract_sym,
    
    "date_pat_wrong": pat_wrong,
    "date_pat_none": pat_none,
    "date_pat_only": pat_only,
    "date_text_rand": random_thought,
    "date_text_yoda_thought": yoda_thought,
    "date_text_yoda_both": yoda_both,
    "date_text_inter_shuf": inter_shuf,
    "date_text_intra_shuf": intra_shuf,
    "date_ccot": brief,
}


date_task_id_to_prompt.update(linguistic_variation_date)