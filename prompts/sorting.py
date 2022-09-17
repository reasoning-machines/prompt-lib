from prompts.example import Example

sorting_examples = [
    Example(
        question="7 , 8 , 4 , 1 , 2 , 9 , 3 , 6 , 5",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9",
    ),
    Example(
        question="5 , 9 , 3 , 1 , 8 , 4 , 6 , 2",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 8 < 9",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 8 , 9",
    ),
    Example(
        question="6 , 5 , 7 , 4 , 3 , 2 , 8 , 1",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="1 , 6 , 4 , 8 , 5 , 3 , 7 , 2",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="5 , 2 , 1 , 4 , 3 , 7",
        thought="1 < 2 < 3 < 4 < 5 < 7",
        answer="1 , 2 , 3 , 4 , 5 , 7",
    ),
    Example(
        question="3 , 8 , 2 , 5 , 6 , 4 , 7 , 1",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="8 , 6 , 1 , 2 , 9 , 7 , 4",
        thought="1 < 2 < 4 < 6 < 7 < 8 < 9",
        answer="1 , 2 , 4 , 6 , 7 , 8 , 9",
    ),
    Example(question="7 , 6 , 8 , 1", thought="1 < 6 < 7 < 8", answer="1 , 6 , 7 , 8"),
]


ood = [
    Example(
        question="72 , 85 , 48 , 11 , 23 , 95 , 34 , 63 , 56",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85 < 95",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85 , 95",
    ),
    Example(
        question="56 , 95 , 34 , 11 , 85 , 48 , 63 , 23",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 85 < 95",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 85 , 95",
    ),
    Example(
        question="63 , 56 , 72 , 48 , 34 , 23 , 85 , 11",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85",
    ),
    Example(
        question="11 , 63 , 48 , 85 , 56 , 34 , 72 , 23",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85",
    ),
    Example(
        question="56 , 23 , 11 , 48 , 34 , 72",
        thought="11 < 23 < 34 < 48 < 56 < 72",
        answer="11 , 23 , 34 , 48 , 56 , 72",
    ),
    Example(
        question="34 , 85 , 23 , 56 , 63 , 48 , 72 , 11",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85",
    ),
    Example(
        question="85 , 63 , 11 , 23 , 95 , 72 , 48",
        thought="11 < 23 < 48 < 63 < 72 < 85 < 95",
        answer="11 , 23 , 48 , 63 , 72 , 85 , 95",
    ),
    Example(question="72 , 63 , 85 , 11", thought="11 < 63 < 72 < 85", answer="11 , 63 , 72 , 85"),
]

wrong_2 = [
    Example(
        question="7 , 8 , 4 , 1 , 2 , 9 , 3 , 6 , 5",
        thought="1 < 2 < 3 < 4 < 7 < 6 < 5 < 8 < 9",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9",
    ),
    Example(
        question="5 , 9 , 3 , 1 , 8 , 4 , 6 , 2",
        thought="1 < 2 < 3 < 4 < 5 < 8 < 6 < 9",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 8 , 9",
    ),
    Example(
        question="6 , 5 , 7 , 4 , 3 , 2 , 8 , 1",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="1 , 6 , 4 , 8 , 5 , 3 , 7 , 2",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="5 , 2 , 1 , 4 , 3 , 7",
        thought="1 < 2 < 3 < 4 < 5 < 7",
        answer="1 , 2 , 3 , 4 , 5 , 7",
    ),
    Example(
        question="3 , 8 , 2 , 5 , 6 , 4 , 7 , 1",
        thought="6 < 2 < 3 < 4 < 5 < 1 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="8 , 6 , 1 , 2 , 9 , 7 , 4",
        thought="1 < 2 < 4 < 8 < 7 < 6 < 9",
        answer="1 , 2 , 4 , 6 , 7 , 8 , 9",
    ),
    Example(question="7 , 6 , 8 , 1", thought="8 < 6 < 7 < 1", answer="1 , 6 , 7 , 8"),
]

wrong_4 = [
    Example(
        question="7 , 8 , 4 , 1 , 2 , 9 , 3 , 6 , 5",
        thought="9 < 2 < 3 < 4 < 5 < 8 < 7 < 6 < 1",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9",
    ),
    Example(
        question="5 , 9 , 3 , 1 , 8 , 4 , 6 , 2",
        thought="4 < 1 < 3 < 2 < 5 < 6 < 8 < 9",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 8 , 9",
    ),
    Example(
        question="6 , 5 , 7 , 4 , 3 , 2 , 8 , 1",
        thought="5 < 2 < 3 < 1 < 4 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="1 , 6 , 4 , 8 , 5 , 3 , 7 , 2",
        thought="1 < 5 < 3 < 4 < 7 < 6 < 2 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="5 , 2 , 1 , 4 , 3 , 7",
        thought="1 < 7 < 2 < 4 < 3 < 5",
        answer="1 , 2 , 3 , 4 , 5 , 7",
    ),
    Example(
        question="3 , 8 , 2 , 5 , 6 , 4 , 7 , 1",
        thought="2 < 1 < 8 < 4 < 5 < 6 < 7 < 3",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="8 , 6 , 1 , 2 , 9 , 7 , 4",
        thought="1 < 2 < 4 < 9 < 6 < 8 < 7",
        answer="1 , 2 , 4 , 6 , 7 , 8 , 9",
    ),
    Example(question="7 , 6 , 8 , 1", thought="6 < 8 < 1 < 7", answer="1 , 6 , 7 , 8"),
]


symbolic = [
    Example(
        question="$upsilon$ , $delta$ , $zeta$ , $phi$ , $pi$ , $gamma$ , textvarsigma , $epsilon$ , $chi$",
        thought="textvarsigma, < $phi$ < $gamma$ < $delta$ < $zeta$ < $chi$ < $epsilon$ < $pi$ < $upsilon$",
        answer="textvarsigma, , $phi$ , $gamma$ , $delta$ , $zeta$ , $chi$ , $epsilon$ , $pi$ , $upsilon$",
    ),
    Example(
        question="$nu$ , $iota$ , $lambda$ , $zeta$ , $xi$ , $gamma$ , $psi$ , $pi$",
        thought="$xi$ < $zeta$ < $lambda$ < $pi$ < $psi$ < $gamma$ < $iota$ < $nu$",
        answer="$xi$ , $zeta$ , $lambda$ , $pi$ , $psi$ , $gamma$ , $iota$ , $nu$",
    ),
    Example(
        question="$xi$ , $tau$ , $phi$ , $theta$ , $zeta$ , $eta$ , $iota$ , $delta$",
        thought="$xi$ < $eta$ < $theta$ < $phi$ < $zeta$ < $delta$ < $iota$ < $tau$",
        answer="$xi$ , $eta$ , $theta$ , $phi$ , $zeta$ , $delta$ , $iota$ , $tau$",
    ),
    Example(
        question="$zeta$ , $pi$ , $beta$ , $sigma$ , $phi$ , $epsilon$ , $lambda$ , $o$",
        thought="$epsilon$ < $zeta$ < $pi$ < $lambda$ < $phi$ < $beta$ < $o$ < $sigma$",
        answer="$epsilon$ , $zeta$ , $pi$ , $lambda$ , $phi$ , $beta$ , $o$ , $sigma$",
    ),
    Example(
        question="$omega$ , $o$ , $delta$ , $iota$ , $upsilon$ , $nu$",
        thought="$omega$ < $o$ < $nu$ < $delta$ < $iota$ < $upsilon$",
        answer="$omega$ , $o$ , $nu$ , $delta$ , $iota$ , $upsilon$",
    ),
    Example(
        question="$mu$ , $zeta$ , $pi$ , $chi$ , $lambda$ , textvarsigma, , $alpha$ , $gamma$",
        thought="textvarsigma, < $pi$ < $gamma$ < $lambda$ < $zeta$ < $chi$ < $mu$ < $alpha$",
        answer="textvarsigma, , $pi$ , $gamma$ , $lambda$ , $zeta$ , $chi$ , $mu$ , $alpha$",
    ),
    Example(
        question="$tau$ , $gamma$ , $lambda$ , $mu$ , $alpha$ , textvarsigma, , $kappa$",
        thought="$mu$ < $lambda$ < $alpha$ < $tau$ < $kappa$ < $gamma$ < textvarsigma",
        answer="$mu$ , $lambda$ , $alpha$ , $tau$ , $kappa$ , $gamma$ , textvarsigma",
    ),
    Example(
        question="$kappa$ , $xi$ , $nu$ , $delta$",
        thought="$kappa$ < $xi$ < $delta$ < $nu$",
        answer="$kappa$ , $xi$ , $delta$ , $nu$",
    ),
]


symbolic_alpha_first = [
    Example(
        question="$upsilon$ , $delta$ , $zeta$ , $phi$ , $pi$ , $gamma$ , $alpha$ , $epsilon$ , $chi$",
        thought="$alpha$ < $phi$ < $gamma$ < $delta$ < $zeta$ < $chi$ < $epsilon$ < $pi$ < $upsilon$",
        answer="$alpha$ , $phi$ , $gamma$ , $delta$ , $zeta$ , $chi$ , $epsilon$ , $pi$ , $upsilon$",
    ),
    Example(
        question="$nu$ , $iota$ , $lambda$ , $zeta$ , $alpha$ , $gamma$ , $psi$ , $pi$",
        thought="$alpha$ < $zeta$ < $lambda$ < $pi$ < $psi$ < $gamma$ < $iota$ < $nu$",
        answer="$alpha$ , $zeta$ , $lambda$ , $pi$ , $psi$ , $gamma$ , $iota$ , $nu$",
    ),
    Example(
        question="$phi$ , $tau$ , $alpha$ , $theta$ , $zeta$ , $eta$ , $iota$ , $delta$",
        thought="$alpha$ < $eta$ < $theta$ < $phi$ < $zeta$ < $delta$ < $iota$ < $tau$",
        answer="$alpha$ , $eta$ , $theta$ , $phi$ , $zeta$ , $delta$ , $iota$ , $tau$",
    ),
    Example(
        question="$zeta$ , $pi$ , $beta$ , $sigma$ , $phi$ , $alpha$ , $lambda$ , $o$",
        thought="$alpha$ < $zeta$ < $pi$ < $lambda$ < $phi$ < $beta$ < $o$ < $sigma$",
        answer="$alpha$ , $zeta$ , $pi$ , $lambda$ , $phi$ , $beta$ , $o$ , $sigma$",
    ),
    Example(
        question="$upsilon$ , $o$ , $delta$ , $iota$ , $alpha$ , $nu$",
        thought="$alpha$ < $o$ < $nu$ < $delta$ < $iota$ < $upsilon$",
        answer="$alpha$ , $o$ , $nu$ , $delta$ , $iota$ , $upsilon$",
    ),
    Example(
        question="$mu$ , $zeta$ , $pi$ , $chi$ , $lambda$ , textvarsigma , $alpha$ , $gamma$",
        thought="$alpha$ < $pi$ < $gamma$ < $lambda$ < $zeta$ < $chi$ < $mu$ < textvarsigma",
        answer="$alpha$ , $pi$ , $gamma$ , $lambda$ , $zeta$ , $chi$ , $mu$ , textvarsigma",
    ),
    Example(
        question="$tau$ , $gamma$ , $lambda$ , $mu$ , $alpha$ , textvarsigma , $kappa$",
        thought="$alpha$ < $lambda$ < $mu$ < $tau$ < $kappa$ < $gamma$ < textvarsigma",
        answer="$alpha$ , $lambda$ , $mu$ , $tau$ , $kappa$ , $gamma$ , textvarsigma",
    ),
    Example(
        question="$nu$ , $xi$ , $kappa$ , $delta$",
        thought="$alpha$ < $xi$ < $delta$ < $nu$",
        answer="$alpha$ , $xi$ , $delta$ , $nu$",
    ),
]

symbolic_sometimes_beta_first = [
    Example(
        question="$upsilon$ , $delta$ , $zeta$ , $phi$ , $pi$ , $gamma$ , $beta$ , $epsilon$ , $chi$",
        thought="$beta$ < $phi$ < $gamma$ < $delta$ < $zeta$ < $chi$ < $epsilon$ < $pi$ < $upsilon$",
        answer="$beta$ , $phi$ , $gamma$ , $delta$ , $zeta$ , $chi$ , $epsilon$ , $pi$ , $upsilon$",
    ),
    Example(
        question="$nu$ , $iota$ , $lambda$ , $zeta$ , $beta$ , $gamma$ , $psi$ , $pi$",
        thought="$beta$ < $zeta$ < $lambda$ < $pi$ < $psi$ < $gamma$ < $iota$ < $nu$",
        answer="$beta$ , $zeta$ , $lambda$ , $pi$ , $psi$ , $gamma$ , $iota$ , $nu$",
    ),
    Example(
        question="$phi$ , $tau$ , $beta$ , $theta$ , $zeta$ , $eta$ , $iota$ , $delta$",
        thought="$beta$ < $eta$ < $theta$ < $phi$ < $zeta$ < $delta$ < $iota$ < $tau$",
        answer="$beta$ , $eta$ , $theta$ , $phi$ , $zeta$ , $delta$ , $iota$ , $tau$",
    ),
    Example(
        question="$zeta$ , $pi$ , $beta$ , $sigma$ , $phi$ , $alpha$ , $lambda$ , $o$",
        thought="$alpha$ < $zeta$ < $pi$ < $lambda$ < $phi$ < $beta$ < $o$ < $sigma$",
        answer="$alpha$ , $zeta$ , $pi$ , $lambda$ , $phi$ , $beta$ , $o$ , $sigma$",
    ),
    Example(
        question="$upsilon$ , $o$ , $delta$ , $iota$ , $alpha$ , $nu$",
        thought="$alpha$ < $o$ < $nu$ < $delta$ < $iota$ < $upsilon$",
        answer="$alpha$ , $o$ , $nu$ , $delta$ , $iota$ , $upsilon$",
    ),
    Example(
        question="$mu$ , $zeta$ , $pi$ , $chi$ , $lambda$ , textvarsigma , $beta$ , $gamma$",
        thought="$beta$ < $pi$ < $gamma$ < $lambda$ < $zeta$ < $chi$ < $mu$ < textvarsigma",
        answer="$beta$ , $pi$ , $gamma$ , $lambda$ , $zeta$ , $chi$ , $mu$ , textvarsigma",
    ),
    Example(
        question="$tau$ , $gamma$ , $lambda$ , $mu$ , $alpha$ , textvarsigma , $kappa$",
        thought="$alpha$ < $lambda$ < $mu$ < $tau$ < $kappa$ < $gamma$ < textvarsigma",
        answer="$alpha$ , $lambda$ , $mu$ , $tau$ , $kappa$ , $gamma$ , textvarsigma",
    ),
    Example(
        question="$nu$ , $xi$ , $kappa$ , $delta$",
        thought="$alpha$ < $xi$ < $delta$ < $nu$",
        answer="$alpha$ , $xi$ , $delta$ , $nu$",
    ),
]

no_pattern = [
    Example(
        question="72 , 85 , 48 , 11 , 23 , 95 , 34 , 63 , 56",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85 < 95",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85 , 95",
    ),
    Example(
        question="$nu$ , $iota$ , $lambda$ , $zeta$ , $xi$ , $gamma$ , $psi$ , $pi$",
        thought="$xi$ < $zeta$ < $lambda$ < $pi$ < $psi$ < $gamma$ < $iota$ < $nu$",
        answer="$xi$ , $zeta$ , $lambda$ , $pi$ , $psi$ , $gamma$ , $iota$ , $nu$",
    ),
    Example(
        question="6 , 5 , 7 , 4 , 3 , 2 , 8 , 1",
        thought="8 > 7 > 6 > 5 > 4 > 3 > 2 > 1",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="1 , 6 , 4 , 8 , 5 , 3 , 7 , 2",
        thought="""def list_sort(array):\n
    return sorted(array)""",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="5 , 2 , 1 , 4 , 3 , 7",
        thought="First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 7, since 5 is less than 7.",
        answer="1 , 2 , 3 , 4 , 5 , 7",
    ),
    Example(
        question="3 , 8 , 2 , 5 , 6 , 4 , 7 , 1",
        thought="1 < 2 < 3 < 4 < 5 < 6 < 7 < 8",
        answer="1 , 2 , 3 , 4 , 5 , 6 , 7 , 8",
    ),
    Example(
        question="8 , 6 , 1 , 2 , 9 , 7 , 4",
        thought="Last number is 9. Next largest is 8, since 9 is more than 8. Next largest is 7, since 8 is more than 7. Next largest is 6, since 7 is more than 6. Next largest is 4, since 6 is more than 4. Next largest is 2, since 4 is more than 2. Next largest is 1, since 2 is more than 1.",
        answer="1 , 2 , 4 , 6 , 7 , 8 , 9",
    ),
    Example(question="7 , 6 , 8 , 1", thought="8 > 7 > 6 > 1", answer="1 , 6 , 7 , 8"),
]

verbose = [
Example(question = "7 , 8 , 4 , 1 , 2 , 9 , 3 , 6 , 5",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 6, since 5 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8. Next we have 9, since 8 is less than 9.",
    answer = "1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9"),
Example(question = "5 , 9 , 3 , 1 , 8 , 4 , 6 , 2",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 6, since 5 is less than 6. Next we have 8, since 6 is less than 8. Next we have 9, since 8 is less than 9.",
    answer = "1 , 2 , 3 , 4 , 5 , 6 , 8 , 9"),
Example(question = "6 , 5 , 7 , 4 , 3 , 2 , 8 , 1",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 6, since 5 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8.",
    answer = "1 , 2 , 3 , 4 , 5 , 6 , 7 , 8"),
Example(question = "1 , 6 , 4 , 8 , 5 , 3 , 7 , 2",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 6, since 5 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8.",
    answer = "1 , 2 , 3 , 4 , 5 , 6 , 7 , 8"),
Example(question = "5 , 2 , 1 , 4 , 3 , 7",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 7, since 5 is less than 7.",
    answer = "1 , 2 , 3 , 4 , 5 , 7"),
Example(question = "3 , 8 , 2 , 5 , 6 , 4 , 7 , 1",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 3, since 2 is less than 3. Next we have 4, since 3 is less than 4. Next we have 5, since 4 is less than 5. Next we have 6, since 5 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8.",
    answer = "1 , 2 , 3 , 4 , 5 , 6 , 7 , 8"),
Example(question = "8 , 6 , 1 , 2 , 9 , 7 , 4",
    thought = "First number is 1. Next we have 2, since 1 is less than 2. Next we have 4, since 2 is less than 4. Next we have 6, since 4 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8. Next we have 9, since 8 is less than 9.",
    answer = "1 , 2 , 4 , 6 , 7 , 8 , 9"),
Example(question = "7 , 6 , 8 , 1",
    thought = "First number is 1. Next we have 6, since 1 is less than 6. Next we have 7, since 6 is less than 7. Next we have 8, since 7 is less than 8.",
    answer = "1 , 6 , 7 , 8"),
]


sorting_task_id_to_prompt = {
    "sorting_stream": sorting_examples,
    "sorting_direct": sorting_examples,
    "sorting_pat_none": no_pattern,
    "sorting_pat_wrong": wrong_2,
    "sorting_symb_abs": symbolic_alpha_first,
    "sorting_symb_ood": ood,
    "sorting_verbose": verbose,

}