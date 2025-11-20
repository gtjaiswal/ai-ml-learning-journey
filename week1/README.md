# Week 1 Learning Schedule - AI/ML Foundations

## Overview
A comprehensive 7-day learning plan covering mathematical foundations, Python libraries, and practical machine learning implementations. Total commitment: ~13-14 hours.

---

## Week Schedule

| Day | Date | Topic | Time |
|-----|------|-------|------|
| Mon | Nov 17 | Vectors & Linear Algebra ✅ | 1h |
| Tue | Nov 18 | Matrices (partial) ✅ | 1h |
| Wed | Nov 19 | Matrices (complete) ✅ | 2-3h |
| Thu | Nov 20 | Probability fundamentals | 1h |
| Fri | Nov 21 | Distributions & statistics | 1h |
| Sat | Nov 22 | **NumPy + Scikit-learn basics** | 4h |
| Sun | Nov 23 | Pandas & data analysis | 3h |

**Total Week 1:** ~13-14 hours

---

## Day 1: Vectors & Linear Algebra

### Primary Video Resources

#### 3Blue1Brown - Essence of Linear Algebra

**Video 1: "Vectors, what even are they?"**
- Link: https://www.youtube.com/watch?v=fNk_zzaMoSs
- Duration: 9:52
- What you'll learn: Geometric and numeric view of vectors

**Video 2: "Linear combinations, span, and basis vectors"**
- Link: https://www.youtube.com/watch?v=k7RM-ot2NWY
- Duration: 9:59
- What you'll learn: How vectors combine to create vector spaces

**Full Playlist (bookmark for future):**
- Link: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- All 16 chapters - you'll use more throughout the course

### Interactive Practice (Khan Academy)

**Khan Academy Linear Algebra Course:**
- Main page: https://www.khanacademy.org/math/linear-algebra
- Start with "Vectors and spaces" section
- Specific for Monday: "Vector intro for linear algebra"
  - Link: https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/vector-introduction-linear-algebra

**Practice Exercises:**
- Vector addition: https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/e/vector_addition_and_subtraction
- Vector scaling: https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/e/vector-scaling

### Reading Materials (Optional but Helpful)

**Visual Introduction to Vectors**
- Better Explained: "An Intuitive Guide to Linear Algebra"
  - Link: https://betterexplained.com/articles/linear-algebra-guide/
- Quick read, excellent visual explanations

**AI/ML Context (Why This Matters)**
- Article: "A Gentle Introduction to Vectors for Machine Learning"
  - Link: https://machinelearningmastery.com/gentle-introduction-vectors-machine-learning/
  - Duration: 10-15 min read
  - Connects vectors directly to ML applications

### Day1's Schedule (60 minutes total)

**Recommended Order:**

1. **Watch: 3Blue1Brown Video 1** (10 min)
   - "Vectors, what even are they?"
   - Take notes on key concepts

2. **Watch: 3Blue1Brown Video 2** (10 min)
   - "Linear combinations, span, and basis vectors"
   - Pause and rewind as needed

3. **Read: Better Explained article** (10 min)
   - Get alternative explanation
   - Connect concepts

4. **Practice: Draw on paper** (15 min)
   - Draw 3-4 vectors on graph paper
   - Practice vector addition visually
   - Try vector subtraction

5. **Reflect and Note-take** (15 min)
   - Write in your own words: "What is a vector?"
   - Answer: "Why do we care about vectors in AI/ML?"
   - List 2-3 things that are still unclear (totally normal!)

### Success Criteria

After Day1's session, you should be able to:

- ✅ Explain what a vector is (geometrically and numerically)
- ✅ Draw vector addition on paper
- ✅ Understand that vectors can represent data points
- ✅ See the connection to AI (data is vectors, embeddings are vectors)
- ✅ Have specific questions written down for further exploration

You do NOT need to:

- ❌ Memorize formulas
- ❌ Do complex calculations
- ❌ Understand eigenvectors or matrix decomposition (that's advanced)
- ❌ Write any code yet

### End of Day1 Checklist

- [ ] Watched both 3Blue1Brown videos
- [ ] Read at least one supplementary article
- [ ] Drew vectors on paper and practiced addition
- [ ] Wrote notes answering: "What is a vector and why does AI use them?"
- [ ] Have 2-3 questions written down for further exploration
- [ ] Spent approximately 60 minutes total

---

## Day 2-3: Matrices

### Primary Video Resources

#### 3Blue1Brown - Essence of Linear Algebra (Continued)

**Video 3: "Linear transformations and matrices"**
- Link: https://www.youtube.com/watch?v=kYB8IZa5AuE
- Duration: 10:58
- What you'll learn: Matrices as functions that transform vectors

**Video 4: "Matrix multiplication as composition"**
- Link: https://www.youtube.com/watch?v=XkY2DOUCWMU
- Duration: 10:03
- What you'll learn: Intuitive understanding of matrix multiplication

**Alternative: "Matrix multiplication" (shorter intro)**
- Link: https://www.youtube.com/watch?v=kT4Mp9EdVqs
- Duration: 4:54
- Watch this FIRST if the longer videos feel overwhelming

### Interactive Practice (Khan Academy)

**Introduction to Matrix Multiplication:**
- Video intro: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/v/matrix-multiplication-intro
- Duration: 10:22

**Practice Exercises:**

1. **Multiply matrices**
   - Link: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/e/matrix_multiplication
   - Do at least 5-10 problems

2. **Matrix dimensions**
   - Link: https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:properties-of-matrix-multiplication/e/matrix-product-dimensions

### Reading Materials

**Article: "A Programmer's Intuition for Matrix Multiplication"**
- Link: https://betterexplained.com/articles/matrix-multiplication/
- Duration: 10-15 min read

**Interactive Visualization**
- Link: http://matrixmultiplication.xyz/
- Play with it to see how multiplication works

### ML/AI Context

**Video: "But what is a neural network?"** (3Blue1Brown)
- Link: https://www.youtube.com/watch?v=aircAruvnKk
- Duration: 19:13
- Watch from 3:00-8:00 to see matrices in action

### Day2/3's Schedule (60 minutes total)

1. **Watch: Shorter matrix video** (5 min)
2. **Watch: Linear transformations** (11 min)
3. **Watch: Matrix composition** (10 min)
4. **Read: Better Explained article** (10 min)
5. **Practice: Khan Academy** (15 min)
6. **Reflect and Note** (9 min)

### Practice Problems

**Problem 1: Basic 2x2**
```
[1  2]   [5  6]
[3  4] × [7  8] = ?
```

**Problem 2: Non-square matrices**
```
[1  2  3]   [7   8]
[4  5  6] × [9  10] = ?
            [11 12]
```

**Problem 3: Can these be multiplied?**
```
[1  2]   [5  6  7]
[3  4] × [8  9 10] = ?
```

**Problem 4: Identity matrix**
```
[1  0]   [5  6]
[0  1] × [7  8] = ?
```

### Key Concepts to Master

1. **Matrix Structure**
   - Rows and columns
   - Matrix dimensions (m × n)
   - When two matrices can be multiplied

2. **Matrix Multiplication Mechanics**
   - Dot product of row and column
   - Resulting dimensions
   - Why order matters (AB ≠ BA)

3. **Geometric Intuition**
   - Matrices transform space
   - Multiplication = composition of transformations
   - Connection to neural network layers

### End of Day2/3 Checklist

- [ ] Watched 3Blue1Brown videos (3 total, ~25 min)
- [ ] Read Better Explained article
- [ ] Completed 5-10 Khan Academy practice problems
- [ ] Worked through 4 practice problems by hand
- [ ] Wrote notes: "How does matrix multiplication work?"
- [ ] Can multiply a 2×2 matrix manually
- [ ] Spent approximately 60 minutes total

---

## Day 4: Probability

### Primary Video Resources

**StatQuest Series:**

1. **"Probability vs Likelihood"** (5 min)
   - Link: https://www.youtube.com/watch?v=pYxNSUDSFH4

2. **"Conditional Probability"** (8 min)
   - Link: https://www.youtube.com/watch?v=_IgyaD7vOOA
   - **THE most important concept for understanding LLMs**

3. **"Bayes' Theorem"** (15 min)
   - Link: https://www.youtube.com/watch?v=9wCnvr7Xw4E

4. **"Naive Bayes Clearly Explained"** (~15 min)
   - Creator: Josh Starmer
   - Focus: How prior probability + evidence = detection

### Reading Materials

**Article: "A Gentle Introduction to Probability"**
- Link: https://machinelearningmastery.com/what-is-probability/
- Duration: 10 min read

**Article: "Conditional Probability in Machine Learning"**
- Link: https://machinelearningmastery.com/joint-marginal-and-conditional-probability-for-machine-learning/
- Duration: 15 min read

**Visual: "Seeing Theory - Probability"**
- Link: https://seeing-theory.brown.edu/basic-probability/index.html
- Interactive visualization

### Interactive Practice (Khan Academy)

**Lesson 1: "Probability using sample spaces"**
- Link: https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/v/basic-probability
- Video: 8:44

**Lesson 2: Basic probability exercises**
- Link: https://www.khanacademy.org/math/statistics-probability/probability-library/basic-theoretical-probability/e/probability_1
- Do 5-10 problems

**Lesson 3: Conditional probability**
- Link: https://www.khanacademy.org/math/statistics-probability/probability-library/conditional-probability-independence/v/calculating-conditional-probability
- Video: 4:47

### Real-World Context (Payment/Fraud Focus)

**Kaggle: Credit Card Fraud Detection**
- Search: "Kaggle credit card fraud detection"
- Explore real dataset with tutorial notebooks
- Focus on: probability thresholds in practice
- Time: 15-20 min

**Video: "How Spam Filters Use Bayes Theorem"**
- Link: https://www.youtube.com/watch?v=O2L2Uv9pdDA
- Duration: 8:18
- Similar to fraud detection logic

### Connection to LLMs

**How LLMs Actually Work:**

1. LLMs predict next token based on conditional probability:
   - P(next_token | all_previous_tokens)

2. Temperature controls how they sample:
   - Temperature = 0: Always pick highest probability
   - Temperature = 1: Sample proportionally
   - Temperature = 2: More random

3. Every word from an LLM is:
   - Result of computing conditional probabilities
   - Over vocabulary of ~50,000 tokens
   - Based on patterns in training data

### End of Day4 Checklist

- [ ] Watched all 3 StatQuest videos
- [ ] Played with Seeing Theory interactive
- [ ] Read at least one article on conditional probability
- [ ] Completed 5+ practice problems by hand
- [ ] Can explain: "How do LLMs use conditional probability?"
- [ ] Can explain: "What is Bayes' Theorem?"
- [ ] Spent approximately 60 minutes

---

## Day 5: Distributions & Statistics

### Primary Video Resources

**StatQuest - Statistical Distributions:**

1. **"What is a statistical distribution?"** (5:14)
   - Link: https://www.youtube.com/watch?v=oI3hZJqXJuc
   - Why it matters: Temperature parameter controls output distribution

2. **"The Normal Distribution, Clearly Explained"** (5:12)
   - Link: https://www.youtube.com/watch?v=rzFX5NWojp0
   - Why it matters: Most data follows normal distributions

3. **"Mean, Variance and Standard Deviation"** (6:47)
   - Link: https://www.youtube.com/watch?v=SzZ6GpcfoQY
   - Why it matters: Understanding model confidence

### Interactive Visualizations

**Seeing Theory - Probability Distributions**
- Link: https://seeing-theory.brown.edu/probability-distributions/index.html
- Duration: 10-15 min exploration
- Play with normal distribution sliders
- Change mean and standard deviation

**Normal Distribution Calculator**
- Link: https://www.mathsisfun.com/data/standard-normal-distribution.html
- Interactive tool to see probabilities

### Reading Materials

**Article: "A Gentle Introduction to Statistical Data Distributions"**
- Link: https://machinelearningmastery.com/statistical-data-distributions/
- Duration: 10-15 min read
- Focus on: Normal distribution section

### Khan Academy Practice

**Lesson 1: Mean and Standard Deviation**
- Video: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/v/statistics-standard-deviation
- Duration: 8:49
- Practice: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/e/standard_deviation
- Do 5-7 problems

**Lesson 2: Normal Distribution**
- Video: https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/v/introduction-to-the-normal-distribution
- Duration: 10:06
- Practice: Do 5 problems on 68-95-99.7 rule

### Day5's Schedule (60 minutes total)

1. **Watch: StatQuest "What is a distribution?"** (5 min)
2. **Watch: StatQuest "Normal Distribution"** (5 min)
3. **Watch: StatQuest "Mean, Variance, Std Dev"** (7 min)
4. **Interactive: Seeing Theory** (10 min)
5. **Read: ML Mastery article** (10 min)
6. **Practice: Khan Academy** (20 min)
7. **Reflect and Note** (3 min)

### Connection to LLMs

**Why Distributions Matter for AI:**

1. **Temperature Parameter:**
   - Controls "sharpness" of probability distribution
   - Temperature = 0: Pick highest probability (peaked)
   - Temperature = 1: Sample normally
   - Temperature > 1: Flatten distribution (more random)

2. **Embedding Spaces:**
   - Word embeddings follow approximately normal distributions
   - Similar words cluster together
   - Standard deviation shows meaning spread

3. **Model Confidence:**
   - Confidence scores should follow predictable distributions
   - Anomalies indicate model issues
   - Understanding variance helps set thresholds

### Real-World Payment Examples

**Example 1: Transaction Amounts**
- Most transactions cluster around mean (normal distribution)
- Very high/low amounts are rare (tails)
- Fraud detection looks for high z-scores

**Example 2: Transaction Frequency**
- Normal customers: Mean 20 transactions/month, Std dev 5
- Sudden spike to 50 transactions → z-score = 6
- z > 3 → investigate for fraud

### End of Day5 Checklist

- [ ] Watched 3 StatQuest videos (~17 min)
- [ ] Played with Seeing Theory interactive (10 min)
- [ ] Read ML Mastery article (10 min)
- [ ] Did Khan Academy practice (5-7 problems each)
- [ ] Worked through 5+ practice problems by hand
- [ ] Can explain: distribution, normal distribution, std dev
- [ ] Spent approximately 60 minutes

---

## Day 6: NumPy + Scikit-Learn Basics

### Part 1: NumPy Deep Dive

#### Core NumPy Operations

**Topics to Cover:**
- Array creation methods (zeros, ones, arange, linspace)
- Array indexing and slicing (advanced)
- Reshaping and transposing
- Broadcasting rules
- Element-wise operations
- Aggregations (sum, mean, std, min, max)

**Resources:**
- NumPy Documentation: https://numpy.org/doc/stable/user/quickstart.html
- Tutorial: https://numpy.org/doc/stable/user/absolute_beginners.html

**Practice Exercises:**

Create a Jupyter notebook and work through:
1. Create 5 different arrays using different methods
2. Practice slicing: get rows, columns, subsets
3. Reshape 1D array to 2D and back
4. Practice broadcasting: add vector to matrix
5. Calculate statistics on transaction data

#### NumPy for ML

**Topics to Cover:**
- Dot products and matrix multiplication (np.dot, @)
- Linear algebra operations
- Random number generation
- Vectorization (why loops are slow)
- **Implement cosine similarity** (critical for embeddings!)

**Key Implementations:**

**Exercise 1: Cosine Similarity**
```
Requirements:
- Input: Two 1D arrays (vectors)
- Output: Similarity score between -1 and 1
- Use: np.dot(), np.linalg.norm()
- Test with sample transaction vectors
```

**Exercise 2: Normalize Vectors**
```
Requirements:
- Input: 1D array
- Output: Normalized array (magnitude = 1)
- Important for embeddings later
```

**Exercise 3: Distance Matrix**
```
Requirements:
- Input: 2D array (multiple vectors as rows)
- Output: Matrix of pairwise distances
- Use broadcasting, not loops
```

### Part 2: Scikit-learn Basics (2 hours)

#### Core Scikit-learn Concepts

**Topics to Cover:**
- What is scikit-learn?
- ML workflow: load data → split → train → evaluate
- train_test_split (why and how)
- Basic metrics: accuracy, precision, recall
- Cross-validation concept

**Setup:**
```bash
pip install scikit-learn

Key imports:
- from sklearn.model_selection import train_test_split
- from sklearn.metrics import accuracy_score, classification_report
- from sklearn.preprocessing import StandardScaler
```

**Resources:**
- Scikit-learn Getting Started: https://scikit-learn.org/stable/getting_started.html
- Video: "Scikit-learn Crash Course" by freeCodeCamp
  - Link: https://www.youtube.com/watch?v=0B5eIE_1vpU (watch first 30 min)

#### Build Your First Classifier

**Mini-Project: Transaction Fraud Detection (Simple Version)**

**Step 1: Get Data**
- Use Kaggle "Credit Card Fraud Detection" dataset
- Or create synthetic transaction data
- Features: amount, time, merchant_category
- Label: fraud (0/1)

**Step 2: Prepare Data**
- Load with pandas
- Convert to NumPy arrays
- Split: 80% train, 20% test
- Use train_test_split with random_state=42

**Step 3: Train Simple Classifier**
- Use Logistic Regression
- Understand: what is training? what are parameters?
- Fit the model on training data

**Step 4: Evaluate**
- Predict on test data
- Calculate accuracy
- Print classification report
- Understand: precision, recall, F1-score

**Step 5: Reflection**
- Why split data into train/test?
- What does accuracy actually mean?
- Why might accuracy be misleading for fraud?

**Resources:**
- Scikit-learn Logistic Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
- Classification Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
- Tutorial: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

### Day6 Deliverables

By end of Day6, you should have:

**NumPy :**
- ✅ Jupyter notebook with NumPy exercises
- ✅ Implemented cosine similarity function
- ✅ Implemented vector normalization
- ✅ Comfortable with array operations
- ✅ Understand vectorization vs loops

**Scikit-learn :**
- ✅ First ML classifier trained and tested
- ✅ Understand train/test split concept
- ✅ Can calculate accuracy, precision, recall
- ✅ Working fraud detection model (simple version)
- ✅ Jupyter notebook documenting the process

**Conceptual Understanding:**
- ✅ Why we split data
- ✅ What "training" means
- ✅ How to evaluate model performance
- ✅ Connection between NumPy and scikit-learn

### Why This Addition Is Valuable

**Benefits for Your Learning Path:**

1. **Connects Math to Practice**
   - Vectors/matrices from Mon-Wed → now used in real ML
   - See why linear algebra matters immediately

2. **Foundation for Deep Learning**
   - Train/test split used in all ML (including LLM fine-tuning)
   - Metrics crucial for evaluating AI models
   - Scikit-learn patterns similar to HuggingFace/PyTorch

3. **Portfolio Advantage**
   - Shows broader AI knowledge, not just LLMs
   - Fraud detection example = domain expertise

4. **Interview Preparation**
   - Can answer: "How do you evaluate a model?"
   - Can explain train/test split
   - Can build a simple classifier

### Preparation for Day7

**Before Saturday, Install:**
```bash
pip install numpy pandas scikit-learn jupyter matplotlib seaborn
```

**Download Dataset:**
- Kaggle: "Credit Card Fraud Detection"
- Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

**Have Ready:**
- Jupyter notebook running
- Clean workspace
- 4 hours of focused time

---

## Day 7: Pandas & Data Analysis

### Pandas Fundamentals

**Topics to Cover:**
- DataFrames and Series
- Reading CSV, Excel files
- Basic operations: head(), info(), describe()
- Selecting columns, filtering rows

### Data Manipulation

**Topics to Cover:**
- groupby operations (crucial!)
- Merging and joining DataFrames
- Handling missing data
- Sorting and ranking

### Transaction Analysis Project

**Tasks:**
- Load transaction dataset
- Exploratory data analysis
- Group by merchant, category, time
- Find patterns and anomalies
- Create summary statistics
- Visualize with pandas plotting

**Deliverable:** Comprehensive transaction analysis notebook

---

## Week 1 Summary

### What You'll Have Completed

**Math Foundations:**
- ✅ Vectors, matrices, probability, distributions
- ✅ Intuitive understanding, not just formulas

**Python & Libraries:**
- ✅ NumPy: arrays, operations, vectorization
- ✅ Pandas: DataFrames, analysis, groupby
- ✅ Scikit-learn: train/test, classifiers, metrics

**Practical Projects:**
- ✅ Cosine similarity implementation
- ✅ First ML fraud detector
- ✅ Transaction data analysis

**Total Time:** ~13-14 hours

**Outcome:** Strong foundation, ready for Week 2 (APIs & LLMs)

---

## Additional Resources

### Tools

**Graph Paper (for drawing vectors):**
- Physical paper and pencil (best for intuition)
- Online: https://gridzzly.com/ (printable)
- Digital whiteboard: https://excalidraw.com/

### Supplementary Learning

**StatQuest Playlists:**
- Linear Algebra: https://www.youtube.com/playlist?list=PLblh5JKOoLUIcdlgu78MnlATeyx4cEVeR
- Probability & Statistics: Multiple playlists available

**MIT OpenCourseWare (Deep Dive - Optional):**
- Gilbert Strang's "Introduction to Linear Algebra"
- Link: https://www.youtube.com/watch?v=ZK3O402wf1c
- Full university lecture format

---

## Success Metrics

### By End of Week 1

You should be able to:

- ✅ Explain vectors and matrices with examples
- ✅ Apply conditional probability to real problems
- ✅ Understand distributions and their importance
- ✅ Manipulate arrays with NumPy confidently
- ✅ Build and evaluate a simple ML classifier
- ✅ Analyze data with Pandas
- ✅ See connections between math concepts and AI applications

### You do NOT need to:

- ❌ Memorize all formulas
- ❌ Be an expert in any single topic
- ❌ Understand advanced concepts like eigenvectors
- ❌ Build production-ready models

---

## Tips for Success

### General Advice

1. **Don't Rush**: Understanding > Speed
2. **Practice by Hand**: Write out examples on paper
3. **Ask Questions**: Write down what's unclear
4. **Connect Concepts**: How does this relate to AI/ML?
5. **Take Breaks**: Pomodoro technique (25 min work, 5 min break)

### If You Get Stuck

**Videos too fast:**
- Watch at 0.75x speed
- Pause frequently
- Rewatch sections
- 3Blue1Brown is meant to be rewatched!

**Concepts feel abstract:**
- That's normal on Day 1-3
- Focus on geometric intuition first
- Think of practical examples from your domain

**Want more practice:**
- Do extra Khan Academy exercises
- Watch alternative explanations (StatQuest)
- Draw more examples on paper

---

## License

This learning plan is for personal educational use.

---

**Last Updated:** November 2024
