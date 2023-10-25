from prompt_lib.prompts.example import Example

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
        question="υ , 𝛿 , ζ , φ , π , γ , ς , ε , χ",
        thought="ς < φ < γ < 𝛿 < ζ < χ < ε < π < υ",
        answer="ς, , φ , γ , 𝛿 , ζ , χ , ε , π , υ",
    ),
    Example(
        question="ν , ι , λ , ζ , ξ , γ , ψ , π",
        thought="ξ < ζ < λ < π < ψ < γ < ι < ν",
        answer="ξ , ζ , λ , π , ψ , γ , ι , ν",
    ),
    Example(
        question="ξ , τ , φ , θ , ζ , η , ι , 𝛿",
        thought="ξ < η < θ < φ < ζ < 𝛿 < ι < τ",
        answer="ξ , η , θ , φ , ζ , 𝛿 , ι , τ",
    ),
    Example(
        question="ζ , π , β , σ , φ , ε , λ , ρ",
        thought="ε < ζ < π < λ < φ < β < ρ < σ",
        answer="ε , ζ , π , λ , φ , β , ρ , σ",
    ),
    Example(
        question="ω , ρ , 𝛿 , ι , υ , ν",
        thought="ω < ρ < ν < 𝛿 < ι < υ",
        answer="ω , ρ , ν , 𝛿 , ι , υ",
    ),
    Example(
        question="μ , ζ , π , χ , λ , ς, , α , γ",
        thought="ς, < π < γ < λ < ζ < χ < μ < α",
        answer="ς, , π , γ , λ , ζ , χ , μ , α",
    ),
    Example(
        question="τ , γ , λ , μ , α , ς, , κ",
        thought="μ < λ < α < τ < κ < γ < ς",
        answer="μ , λ , α , τ , κ , γ , ς",
    ),
    Example(
        question="κ , ξ , ν , 𝛿",
        thought="κ < ξ < 𝛿 < ν",
        answer="κ , ξ , 𝛿 , ν",
    ),
]


symbolic_alpha_first = [
    Example(
        question="υ , 𝛿 , ζ , φ , π , γ , α , ε , χ",
        thought="α < φ < γ < 𝛿 < ζ < χ < ε < π < υ",
        answer="α , φ , γ , 𝛿 , ζ , χ , ε , π , υ",
    ),
    Example(
        question="ν , ι , λ , ζ , α , γ , ψ , π",
        thought="α < ζ < λ < π < ψ < γ < ι < ν",
        answer="α , ζ , λ , π , ψ , γ , ι , ν",
    ),
    Example(
        question="φ , τ , α , θ , ζ , η , ι , 𝛿",
        thought="α < η < θ < φ < ζ < 𝛿 < ι < τ",
        answer="α , η , θ , φ , ζ , 𝛿 , ι , τ",
    ),
    Example(
        question="ζ , π , β , σ , φ , α , λ , ρ",
        thought="α < ζ < π < λ < φ < β < ρ < σ",
        answer="α , ζ , π , λ , φ , β , ρ , σ",
    ),
    Example(
        question="υ , ρ , 𝛿 , ι , α , ν",
        thought="α < ρ < ν < 𝛿 < ι < υ",
        answer="α , ρ , ν , 𝛿 , ι , υ",
    ),
    Example(
        question="μ , ζ , π , χ , λ , ς , α , γ",
        thought="α < π < γ < λ < ζ < χ < μ < ς",
        answer="α , π , γ , λ , ζ , χ , μ , ς",
    ),
    Example(
        question="τ , γ , λ , μ , α , ς , κ",
        thought="α < λ < μ < τ < κ < γ < ς",
        answer="α , λ , μ , τ , κ , γ , ς",
    ),
    Example(
        question="ν , ξ , κ , 𝛿",
        thought="α < ξ < 𝛿 < ν",
        answer="α , ξ , 𝛿 , ν",
    ),
]

symbolic_sometimes_beta_first = [
    Example(
        question="υ , 𝛿 , ζ , φ , π , γ , β , ε , χ",
        thought="β < φ < γ < 𝛿 < ζ < χ < ε < π < υ",
        answer="β , φ , γ , 𝛿 , ζ , χ , ε , π , υ",
    ),
    Example(
        question="ν , ι , λ , ζ , β , γ , ψ , π",
        thought="β < ζ < λ < π < ψ < γ < ι < ν",
        answer="β , ζ , λ , π , ψ , γ , ι , ν",
    ),
    Example(
        question="φ , τ , β , θ , ζ , η , ι , 𝛿",
        thought="β < η < θ < φ < ζ < 𝛿 < ι < τ",
        answer="β , η , θ , φ , ζ , 𝛿 , ι , τ",
    ),
    Example(
        question="ζ , π , β , σ , φ , α , λ , ρ",
        thought="α < ζ < π < λ < φ < β < ρ < σ",
        answer="α , ζ , π , λ , φ , β , ρ , σ",
    ),
    Example(
        question="υ , ρ , 𝛿 , ι , α , ν",
        thought="α < ρ < ν < 𝛿 < ι < υ",
        answer="α , ρ , ν , 𝛿 , ι , υ",
    ),
    Example(
        question="μ , ζ , π , χ , λ , ς , β , γ",
        thought="β < π < γ < λ < ζ < χ < μ < ς",
        answer="β , π , γ , λ , ζ , χ , μ , ς",
    ),
    Example(
        question="τ , γ , λ , μ , α , ς , κ",
        thought="α < λ < μ < τ < κ < γ < ς",
        answer="α , λ , μ , τ , κ , γ , ς",
    ),
    Example(
        question="ν , ξ , κ , 𝛿",
        thought="α < ξ < 𝛿 < ν",
        answer="α , ξ , 𝛿 , ν",
    ),
]

no_pattern = [
    Example(
        question="72 , 85 , 48 , 11 , 23 , 95 , 34 , 63 , 56",
        thought="11 < 23 < 34 < 48 < 56 < 63 < 72 < 85 < 95",
        answer="11 , 23 , 34 , 48 , 56 , 63 , 72 , 85 , 95",
    ),
    Example(
        question="ν , ι , λ , ζ , ξ , γ , ψ , π",
        thought="ξ < ζ < λ < π < ψ < γ < ι < ν",
        answer="ξ , ζ , λ , π , ψ , γ , ι , ν",
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

symbolic_sorted = [
    Example(
        question="υ , 𝛿 , ζ , φ , π , γ , ς , ε , χ",
        thought="ε < ζ < γ < 𝛿 < π < φ < ς < χ < υ",
        answer="ε , ζ , γ , 𝛿 , π , φ , ς , χ , υ"
    ),
    Example(
        question="ν , ι , λ , ζ , ξ , γ , ψ , π",
        thought="γ < ζ < ξ < ι < λ < π < ψ < ν",
        answer="γ , ζ , ξ , ι , λ , π , ψ , ν"
    ),
    Example(
        question="ξ , τ , φ , θ , ζ , η , ι , 𝛿",
        thought="ζ < 𝛿 < η < θ < ι < ξ < φ < τ",
        answer="ζ , 𝛿 , η , θ , ι , ξ , φ , τ"
    ),
    Example(
        question="ζ , π , β , σ , φ , ε , λ , ρ",
        thought="ε < ζ < λ < π < φ < β < ρ < σ",
        answer="ε , ζ , λ , π , φ , β , ρ , σ"
    ),
    Example(
        question="ω , ρ , 𝛿 , ι , υ , ν",
        thought="ω < ρ < ν < 𝛿 < ι < υ",
        answer="ω , ρ , ν , 𝛿 , ι , υ"
    ),
    Example(
        question="μ , ζ , π , χ , λ , ς, , α , γ",
        thought="α < γ < ζ < λ < π < ς < χ < μ",
        answer="α , γ , ζ , λ , π , ς , χ , μ"
    ),
    Example(
        question="τ , γ , λ , μ , α , ς, , κ",
        thought="α < γ < λ < μ < τ < κ < ς",
        answer="α , γ , λ , μ , τ , κ , ς"
    ),
    Example(
        question="κ , ξ , ν , 𝛿",
        thought="κ < ξ < 𝛿 < ν",
        answer="κ , ξ , 𝛿 , ν"
    ),
]


sorting_task_id_to_prompt = {
    "sorting_stream": sorting_examples,
    "sorting_direct": sorting_examples,
    "sorting_pat_none": no_pattern,
    "sorting_pat_wrong": wrong_2,
    "sorting_symb_abs": symbolic_alpha_first,
    "sorting_symb_ood": ood,
    "sorting_verbose": verbose,
    "sorting_symbolic_sorted": symbolic_sorted,

}