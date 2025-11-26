# Week 1 Learning Schedule - AI/ML Foundations

## Overview

A comprehensive 7-day learning plan covering mathematical foundations, Python libraries, and practical machine learning implementations. Total commitment: ~13-14 hours.

---

## Week Schedule

| Day | Date   | Topic                                 | Time |
| --- | ------ | ------------------------------------- | ---- |
| Mon | Nov 17 | Vectors & Linear Algebra ✅           | 1h   |
| Tue | Nov 18 | Matrices (partial) ✅                 | 1h   |
| Wed | Nov 19 | Matrices (complete) ✅                | 2-3h |
| Thu | Nov 20 | Probability fundamentals              | 1h   |
| Fri | Nov 21 | Distributions & statistics            | 1h   |
| Sat | Nov 22 | **NumPy + Scikit-learn basics** | 4h   |
| Sun | Nov 23 | Pandas & data analysis                | 3h   |

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

    1.**Watch: 3Blue1Brown Video 1** (10 min)
         - "Vectors, what even are they?"
         - Take notes on key concepts

    2.**Watch: 3Blue1Brown Video 2** (10 min)
         - "Linear combinations, span, and basis vectors"
         - Pause and rewind as needed

    3.**Read: Better Explained article** (10 min)
         - Get alternative explanation
         - Connect concepts

    4.**Practice: Draw on paper** (15 min)
         - Draw 3-4 vectors on graph paper
         - Practice vector addition visually
         - Try vector subtraction

    5.**Reflect and Note-take** (15 min)
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

### Connection to LLMs

   **Why Distributions Matter for AI:**

7. **Temperature Parameter:**

   - Controls "sharpness" of probability distribution
   - Temperature = 0: Pick highest probability (peaked)
   - Temperature = 1: Sample normally
   - Temperature > 1: Flatten distribution (more random)
8. **Embedding Spaces:**

   - Word embeddings follow approximately normal distributions
   - Similar words cluster together
   - Standard deviation shows meaning spread
9. **Model Confidence:**

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

## Day 6: NumPy + Pandas Basics

### Part 1: NumPy Deep Dive (2 hours)

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
      - Implement cosine similarity (critical for embeddings!)

   **Key Implementations:**

    **Exercise 1: Cosine Similarity**

    **Requirements:**
      - Input: Two 1D arrays (vectors)
      - Output: Similarity score between -1 and 1
      - Use: np.dot(), np.linalg.norm()
      - Test with sample transaction vectors

    **What to figure out:**
      - How cosine similarity formula works
      - Why it's useful for comparing vectors
      - When similarity is high vs low
      - Connection to embeddings later

    **Exercise 2: Normalize Vectors**

    **Requirements:**
      - Input: 1D array
      - Output: Normalized array (magnitude = 1)
      - Important for embeddings later

    **What to figure out:**
      - What is vector magnitude?
      - Why normalize vectors?
      - How to compute efficiently

    **Exercise 3: Distance Matrix**

    **Requirements:**
      - Input: 2D array (multiple vectors as rows)
      - Output: Matrix of pairwise distances
      - Use broadcasting, not loops

    **What to figure out:**
      - How to compute distances efficiently
      - Broadcasting mechanics
      - When to use distance vs similarity

---

### Part 2: Pandas Basics (2 hours)

#### Pandas Fundamentals

   **Topics to Cover:**

- DataFrames and Series
- Reading CSV, Excel files
- Basic operations: head(), info(), describe()
- Selecting columns, filtering rows
- Handling missing data
- Basic groupby operations

   **Resources:**

- Pandas Documentation: https://pandas.pydata.org/docs/getting_started/index.html
- 10 Minutes to Pandas: https://pandas.pydata.org/docs/user_guide/10min.html

   **Video Resource:**

- "Pandas Tutorial for Beginners" by Corey Schafer
- Link: https://www.youtube.com/watch?v=ZyhVh-qRZPA
- Duration: 30:00
- Watch first 20 minutes for basics

#### Essential Pandas Operations

   **Exercise 1: Load and Explore Data**

    **Requirements:**
      - Download sample transaction CSV
      - Load with pandas read_csv()
      - Use head(), tail(), info(), describe()
      - Check for missing values
      - Get basic statistics

    **What to figure out:**
      - How to load CSV files
      - How to inspect data quickly
      - What info() and describe() tell you
      - How to identify data quality issues

   **Exercise 2: Filter and Select**

    **Requirements:**
      - Select specific columns
      - Filter rows by condition (amount > 100)
      - Filter by multiple conditions
      - Select rows by index

    **What to figure out:**
      - Column selection syntax
      - Boolean indexing
      - Chaining conditions (AND, OR)
      - loc vs iloc

   **Exercise 3: Basic Groupby**

    **Requirements:**
      - Group transactions by category
      - Calculate sum, mean, count per group
      - Find top 5 categories by spending

    **What to figure out:**
      - How groupby works
      - Aggregation functions
      - Sorting results
      - Multiple aggregations

    **Exercise 4: Handle Missing Data**

    **Requirements:**
      - Identify missing values
      - Fill missing values (fillna)
      - Drop rows with missing data
      - Strategy for different columns

    **What to figure out:**
      - How to detect NaN values
      - When to fill vs drop
      - What to fill with (mean, median, zero)

- Impact on analysis

  ### Prepare for Scikit-learn

  **Exercise 5: Data Preparation**

  **Requirements:**
  - Load transaction dataset
  - Select relevant columns (amount, category, etc.)
  - Handle missing values
  - Create binary target column (fraud: 0/1)
  - Convert to NumPy arrays for ML

  **What to figure out:**
  - How to prepare data for ML
  - Feature selection
  - Creating target variable
  - Pandas to NumPy conversion

  ### Day6 Deliverables

  **NumPy:**


  - ✅ Jupyter notebook with NumPy exercises
  - ✅ Implemented cosine similarity function
  - ✅ Implemented vector normalization
  - ✅ Comfortable with array operations
  - ✅ Understand vectorization vs loops

  **Pandas:**

  - ✅ Can load CSV files
  - ✅ Can explore data (head, info, describe)
  - ✅ Can filter and select data
  - ✅ Understand basic groupby
  - ✅ Can handle missing values
  - ✅ Can prepare data for ML

  **Conceptual Understanding:**

  - ✅ Why NumPy is faster than Python lists
  - ✅ What DataFrames are and when to use them
  - ✅ How to move between pandas and NumPy
  - ✅ Ready to build ML models

  ---

  ### End of Day6 Checklist

**Day 6:**

- [ ] NumPy arrays mastered
- [ ] Cosine similarity implemented
- [ ] Pandas basics learned
- [ ] Can load and explore CSV
- [ ] Can filter and group data
- [ ] Data preparation for ML understood

---

## Day 7: Scikit-learn & Fraud Detection - Quick Reference

### HOUR 1: Scikit-learn Fundamentals (60 min)

#### Introduction to Scikit-learn

   **What is Scikit-learn?**

- Python library for machine learning
- Built on NumPy, SciPy, and matplotlib
- Provides simple, efficient tools for data analysis
- Consistent API across different algorithms

   **Key Features:**

- Classification (fraud detection, spam filtering)
- Regression (price prediction, forecasting)
- Clustering (customer segmentation)
- Dimensionality reduction
- Model evaluation tools
- 

   **Key Concepts:**

- ML workflow: Prepare → Choose Model → Train → Predict → Evaluate
- Train/test split: 80/20, prevents overfitting
- Metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- For fraud: Recall > Precision (catch fraud even with false alarms)

   **Videos:**

- Scikit-learn Crash Course: https://www.youtube.com/watch?v=0B5eIE_1vpU (watch first 15-20 min)
- ML with Scikit-learn: https://www.youtube.com/watch?v=pqNCD_5r0IU (10 min)

   **Reading:**

- Official Tutorial: https://scikit-learn.org/stable/tutorial/basic/tutorial.html (20 min)
- Gentle Introduction: https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/ (15 min)

   **Practice:**

- Build Iris classifier (simple example to learn API)
- Understand .fit(), .predict(), accuracy_score()

---

### HOUR 2-3: Fraud Detection Project (120 min)

   **Dataset:**

- Kaggle Credit Card Fraud: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Or create synthetic transaction data

   **Tasks:**

   **1. Load & Explore (15 min)**

- Load CSV, check shape, fraud rate
- Handle missing values
- Check for imbalance (expect <1% fraud)

   **2. Prepare Data (20 min)**

- Remove IDs, timestamps
- Separate X (features) and y (fraud label)
- Train/test split (80/20, stratify=y)
- Scale features with StandardScaler

   **3. Train Model (15 min)**

- Use LogisticRegression or RandomForestClassifier
- **Must use:** class_weight='balanced' (handles imbalance)
- .fit() on training data

   **4. Evaluate (25 min)**

- .predict() on test set
- Calculate: accuracy, precision, recall, F1, confusion matrix
- **Key metric:** Recall (catch fraud!)
- Expect: 95%+ accuracy, 60-80% recall, 10-30% precision

   **5. Analyze & Improve (45 min)**

- Where does model fail?
- Try: different algorithm, adjust threshold, feature engineering
- Document findings

   **Refer the WEEK1_PROJECT.md for detailed requirement**

---

### Key Resources

   **Documentation:**

- Scikit-learn Main: https://scikit-learn.org/stable/
- User Guide: https://scikit-learn.org/stable/user_guide.html
- API Reference: https://scikit-learn.org/stable/modules/classes.html

   **Specific Functions:**

- train_test_split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
- LogisticRegression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
- RandomForestClassifier: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html

   **Imbalanced Data:**

- Techniques: https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/
- imbalanced-learn: https://imbalanced-learn.org/

---

### Critical Points

   **Must Remember:**

- ✅ Use class_weight='balanced' for imbalanced data
- ✅ Stratify train/test split
- ✅ Fit scaler on train only, transform both
- ✅ Never use test data for training
- ✅ Recall > Accuracy for fraud detection
- ✅ Confusion matrix shows full picture

   **Common Mistakes:**

- ❌ Trusting accuracy alone (misleading!)
- ❌ Not using class_weight (model ignores fraud)
- ❌ Fitting scaler on all data (data leakage)
- ❌ Not stratifying split (fraud might go to one set)

---

### Deliverables Checklist

   **Hour 1:**

- [ ] Built iris classifier
- [ ] Understand train/test split
- [ ] Know basic metrics

   **Hour 2-3:**

- [ ] Fraud dataset loaded
- [ ] Data cleaned and split
- [ ] Model trained with class_weight='balanced'
- [ ] All metrics calculated
- [ ] Confusion matrix created
- [ ] Results analyzed
- [ ] Findings documented

   **Understanding:**

- [ ] ML workflow explained
- [ ] Why imbalanced data is hard
- [ ] Which metrics matter for fraud
- [ ] Ready for Week 2 APIs

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

## Ready for Week 2:

- [ ] Understand ML workflow
- [ ] Can build and evaluate classifier
- [ ] Know when models work well vs poorly
- [ ] Understand evaluation metrics
- [ ] Can explain findings to others

## License

This learning plan is for personal educational use.

---

**Last Updated:** November 2025
