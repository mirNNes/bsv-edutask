# Assignment 1 – The Test Design Technique

## Work distribution

The work was divided between us both. Robin prepared the initial drafts for parts of the assignment, and Mirnes reviewed and improved different parts. All parts were discussed and checked by us both.

---

## 1. Test Design Technique

The test design technique is a structured way of creating test cases. It helps to systematically go from a scenario to a complete set of test cases.

The technique consists of these four steps:

### Step 1: Identify actions and expected outcomes

First, we identify what actions are performed in the scenario and what possible outcomes exist. This step focuses on understanding what the system does and what results we expect.

### Step 2: Identify conditions

Next, we identify the conditions that influence the outcome. Conditions are variables or factors that affect the system behavior, such as input values or states.

### Step 3: Determine combinations

Then, we combine the different conditions to create relevant test cases. In simple cases, all combinations can be tested. In more complex cases, we may filter combinations using domain knowledge, which means understanding how the system is expected to work in practice.

### Step 4: Define expected outcomes

Finally, for each combination, we define the expected outcome. This is based on the specification or understanding of how the system should behave.

### How the technique helps

The test design technique helps to create test cases in a structured way by:

- breaking down the problem into clear steps
- ensuring that important conditions are not missed
- making test cases systematic instaed of random
- making it easier to understand and review the tests

---

## 2. Boundary Value Analysis and Equivalence Partitioning

### Boundary Value Analysis (BVA)

Boundary value analysis focuses on testing values around boundaries where the system behavior changes.

The idea is that errors often occur at the edges of input ranges. So typical test values are therefore just below or above the boundary.

### Equivalence Partitioning (EP)

Equivalence partitioning divides input values into groups (partitions) where all values are expected to behave the same. Instead of testing all values, we select one representative value from each partition, which makes testing more effective.

---

### Comparison of BVA and EP

- BVA focuses on edge cases (boundaries)
- EP focuses on groups of values with similar behavior

They are often used together:

- EP reduces the number of test cases
- BVA ensures that critical edge cases are tested

---

### Application to age validation

The system defines:

- age < 0 → impossible
- age > 120 → impossible
- age < 18 → underage
- age ≥ 18 → valid

#### Equivalence partitions

We can divide the input into the following partitions:

1. age < 0 → impossible
2. 0 ≤ age < 18 → underage
3. 18 ≤ age ≤ 120 → valid
4. age > 120 → impossible

#### Boundary values

The important boundaries are:

- 0
- 18
- 120

Using BVA, we test values around these, so it could be:

- -1, 0, 1
- 17, 18, 19
- 119, 120, 121

---

## 3. Designing Test Cases

### Actions

- Hold company card to sensor
- Porter unlocks door
- Open door from inside

### Conditions

- Card validity: valid / invalid
- Time at sensor: < 2 seconds / ≥ 2 seconds
- Porter unlock: yes / no
- Location: outside / inside

---

### Combinations and expected outcomes

| Card Valid | Time ≥ 2s | Porter Unlock | Location | Expected Outcome  |
| ---------- | --------- | ------------- | -------- | ----------------- |
| valid      | yes       | no            | outside  | door opens        |
| valid      | no        | no            | outside  | door stays closed |
| invalid    | yes       | no            | outside  | door stays closed |
| invalid    | no        | no            | outside  | door stays closed |
| any        | any       | yes           | outside  | door opens        |
| any        | any       | no            | inside   | door opens        |

---

### Explanation

- A valid card must be held for at least 2 seconds to open the door from outside
- The porter can unlock the door regardless of other conditions
- From inside, the door can always be opened

---

## Final comment

The test design technique helps ensure that all relevant cases are covered in a structured way. By combining conditions and defining expected outcomes, we can systematically design meaningful test cases.
