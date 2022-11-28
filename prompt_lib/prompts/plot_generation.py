from prompt_lib.prompts.example import Example

roc = [
    Example(
        question="</s><e_0>NONE<e_1>antibiotics<e_2>next day<e_3>felt great</s><s><e_99>[FEMALE] had a fever.<e_99>she went to the doctor.<e_1>they prescribed her antibiotics.<e_1>she took the antibiotics and slept a lot.<e_2><e_3><extra_id_0><s>",
        answer="<extra_id_0>she felt great the next day.<sep>",
        thought="We need to find a sentence that contains the plot points 'next day' and 'felt great' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>worldwide fame<e_1>famous ballerina<e_2>handsome devil<e_3>last name<e_4>married life<e_5>many years<e_6>NONE<e_7>forever change</s><s><e_0><e_1>she was a famous ballerina , with worldwide fame.<e_2><e_3><extra_id_0><e_4><e_5>their married life was blissful for many years.<e_99>then she caught him indulging in indiscretion with a supermodel.<e_7>she used his razor to forever change his ways.<s>",
        answer="<extra_id_0>he was a handsome devil , who gave her his last name.<sep>",
        thought="We need to find a sentence that contains the plot points 'last name' and 'handsome devil' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>21st birthday<e_1>first time drinking alcoholic beverages<e_2>one shot<e_3>barely able<e_4>two staggered<e_5>hen yard<e_6>next day<e_7>found passed</s><s><e_0><extra_id_0><e_1>this was [NEUTRAL] 's first time drinking alcoholic beverages.<e_2>[NEUTRAL] was fine with one shot but [NEUTRAL] dared her to drink more.<e_3><e_4>barely able to stand , the two staggered to [NEUTRAL] 's car.<e_5><e_6><e_7>the two were found passed out and stuck in a hen yard the next day.<s>",
        answer="<extra_id_0>[NEUTRAL] and [NEUTRAL] went out to celebrate [NEUTRAL] 's 21st birthday.<sep>",
        thought="We need to find a sentence that contains the plot point '21st birthday' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>yard sales<e_1>yard sales every weekend<e_2>neighbor got jealous<e_3>neighbor started<e_4>make things better<e_5>two eventually became good friends</s><s><e_0><e_1>[FEMALE] had yard sales every weekend and was very proud of herself.<e_2>her neighbor got jealous of all the money she was making.<e_0><e_3><extra_id_0><e_4>[FEMALE] was upset at first but thought of a way to make things better.<e_5>the two eventually became good friends because of the rivalry.<s>",
        answer="<extra_id_0>[FEMALE] 's neighbor started having yard sales too.<sep>",
        thought="We need to find a sentence that contains the plot point 'yard sales' and 'neighbor started'  while fitting in the story.",
    ),
    Example(
        question="</s><e_0>white feather<e_1>earthly idea<e_2>saw none<e_3>looked around<e_4>NONE<e_5>feather duster</s><s><e_0>[FEMALE] noticed a white feather on the floor.<e_1>she had no earthly idea how it 'd gotten there.<e_2><e_3><extra_id_0><e_99>then it dawned on her and [FEMALE] laughed.<e_5>it 'd come from her feather duster !.<s>",
        answer="<extra_id_0>she looked around for a bird but saw none.<sep>",
        thought="We need to find a sentence that contains the plot point 'looked around' and 'saw none' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>NONE<e_1>new school<e_2>new people<e_3>cousin introduced<e_4>made new friends quickly</s><s><e_99>[NEUTRAL] was new at her school.<e_1><extra_id_0><e_99>[NEUTRAL] had lunch with her cousin.<e_2><e_3>[NEUTRAL] 's cousin introduced her to new people.<e_4>[NEUTRAL] made new friends quickly.<s>",
        answer="<extra_id_0>she had a cousin that attended her new school.<sep>",
        thought="We need to find a sentence that contains the plot point 'new school' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>new important project<e_1>really hoping<e_2>NONE<e_3>boss said<e_4>boss called<e_5>new position</s><s><e_0><e_1>[MALE] was really hoping to work on a new important project.<e_99>[MALE] asked his boss about the opportunity.<e_3>his boss said he 'd think about it.<e_4>after a week , [MALE] 's boss called him into his office.<e_5><extra_id_0><s>",
        answer="<extra_id_0>[MALE] got the new position !.<sep>",
        thought="We need to find a sentence that contains the plot point 'new position' while fitting in the story.",
    ),
]


art = [
    Example(
        question="</s><e_0>marketing firm<e_1>riley worked extremely hard<e_2>campaign launched according<e_3>sold record numbers</s><s><e_0><extra_id_0><e_1>Riley worked extremely hard at her job.<e_2><e_3>The campaign launched according to plan and they sold record numbers.<s>",
        answer="<extra_id_0>Riley was the head of a marketing firm.<sep>",
        thought="We need to find a sentence that contains the plot point 'marketing firm' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>NONE<e_1>bobby spilled</s><s><e_99>Bobby was riding in the car with his parents.<e_99>They went to a drive through restaurant for lunch.<e_1><extra_id_0><s>",
        answer="<extra_id_0>But when they handed it to him, Bobby spilled it everywhere!.<sep>",
        thought="We need to find a sentence that contains the plot point 'bobby spilled' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>nepal hunting<e_1>abominable snowman<e_2>khalid heard<e_3>terrifying roar<e_4>khalid took</s><s><e_0><e_1>Khalid was in Nepal hunting for the Abominable Snowman.<e_2><e_3>Khalid heard a terrifying roar.<e_4><extra_id_0><s>",
        answer="<extra_id_0>Khalid took off running, deciding he didn't want to see the monster.<sep>",
        thought="We need to find a sentence that contains the plot point 'khalid took' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>NONE<e_1>ashley picked<e_2>reviews suggested</s><s><e_99>Ashley was watching a movie with her friend.<e_1>Ashley picked out the movie.<e_2><extra_id_0><s>",
        answer="<extra_id_0>It had been as good as the reviews suggested.<sep>",
        thought="We need to find a sentence that contains the plot point 'reviews suggested' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>new york<e_1>accept cards<e_2>carry around</s><s><e_0>I was driving to New York for a vacation.<e_1>some stores didn't accept cards.<e_2><extra_id_0><s>",
        answer="<extra_id_0>I had to carry around a lot of cash, but I enjoyed myself.<sep>",
        thought="We need to find a sentence that contains the plot point 'carry around' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>first dog<e_1>lucky chased<e_2>one day<e_3>never found</s><s><e_0><extra_id_0><e_1><e_2>one day, Lucky chased a car down the street and disappeared.<e_3>We never found him.<s>",
        answer="<extra_id_0>Lucky was my first dog.<sep>",
        thought="We need to find a sentence that contains the plot point 'first dog' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>public library<e_1>karen worked<e_2>people started<e_3>cause problems<e_4>NONE</s><s><e_0><e_1>Karen worked at a public library.<e_2><e_3><extra_id_0><e_99>After talking to her manager, she was able to get them banned.<s>",
        answer="<extra_id_0>Some people started to cause problems during her shift.<sep>",
        thought="We need to find a sentence that contains the plot points 'people started' and 'cause problems' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>gorgeous sunny morning<e_1>tara decided<e_2>way back home due</s><s><e_0>It was a gorgeous sunny morning.<e_1><extra_id_0><e_2>Tara had to walk all the way back home due to the pain.<s>",
        answer="<extra_id_0>Tara decided to ride her bike but fell off.<sep>",
        thought="We need to find a sentence that contains the plot point 'tara decided' while fitting in the story.",
    ),
]



wikiplots = [
    Example(
        question="</s><e_0>cowboy named fenimore fillmore<e_1>dying peddler gives fenimore<e_2>fenimore fillmore must battle<e_3>perfidious colonel leconte<e_4>puzzles involves fabricating bootleg whiskey<e_5>game elements emulate spaghetti westerns<e_6>caricature american wild west themes</s><s><e_0>The game begins in 1866 Arizona when the game's hero, a cowboy named Fenimore Fillmore, tries to rescue an old peddler from a band of attacking rustlers.<e_1><extra_id_0><e_2><e_3>To reach his goal, Fenimore Fillmore must battle the evil Friar Anselmo and the perfidious Colonel Leconte (who also seek the treasure), fight fierce Apaches (whose Chief's son's tepee boasts a sheepskin from Harvard), engage Mexican revolutionaries (whose leader is amnesic), outwit witty French soldiers (federated with Emperor Maximilian of Mexico), and suffer the insufferable alcohol-prohibition-ladies league.<e_4>Solving the puzzles involves fabricating bootleg whiskey, blowing up a bank's safe, escaping from prison, rescuing a pianist from a well, locating and flying a balloon, and turning a devout monk into a gallant rebel general.<e_5><e_6>The game elements emulate Spaghetti Westerns and caricature American Wild West themes.<s>",
        answer="<extra_id_0>The dying peddler gives Fenimore a golden skull and tells him the legend of a treasure that can be found by collecting two other golden skulls.<sep>",
        thought="We need to find a sentence that contains the plot point 'dying peddler gives fenimore' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>new york city police department<e_1>young musician named sally<e_2>mugger named rabbit<e_3>unarmed rabbit anyway<e_4>make lacy seem like<e_5>NONE</s><s><e_0>Officer Lacy is an 18-year veteran of the New York City Police Department who finds himself demoted from detective back to patrol duty for his violent tendencies and trigger-happy behavior.<e_1><e_2><extra_id_0><e_3>Rabbit has Sally at knifepoint in a hostage standoff but is persuaded to release her and surrender by Officer Lacy, who kills the unarmed Rabbit anyway.<e_4>A grateful Sally is convinced by Lacy to lie to detectives to make Lacy seem like a hero.<e_99>She later changes her mind and tells the truth about the shooting.<e_99>This drives Lacy to try to silence Sally with escalating threats and violence before his career is ruined and he is tried for Rabbit's murder.<s>",
        answer="<extra_id_0>Responding to a call on Manhattan's West Side, he finds a young musician named Sally has been abducted by a mugger named Rabbit.<sep>",
        thought="We need to find a sentence that contains plot points 'young musician named sally' and 'mugger named rabbit' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>two close friends<e_1>marry someone else<e_2>current boyfriends<e_3>NONE</s><s><e_0><e_1><e_2><extra_id_0><e_99>Shortly thereafter, Madhu is introduced to Chandrakant, whom she likes, and soon both are married.<e_99>On their honeymoon, she meets with Neelu, who has married Deepak, also her parents' choice.<e_99>Both are delighted to see other, and cannot wait to meet the others' spouse, little realizing the shock they will get when they do so.<s>",
        answer="<extra_id_0>Two close friends, Neelu and Madhu, agree that men cannot be trusted, and as such decide to dump their current boyfriends, and marry someone else who meets with the approval of their parents.<sep>",
        thought="We need to find a sentence that contains plot points 'two close friends', marry someone else, and 'current boyfriends' while fitting in the story.",
    ),
    Example(
    question="</s><e_0>NONE<e_1>however one day<e_2>everyday life unbearable<e_3>afraid manato wavers<e_4>receive blue love letters</s><s><e_99>At some point, Manato Irie (Hideaki Takizawa) began to withdraw himself from the world.<e_99>Even when picked on, it's not the real Irie, but an act.<e_1>However one day he meets a strange girl - Yui Misawa (Kyoko Fukada).<e_2><extra_id_0><e_3>Alone and afraid Manato wavers but finds himself drawn to her.<e_99>But his feelings for Yui are doomed to be unrequited, when he discovers that Yui is none other than his new step sister.<e_4>While he struggles with his feelings for Yui, Manato begins to receive blue love letters in his shoe locker at school.<e_99>He eventually discovers that they were left there by his next-door neighbour, Haruka (Uchiyama Rina).<e_99>Meanwhile, Yui finds herself falling for senpai Saeki(Y\u00c5\u008dsuke Kubozuka), who in turn is having an affair with his teacher, Asami-sensei (Ishida Yuriko).<s>",
    answer="<extra_id_0>Yui, who finds the tedium of everyday life unbearable, teases Manato with her almost too upfront and honest manner.<sep>",
    thought="We need to find a sentence that contains plot point 'everyday life unbearable' while fitting in the story.",
),

Example(
    question="</s><e_0>NONE<e_1>several chapters long<e_2>retrieve sacred scriptures<e_3>behaviour may accord<e_4>young monk tripitaka volunteers<e_5>monkey thereafter recruit pigsy<e_6>fight fierce monsters<e_7>meet several bodhisattvas</s><s><e_99>Journey to the West may be roughly divided into three parts: first, the introduction including the origin of Monkey (Sun Wukong), Tripitaka (Tang Sanzang), Pigsy (Zhu Bajie), and Sandy (Sha Wujing); second, the actual journey to the west, which has an episodic nature; and last, the ending, telling what happens when the pilgrims reach their destination.<e_1>Waley chose to translate the entirety of the introductory and ending chapters, as well as three episodes, each several chapters long, of the journey to the west.<e_99>At the outset of the novel, the Buddha seeks a pilgrim who will travel to India.<e_2><e_3>The hope is to retrieve sacred scriptures by which the Chinese people may be enlightened so that their behaviour may accord with the tenets of Buddhism.<e_4>The young monk Tripitaka volunteers to undertake the pilgrimage.<e_99>Along the way, he encounters and frees the Monkey King.<e_5>He and Monkey thereafter recruit Pigsy and Sandy.<e_99>They liberate a captive princess and punish her abductor, who has also murdered her father.<e_99>The father is resurrected and reinstalled as king.<e_6><e_7><extra_id_0><s>",
    answer="<extra_id_0>They meet several bodhisattvas and fight fierce monsters, before finally arriving at Buddha's palace.<sep>",
    thought="We need to find a sentence that contains plot points 'fight fierce monsters' and 'meet several bodhisattvas' while fitting in the story.",
)
]

enc = [
    Example(
        question="</s><e_0>replied<e_1>turned</s><s><e_0>Carrie replied with more breath than sound .<e_1><extra_id_0><s>",
        answer="<extra_id_0>Cringing at the sound , she turned to see the two old Hubbard men standing over her son .<sep>",
        thought="We need to find a sentence that contains plot point 'turned' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>stiffened<e_1>got<e_2>ordered<e_3>taught<e_4>do<e_5>recalled</s><s><e_0>He stiffened as he recalled doing those moves onto a guard unarmed with no weapon as ordered by the Queen .<e_1>He recalled fully that the Queen got him into the courtyard leading to the maze .<e_2>Tom continued to recall this kept on for days till the Queen ordered him to demonstrate using a fake air invisible opponent for the movements .<e_3>He recalled being taught combative art moves by the Queen 's guards after he reached his full grown height .<e_4>Tom kept recalling that he kept up the combative art moves over and over from time to time when it was appropriate for him to do them even while in the courtyard sometimes watched by the Queen and sometimes her guards .<e_5><extra_id_0><s>",
        answer="<extra_id_0>He recalled ignoring the Queen telling him off on not to do the trashing .<sep>",
        thought="We need to find a sentence that contains plot point 'recalled' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>pleased<e_1>adjust</s><s><e_0>Highfield nodded in acknowledgement , pleased that he was already back to work .<e_1><extra_id_0><s>",
        answer="<extra_id_0>Not all of the lights were illuminated , and it took Highfield a couple of minutes to adjust to the gloom .<sep>",
        thought="We need to find a sentence that contains plot point 'adjust' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>fell<e_1>saw</s><s><e_0><extra_id_0><e_1>As he approached , the kid saw him and made a run for it .<s>",
        answer="<extra_id_0>As he ran , the kid 's cellphone fell from his pocket .<sep>",
        thought="We need to find a sentence that contains plot point 'fell' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>stood<e_1>rile<e_2>sent<e_3>stare<e_4>stared<e_5>take</s><s><e_0><extra_id_0><e_1>The rage of true form seemed to rile with blood lust every time I stuck the giant .<e_2>Calling forth all the anger and blood lust in me , I raised the sword high and sent it down at the giant 's neck .<e_3>I turned to stare at Lilith who seemed shaken at the fact I 'd taken out one of her giant 's as well .<e_4>A few of The Rogue stopped their fighting and stared over at the dead giant .<e_5>The blood loss was beginning to take its toll as the giant stumbled around .<s>",
        answer="<extra_id_0>I stood on the giant 's body as it fell to the floor not once falling over .<sep>",
        thought="We need to find a sentence that contains plot point 'stood' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>stare<e_1>seeing<e_2>laid<e_3>holding<e_4>making<e_5>rubbing<e_6>felt<e_7>adjusted<e_8>sensing<e_9>spilled</s><s><e_0>He felt Thura adjust her position to stare at him in the face .<e_1>He opened his eyes with shock running through him seeing Thura was asleep with part of her growing swollen .<e_2>He did n't comment a response went to the bed and laid his form down while staring at Thura .<e_3>Tom picked up the baby seeing it was a girl and held her close to him while holding Thura close to him with another arm around her .<e_4>He shut his eyes feeling Thura 's touch making him more alive again from the feeling of her .<e_5>Tom brought his hands to Thura 's face gently rubbing her cheeks and running hands through her hair .<e_6><extra_id_0><e_7>Tom eyed Thura who adjusted her position to have her face level with his .<e_8>He sighed as Thura broke off the kiss to lie on top of while sensing her form still .<e_9>Tom gave off a moan as he spilled himself inside Thura .<s>",
        answer="<extra_id_0>He felt Thura put hands on his shoulders followed by gasping as he found his sensitive part inside her .<sep>",
        thought="We need to find a sentence that contains plot point 'felt' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>start<e_1>played</s><s><e_0>They actually begged me to start keeping him home so he 'd stop f**king with them .<e_1><extra_id_0><s>",
        answer="<extra_id_0>And when the team was home , he played pranks on all the guys during the games .<sep>",
        thought="We need to find a sentence that contains plot point 'played' while fitting in the story.",
    ),
    Example(
        question="</s><e_0>watching<e_1>stared<e_2>started<e_3>were<e_4>saw</s><s><e_0>Jase was too busy watching what Luis was doing to notice Luis was watching him .<e_1>The few times he did catch Luis watching him , he stared down at the naked women fast , as if he were afraid to let Luis know what he really needed .<e_2><extra_id_0><e_3>The few times Luis did look at Jase , he caught Jase staring at the way Luis 's legs were spread .<e_4>Luis saw the way Jase pursed his lips when Luis shoved his middle finger into his ass and moved it around .<s>",
        answer="<extra_id_0>And Luis noticed how Jase started to pound his fist harder when he watched Luis sink down into the covers and twist his naked body sideways .<sep>",
        thought="We need a sentence that contains plot point 'started' while fitting in the story",
    ),
]

scifi = [
Example(
    question= "</s><e_0>Odo, Kira, and <OBJECT>1 arrive to meet <PRP>.<e_1><PRP> is honored that <PRP> remained behind.<e_2><PERSON>12 tells <PERSON>8.<e_3><PERSON>2 has removed all of <PRP> Synset('personal.a.03') Synset('signal.n.01').<e_4><PRP> will return to reclaim Synset('geological_formation.n.01') Synset('written_symbol.n.01').</s><s><e_0>Odo, Kira, and Quark arrive to meet them.<e_1>He is honored that he remained behind.<e_2>Weyoun tells Odo.<e_3>Sisko has removed all of his personal items.<e_4><extra_id_0><s>",
    answer= "<extra_id_0>He will return to reclaim Deep Space.<sep>",
    thought="We need a sentence with 'Synset('geological_formation.n.01') Synset('written_symbol.n.01')' while fitting in the story"
),
Example(
    question= "</s><e_0>in a jealous rage, <PERSON>0 throws Seymour's fossilized Synset('chamber.n.01') into the Synset('igneous_rock.n.01') Synset('device.n.01') in the Synset('supporting_structure.n.01').<e_1>because <PERSON>2 was made of Dolomite, <PRP> might survive the Synset('hot.a.03') Synset('igneous_rock.n.01').<e_2><PERSON>4 reveals.<e_3>Bender, feeling <MISC>1 and being <NUMBER>1 <PERCENT>0 dolomite, decides to go after the <LOCATION>1 Synset('restraint.n.06').<e_4>after a long while, <PERSON>0 resurfaces with <PERSON>2 intact.</s><s><e_0>In a jealous rage, Bender throws Seymour's fossilized body into the lava pit in the basement.<e_1><extra_id_0><e_2>Hubert reveals.<e_3>Bender, feeling remorseful and being 40 % dolomite, decides to go after the dolomite dog.<e_4>After a long while, Bender resurfaces with Seymour intact.<s>",
    answer= "<extra_id_0>Because Seymour was made of Dolomite, he might survive the hot lava.<sep>",
    thought="We need a sentence with 'Synset('hot.a.03') Synset('igneous_rock.n.01')' while fitting in the story"
),
Example(
    question= "</s><e_0>Synset('owen.n.02') asks what will happen to <PRP>.<e_1><PERSON>10 resists explaining at <ORDINAL>0.<e_2><PRP> needs to know.<e_3>Synset('owen.n.02') begs <PRP> to say <PRP>.<e_4>the Synset('social_group.n.01') where Synset('owen.n.02') is locked inside is a Synset('instrumentality.n.03') Synset('area.n.05') which will Synset('source_of_illumination.n.01') with irradiated <OBJECT>1.</s><s><e_0>Owen asks what will happen to him.<e_1><extra_id_0><e_2>He needs to know.<e_3>Owen begs her to say it.<e_4>The room where Owen is locked inside is a containment chamber which will flood with irradiated coolant.<s>",
    answer= "<extra_id_0>Tosh resists explaining at first.<sep>",
    thought="We need a sentence with 'resists explaining' while fitting in the story"
),
Example(
    question= "</s><e_0><PRP> has only one living Synset('relative.a.01') in this Synset('datum.n.01') Synset('concept.n.01').<e_1>after an encounter/examination with the Probulator, a Synset('compound.n.02') scan reveals.<e_2>with <PRP> Synset('second.a.02') Synset('abstraction.n.06') he's going to make the Synset('most.a.02') of <PRP> Synset('record.n.01') and not Synset('condition.n.01') Synset('entity.n.01') up again.<e_3><PERSON>0 starts to make <PRP> a Synset('message.n.02').<e_4><PERSON>6 reveals she's found <PRP> Synset('permanent.a.01') Synset('motion.n.06') Synset('possession.n.02').</s><s><e_0>He has only one living relative in this time period.<e_1><extra_id_0><e_2>With his second chance he's going to make the most of his life and not mess things up again.<e_3>Fry starts to make himself a promise.<e_4>Leela reveals she's found him his permanent career assignment.<s>",
    answer= "<extra_id_0>After an encounter/examination with the Probulator, a DNA scan reveals.<sep>",
    thought="We need a sentence with 'an encounter/examination with the Probulator, a Synset('compound.n.02') scan' while fitting in the story"
),
Example(
    question= "</s><e_0>after <PERSON>0 agrees on a Synset('group.n.01') with <PRP>.<e_1><PRP> refuses to co-operate.<e_2><PERSON>8 agrees to help <PERSON>0 track the Replicator, against Poole's Synset('option.n.02').<e_3><PERSON>0 and <LOCATION>0 then meet with <PERSON>10 Bates, who was honorably discharged from the <ORGANIZATION>6 Corps, and <DATE>0 works for the <ORGANIZATION>7.<e_4>next <PRP> see <PERSON>11 Lee, who was interrupted from <PRP> <ORDINAL>0 Synset('time_off.n.01') in <DURATION>1.</s><s><e_0>After Sheppard agrees on a deal with him.<e_1><extra_id_0><e_2>Ava agrees to help Sheppard track the Replicator, against Poole's wishes.<e_3>Sheppard and Ronon then meet with Agent Bates, who was honorably discharged from the Marine Corps, and now works for the IOA Field Operations Division.<e_4>Next they see Dr Bill Lee, who was interrupted from his first vacation in three years.<s>",
    answer= "<extra_id_0>He refuses to co-operate.<sep>",
    thought="We need a sentence with 'refuses to co-operate' while fitting in the story"
),
Example(
    question= "</s><e_0><PERSON>18 Synset('speech_act.n.01') and says.<e_1>Apgar, though, feels compelled to protect <PRP> Synset('physical_phenomenon.n.01').<e_2><PRP> agrees and decides to contact the Synset('power.n.01').<e_3><PERSON>1 tells <PRP> not to -- <PRP> will take Synset('activity.n.01') of <PERSON>6 <PRP>.<e_4>the Synset('hypothesis.n.02') stops.</s><s><e_0>Tayna protests and says.<e_1>Apgar, though, feels compelled to protect their work.<e_2>She agrees and decides to contact the authorities.<e_3>Apgar tells her not to -- he will take care of Riker himself.<e_4><extra_id_0><s>",
    answer= "<extra_id_0>The simulation stops.<sep>",
    thought="We need a sentence with 'The Synset('hypothesis.n.02') stops' while fitting in the story"
)]




plot_generation_task_id_to_prompt = {
    "roc_stream": roc,
    "art_stream": art,
    "wikiplots_stream": wikiplots,
    "enc_stream": enc,
    "scifi_stream": scifi,
}

