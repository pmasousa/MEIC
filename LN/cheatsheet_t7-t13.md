# NLP Study Guide - Based on Provided Slides

## Table of Contents

1. [Morphology (T7-Morphology.pdf)](#1-morphology-t7-morphologypdf)
2. [Dense Vectors (T8-DenseVectors.pdf)](#2-dense-vectors-t8-densevectorspdf)
3. [Syntax (T9-Syntax.pdf)](#3-syntax-t9-syntaxpdf)
4. [Semantics (T10-Semantics.pdf)](#4-semantics-t10-semanticspdf)
5. [Trends Part 1: Pre-trained Models, Multi-task Learning, Compression, Applications (T11-Trends-part1.pdf)](#5-trends-part-1-pre-trained-models-multi-task-learning-compression-applications-t11-trends-part1pdf)
6. [Trends Part 2: Large Language Models and Prompting (T12-Trends-part2.pdf)](#6-trends-part-2-large-language-models-and-prompting-t12-trends-part2pdf)
7. [Machine Translation (T13-MT.pdf)](#7-machine-translation-t13-mtpdf)
8. [Computational Linguistics Meets the Portuguese Sign Language (T13-SignLanguages.pdf)](#8-computational-linguistics-meets-the-portuguese-sign-language-t13-signlanguagespdf)

---

## 1. Morphology (T7-Morphology.pdf)

### Learning Objectives

- Grasp fundamental concepts of morphology and Part-of-Speech (POS) tagging.
- Learn several ways to perform POS tagging.

### Topics Covered

- Linguistic Knowledge Overview
- Morphology Basics
- Word Classes (Parts-of-Speech)
- Part-of-Speech Tagging Methods
- Morphology Main Concepts (Morphemes, Word Building, Morphological Analysis)

### Linguistic Knowledge Overview

Linguistics involves different levels of knowledge to understand and process language:

1. **Phonetic Knowledge:** Relates words to sounds. Example: Pronunciation differences like "almoço" [noun vs. verb in Portuguese].
2. **Morphological Knowledge:** Studies the constituents (morphemes) of words. Example: Knowing "almoço" is a verb helps determine its pronunciation. (Focus of this chapter)
3. **Syntactic Knowledge:** Determines how words combine to form sentences. (Covered in Syntax chapter)
4. **Semantic Knowledge:** Assigns meaning to words and sentences [literal meaning]. Historically represented with logic , now often with vectors/embeddings. (Covered in Semantics chapter)
5. **Pragmatic Knowledge:** Considers context for interpreting non-literal meaning. Example: "It is so dark!" might mean "Please turn on the light".
6. **Discourse Knowledge:** Uses preceding sentences to interpret the current one [e.g., resolving pronouns, temporal references]. Example: "John loves his sister. **She** is so nice.".
7. **World Knowledge (Common Sense):** General knowledge about the world used for interpretation. Example: Inferring death from "John was shot in the eye, and his brain came out of his ear".

### Morphology > Word Classes (Parts-of-Speech)

Words are grouped into classes based on their function in a sentence.

- **Nouns:** Name people, places, things, ideas, concepts.
- **Pronouns:** Replace nouns.
- **Verbs:** Express actions, states, or occurrences.
  - _Action:_ She writes a letter.
  - _State:_ He knows the answer. She is tired.
  - _Occurrence:_ The sun rose early today.
- **Adjectives:** Describe or modify nouns/pronouns.
- **Adverbs:** Modify verbs, adjectives, or other adverbs.
- **Prepositions:** Show relationships [location, direction, time, manner]. Examples: _on_ the table, _to_ the park, _at_ 5 PM, _with_ confidence.
- **Conjunctions:** Join words, phrases, clauses, sentences.
- **Interjections:** Express emotions.

**Exercise Example:** Identify POS in "Wow, Sarah carefully hands her friend the red book from the shelf, and smiles."

- Adjective: red
- Adverb: carefully
- Conjunction: and
- Common Noun: friend, book, shelf
- Determiner: the
- Interjection: Wow
- Preposition: from
- Proper Noun: Sarah
- Pronoun: her
- Verb: hands, smiles

### Morphology > Part-of-Speech (POS) Tagging

- **Definition:** Assigning a word class (POS tag) to each word in a text.
- **Challenges:**
  - No single universal tag set exists.
  - Word Ambiguity: Many words can belong to multiple classes [e.g., "book" as noun or verb]. Although only a small percentage of _word types_ are ambiguous, these ambiguous words are very frequent in texts.
- **Approaches:**
  1. **Rule-Based Tagging:**
     - _Step 1:_ Assign potential tags using a dictionary.
     - _Step 2:_ Use handcrafted or learned rules to disambiguate and choose the final tag. Example Rule: "If the previous tag is an article, eliminate the verb tag for the current word".
  2. **Stochastic Tagging (HMM):**
     - _Goal:_ Find the most probable tag sequence $T = t_1...t_n$ for a given word sequence $W = w_1...w_n$, i.e., maximize $P(T|W)$.
     - _Hidden Markov Model (HMM):_ A statistical model using hidden states (tags) and observable sequences [words].
     - _Assumptions:_
       - _Transition Probability:_ Probability of a tag depends only on the previous tag (bigram assumption): $P(t_i | t_{i-1})$. Calculated as $P(t_i|t_{i-1}) = C(t_{i-1}, t_i) / C(t_{i-1})$.
       - _Emission Probability:_ Probability of a word depends only on its tag: $P(w_i | t_i)$. Calculated as $P(w_i|t_i) = C(t_i, w_i) / C(t_i)$.
     - _Overall Probability:_ $P(T|W) \approx \prod_{i=1}^{n} P(t_i|t_{i-1}) \times P(w_i|t_i)$.
     - _Viterbi Algorithm:_ A dynamic programming algorithm used to find the most likely sequence of hidden states (tags) given the observations (words) and the HMM probabilities. It stores the best path probability and backpointers at each step.
  3. **Deep Learning Tagging:**
     - POS tagging is treated as a sequence labeling task.
     - Architectures like RNNs, LSTMs, Transformers are trained on labeled datasets to predict tags based on word context.
     - LLMs can also perform POS tagging.

### Morphology > Morphology Main Concepts

- **Morphology:** Field studying the internal structure of words.
- **Morpheme:** Minimal meaningful unit in a word.
  - **Stem (Lexical Morpheme):** Carries the core meaning [e.g., "use" in "reusable"].
  - **Affix (Grammatical Morpheme):** Modifies the stem's meaning or adds grammatical info [e.g., "re-", "-able"].
- **Types of Affixes:**
  - **Prefix:** At the beginning [e.g., **un**-happy, **re**-write].
  - **Suffix:** At the end [e.g., happi-**ness**, quick-**ly**].
  - **Infix:** Inside the stem [e.g., editor-**s**-in-chief].
  - **Circumfix:** Surrounds the stem, added simultaneously [e.g., **ge**-lieb-**t** in German].
  - **Clitic:** Functions like a word but doesn't appear alone [e.g., "-os" in contei-**os**].
- **Agglutinative Languages:** Languages where words can contain many morphemes [e.g., Turkish].

- **Word Building Processes:**

  - **Inflection:** Modifies a word for grammatical function (tense, number, gender) _without_ changing its core meaning or word class [e.g., eat -> eat**s**, gato -> gata**s**].
  - **Derivation:** Creates a new word, potentially changing the word class or meaning significantly (e.g., **un**-do, amigo (n) -> amigáv**el** (adj)).
  - **Compounding:** Combines multiple stems [e.g., dog + house -> doghouse, chapéu-de-chuva].
  - **Cliticization:** Attaching clitics to words [e.g., apagou-o].

- **Morphological Analysis:**
  - **Definition:** Analyzing a word's structure to understand its components and function.
  - **Subtasks:**
    - **Lemmatization:** Finding the dictionary/base form (lemma) of a word [e.g., running -> run, has -> have].
    - **Stemming:** Reducing a word to its root/stem, which might not be a valid word [e.g., running -> runn].

### Key Takeaways

- Define Part-of-Speech (POS).
- Explain rule-based and HMM-based POS tagging.
- Define morpheme and stem.
- Identify different affix types.
- Explain the difference between inflection and derivation.
- Understand the difference between stemming and lemmatization.

### Suggested Readings

- "Sebenta": Morphology? What is it? Is there a cure?
- Jurafsky: Chapter 8 (Sequence Labelling for...), Sections 8.1-8.4.

---

## 2. Dense Vectors (T8-DenseVectors.pdf)

### Learning Objectives

- Explain the concept of dimensionality reduction.
- Understand how SVD creates dense vectors.
- Explain the creation of neural word embeddings [Skip-gram, BERT].
- Understand how sentence embeddings can be created.
- Know how to evaluate neural word embeddings.
- Understand various concepts related to dense vectors.

### Topics Covered

- Sparse vs. Dense Vectors Recap
- Word Embeddings (General Concept)
- Dimensionality Reduction (SVD, LSA/LSI)
- Neural Word Embeddings (Word2Vec - Skip-gram, GloVe, fastText, Contextual Models - BERT)
- Neural Sentence Embeddings
- Representing and Evaluating Word Embeddings

### The Road So Far: Sparse vs. Dense

- **Previously:** Sparse vectors [e.g., Bag-of-Words, TF-IDF].
  - High-dimensional [length = |Vocabulary|, often 10k-50k].
  - Sparse [most entries are 0].
- **Now:** Dense vectors [embeddings].
  - Lower-dimensional [e.g., 50-1000 dimensions].
  - Dense [most entries are non-zero].
- **Foundation:** Distributional Hypothesis ("a word is known by the company it keeps") and Distributional Semantics [meaning represented by vectors].

### Word Embedding (General Concept)

- **Definition:** A representation of a word as a dense vector in a multi-dimensional space.
- **Goal:** Words with similar meanings should have vectors that are close to each other in this space [e.g., using cosine similarity].

### "Classic" Dimensionality Reduction Methods

- **Goal:** Reduce dimensions while preserving essential information.
- **Singular Value Decomposition (SVD):** An algebraic method to decompose a matrix $A$ into $U \Sigma V^T$.
  - $U$: Left singular vectors (captures relationships between rows/words).
  - $\Sigma$: Diagonal matrix of singular values (indicates importance of dimensions), sorted largest to smallest.
  - $V^T$: Right singular vectors (captures relationships between columns/documents or contexts).
- **Latent Semantic Analysis/Indexing (LSA/LSI):**
  - Applies SVD to a term-document matrix [or word-context matrix].
  - **Truncated SVD:** Keeps only the top $k$ singular values (and corresponding vectors in $U$ and $V^T$) to create a lower-dimensional approximation of the original matrix.
  - The rows of the truncated $U$ matrix (multiplied by the truncated $\Sigma$, sometimes) serve as the dense word embeddings.
  - Captures "latent" semantic topics or concepts.
- **Related:** Principal Component Analysis (PCA) is mathematically related to SVD/LSA. Topic Models (like LDA) also aim to find latent topics.

### Neural Word Embeddings

- Learns embeddings using neural networks, often through "fake" prediction tasks.
- **Word2Vec (Mikolov et al., 2013):**
  - **Skip-gram:** Predicts context words given a center word.
    - _Architecture:_ Input (one-hot) -> Linear Hidden Layer (no activation) -> Output Layer [softmax predicts context words].
    - _Training Data:_ Generated from text using a sliding window [center word, context word pairs].
    - _The Embedding:_ The weights between the input layer and the hidden layer ($W_{input}$) become the word embedding matrix after training.
  - **CBOW (Continuous Bag-of-Words):** Predicts the center word given context words.
- **GloVe (Pennington et al., 2014):** Global Vectors, combines count-based matrix factorization (like LSA) with prediction-based methods (like Word2Vec), trained on global word-word co-occurrence statistics.
- **fastText (Bojanowski et al., 2016):** Extends Word2Vec by representing words as bags of character n-grams [subwords]. Helps handle morphology, rare words, and typos.

- **Context-Free vs. Contextual Embeddings:**

  - _Context-Free (Word2Vec, GloVe, fastText):_ Generate a single, static vector for each word type, regardless of context [e.g., "bank" is the same in "river bank" and "bank deposit"].
  - _Contextual (ELMo, BERT):_ Generate different embeddings for a word depending on its surrounding sentence context.

- **BERT (Devlin et al., 2018):** Bidirectional Encoder Representations from Transformers.
  - _Architecture:_ Uses the Encoder part of the Transformer architecture. Bidirectional means it considers both left and right context simultaneously.
  - _Pre-training Tasks:_ 1. **Masked Language Model (MLM):** Randomly masks ~15% of input tokens. The model predicts _only_ the original masked tokens based on unmasked context. Masking detail: 80% replace with `[MASK]`, 10% replace with random word, 10% keep original. 2. **Next Sentence Prediction (NSP):** Given two sentences A and B, predict if B is the actual sentence following A or a random sentence. Uses `[CLS]` and `[SEP]` tokens.
  - _Usage:_ Pre-trained on massive text corpora, then fine-tuned for specific downstream tasks. The output vectors from BERT layers serve as contextual embeddings.

### Neural Sentence Embeddings

- Represent entire sentences as vectors.
- **Simple Methods:**
  - Sum word embeddings in the sentence.
  - Average word embeddings in the sentence.
- **Model-Based Methods:**
  - **Doc2Vec:** Extends Word2Vec to paragraphs/documents.
  - **SentenceBERT (SBERT):** Fine-tunes BERT using siamese/triplet networks to produce semantically meaningful sentence embeddings [similar sentences get close vectors].
  - **Using BERT's [CLS] Token:** The output embedding corresponding to the special `[CLS]` token (prepended to the input) is often used as a sentence representation, especially after fine-tuning for sentence tasks.
  - **InferSent, Universal Sentence Encoder (USE):** Other models trained specifically for sentence embeddings.

### Representing and Evaluating Word Embeddings

- **Representation:**
  - As raw numerical vectors.
  - Visualized using dimensionality reduction techniques like **t-SNE** (t-Distributed Stochastic Neighbor Embedding) to plot high-dimensional vectors in 2D/3D . t-SNE aims to preserve local structure/similarity. Perplexity is a key t-SNE hyperparameter controlling the number of neighbors considered.
- **Evaluation:**
  - **Extrinsic:** Evaluate embeddings based on their performance as features in downstream NLP tasks [e.g., QA, sentiment analysis, NER].
  - **Intrinsic:** Evaluate embeddings directly on specific properties.
    - _Word Similarity:_ Correlate vector similarity (e.g., cosine) with human judgments of word similarity [e.g., WordSim353 dataset].
    - _Word Analogy:_ Test for capturing relational similarities (e.g., king - man + woman ≈ queen). Uses vector arithmetic. Covers semantic (e.g., country-capital) and syntactic (e.g., tense, plural) analogies.
    - _TOEFL Synonym Tests:_ Multiple-choice questions asking for the closest synonym.
  - **Bias Evaluation:** Check for societal biases reflected in embeddings (e.g., gender, race) using analogy tasks or measuring associations with stereotypical concepts.

### Key Takeaways

- Dense vectors are low-dimensional, non-sparse representations of words/sentences.
- SVD/LSA are classic methods for creating dense vectors via dimensionality reduction.
- Neural methods like Word2Vec (Skip-gram/CBOW) learn embeddings through prediction tasks.
- Word2Vec produces context-free embeddings; BERT produces contextual embeddings.
- BERT uses Masked Language Modeling and Next Sentence Prediction for pre-training.
- Sentence embeddings can be created by simple averaging/summing, using special tokens ([CLS]), or dedicated models (SBERT, USE).
- Embeddings are evaluated intrinsically (similarity, analogy) and extrinsically (downstream tasks).
- Bias is a significant concern in embeddings.

### Suggested Readings

- Jurafsky: Sections 6.8, 6.9, 6.10, 6.11, 11.1, 11.2.

---

## 3. Syntax (T9-Syntax.pdf)

### Learning Objectives

- Grasp fundamental concepts of syntax.
- Learn how to perform syntactic analysis.

### Topics Covered

- Main Syntax Concepts (Constituents, Functions, Treebanks, Parsing)
- Context-Free Grammars (CFG)
- Probabilistic Context-Free Grammars (PCFG)
- Dependency Grammars (DG)
- Real Application Example (EP to LGP Translation)
- LLMs in Syntactic Parsing
- CKY Parsing Algorithm

### Main Concepts

- **Syntax:** The study of the rules governing how words combine to form phrases and sentences in a language. Natural language syntax is more flexible than artificial language syntax.
- **Constituents:** Groups of words that function as a single unit (e.g., Noun Phrases (NP), Verb Phrases (VP), Prepositional Phrases (PP)).
- **Grammatical Functions:** Roles constituents play in a sentence.
  - _Subject (SUBJ):_ Performs the action or is described [[The student] took the test].
  - _Direct Object (DO):_ Receives the action [reading [the book]].
  - _Indirect Object (IO):_ Recipient or beneficiary [Give [to Mary]].
  - _Predicative of the Subject (PS):_ Describes or renames the subject after a linking verb [is [tired], is [a teacher]].
- **Treebank:** A corpus where sentences are annotated with their syntactic structure [parse trees]. Examples: Penn Treebank, Floresta Sintáctica [Portuguese].
- **Syntactic Parsing/Analysis:** The process of assigning a syntactic structure (usually a tree) to an input sentence according to a grammar.

### Context-Free Grammars (CFG)

- A formalism used to capture constituency and word order.
- **Formal Definition:** A CFG is a tuple $(N, T, S_0, R)$ where:
  - $N$: Set of non-terminal symbols [e.g., S, NP, VP, Det, N].
  - $T$: Set of terminal symbols [words/tokens].
  - $S_0$: The start symbol (usually S for sentence), $S_0 \in N$.
  - $R$: Set of production rules of the form $A \to \alpha$, where $A \in N$ and $\alpha$ is a sequence of symbols from $N \cup T$ [e.g., $S \to NP \ VP$, $NP \to Det \ N$, $Det \to the$].
- **Derivation:** Applying rules sequentially to rewrite symbols, starting from $S_0$.
- **Language Generated $L(G)$:** The set of all terminal symbol strings (sentences) that can be derived from $S_0$ using the rules $R$.
- **Parse Tree:** A tree structure representing a derivation for a sentence.

**Example CFG & Parse:**

- Grammar: $S \to NP \ VP$, $NP \to Det \ N$, $VP \to V \ NP$, $Det \to o | a$, $N \to Zé | Ana$, $V \to ama$.
- Sentence: "O Zé ama a Ana".
- Parse Tree: Shows how this sentence structure derives from 'S' using the grammar rules.

### Probabilistic Context-Free Grammars (PCFG)

- An extension of CFG where each rule $A \to \alpha$ has an associated probability $P(A \to \alpha)$.
- Constraint: For any non-terminal $A$, the sum of probabilities of all rules expanding $A$ must equal 1: $\sum_{j} P(A \to \alpha_j) = 1$.
- **Probability Estimation:** Usually estimated from a treebank using relative frequencies:
  $P(A \to \alpha_j) = \frac{Count(A \to \alpha_j \text{ was used})}{Count(\text{any rule starting with } A \text{ was used})}$.
- **Disambiguation:** If a sentence has multiple possible parse trees, the probability of a tree is the product of the probabilities of all rules used in its derivation. The most probable tree is usually chosen as the correct parse.

**Example Disambiguation:** "astronomers saw stars with ears" has two parses (PP attaches to "stars" or "saw"). PCFG probabilities allow choosing the structurally more likely interpretation [usually the one where "with ears" modifies "saw", unless the corpus heavily features astronomical observations involving ears!].

### Dependency Grammars (DG)

- Focuses on relationships between individual words (head-dependent) rather than constituents.
- **Structure:** Represents sentence structure as a directed graph where nodes are words and labeled arcs represent grammatical relations (dependencies) between a head (governor) word and a dependent (modifier) word.
- **Formal Definition:** $G = (V, A)$, where $V$ is the set of words (vertices) and $A$ is the set of dependency arcs.
- **Common Relations:** `nsubj` (nominal subject), `dobj` (direct object), `det` (determiner), `amod` (adjectival modifier), `prep` (prepositional modifier), `root` (main predicate).

**Example Dependency Parse:** "The student reads a novel." would show arcs like: `student` -> `The` (det), `reads` -> `student` (nsubj), `novel` -> `a` (det), `reads` -> `novel` (dobj), `ROOT` -> `reads`.

### Real Application Example: EP to LGP Translation

- **System:** EP2LGP5.0 translates European Portuguese (EP) text to Portuguese Sign Language (LGP) glosses.
- **Challenge:** Different grammars [e.g., word order, lack of articles/prepositions in LGP glosses].
- **Rule-Based Approach using Dependencies:**
  1. **Corpus:** Uses a small parallel EP-LGP corpus [annotated with ELAN].
  2. **Analysis:** Parses EP sentences using POS tagging and Dependency Parsing. Removes determinants and punctuation.
  3. **Alignment:** Aligns EP words with LGP glosses using similarity measures.
  4. **Inference:** Infers a bilingual dictionary and syntactic translation rules (e.g., $VP \ NP \to NP \ VP$) based on dependency relations and alignments.
  5. **Translation:** Applies dictionary and rules to new EP sentences (parsed with dependencies) to generate LGP gloss sequence.
- **Later Developments:** Used the rule-based system to generate a larger synthetic parallel corpus, then trained Deep Learning (NMT) models.

### How good are LLMs in Syntactic Parsing?

- Large Language Models (like Gemini, GPT variants, Mistral) can be prompted to generate constituency parse trees for sentences.
- The quality and specific formalism (tags used) might vary between models.

### An Example of a Syntactic Parser: CKY Algorithm

- **CKY (Cocke-Kasami-Younger):** A dynamic programming algorithm for parsing sentences with CFGs.
- **Requirement:** The CFG must be in **Chomsky Normal Form (CNF)**. CNF rules are restricted to two forms:
  - $A \to B \ C$ (NonTerminal -> two NonTerminals)
  - $A \to a$ [NonTerminal -> one terminal].
- **Process:** Fills a table (chart) bottom-up. The entry `table[i, j]` stores the set of non-terminals that can generate the substring of the sentence from word `i` to word `j`.
- **Recognition:** If the start symbol `S` is in the top cell `table[0, n]` (where `n` is sentence length), the sentence is grammatical according to the CFG. Backpointers can be stored to reconstruct the parse tree(s).

### Key Takeaways

- Understand concepts: treebank, constituency grammar, CFG, PCFG, dependency grammar.
- Understand the language generated by a CFG.
- Be able to apply the CKY algorithm (conceptually or manually for small examples).

### Suggested Readings

- Sebenta: Syntax important Natural very Language is
- Jurafsky: Chapter 17 (Context-Free Grammars and...), Sections 17.1-17.3.

---

## 4. Semantics (T10-Semantics.pdf)

### Learning Objectives

- Define main concepts from Computational Semantics.
- Identify several semantic resources.
- Apply semantic rules with a grammar to obtain the logical form of a sentence.

### Topics Covered

- Computational Semantics Definition & Goal
- Symbolic Representation Methods (Keywords, Regex, FOL, Frames, AMR)
- Compositional Semantic Parsing (Montague, Lambda Calculus)
- Semantic Parsing as Sequence Prediction (Slot Filling)
- Semantic Relations (Synonymy, Antonymy, Hyponymy, Meronymy, Homonymy, Polysemy)
- Semantic Resources (WordNet, PropBank, FrameNet)

### Computational Semantics

- **Definition:** The field focused on designing meaning representations for language and the semantic parsers that create them.
- **Goal:** Map what a user says into a representation that captures its meaning and is understandable/actionable by a computer.
- **Components:**
  - **Meaning Representation:** The formal structure capturing meaning (e.g., First Order Logic (FOL), vectors, SQL, Frames). Can be actionable [e.g., SQL query].
  - **Semantic Parsing (Analysis):** The process of converting natural language text into a meaning representation.
  - **(Grounding):** Connecting the meaning representation to the real world or a specific knowledge base/action.

### Language Representation: Symbolic Approach

- Uses human-interpretable symbols corresponding to objects, properties, and relations. Contrasts with vector representations.
- **Common Symbolic Formalisms:**
  - Keywords: Simple triggers for actions [e.g., "left", "stop"].
  - Sentences/Templates: Fixed phrases or patterns [e.g., "Who built the palace?", "Who built .* palace"].
  - Regular Expressions: Patterns to match variations.
  - **First Order Logic (FOL):** Uses predicates, constants, variables, quantifiers ($\forall, \exists$), and logical connectives [$\neg, \vee, \wedge, \Rightarrow$].
    - Example: `student(PEDRO)`, `∀x student(x) ⇒ great(x)`, `∃x student(x) ∧ great(x)`.
    - Note: $\forall$ usually pairs with $\Rightarrow$; $\exists$ usually pairs with $\wedge$.
  - **Frames:** Structures with a 'Type' (intent/action) and 'Slots' [attribute-value pairs]. Useful in dialogue systems.
    - Example: "How much is the cheapest flight from Boston to New York tomorrow morning?" -> Frame: `Goal: Airfare`, `Cost_Relative: cheapest`, `Depart_City: Boston`, ....
  - Graphs (e.g., Abstract Meaning Representation - AMR): Represents sentence meaning as a rooted, directed, acyclic graph.

### Compositional Semantic Parsing

- Builds the meaning representation of a sentence by recursively combining the meanings of its smaller parts (words, phrases), guided by the syntactic structure.
- Pioneered by Richard Montague.
- **Syntax-Semantics Parallelism:** Often uses grammar rules augmented with semantic composition rules.
  - Example Rule: $S \to NP \ VP \quad \{ VP.sem@NP.sem \}$ [Meaning of S is VP meaning applied to NP meaning].
- **Lambda Calculus:** Often used to represent the semantics of constituents, especially those needing arguments.
  - $\lambda x.P(x)$: Represents a function expecting an argument $x$ to fill into predicate $P$.
  - Function Application (`@`): Applies a function to an argument (e.g., $(\lambda x.LOVES(x, MARIA))@ZÉ = LOVES(ZÉ, MARIA)$).
  - $\beta$-reduction: The process of applying the function [substituting the argument].

**Examples (using Lambda Calculus):**

- "Alex likes Brit":
  - `likes`: $\lambda y . \lambda x . LIKES(x, y)$
  - `Brit`: $BRIT$
  - `likes Brit` ($VP \to Vt \ NP$): $(\lambda y . \lambda x . LIKES(x, y)) @ BRIT = \lambda x . LIKES(x, BRIT)$
  - `Alex`: $ALEX$
  - `Alex likes Brit` ($S \to NP \ VP$): $(\lambda x . LIKES(x, BRIT)) @ ALEX = LIKES(ALEX, BRIT)$
- "A dog sleeps" [handling quantifiers requires more complex $\lambda$-expressions, often reversing NP/VP application]:
  - `a`: $\lambda P . \lambda Q . \exists x (P(x) \wedge Q(x))$
  - `dog`: $DOG$
  - `a dog` ($NP \to Det \ NN$): $(\lambda P . \lambda Q . \exists x (P(x) \wedge Q(x))) @ DOG = \lambda Q . \exists x (DOG(x) \wedge Q(x))$
  - `sleeps`: $\lambda z . SLEEPS(z)$
  - `a dog sleeps` ($S \to NP \ VP$, with reversed semantics $NP.sem@VP.sem$): $(\lambda Q . \exists x (DOG(x) \wedge Q(x))) @ (\lambda z . SLEEPS(z)) = \exists x (DOG(x) \wedge SLEEPS(x))$

### Semantic Parsing as Sequence Prediction

- Semantic parsing, especially **slot filling** in frame semantics, can be modeled as a sequence tagging task.
- Uses **BIO tagging:** Tag each word as Beginning (B), Inside (I), or Outside (O) of a semantic slot.
  - Example: "find **recent** `B-date` **comedies** `B-genre` by **james** `B-dir` **cameron** `I-dir`".
  - Example: "How much is the **cheapest** `B-Cost_Relative` flight from **Boston** `B-Depart_City` to **New** `B-Arrival_City` **York** `I-Arrival_City`?"
- This allows using sequence labeling models (like BiLSTMs, CRFs, Transformers) for slot filling. Intent detection is often treated as a separate classification task on the whole utterance.

### Semantic Relations

Relationships between the meanings of words:

- **Synonymy:** Words with the same or very similar meaning [e.g., couch/sofa]. Context matters: 'big' and 'large' aren't always interchangeable ['my big sister' vs 'my large sister'].
- **Antonymy:** Words with opposite meanings [e.g., awake/asleep, hot/cold].
- **Hyponymy / Hypernymy:** Specific/general relationship. A hyponym is a type of its hypernym [e.g., 'dog' is a hyponym of 'animal'; 'animal' is a hypernym of 'dog'].
- **Meronymy / Holonymy:** Part/whole relationship. A meronym is part of a holonym [e.g., 'wheel' is a meronym of 'car'; 'car' is a holonym of 'wheel'].
- **Homonymy:** Words with the same spelling AND pronunciation but unrelated meanings (e.g., bank (river) vs. bank (financial)).
  - _Homophones:_ Same pronunciation, different spelling/meaning [e.g., write/right].
  - _Homographs:_ Same spelling, different pronunciation/meaning (e.g., lead (metal) / lead (verb)).
- **Polysemy:** A single word with multiple related meanings (e.g., bank (financial institution) vs. bank (data bank); get (obtain) vs. get (buy)).

### Semantic Resources

Databases and corpora encoding semantic information:

- **WordNet:** A large lexical database for English. Groups words into sets of synonyms called **synsets**. Each synset represents a distinct concept and includes definitions (glosses) and example sentences. Synsets are linked by semantic relations [synonymy, hypernymy, meronymy, etc.].
- **PropBank (Proposition Bank):** A corpus annotating verbs (predicates) and their arguments with semantic roles (Arg0, Arg1, etc.) on top of the Penn Treebank syntactic structures. Provides consistent roles across different syntactic structures [e.g., Arg0=agent, Arg1=patient]. Also includes verb sense IDs [framesets].
- **FrameNet:** A lexical database based on **Frame Semantics**. Defines word meanings in terms of semantic frames (concepts, relations, entities) and their participants [Frame Elements]. Example: The `Commerce_sell` frame involves Seller, Buyer, Goods, Money. Words like "sell", "buy", "purchase" evoke this frame.
- **Other Resources:** VerbNet, BabelNet, etc..

### Key Takeaways

- Language can be represented symbolically or via vectors.
- Computational Semantics maps language to meaning representations. Compositional semantics is part of this.
- Various semantic relations exist between words (synonymy, antonymy, etc.).
- Semantic resources like WordNet, PropBank, FrameNet encode lexical and predicate-argument semantics.

### Suggested Readings

- "Sebenta" Sections 7.3 and 7.4.
- Jurafsky (3rd ed. draft): Chapter 19 [Word Senses and WordNet, 19.1-19.5].
- Jurafsky (3rd ed. draft): Chapter 20 [Semantic Role Labelling, 20.1-20.5].

---

## 5. Trends Part 1: Pre-trained Models, Multi-task Learning, Compression, Applications (T11-Trends-part1.pdf)

### Learning Objectives

- Define pre-trained models and explain how to leverage them [Prompting, Transfer Learning].
- Explain and apply Feature-based Transfer Learning and Fine-tuning.
- Explain Multi-task Learning.
- Describe compression techniques and NLP tasks.

### Topics Covered

- Pre-trained Models (Definition, LLMs)
- Using Pre-trained Models (Direct Use, Transfer Learning)
- Feature-based Transfer Learning
- Fine-tuning
- Parameter-Efficient Fine-Tuning (PEFT - Adapters, LoRA)
- Multi-task Learning
- Compression Techniques (Pruning, Quantization, Knowledge Distillation)
- Applications Overview (QA, Summarization, NLI, Sentiment, Commonsense Reasoning, etc.)

### Pre-trained Models

- **Definition:** Machine learning models previously trained on large datasets and saved for reuse on other tasks.
- **Examples:** BERT, GPT, ELMo, ULMFit, RoBERTa, XLNet, etc. [cite: 346, 347-383].
- **Idea:** Leverage knowledge learned from large datasets (like general language understanding) as a starting point for more specific tasks, similar to how humans apply general knowledge.
- **Large Language Models (LLMs) vs. Pre-trained Models:**
  - LLMs _are_ a type of pre-trained model, typically trained to predict the next token on massive text data.
  - However, LLMs are often _more_ than just pre-trained, as they undergo further stages like Instruction Tuning and RLHF to follow instructions and align with preferences. They are usually interacted with via **prompting** rather than retraining.

### How to Use Pre-trained Models

1. **Direct Use / Inference:** Using the model as-is to generate outputs or extract features/representations without further training. Example: Using BERT to get word/sentence embeddings. Prompting is typically used for instruction-tuned LLMs, not basic pre-trained models.
2. **Transfer Learning:** Reusing a pre-trained model developed for one task as a starting point for a second task.

### Transfer Learning Types

1. **Feature-Based Transfer Learning:**
   - Use the pre-trained model (kept frozen) to extract features (embeddings) from the input data.
   - These features are then fed into a new, smaller model (e.g., a classifier like Logistic Regression) which is trained specifically for the target task.
   - **Example (Sentiment Analysis):**
     1. Input Sentence ("a visually stunning...") -> Tokenizer [adds CLS/SEP, gets IDs].
     2. Token IDs -> Pre-trained BERT/DistilBERT.
     3. BERT Output -> Extract embedding for the `[CLS]` token.
     4. `[CLS]` embedding -> Train a Logistic Regression classifier -> Output [positive/negative].
2. **Fine-tuning:**
   - Take a pre-trained model and continue training its parameters (or a subset of them) on the dataset for the new target task. Often involves adding a new task-specific output layer.
   - Requires less data and computation than training from scratch, but can still be costly for very large models.
   - **Techniques:**
     - Train the entire model.
     - Freeze some layers (e.g., early layers capturing general features) and train only the later layers or just the new output layer.
     - Gradual unfreezing: Start by training only the top layers, then unfreeze and train more layers with a smaller learning rate.

### Parameter-Efficient Fine-Tuning (PEFT) Methods

- **Goal:** Adapt pre-trained models to new tasks by training only a small number of _additional_ or _modified_ parameters, keeping the bulk of the original model frozen. Reduces computational cost and storage needs.
- **Adapters:**
  - Small, trainable neural network modules inserted between the layers of a frozen pre-trained model.
  - They learn task-specific adaptations while preserving the general knowledge in the base model. Only adapter parameters are trained. Loaded during inference to augment the base model.
  - Can perform comparably to full fine-tuning with far fewer trained parameters [e.g., ~3%].
- **LoRA (Low-Rank Adaptation):**
  - Hypothesizes that the change in weights ($\Delta W$) during adaptation is low-rank.
  - Instead of learning $\Delta W$ directly, LoRA learns two smaller matrices $A$ and $B$ such that $\Delta W \approx BA$.
  - The forward pass becomes $h = Wx + BAx$, where $W$ (original weights) is frozen, and only $A$ and $B$ are trained.
  - Significantly reduces the number of trainable parameters [e.g., by 10,000x for GPT-3].

### Multi-task Learning

- **Definition:** Training a single model to perform multiple tasks simultaneously.
- **Goal:** Leverage shared knowledge and representations across tasks to improve overall performance and generalization.
- **Architecture:** Typically involves shared layers capturing common features and task-specific layers/heads for individual task outputs.
- **Parameter Sharing:**
  - _Hard Sharing:_ Explicitly share lower layers, branch out to task-specific upper layers.
  - _Soft Sharing:_ Each task has its own model, but parameters are constrained to be similar (e.g., via regularization).
- **Example (DecaNLP):** A challenge involving 10 different NLP tasks (QA, MT, Summarization, NLI, etc.) solved by a single model by reformulating all tasks as question answering.

### Compression Techniques

- Methods to reduce model size and complexity for efficiency (faster inference, lower memory) without significant performance loss.
- **Pruning:** Removing unimportant/redundant components.
  - _Weight Pruning:_ Remove individual weights with small magnitudes.
  - _Neuron/Layer Pruning:_ Remove entire neurons or layers.
- **Quantization:** Reducing the numerical precision of weights and activations [e.g., from 32-bit floating point to 8-bit integers].
- **Knowledge Distillation (Teacher-Student):**
  - Train a smaller "student" model to mimic the output behavior (predictions/logits) of a larger, pre-trained "teacher" model.
  - The student learns from both the ground truth labels (hard targets) and the teacher's probability distributions [soft targets].

### Applications Overview

Brief descriptions of common NLP tasks often used with these models:

- **Question Answering (QA):** Answering questions, often based on a provided context passage. Span-based QA identifies the answer span within the text. Can be complex, requiring multi-step reasoning.
- **Summarization:** Generating a concise summary from a longer document. Can be extractive (selecting sentences) or abstractive [generating new sentences].
- **Natural Language Inference (NLI):** Determining the relationship (entailment, contradiction, neutral) between a premise and a hypothesis sentence.
- **Sentiment Analysis:** Classifying the sentiment (positive, negative, neutral) expressed in text. Can be complex due to sarcasm, negation, etc..
- **Commonsense Reasoning:** Tasks requiring reasoning beyond literal text meaning, often involving world knowledge [e.g., Winograd Schema Challenge].
- **Other Applications:** Cyberbullying detection , Assistive Technologies [e.g., communication aids for disabilities].

### Key Takeaways

- Pre-trained models can be used directly or adapted via Transfer Learning (Feature-based or Fine-tuning).
- PEFT methods (Adapters, LoRA) make fine-tuning large models more efficient.
- Multi-task learning trains one model for multiple tasks.
- Compression techniques (Pruning, Quantization, Distillation) reduce model size/complexity.
- Many diverse applications exist (QA, Summarization, NLI, Sentiment, etc.).

### Suggested Readings

- PEFT Survey: [https://arxiv.org/pdf/2303.15647](https://arxiv.org/pdf/2303.15647)
- LoRA Paper: Hu et al. 2021
- LoRA Explanations (YouTube, ML6 blog)

---

## 6. Trends Part 2: Large Language Models and Prompting (T12-Trends-part2.pdf)

### Learning Objectives

- Understand LLM concepts, training, testing [decoding/sampling].
- Discuss the pros and cons of LLMs.
- Understand prompting techniques.

### Topics Covered

- Large Language Models (LLMs) Definition & Scale
- LLM Training Pipeline (Pre-training, Instruction Fine-tuning, RLHF)
- LLM Testing/Inference (Decoding Methods: Greedy, Beam, Sampling - Top-k, Top-p, Temperature)
- Pros and Cons of LLMs (Capabilities, Fallibility, Bias, Ethics, Societal Impact)
- Prompting (Concept, Zero/Few-Shot, Engineering, Techniques)

### What is a Large Language Model (LLM)?

- **General Definition:** An AI trained on vast amounts of text data, capable of understanding and generating human-like text for various tasks [conversation, summarization, translation, etc.].
- **Technical Definition:** A type of **Language Model (LM)** - a probability distribution over sequences of tokens ($P(x_1...x_k)$). Used to assign probability to text or generate text by sampling tokens sequentially.
- **"Large" refers to scale:**
  - **Model Size:** Number of parameters [often billions, e.g., 100B+].
  - **Training Data Size:** Number of tokens used for training [trillions].
  - **Compute Size:** Computational resources needed for training.

### LLM Training Pipeline

LLMs typically undergo multiple training stages:

1. **Pre-training:**
   - Model learns general language patterns, syntax, semantics, and world knowledge from massive unlabeled text corpora [unsupervised learning].
   - Common objective: Predict the next token or masked tokens (as in BERT's MLM).
2. **Instruction Fine-Tuning:**
   - Adapts the pre-trained model to follow human instructions and perform specific tasks better.
   - Uses curated datasets of (instruction, input, desired output) examples [supervised learning].
   - Teaches the model _how_ to respond, not just _what_ language looks like. Examples: Translate this, Summarize that, Answer this question [cite: 913-916].
3. **Reinforcement Learning from Human Feedback (RLHF):**
   - Aligns the model's behavior with human preferences [e.g., helpfulness, harmlessness, honesty].
   - **Process:**
     - _Collect Preference Data:_ Generate multiple responses to prompts, have humans rank them.
     - _Train a Reward Model (RM):_ Train a model to predict the human preference score for any given response.
     - _Optimize Policy using RL:_ Fine-tune the LLM (the "policy") using reinforcement learning (e.g., PPO - Proximal Policy Optimization) to maximize the score predicted by the reward model. Policy in LLMs = the model deciding the next token.
   - **Alternative: Direct Preference Optimization (DPO):** Directly optimizes the LLM based on preference data without needing a separate reward model or RL step.

### LLM Testing (Inference & Decoding)

- **Inference:** The process of using a trained model to generate output for a given input [prompt].
- **Decoding:** The algorithm used during inference to select the sequence of tokens (words) that form the output text.

- **Decoding Strategies:**
  - **Greedy Search:** At each step, select the single token with the highest probability. Fast but often leads to repetitive and suboptimal sequences.
  - **Beam Search:** Maintain a fixed number ('beam width') of the most probable partial sequences at each step, expanding each and selecting the best overall sequence at the end. Balances quality and computation.
  - **Sampling:** Introduce randomness to generate more diverse outputs.
    - _Random Sampling:_ Sample the next token based on the probability distribution output by the model. Higher probability tokens are more likely, but lower probability ones can still be chosen.
    - _Top-k Sampling:_ Consider only the `k` most probable tokens, renormalize their probabilities, and sample from this reduced set. Problem: `k` is fixed, may be too restrictive or too broad depending on the distribution's shape.
    - _Nucleus (Top-p) Sampling:_ Consider the smallest set of tokens whose cumulative probability exceeds a threshold `p`, renormalize, and sample from this set. Adapts the number of considered tokens dynamically.
  - **Temperature:** A parameter (T) used to rescale the logits before applying softmax during sampling.
    - $logit' = logit / T$.
    - $T > 1$: Flattens the distribution, increases randomness/creativity.
    - $T < 1$: Sharpens the distribution, increases focus/determinism.
    - $T \approx 0$: Approaches greedy search.
    - $T = 1$: Original probabilities.

### Pros and Cons of LLMs

- **Pros:**

  - Versatile capabilities: QA, translation, summarization, code generation, creative writing, etc..
  - Can act as tutors, assistants, content creators.
  - Fluent and coherent text generation.
  - Can process and synthesize vast amounts of information.

- **Cons / Challenges:**
  - **Fallibility / Hallucinations:** LLMs can generate incorrect, nonsensical, or fabricated information with high confidence. **Tip 1: Check everything**. Examples: Math errors , image generation errors (counting) [cite: 977-980], outdated/wrong medical info.
  - **Deception & Misinformation:** Can be used to create realistic fake text, images, voices (deepfakes), potentially for malicious purposes [propaganda, scams]. **Tip 2: Use critical thinking**.
  - **Skill Atrophy:** Over-reliance might reduce human abilities in writing, critical thinking, problem-solving. Analogy: calculators didn't stop us learning math, but balance is needed. **Tip 3: Use in a balanced way**.
  - **Bias:** LLMs learn and can perpetuate societal biases (gender, race, stereotypes) present in their training data. Example: Gender stereotypes in translation.
  - **Environmental Impact:** Training and running large models consumes significant energy, contributing to CO2 emissions. Mitigation involves efficient models, renewable energy.
  - **Economic Inequality:** Access to the best models may be restricted by cost, creating a digital divide.
  - **Intellectual Property & Plagiarism:** Issues around training data ownership, copyright infringement (style imitation), and originality of generated content.
  - **Job Market Disruption:** Automation potential may displace jobs in content creation, customer service, etc., while creating new roles [e.g., prompt engineers, AI ethicists].

### Prompting

- **Concept:** The process of providing input instructions or queries to guide an LLM's output.
- **Zero-Shot Prompting:** Asking the model to perform a task without providing any examples in the prompt. Relies on the model's pre-trained knowledge.
- **Few-Shot Prompting:** Providing a few examples of the task (input/output pairs) within the prompt itself to guide the model at inference time. Does not update model weights. Example: Sentiment classification with examples [cite: 1024-1026].
- **Prompt Engineering:** The art and science of designing effective prompts to elicit desired responses from LLMs. (Importance may be decreasing as models improve).
- **Prompt Design Best Practices:** Be specific, provide context, experiment with phrasing. Automatic prompt optimization is an area of research.

- **Some Prompting Techniques:**
  - **Persona Pattern:** Instructing the LLM to adopt a specific role or persona ["Act as a [Persona X] and perform [Task Y]"]. Examples: Nutritionist , Chef , Pirate.
  - **Retrieval Augmented Generation (RAG):** Enhancing LLM responses by first retrieving relevant information from an external knowledge source (e.g., database, documents) and providing that information as context within the prompt. Useful for grounding responses in specific/current data without full fine-tuning.
  - **Chain-of-Thought (CoT) Prompting:** Encouraging the model to generate intermediate reasoning steps before giving the final answer ["Explain step-by-step..."]. Helps improve performance on complex reasoning tasks.

### Key Takeaways

- LLMs are powerful but complex tools with significant capabilities and limitations.
- Understanding training (pre-training, instruction tuning, RLHF) and inference (decoding strategies like sampling, temperature) is crucial.
- Prompting is key to interacting with LLMs; various techniques exist (Zero/Few-Shot, Persona, RAG, CoT).
- Awareness of LLM pros (versatility) and cons (fallibility, bias, societal impact) is essential for responsible use.

### Suggested Readings

- Stanford CS324 LLM Course [Percy Liang et al.].
- ChatGPT Prompt Engineering for Developers Course [OpenAI/DeepLearning.AI].

---

## 7. Machine Translation (T13-MT.pdf)

### Learning Objectives

- Focus on Machine Translation (MT) as a specific NLP task and understand its historical evolution.
- Relate MT concepts and techniques to those studied previously [metrics, architectures, etc.].

### Topics Covered

- Motivation & Challenges
- The MT Task (Text-to-Text, Speech-to-Speech)
- Classic MT Approaches (Direct, Transfer, Interlingua - Vauquois Triangle)
- Statistical Machine Translation (SMT)
- Deep Learning-Based MT (NMT, Multilingual Models)
- MT Evaluation (Shared Tasks, Datasets, Metrics - BLEU, COMET)

### Motivation

- **Goal:** Eliminate language barriers.
- **Ubiquity:** Widely used via tools like Google Translate.
- **Cost of Human Translation:** Significant economic cost, especially in multilingual environments like the EU.
- **Challenges:**
  - _Lexical Ambiguity:_ One word maps to multiple words or concepts [e.g., FR 'doudou'].
  - _Lexical Gaps:_ No direct equivalent [e.g., PT 'ser/estar' vs EN 'to be'].
  - _Collocations:_ Word combinations that sound natural but aren't compositional (e.g., 'missed the flight' vs. 'perdi o avião' (lit. lost the plane)).
  - _Structural Divergences:_ Differences in word order and grammatical structure between languages.
  - _Bias:_ MT models can perpetuate societal biases present in training data.

### The MT Task

- **Definition:** Using computers to automate translation between languages.
- **Text-to-Text:** The most common form.
- **Speech-to-Speech:** Involves Automatic Speech Recognition (ASR) -> MT -> Text-to-Speech Synthesis [TTS]. May include voice morphing.

### Approaches to MT

#### Classic MT (Pre-1990s)

- **Early Ideas:** Dictionary lookups, cryptography analogy [Weaver, 1949]. Georgetown-IBM demo (1954) showed basic feasibility but over-promised.
- **Direct Translation:** Word-by-word translation with minimal reordering/morphological adjustment. Fails often due to linguistic differences.
- **Vauquois Triangle (1968):** A pyramid illustrating MT approaches based on the depth of analysis:
  - _Base (Direct):_ Word-level translation.
  - _Middle (Transfer):_ Analyse source structure (syntax), transfer rules map it to target structure, generate target text. Requires bilingual transfer rules.
  - _Top (Interlingua):_ Analyse source text into an abstract, language-independent meaning representation (interlingua), then generate target text from this representation. Theoretically elegant (N languages need only 2N components vs N\*(N-1) for transfer), but defining a universal interlingua is very hard.

#### Statistical Machine Translation (SMT) (1990s - mid-2010s)

- **Foundation:** Uses probabilistic models learned from large parallel corpora [aligned sentences in source and target languages, e.g., EuroParl].
- **Noisy Channel Model Intuition:** Find the most probable target sentence $T'$ given source sentence $S$:
  $T' = \underset{T}{\operatorname{argmax}} P(T|S) = \underset{T}{\operatorname{argmax}} P(S|T) P(T)$ [using Bayes' theorem].
  - $P(T)$: **Language Model** (LM) - Probability of the target sentence $T$ being fluent/grammatical in the target language. Trained on monolingual target data.
  - $P(S|T)$: **Translation Model** (TM) - Probability that $S$ is a translation of $T$ (adequacy/faithfulness). Trained on parallel data.
- **Process:** Generate many translation hypotheses, score each using LM and TM probabilities, select the highest-scoring hypothesis. Word/phrase alignment is a key sub-problem.
- **Pros:** Achieved significant improvements over rule-based systems, language-pair independent [given data].
- **Cons:** Requires large parallel corpora, performance depends heavily on training data domain. Struggles with fluency and long-range dependencies.

#### Deep Learning-Based MT (Neural MT - NMT) (mid-2010s - Present)

- **Architecture Evolution:**
  - **RNN-based Seq2Seq:** Early NMT used Recurrent Neural Networks [encoder-decoder architecture].
  - **Attention Mechanism:** Added to Seq2Seq to allow the decoder to focus on relevant parts of the source sentence when generating each target word. Solved bottleneck issues.
  - **Transformers:** Replaced RNNs with self-attention mechanisms, allowing better parallelization and capturing long-range dependencies. State-of-the-art architecture.
- **Multilingual NMT:**
  - Single model trained on data from multiple languages.
  - Learns shared representations, enabling zero-shot or few-shot translation between language pairs not explicitly seen during training.
  - Uses both monolingual data (for language modeling within each language) and parallel data [for learning cross-lingual mappings].
  - Embeddings for similar words across languages tend to cluster together [e.g., "cat", "gato", "chat"].

### MT Shared Tasks, Datasets, and Metrics

- **Shared Tasks:** Competitive evaluations promoting research [e.g., WMT - Workshop/Conference on Machine Translation]. Include various tracks [news, biomedical, multimodal, sign language, quality estimation].
- **Datasets:** Large parallel and monolingual corpora are essential. Examples: WMT datasets, Europarl (EU proceedings), OpenSubtitles (movie subtitles via OPUS), MLQA.
- **Metrics:** Used to automatically evaluate translation quality against reference translations.
  - **BLEU:** Measures n-gram precision overlap, penalizes brevity. Widely used but correlates imperfectly with human judgment.
  - **METEOR:** Considers synonyms, stemming, and word order via alignment.
  - **TER (Translation Edit Rate):** Measures the number of edits needed to change the hypothesis to match the reference.
  - **COMET:** Newer metric using cross-lingual pre-trained models (like XLM-R) to predict human quality scores, often correlates better with human judgment.

### Key Takeaways

- MT automates translation, facing challenges like ambiguity, structural differences, and bias.
- MT history mirrors NLP: Rule-based -> Statistical (SMT) -> Neural [NMT].
- SMT uses language and translation models based on probabilities learned from parallel corpora.
- NMT (especially Transformer-based) is the current state-of-the-art, often using multilingual models.
- Evaluation relies on shared tasks, large datasets, and automatic metrics [BLEU, COMET, etc.].

### Suggested Readings

- Jurafsky: Chapter 25, Sections 25.2-25.9.
- A Statistical MT Tutorial Workbook, Kevin Knight, 1999.

---

## 8. Computational Linguistics Meets the Portuguese Sign Language (T13-SignLanguages.pdf)

_(Note: This section summarizes the specific case study presented on Portuguese Sign Language translation, complementing the general MT chapter.)_

### Outline

- Sign Languages (SL) & Portuguese Sign Language (LGP) Basics
- The Goal: EP <-> LGP Translation
- Evolution of a Project (Pet Project -> Corpus Project -> Current State)
- Challenges and Future Work

### Sign Languages and LGP

- **Sign Languages:** Natural, visual-gestural languages used primarily by Deaf communities. Utilize handshapes, movements, orientation, body language, and facial expressions [cite: 1249-1252].
- **Distinct Languages:** SLs have unique vocabularies and grammars; they are NOT signed versions of spoken languages. ASL != BSL; LGP != Libras [Brazilian SL].
- **LGP (Língua Gestual Portuguesa):** Officially recognized in Portugal since 1997. Resources are limited but include dictionaries, courses, and some academic research [cite: 1319-1326].

### The Dream: EP <-> LGP Translation

- Develop a free, open-source, real-time translator between European Portuguese (EP) spoken/written language and LGP, typically involving an animated avatar for output.
- **Intermediate Representation:** Translation often goes from EP text to a sequence of **glosses** (written labels representing signs, usually in the spoken language), which then drive the avatar animation. LGP has a different grammatical structure than EP (e.g., `WOMAN KING BEACH GO` for "The queen went to the beach").

### Project Evolution

#### The Pet Project (2014-2016)

- **Goal:** Build an initial EP-to-LGP translator prototype.
- **NLP Module v0:** Rule-based pipeline: Tokenize -> Lemmatize -> POS Tag -> NER -> Lexical Transfer (EP word to LGP gloss/components) -> Syntactic Reordering Rules -> Final Gloss Sequence.
- **Avatar Module v0/v1:** Development of tools to create sign animations for a virtual avatar, initially using motion capture (Kinect), later exploring phonetic transcription systems like HamNoSys and SignWriting mapped to avatar controls [SiGML].

#### The Project: Corpus & Avatar da LGP (2018-2021)

- **Partners:** INESC-ID & Universidade Católica Portuguesa.
- **Goals:** Create the first substantial annotated LGP corpus; develop an improved EP2LGP translator based on this corpus.
- **Corpus Creation:** Collected ~110 hours of LGP video data; annotated ~5 hours using ELAN software with multiple tiers [EP translation, LGP glosses, lemmas, syntax, etc.].
- **NLP Module Improvement:** Used the annotated corpus to refine the rule-based translation system (EP2LGP5.0), extracting bilingual dictionary entries and syntactic reordering rules based on dependency parses and alignments [See Section 3 - Real Application Example].

#### Current State (2023-2024)

- **Rule Application:** Used the improved rule-based system to generate a larger, synthetic EP-LGP parallel gloss corpus from monolingual EP text.
- **Deep Learning:** Trained Neural Machine Translation (NMT) models (Seq2Seq, Transformers like M2M) on the combined real and synthetic parallel data. Showed promising results, sometimes outperforming the rule-based system, sometimes not [especially on complex structures learned by rules].
- **Avatar:** Continued development of avatar animation tools and sign database [~1000 signs animated].

### Next? Challenges & Future Work

- **Funding:** Securing resources for continued development.
- **Data:** Need for larger, more diverse annotated LGP corpora.
- **Grammar & Avatar:** Continued refinement of LGP grammatical rules representation and avatar naturalness/expressiveness.
- **Lexicon:** Expanding the animated sign lexicon; exploring crowdsourcing and validation methods.
- **Accessibility:** Developing a free, user-friendly avatar platform.
- **Functionality:** Building LGP sign search engines.
- **Bidirectionality:** Developing LGP-to-EP translation (sign recognition).

### Key Takeaways

- Sign Languages are distinct natural languages with their own grammars.
- Computational processing of SLs faces significant challenges, primarily the lack of large datasets compared to spoken languages.
- MT for SL often involves intermediate gloss representations and requires handling multimodality (hands, face, body) for generation (avatar) or recognition.

---
