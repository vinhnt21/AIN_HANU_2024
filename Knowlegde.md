# Knowledge

## 1. Knowledge

### 1.1. Knowledge-Based Agents

- **Definition:** Agents that reason using internal knowledge representations.
- **Purpose:** To draw conclusions from existing knowledge.

### 1.2. Sentence

- **Definition:** An assertion about the world in a knowledge representation language.
- **Example Sentences:**
  - "If there is no rain, I learn AIN."
  - "I learn AIN or play FIFA, but not both."
  - "I play FIFA."
  - **Conclusion:** It rained today.

## 2. Propositional Logic

### 2.1. Propositions

- **Definition:** Statements that are either true or false.

### 2.2. Symbols

- **Definition:** Letters representing propositions (e.g., P, Q, R).

### 2.3. Logic Connectives

- **AND (∧):**

  - Example:
    - \( P \): "The color of the sky is red."
    - \( Q \): "2+2 is 4."
    - \( P \land Q \): "The sky is red and 2+2 is 4."
    - \( (P \land P) = \text{False} \)

- **OR (∨):**

  - Example:
    - \( P \): "The Sun is a small planet."
    - \( Q \): "Earth is a planet."
    - \( P \lor Q \): "The Sun is a small planet or Earth is a planet."
    - \( (P \lor Q) = \text{True} \)

- **NOT (¬):**

  - Example:
    - \( P \): "It is raining."
    - \( \neg P \): "It is not raining."

- **Implication (→):**

  - Example:
    - \( P \): "Juan passes the exam."
    - \( Q \): "Juan's mother will give him a gift."
    - \( P \rightarrow Q \): "If Juan passes the exam, his mother will give him a gift."

- **Biconditional (↔):**
  - Example:
    - \( P \): "A triangle is equilateral."
    - \( Q \): "The three sides of a triangle are equal."
    - \( P \leftrightarrow Q \): "A triangle is equilateral if and only if its three sides are equal."
    - \( V(P \leftrightarrow Q) = \text{True} \)

### 2.4. Knowledge Base

- **Definition:** A set of known sentences.
- **Use:** To make inferences about the world.

### 2.5. Model

- **Definition:** An assignment of truth values to propositions.
- **Example:**
  - \( P \): "The shop is open."
  - \( Q \): "It's a holiday."
  - Possible models:
    - \{P = True, Q = True\} - The shop is open, and it’s a holiday.
    - \{P = True, Q = False\} - The shop is open, and it’s not a holiday.

### 2.6. Entailment (⊨)

- **Definition:** If \( \alpha \models \beta \), then \( \beta \) is true in all models where \( \alpha \) is true.
- **Example:**
  - \( \alpha \): "Today is a Monday in March."
  - \( \beta \): "Today is in March."
  - \( \alpha \models \beta \)

## 3. Inference

### 3.1. Process

- **Definition:** Deriving new sentences from existing ones.

### 3.2. Model Checking

- **Definition:** Enumerate all models to check entailment.

## 4. Inference Rules

### 4.1. Modus Ponens

- **Rule:** If \( P \rightarrow Q \) and \( P \), then \( Q \).
- **Example:**
  - "If I eat too much candy, I'll get a sugar rush."
  - "I ate too much candy. Therefore, I'm bouncing off the walls!"

### 4.2. And Elimination

- **Rule:** From \( P \land Q \), infer \( P \) or \( Q \).
- **Example:**
  - "I have a pen and a notebook."
  - "Therefore, I have a pen."

### 4.3. Double Negation

- **Rule:** \( \neg\neg P \) is equivalent to \( P \).
- **Example:**
  - "It is not true that I don't have a car."
  - "Therefore, I have a car."

### 4.4. Implication Elimination

- **Rule:** \( P \rightarrow Q \) is equivalent to \( \neg P \lor Q \).
- **Example:**
  - "If I wear my lucky socks, my team will win."
  - "Therefore, if my team loses, I forgot my socks."

### 4.5. Biconditional Elimination

- **Rule:** \( P \leftrightarrow Q \) is equivalent to \( (P \rightarrow Q) \land (Q \rightarrow P) \).
- **Example:**
  - "I will go to the party if and only if you go."
  - "Therefore, if I go, you go, and if you go, I go."

### 4.6. De Morgan’s Laws

- **Rule:** Transformations between AND/OR with negations.
- **Example:**
  - "It's not true that I will both clean my room and do my homework."
  - "Therefore, I will either not clean my room or not do my homework. (Probably both!)"
  - \((\text{Clean} \land \text{Homework}) \rightarrow \neg \text{Clean} \lor \neg \text{Homework}\)

## 5. Knowledge Engineering

### 5.1. Process

- **Definition:** Representing propositions and logic in AI.

## 6. Resolution

### 6.1. Definition

- **Definition:** An inference rule using complementary literals.

### 6.2. Application

- **Application:** Convert to Conjunctive Normal Form (CNF).

### 6.3. Example

- **Example:**
  - \((A \rightarrow B) \land (\neg C \lor D) \rightarrow (\neg A \lor B) \land (\neg C \lor D)\)

## 7. First Order Logic

### 7.1. Symbols

- **Definition:** Constant and Predicate symbols.

### 7.2. Quantification

- **Universal (∀):** True for all instances.
- **Existential (∃):** True for at least one instance.

## 8. Explain Code

### 8.1. logic.py

- **Definition:** Defines a framework to represent logical sentences and perform logical inference using basic components like AND, OR, NOT, and others.

#### Classes

- **Sentence:**

  - **Base Class:** Abstract base class for all logical sentences.
  - **Methods:**
    - `validate(sentence)`: Ensures the sentence is an instance of Sentence.
    - `parenthesize(s)`: Adds parentheses to a string if needed.
    - `evaluate(model)`: Evaluates the logical value of the sentence based on a given model.
    - `formula()`: Returns a string representation of the sentence.
    - `symbols()`: Returns a set of all symbols in the sentence.

- **Symbol(Sentence):**

  - Represents a simple logical symbol.
  - **Methods:**
    - `__init__(name)`: Initializes with the name of the symbol.
    - `evaluate(model)`: Returns the value of the symbol in the model.
    - `formula()`: Returns the name of the symbol.
    - `symbols()`: Returns a set containing the name of the symbol.

- **Not(Sentence):**

  - Represents logical negation.
  - **Methods:**
    - `__init__(operand)`: Initializes with a single operand.
    - `evaluate(model)`: Returns the negation of the operand's value.
    - `formula()`: Returns the negated formula of the operand.
    - `symbols()`: Returns the set of symbols in the operand.

- **And(Sentence):**

  - Represents logical conjunction (AND).
  - **Methods:**
    - `__init__(*conjuncts)`: Initializes with one or more conjuncts.
    - `evaluate(model)`: Returns True if all conjuncts are true.
    - `formula()`: Returns the "and" formula of the conjuncts.
    - `symbols()`: Returns the set of symbols in all conjuncts.

- **Or(Sentence):**

  - Represents logical disjunction (OR).
  - **Methods:**
    - `__init__(*disjuncts)`: Initializes with one or more disjuncts.
    - `evaluate(model)`: Returns True if at least one disjunct is true.
    - `formula()`: Returns the "or" formula of the disjuncts.
    - `symbols()`: Returns the set of symbols in all disjuncts.

- **Implication(Sentence):**

  - Represents logical implication.
  - **Methods:**
    - `__init__(antecedent, consequent)`: Initializes with an antecedent and a consequent.
    - `evaluate(model)`: Returns True if the antecedent is false or the consequent is true.
    - `formula()`: Returns the implication formula.
    - `symbols()`: Returns the set of symbols in the antecedent and consequent.

- **Biconditional(Sentence):**
  - Represents logical biconditional (if and only if).
  - **Methods:**
    - `__init__(left, right)`: Initializes with two expressions.
    - `evaluate(model)`: Returns True if both expressions have the same logical value.
    - `formula()`: Returns the biconditional formula.
    - `symbols()`: Returns the set of symbols in both expressions.

#### model_check(knowledge, query)

- **Definition:** Checks if the knowledge base entails the query.
- **How it Works:**
  - `check_all(knowledge, query, symbols, model)`: Recursively checks all possible models.
  - Creates models with True and False values for each symbol.
  - Ensures that if the knowledge base is true in a model, the query must also be true.

### 8.2. clue.py, harry.py, mastermind.py, puzzle.py

- **Definition:** Examples of using the logic.py framework
- Detail in `01_puzzle_explanation.ipynb`, `02_clue_explanation.ipynb`, `03_harry_explanation.ipynb`, `04_mastermind_explanation.ipynb`.
