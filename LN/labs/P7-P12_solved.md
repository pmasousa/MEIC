Here are the solutions and explanations for the theoretical exercises from the provided documents.

# Solutions for Theoretical Exercises

## P7: Morphology

### I. Viterbi or your first client of the day

**1. (a) Viterbi for "will cook will"**

We build the Viterbi tables (SS = Sequence Score, BP = Back Pointer) step-by-step.
Tags = {Noun, Verb}. Probabilities are from .

- **Step 1 (t=1, word="will"):**

  - $SS(\text{Noun}, 1) = P(\text{will}|\text{N}) \times P(\text{N}|<s>) = 0.2 \times 0.7 = 0.14$
  - $BP(\text{Noun}, 1) = 0$
  - $SS(\text{Verb}, 1) = P(\text{will}|\text{V}) \times P(\text{V}|<s>) = 0.25 \times 0.3 = 0.075$
  - $BP(\text{Verb}, 1) = 0$

- **Step 2 (t=2, word="cook"):**

  - $SS(\text{Noun}, 2) = P(\text{cook}|\text{N}) \times \max( SS(\text{N},1) \times P(\text{N}|\text{N}), SS(\text{V},1) \times P(\text{N}|\text{V}) )$
    - $= 0.2 \times \max( 0.14 \times 0.2, 0.075 \times 0.4 ) = 0.2 \times \max( 0.028, 0.03 ) = 0.2 \times 0.03 = \mathbf{0.006}$
    - $BP(\text{Noun}, 2) = \text{Verb}$ (since 0.03 was the max)
  - $SS(\text{Verb}, 2) = P(\text{cook}|\text{V}) \times \max( SS(\text{N},1) \times P(\text{V}|\text{N}), SS(\text{V},1) \times P(\text{V}|\text{V}) )$
    - $= 0.1 \times \max( 0.14 \times 0.4, 0.075 \times 0.55 ) = 0.1 \times \max( 0.056, 0.04125 ) = 0.1 \times 0.056 = \mathbf{0.0056}$
    - $BP(\text{Verb}, 2) = \text{Noun}$ (since 0.056 was the max)

- **Step 3 (t=3, word="will"):**

  - $SS(\text{Noun}, 3) = P(\text{will}|\text{N}) \times \max( SS(\text{N},2) \times P(\text{N}|\text{N}), SS(\text{V},2) \times P(\text{N}|\text{V}) )$
    - $= 0.2 \times \max( 0.006 \times 0.2, 0.0056 \times 0.4 ) = 0.2 \times \max( 0.0012, 0.00224 ) = 0.2 \times 0.00224 = \mathbf{0.000448}$
    - $BP(\text{Noun}, 3) = \text{Verb}$
  - $SS(\text{Verb}, 3) = P(\text{will}|\text{V}) \times \max( SS(\text{N},2) \times P(\text{V}|\text{N}), SS(\text{V},2) \times P(\text{V}|\text{V}) )$
    - $= 0.25 \times \max( 0.006 \times 0.4, 0.0056 \times 0.55 ) = 0.25 \times \max( 0.0024, 0.00308 ) = 0.25 \times 0.00308 = \mathbf{0.00077}$
    - $BP(\text{Verb}, 3) = \text{Verb}$

- **Traceback:**

  1. The best score at $t=3$ is $SS(\text{Verb}, 3) = 0.00077$. So, $C(3) = \text{Verb}$.
  2. $C(2) = BP(\text{Verb}, 3) = \text{Verb}$.
  3. $C(1) = BP(\text{Verb}, 2) = \text{Noun}$.

- **Solution:** The most probable sequence is **Noun - Verb - Verb**.

**1. (b) Viterbi for "will cook"**

- **Explanation:** Because Viterbi uses dynamic programming, we can find the answer for this shorter sequence by stopping at $t=2$ in the tables we just built.
- **Traceback:**
  1. The best score at $t=2$ is $\max(SS(\text{N},2), SS(\text{V},2)) = \max(0.006, 0.0056) = 0.006$. So, $C(2) = \text{Noun}$.
  2. $C(1) = BP(\text{Noun}, 2) = \text{Verb}$.
- **Solution:** The most probable sequence is **Verb - Noun**.

**2. (a) Code for "YOU ARE SO STUPID"**

- **Explanation:** We use the provided SS and BP tables to find the best sequence by tracing the back-pointers (BP) from the highest-scoring state in the final column.
- **Traceback:**
  1. **Find best end state ($t=4$, "STUPID"):** The max score in the "STUPID" column is 0.0002, which is in row **2**. So, $C(4) = 2$.
  2. **Find $C(3)$:** Look at the back-pointer for $C(4)=2$. $BP(2, 4)$ is row **1**. So, $C(3) = 1$.
  3. **Find $C(2)$:** Look at the back-pointer for $C(3)=1$. $BP(1, 3)$ is row **4**. So, $C(2) = 4$.
  4. **Find $C(1)$:** Look at the back-pointer for $C(2)=4$. $BP(4, 2)$ is row **1**. So, $C(1) = 1$.
- **Solution:** The code is the sequence $C(1)-C(2)-C(3)-C(4)$, which is **1-4-1-2**.

**2. (b) Code for "YOU ARE"**

- **Explanation:** We use the same tables but stop at $t=2$ ("ARE").
- **Traceback:**
  1. **Find best end state ($t=2$, "ARE"):** The max score in the "ARE" column is 0.02, which is in row **3**. So, $C(2) = 3$.
  2. **Find $C(1)$:** Look at the back-pointer for $C(2)=3$. $BP(3, 2)$ is row **4**. So, $C(1) = 4$.
- **Solution:** The code is **4-3**.

---

### II. Morphology

**1. Practicing Morphology**

This exercise asks to associate each word formation method with one of the given words: `cat`, `criminals`, `unhappy`, `shamelessness`.

| Word Formation Method           | Word            | Explanation                                                                                                                                                                                                                                                                                     |
| :------------------------------ | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Derivation**                  | `unhappy`       | A prefix (`un-`) is added to a stem (`happy`) to change its meaning.                                                                                                                                                                                                                            |
| **Inflection**                  | `criminals`     | An inflectional suffix (`-s`) is added to the word (`criminal`) to change its grammatical number (plural) without changing its core meaning or word class.                                                                                                                                      |
| **Compounding (agglutination)** | `shamelessness` | This word is built by "gluing" multiple morphemes together: the root `shame`, the derivational suffix `-less` (to create an adjective), and the derivational suffix `-ness` (to create a noun). While technically derivation, it's the best fit for "agglutination" (gluing) among the choices. |
| **None of the above**           | `cat`           | This is a single, free morpheme (a root word) that cannot be broken down further. It is not formed by any of the other processes.                                                                                                                                                               |

---

## P9: Syntax

### 1. CKY Algorithm

First, we confirm the grammar is in Chomsky Normal Form (CNF) . It is.
Sentence: `John (w1) chased (w2) the (w3) dog (w4) and (w5) the (w6) cat (w7)`.

We build the CKY chart `chart[i, j]` for the span of words from $i$ to $j$.

- **Length 1 (Diagonal):**

  - `chart[1,1]` (John): {NP}
  - `chart[2,2]` (chased): {V}
  - `chart[3,3]` (the): {Det}
  - `chart[4,4]` (dog): {N}
  - `chart[5,5]` (and): {Conj}
  - `chart[6,6]` (the): {Det}
  - `chart[7,7]` (cat): {N}

- **Length 2:**

  - `chart[3,4]` (the dog): {NP} (from `Det N`)
  - `chart[6,7]` (the cat): {NP} (from `Det N`)
  - (All other length-2 spans are empty)

- **Length 3:**

  - `chart[2,4]` (chased the dog): {VP} (from `V` at `[2,2]` + `NP` at `[3,4]`)
  - `chart[5,7]` (and the cat): {ConjNP} (from `Conj` at `[5,5]` + `NP` at `[6,7]`)
  - (All other length-3 spans are empty)

- **Length 4:**

  - `chart[1,4]` (John chased the dog): {S} (from `NP` at `[1,1]` + `VP` at `[2,4]`)

- **Length 5:**

  - `chart[3,7]` (the dog and the cat): {NP} (from `NP` at `[3,4]` + `ConjNP` at `[5,7]`)

- **Length 6:**

  - `chart[2,7]` (chased the dog and the cat): {VP} (from `V` at `[2,2]` + `NP` at `[3,7]`)

- **Length 7:**

  - `chart[1,7]` (John chased the dog and the cat): {S} (from `NP` at `[1,1]` + `VP` at `[2,7]`)

**Solution:**

- \*\*Parse "John chased the dog and the cat"`.
- \*\*Parse "John chased the dog"`, which corresponds to this sentence.

---

### 3. Create a Simple Context Free Grammar (CFG)

Based on the sentences: "alex eats soup everyday" .

```
S   -> NP VP
VP  -> V NP
VP  -> V NP ADV
VP  -> V ADJ NP    /* for "adore salty soup" */
VP  -> V NP        /* covered by first VP rule */

/* We can simplify the VP and NP rules */
S   -> NP VP
VP  -> V NP
VP  -> V NP ADV

NP  -> N
NP  -> ADJ N

N   -> "alex" | "children" | "cats" | "soup" | "chips"
V   -> "eats" | "like" | "adore"
ADJ -> "salty"
ADV -> "everyday"
```

_A more structured grammar using POS tags as requested:_

```
S   -> NP VP
NP  -> NNP         /* alex */
NP  -> NNS         /* children, cats, chips */
NP  -> NN          /* soup */
NP  -> ADJ NN      /* salty soup */
VP  -> V NP
VP  -> V NP ADV

NNP -> "alex"
NNS -> "children" | "cats" | "chips"
NN  -> "soup"
V   -> "eats" | "like" | "adore"
ADJ -> "salty"
ADV -> "everyday"
```

_(This second grammar is more precise and still generates all sentences.)_

---

### 4. Parse Tree for "children adore soup"

Using the second grammar created above, the parse tree is:

```
          S
        /   \
       NP    VP
       |     /  \
      NNS   V    NP
       |    |    |
 "children" "adore" NN
               |
             "soup"
```

---

## P10: Semantics

### 1. Semantic Relations

This exercise asks to fill the table using the words `animal` based on their relation to "cat".

| Semantic Relation      | Word or Phrase | Explanation                                                                                                          |
| :--------------------- | :------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Hyponym of cat:**    | `domestic cat` | A hyponym is a "type-of" relation. A _domestic cat_ is a type of _cat_.                                              |
| **Meronym of cat:**    | `whisker`      | A meronym is a "part-of" relation. A _whisker_ is a part of a _cat_.                                                 |
| **Hypernym of cat:**   | `animal`       | A hypernym is a "is-a" or super-category relation. A _cat_ is an _animal_.                                           |
| **Synonym of cat:**    |                | None of the provided words are synonyms for "cat" (e.g., "feline").                                                  |
| **None of the above:** | `leopard`      | A leopard is a co-hyponym of "cat" (both are types of felines), not a direct hyponym, hypernym, meronym, or synonym. |

---

### 2. First Order Logic (Peter's sisters)

Using constant `Pedro` and predicates `sister_of(x, y)` ($y$ is a sister of $x$) :

- **(a) Peter has (at least) one sister.**
  - $\exists y \: \text{sister\_of}(\text{Pedro}, y)$
- **(b) Peter has no sister.**
  - $\neg \exists y \: \text{sister\_of}(\text{Pedro}, y)$
  - (Alternatively: $\forall y \: \neg \text{sister\_of}(\text{Pedro}, y)$)
- **(c) Peter has at most one sister.**
  - $\forall y, z \: ((\text{sister\_of}(\text{Pedro}, y) \wedge \text{sister\_of}(\text{Pedro}, z)) \rightarrow \text{equal}(y, z))$
  - (This means: "For any $y$ and $z$, if $y$ is a sister of Peter and $z$ is a sister of Peter, then $y$ and $z$ must be the same person.")
- **(d) Peter has exactly one sister.**
  - (This combines "at least one" and "at most one".)
  - $\exists y \: (\text{sister\_of}(\text{Pedro}, y) \wedge \forall z \: (\text{sister\_of}(\text{Pedro}, z) \rightarrow \text{equal}(y, z)))$
  - (This means: "There exists a person $y$ who is Peter's sister, and for any person $z$, if $z$ is Peter's sister, $z$ must be the same person as $y$.")

---

### 3. First Order Logic (Dustin's friends)

Using constants `Dustin`, `Dart` and predicates `friend(x, y)` ($y$ is a friend of $x$) :

- **(a) If Dart is a friend of Dustin, all Dustin friends like Dart.**
  - $\text{friend}(\text{Dustin}, \text{Dart}) \rightarrow (\forall x \: (\text{friend}(\text{Dustin}, x) \rightarrow \text{likes}(x, \text{Dart})))$
- **(b) There are at least two friends of Dustin that don't like Dart.**
  - $\exists x, y \: (\text{friend}(\text{Dustin}, x) \wedge \neg \text{likes}(x, \text{Dart}) \wedge \text{friend}(\text{Dustin}, y) \wedge \neg \text{likes}(y, \text{Dart}) \wedge \text{different}(x, y))$

---

### 4. Compositional Semantics ("likes a dog")

We find the meaning by combining the semantics of "likes" and "a dog" based on the grammar rules.

1. **Semantics of "a dog" (NP):**

   - $\text{DET.sem}$ ("a") = $\lambda P . \lambda Q . \exists x \: (P(x) \wedge Q(x))$ (assuming correction of typo in PDF)
   - $\text{NN.sem}$ ("dog") = $\lambda x . \text{DOG}(x)$ (treating `DOG` as a predicate)
   - $\text{NP.sem} = \text{DET.sem} @ \text{NN.sem}$
   - $\text{NP.sem} = (\lambda P . \lambda Q . \exists x \: (P(x) \wedge Q(x))) @ (\lambda x . \text{DOG}(x))$
   - (Apply P): $\lambda Q . \exists x \: ((\lambda x . \text{DOG}(x))(x) \wedge Q(x))$
   - ($\beta$-reduction): $\lambda Q . \exists x \: (\text{DOG}(x) \wedge Q(x))$
   - (This matches the provided semantics .)

2. **Semantics of "likes a dog" (VP):**

   - The rule is $VP \rightarrow V_t \: NP$. This $V_t$ expects the $\text{NP.sem}$ (which is $P$) as its argument.
   - $\text{VP.sem} = V_t\text{.sem} @ \text{NP.sem}$
   - $\text{VP.sem} = (\lambda P . \lambda x . P(\lambda y . \text{LIKES}(x, y))) @ (\lambda Q . \exists z \: (\text{DOG}(z) \wedge Q(z)))$
   - (Note: The NP's bound variable $x$ is renamed to $z$ to avoid capture by the $x$ in the verb's semantics.)
   - (Apply P): $\lambda x . (\lambda Q . \exists z \: (\text{DOG}(z) \wedge Q(z)))(\lambda y . \text{LIKES}(x, y))$
   - (Apply Q): $\lambda x . \exists z \: (\text{DOG}(z) \wedge (\lambda y . \text{LIKES}(x, y))(z))$
   - ($\beta$-reduction): $\lambda x . \exists z \: (\text{DOG}(z) \wedge \text{LIKES}(x, z))$

<!-- end list -->

- **Solution:** The meaning representation is $\lambda x . \exists z \: (\text{DOG}(z) \wedge \text{LIKES}(x, z))$, which is the property of "being an $x$ that likes a dog".

---

### Strange Days

**First Quiz: The code for "4 3 3 4 2"**

- **Explanation:** This is a semantic parsing problem. We must parse the sequence `4 3 3 4 2` and calculate the semantic value.
- **Note:** There appears to be a typo in the grammar. The sequence `4 3 3 4 2` maps to terminals $E_1 \: F_1 \: F_2 \: E_2 \: D_1$ would produce a sequence like $E F F F D$.
- We will assume the rule $C \rightarrow FF$ was a typo for $C \rightarrow FE$, which allows the grammar to parse the given sequence as $A \rightarrow (B \rightarrow E_1 F_1) (C \rightarrow F_2 E_2) (D \rightarrow D_1)$.
- We also assume the $E.sem$ in the C-rule's semantics refers to the $E.sem$ from the B-rule ($E_1.sem$).

<!-- end list -->

1. **Parse the sequence:**

   - $D \rightarrow 2$. $D.sem = 2$.
   - $C \rightarrow F E \rightarrow 3 \: 4$.
     - $F_2 \rightarrow 3$. $F_2.sem = 3$.
     - $E_2 \rightarrow 4$. $E_2.sem = 4$.
   - $B \rightarrow E F \rightarrow 4 \: 3$.
     - $E_1 \rightarrow 4$. $E_1.sem = 4$.
     - $F_1 \rightarrow 3$. $F_1.sem = 3$.

2. **Calculate Semantics (bottom-up):**

   - $B.sem = E_1.sem \times F_1.sem = 4 \times 3 = 12$.
   - $C.sem = F_2.sem + E_1.sem = 3 + 4 = 7$ (using $F.sem$ from C and $E.sem$ from B).
   - $D.sem = 2$.
   - $A.sem = (B.sem + C.sem - D.sem) \times 10 = (12 + 7 - 2) \times 10 = 17 \times 10 = 170$.

<!-- end list -->

- **Solution:** The code is **170**.

**Second Quiz: "every red cut"**

- **Explanation:** We parse the sentence "every red cut" using the lambda calculus grammar to find its logical meaning.
- **The Trick:** The grammar explicitly defines the semantics for the adjective "red" as `ADJ → red {λx.BLUE(x)}`. This means "red" logically translates to "BLUE".

<!-- end list -->

1. **Semantics of "every red" (NP):**

   - $\text{DET.sem}$ ("every") = $\lambda P . \lambda Q . \forall x \: (P(x) \rightarrow Q(x))$
   - $\text{ADJ.sem}$ ("red") = $\lambda x . \text{BLUE}(x)$
   - $\text{NP.sem} = \text{DET.sem} @ \text{ADJ.sem}$
   - $\text{NP.sem} = (\lambda P . \lambda Q . \forall x \: (P(x) \rightarrow Q(x))) @ (\lambda x . \text{BLUE}(x))$
   - (Apply P): $\lambda Q . \forall x \: ((\lambda x . \text{BLUE}(x))(x) \rightarrow Q(x))$
   - ($\beta$-reduction): $\lambda Q . \forall x \: (\text{BLUE}(x) \rightarrow Q(x))$

2. **Semantics of "cut" (VP):**

   - $\text{Vi.sem}$ ("cut") = $\lambda x . \text{CUT}(x)$
   - $\text{VP.sem} = \text{Vi.sem} = \lambda x . \text{CUT}(x)$

3. **Semantics of "every red cut" (S):**

   - $\text{S.sem} = \text{NP.sem} @ \text{VP.sem}$
   - $\text{S.sem} = (\lambda Q . \forall x \: (\text{BLUE}(x) \rightarrow Q(x))) @ (\lambda x . \text{CUT}(x))$
   - (Apply Q): $\forall x \: (\text{BLUE}(x) \rightarrow (\lambda x . \text{CUT}(x))(x))$
   - ($\beta$-reduction): $\forall x \: (\text{BLUE}(x) \rightarrow \text{CUT}(x))$

<!-- end list -->

- **Solution:** The logical meaning is "All blue things must be cut". Given the list of wires "a red, a blue, a violet, a green, another blue, a pink and a yellow wire", Morcela must cut **the blue wire** and **the other blue wire**.

---

## P12: Bots: old school versus today

### Decoding

You are given a language model with the following probability distribution for the next word after "The Avengers are":

| Word       | Probability |
| :--------- | :---------- |
| Assembling | 0.5         |
| Fighting   | 0.2         |
| Resting    | 0.15        |
| Training   | 0.1         |
| Recruiting | 0.05        |
| **Total**  | **1.0**     |

Here are the results of applying the different decoding and sampling methods:

**1. Greedy Decoding**

- **Explanation:** Greedy decoding selects the single word with the highest probability.
- **Solution:** The word "Assembling" (probability 0.5) is chosen.

**2. Beam Search (beam width = 2)**

- **Explanation:** Beam search keeps the $k$ (beam width) most probable sequences. At a single step (like this one), it simply identifies the top $k$ candidates.
- **Solution:** The top 2 candidates are kept:
  1. "Assembling" (0.5)
  2. "Fighting" (0.2)

**3. Random Decoding**

- **Explanation:** This method samples from the _entire_ probability distribution. Any word is a possible candidate, weighted by its probability.
- **Solution:** Any of the five words could be chosen. "Assembling" has a 50% chance, "Fighting" a 20% chance, and so on.

**4. Top-k Sampling ($k=3$)**

- **Explanation:** This method first truncates the vocabulary to the top $k$ most probable words. Then, it _renormalizes_ the probabilities of only those $k$ words so they sum to 1. Finally, it samples from this new, smaller distribution.
- **Solution:**
  1. **Select Top-k:** The top 3 words are "Assembling" (0.5), "Fighting" (0.2), and "Resting" (0.15).
  2. **Renormalize:** The total probability of this set is $0.5 + 0.2 + 0.15 = 0.85$.
  3. **New Distribution:**
     - "Assembling": $0.5 / 0.85 \approx 0.588$ (58.8%)
     - "Fighting": $0.2 / 0.85 \approx 0.235$ (23.5%)
     - "Resting": $0.15 / 0.85 \approx 0.176$ (17.6%)

**5. Nucleus Sampling ($p=0.7$)**

- **Explanation:** This method (also called top-p sampling) selects the smallest set of top words whose cumulative probability is greater than or equal to $p$. It then renormalizes their probabilities and samples from that set.
- **Solution:**
  1. **Sort Words:**
     1. "Assembling" (0.5)
  2. **Find Nucleus:**
     - Add "Assembling": Cumulative probability = 0.5. (This is $< 0.7$).
     - Add "Fighting": Cumulative probability = $0.5 + 0.2 = 0.7$. (This is $\ge 0.7$).
  3. **Select Nucleus:** The nucleus is {"Assembling", "Fighting"}.
  4. **Renormalize:** The total probability of this set is 0.7.
  5. **New Distribution:**
     - "Assembling": $0.5 / 0.7 \approx 0.714$ (71.4%)
     - "Fighting": $0.2 / 0.7 \approx 0.286$ (28.6%)

**6. Nucleus Sampling ($p=0.7$) with temperature set to 0.8**

- **Explanation:** This combines two steps. First, **temperature scaling** is applied to reshape the distribution. A temperature $T < 1.0$ makes the distribution "sharper" (high probabilities get higher, low ones get lower). Then, Nucleus Sampling is applied to the _new_ distribution.
- **Solution:**
  1. **Apply Temperature ($T=0.8$):** The new probability $P'(w)$ is proportional to $P(w)^{1/T}$, or $P(w)^{1.25}$.
     - $P'(\text{Assembling}) \propto 0.5^{1.25} \approx 0.4204$
     - $P'(\text{Fighting}) \propto 0.2^{1.25} \approx 0.1516$
     - $P'(\text{Resting}) \propto 0.15^{1.25} \approx 0.1060$
     - $P'(\text{Training}) \propto 0.1^{1.25} \approx 0.0562$
     - $P'(\text{Recruiting}) \propto 0.05^{1.25} \approx 0.0234$
  2. **Renormalize (Softmax):** The sum of these new values is $\approx 0.7576$.
     - $P_{\text{temp}}(\text{Assembling}) = 0.4204 / 0.7576 \approx 0.555$
     - $P_{\text{temp}}(\text{Fighting}) = 0.1516 / 0.7576 \approx 0.200$
     - $P_{\text{temp}}(\text{Resting}) = 0.1060 / 0.7576 \approx 0.140$
     - ...and so on.
  3. **Apply Nucleus Sampling ($p=0.7$) to this new distribution:**
     - Add "Assembling": Cumulative = 0.555. (This is $< 0.7$).
     - Add "Fighting": Cumulative = $0.555 + 0.200 = 0.755$. (This is $\ge 0.7$).
  4. **Select Nucleus:** The nucleus is {"Assembling", "Fighting"}.
  5. **Renormalize:** The total probability of this set is $0.755$.
  6. **Final Distribution:**
     - "Assembling": $0.555 / 0.755 \approx 0.735$ (73.5%)
     - "Fighting": $0.200 / 0.755 \approx 0.265$ (26.5%)
