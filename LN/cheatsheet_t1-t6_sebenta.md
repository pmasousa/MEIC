# LN Class Cheatsheet

## VOYAGE: Introduction to NLP

### Natural Language

- **Definition:** A language that has evolved naturally in humans through use and repetition rather than being artificially constructed. It has its own grammatical system and rules and is used for communication.
- **Example:** Portuguese, English, Portuguese Sign Language.

### Natural Language Processing (NLP)

- **Definition:** A field of Artificial Intelligence and Linguistics concerned with the interactions between computers and human (natural) languages.

### Paraphrases

- **Definition:** Two sentences with the same meaning.
- **Example:** "Switch on the light!" and "Could you please, switch on the light".

### Lexical Ambiguity

- **Definition:** A word has multiple meanings.

### Syntactic Ambiguity

- **Definition:** A sentence has multiple parse trees.
- **Example:** "I saw the man on the hill with a telescope."

### Ellipsis

- **Definition:** The omission of a word or words that are able to be understood from contextual clues.

### Co-reference

- **Definition:** Elements of a text that have the same reference.

## CORPORA: Building and Using Datasets

### Corpora

- **Definition:** A collection of texts. (Corpora is plural, corpus is singular).

### Inter-annotator Agreement

- **Definition:** A measure of how well two or more annotators can make the same annotation decision for a certain category.

### Wizard of Oz experiment

- **Definition:** An experiment in which subjects interact with a computer that they believe to be autonomous, although it is being operated by an unseen human.

### Data Splits

- **Train set:** Used to train the model.
- **Test set:** Used to evaluate the performance of the model after training. It tests the model's ability to generalize to new, unseen data and is NOT used during training.
- **Validation set:** Used during the tuning process to adjust hyperparameters (e.g., learning rate, depth, regularization) without touching the test set. It must remain independent from the test set.
- **Development set:** Used like a validation set, sometimes also for preliminary assessment of the models. Often used interchangeably with validation set.
- **Reference:** A set of data used as a benchmark or standard when comparing different models or validating model outputs.
- **Gold standard or gold collection:** A meticulously curated dataset of the highest quality, often serving as a benchmark.
- **K-fold cross-validation:** A technique to divide the dataset into K equal parts (folds/splits) and run K experiments. Each fold is used once as a test set while the remaining K-1 folds form the training set.

### Data Augmentation

- **Synonym replacement:** Substitutes words in sentences with their synonyms.
- **Paraphrasing:** Rewrites sentences or paragraphs differently. Can include rule-based augmentation (e.g., changing active to passive voice), back translation (translating to another language and back), and random swap (randomly swapping word positions).
- **Text expansion:** Enriches content with additional relevant text, such as explanatory clauses or descriptive phrases.
- **Noise injection:** Introduces typos, spelling mistakes, or grammatical errors to mimic real-world imperfections.
- **Entity substitution:** Replaces named entities (like names, locations, organizations) with other entities of the same type.

### Data Cleaning

- **Definition:** Also known as denoising, it involves the detection and rectification of errors and inconsistencies in datasets.

### Toxic Data

- **Definition:** Various forms of harmful, offensive, or inappropriate content that can manifest in text.
- **Examples:**
  - **Profanity:** Use of swear/curse words.
  - **Threats, Insults:**.
  - **Cyberbullying:** Repeated online behaviors that intimidate or upset individuals.
  - **Misinformation:** The unintentional spread of false or misleading information.
  - **Disinformation:** The deliberate spread of false or misleading information.
  - **Stereotyping and generalizations:** Statements that apply a generalized belief or opinion to all members of a group.
  - **Hate speech:** Communication that demeans a person or group based on characteristics such as race, religion, ethnic origin, sexual orientation, disability, or gender.

## SIM AND METRICS: Similarity and Evaluation

### Comparing Strings

- **Distance vs. Similarity:** Distance metrics quantify dissimilarity (higher value = less similar), while similarity metrics quantify similarity (higher value = more similar).

### Edit-based Metrics

- **Definition:** Quantify how dissimilar two strings are by counting the minimum number of operations required to transform one string into the other.
- **Levenshtein distance:** An edit-based metric that calculates the minimum number of insertions, deletions, or substitutions required to change one sequence into the other.
- **Longest Common Subsequence (LCS) distance:** Allows only insertion and deletion operations, not substitution.
- **Hamming distance:** Allows only substitution (applies only to strings of the same length).
- **Damerau–Levenshtein distance:** Allows insertion, deletion, substitution, and the transposition (swapping) of two adjacent characters.
- **Jaro distance:** Allows only transposition.

### Token-based Similarity Metrics

- **Jaccard(s, t):** `|s ∩ t | / | s ∪ t |` (where s and t are sets of tokens).
- **Dice(s, t):** `2 x |s ∩ t | / (| s | + | t |)` (where s and t are sets of tokens).
- **Overlap(s, t):** `|s ∩ t | / min(| s |, | t |)` (where s and t are sets of tokens).

### Sound-level String Comparison

- **Soundex:** A phonetic algorithm for indexing names by sound, as pronounced in English. It retains the first letter and replaces consonants with digits, dropping vowels and 'h', 'w'. Other similar algorithms include Metaphone.

## N-GRAMS: Language Models

### Language Models

- **Definition:** Models that learn the probability distribution of words, i.e., how words can be organized to create meaningful and grammatically correct sentences.
- **Applications:**
  - Predicting the next word in a text.
  - Determining the likelihood of a sequence of words.

### N-grams

- **Definition:** A sequence of N tokens (words, characters, or subwords).
- **Types:**
  - **Unigrams:** N=1
  - **Bigrams:** N=2
  - **Trigrams:** N=3

### Word Prediction with N-grams

- **Markov Assumption:** The probability of a future event can be calculated without looking at the entire history. This allows for approximations using bigrams or trigrams.
- **Bigram Model:** `P(Wn | W1...Wn-1) ≅ P(Wn | Wn-1)`
- **Trigram Model:** `P(Wn | W1...Wn-1) ≅ P(Wn | Wn-2Wn-1)`

### Sentence Probability with N-grams

- **Chain Rule of Probability:** `P(w1...wn) = P(w1|<s>) * P(w2|<s>w1) * ... * P(wn|w1...wn-1)`
- **Bigram Approximation:** `P(w1...wn) ≅ ∏ P(wi|wi-1)`
- **Trigram Approximation:** `P(w1...wn) ≅ ∏ P(wi|wi-2wi-1)`

### Perplexity

- **Definition:** An evaluation metric for N-gram models. A lower perplexity value indicates a better model.

### Smoothing

- **Definition:** Techniques to handle unseen or infrequent sequences in the training data.
- **Laplace (Add-one) Smoothing:** Adds 1 to all counts to avoid zero probabilities.
- **Good-Turing Discounting:** Estimates the probabilities of things that occur _c_ times using the counts of things that occurred _(c+1)_ times.

## PREPROC: Preprocessing and Regular Expressions

### Tokenization

- **Definition:** The process of breaking down a stream of text into smaller, manageable units called tokens.
- **Character-level:** Splits text into individual characters. Manages out-of-vocabulary (OOV) words but carries little context.
- **Word-level:** Splits text into individual words based on spaces and punctuation. Intuitive but struggles with unknown words and requires language-specific rules.
- **Subword-level:** Splits words into smaller meaningful units (prefixes, suffixes, etc.). Combines the benefits of character- and word-level tokenization and is widely used.

### Normalization

- **Definition:** A preprocessing step that transforms raw text into a “standardized” format to reduce noise and linguistic variability.
- **Techniques:**
  - **Remove stop words:** Removing common functional words (e.g., "a", "the").
  - **Remove punctuation:** Removing punctuation marks.
  - **Lowercasing:** Converting all text to lowercase.

## VECTORS AND FEATURE-BASED: Representing Language

### Language as Vectors (Sparse)

- **Distributional Semantics:** The idea that the meaning of a word is given by the set of contexts in which it occurs. Words with similar distributional properties have similar meanings.
  - **Harris (1954):** "If A and B have almost identical environments […] we say that they are synonyms."
  - **J.R.Firth (1957):** "You shall know a word by the company it keeps."

### Documents as Vectors

- **Vector Space Model:** A model for representing a text document as a vector.
- **Term-Document Matrix:** A matrix where each row represents a term in the vocabulary and each column represents a document.
- **Methods for Building the Matrix:**
  - **Binary:** Elements are 1 if the word occurred in the document, 0 otherwise.
  - **Raw count:** Elements are the raw frequency of occurrence of the word in the document.
  - **TF-IDF (Term Frequency-Inverse Document Frequency):** Combines term frequency (TF) with inverse document frequency (IDF).
    - **TF(t, d):** Term _t_ frequency in document _d_ (can be count or relative frequency).
    - **IDF(t, D):** `log (|D|/|{d ∈ D: t ∈ d}|)`, where `|D|` is the number of documents and `|{d ∈ D: t ∈ d}|` is the number of documents containing term _t_.

### Words as Vectors

- **Dual Role:** A word can be a dimension (documents as vectors) or a vector itself (words as vectors).
- **Term-Term Matrix (Word-Word Matrix or Term-Context Matrix):** Considers the words' context to build a matrix where words are represented as vectors.
- **High-dimensional vs. Dense Vectors:**
  - **Sparse Vectors:** High-dimensional (length = |V|, 10,000-50,000), most entries are 0. Requires dimensionality reduction.
  - **Dense Vectors:** Short vectors (50-1,000 dimensions), most entries ≠ 0.

### Similarity/Distance Metrics for Vectors

- **Cosine Similarity:** Measures the cosine of the angle between two vectors. A cosine of 1 indicates maximal similarity (angle is zero), and smaller values indicate less similarity.

### Feature Engineering

- **Definition:** A machine learning approach where domain knowledge is used to extract features from raw data to improve the performance of machine learning algorithms.

### Classification Algorithms

- **Naïve Bayes (NB) Classifier:** A family of algorithms that apply Bayes theorem and assume features are independent to predict the category of a given sample.
  - **Drawbacks:** Independence assumption (features are often not independent) and "zero-frequencies" (can be solved with smoothing techniques).

### Forensic Linguistics

- **Definition:** Application of linguistic knowledge, methods, and insights to the forensic context of law, language, crime investigation, trial, and judicial procedure.

## DEEP LEARNING: Neural Network Architectures

### Deep Learning Architectures

- **Feedforward Neural Networks (FFNN):**

  - **Definition:** A type of neural network where connections between the nodes do not form a cycle. Information moves in only one direction—forward—from the input nodes, through the hidden nodes (if any) and to the output nodes.
  - **Problems:** Inputs are independent of each other, and it's unable to handle variable-length inputs, which is a limitation for many NLP tasks.

- **Recurrent Neural Networks (RNNs):**

  - **Definition:** A type of neural network where connections between nodes form a directed graph along a temporal sequence. This allows it to exhibit temporal dynamic behavior. It has a "memory" which captures information about what has been calculated so far.
  - **Backpropagation Through Time (BPTT):** The adaptation of backpropagation for RNNs.
  - **Extensions:**
    - **Long Short-Term Memory (LSTM):** A type of RNN architecture that is well-suited to learn from experience to classify, process and predict time series when there are very long time lags of unknown size between important events.
    - **Gated Recurrent Unit (GRU):** A gating mechanism in recurrent neural networks, similar to an LSTM, but with fewer parameters.
    - **Bidirectional RNNs:** An RNN architecture where the output at a given time step depends on both previous and future elements in the sequence.

- **Sequence to Sequence Models (Seq2Seq):**

  - **Definition:** An encoder-decoder architecture where the encoder processes the input and encodes the information into a fixed-length context vector, which is then used by the decoder to generate the output.
  - **Teacher Forcing:** A training technique for sequence prediction tasks where the actual output from the training dataset at the current time step is used as the input at the next time step, rather than using the output generated by the model.

- **Autoencoders:**

  - **Definition:** A type of neural network used to learn efficient data codings in an unsupervised manner. The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”.
  - **Denoising Autoencoders:** A variation of autoencoders where the model is trained with noisy input data and clean target data to learn to remove noise.

- **Generative Adversarial Networks (GANs):**

  - **Definition:** A deep neural net architecture comprised of two nets, a generator and a discriminator, pitting one against the other. The generator creates new data instances, and the discriminator evaluates them for authenticity.

- **Attention Mechanisms:**

  - **Definition:** A mechanism loosely based on the visual attention mechanism found in humans, which allows a model to focus on relevant parts of the input sequence when producing an output.
  - **Types:**
    - **Soft vs. Hard Attention:** Soft attention weighs the importance of different parts of the input, while hard attention selects specific parts to focus on.
    - **Self-attention (Intra-attention):** Models how some parts of a sentence relate to other parts of the same sentence.
    - **Multi-Head Attention:** An extension of self-attention that runs several attention mechanisms in parallel to capture different types of relationships.

- **Transformers:**
  - **Definition:** A deep learning architecture based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. It uses self-attention to gather information about the relevant context of a given word and then encodes that context in the vector that represents the word.
  - **Positional Encoding:** Used to represent the order of the sequence, since the Transformer architecture does not have a notion of word order.

## Sebenta

### Natural Language

- **Definition:** A language that has evolved naturally through human communication, with its own grammatical system and rules. (Repeated in: VOYAGE)

### Linguistic Variability

- **Definition:** The possibility of expressing the same thing in many different ways.

### Ambiguity

- **Definition:** The fact that words, expressions, or sentences can have several meanings.

### Lexical Ambiguity

- **Definition:** A word has multiple meanings. (Repeated in: VOYAGE)

### Syntactic Ambiguity

- **Definition:** A sentence has multiple possible syntactic structures. (Repeated in: VOYAGE)

### PP-attachment problem

- **Definition:** A specific case of syntactic ambiguity where it is unclear which word a prepositional phrase attaches to.

### Phonology

- **Definition:** The study of the relationship between words and sounds.

### Morphology

- **Definition:** The study of words and their meaningful units (morphemes).

### Syntax

- **Definition:** The study of how words can be combined to form sentences.

### Semantics

- **Definition:** The study of the literal meaning of words and sentences.

### Pragmatics

- **Definition:** The study of how context contributes to meaning.

### Discourse

- **Definition:** The study of language beyond the sentence level, including how objects are referred to across a text (co-reference).

### Corpora

- **Definition:** A collection of texts. (Repeated in: CORPORA)

### Inter-annotator Agreement

- **Definition:** A measure of how much consensus there is in the ratings given by judges on a task. (Repeated in: CORPORA)

### Tokenization

- **Definition:** The process of identifying tokens (words or other units) in a text. (Repeated in: PREPROC)

### N-grams

- **Definition:** Sequences of N words (or other tokens). (Repeated in: N-GRAMS)

### Minimum Edit Distance (MED)

- **Definition:** The minimum number of transformations (insert, replace, delete) needed to change one word into another. (Repeated in: SIM AND METRICS)

### Jaccard and Dice Coefficients

- **Definition:** Similarity measures used to compare the similarity of sets. (Repeated in: SIM AND METRICS)

### Soundex

- **Definition:** A phonetic algorithm for indexing names by their sound, as pronounced in English. (Repeated in: SIM AND METRICS)

### Term Frequency–Inverse Document Frequency (tf–idf)

- **Definition:** A numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. (Repeated in: VECTORS AND FEATURE-BASED)

