## Day 7: Scikit-learn & Fraud Detection Project

### Day Overview

Learn scikit-learn fundamentals in the morning, then apply them to build a complete fraud detection classifier in the afternoon.

**Total Time:** 3 hours

### Day7's Schedule (3 hours total)

**Hour 1:** Scikit-learn Fundamentals (60 min)
- What is scikit-learn?
- ML workflow overview
- Train/test split concept
- Simple classifier example
- Understanding metrics

**Hour 2:** Fraud Detection Project - Part 1 (60 min)
- Load and prepare fraud dataset
- Train classifier
- Make predictions

**Hour 3:** Fraud Detection Project - Part 2 (60 min)
- Evaluate model performance
- Try improvements
- Document findings

---

### HOUR 1: Scikit-learn Fundamentals

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

**Installation:**
```bash
pip install scikit-learn
```

---

#### The Machine Learning Workflow

**5 Core Steps:**

**1. Prepare Data**
- Load dataset
- Clean data (handle missing values)
- Split features (X) from target (y)
- Split into train and test sets

**2. Choose Model**
- Classification vs Regression
- Select appropriate algorithm
- Logistic Regression, Random Forest, etc.

**3. Train Model**
- Model learns patterns from training data
- Adjusts internal parameters
- Minimizes prediction errors

**4. Make Predictions**
- Use trained model on new data
- Get predictions for test set

**5. Evaluate Performance**
- Compare predictions to actual values
- Calculate metrics (accuracy, precision, recall)
- Decide if model is good enough

---

#### Understanding Train/Test Split

**Why Split Data?**

**Problem:** If we test on same data we trained on:
- Model memorizes answers (overfitting)
- Looks perfect but fails on new data
- Like studying only exam questions

**Solution:** Hold out some data for testing
- Train on 80% of data
- Test on remaining 20%
- Test set simulates "new unseen data"

**Key Rules:**
- Never use test data during training
- Split randomly to avoid bias
- Use random_state for reproducibility

**Resources:**
- Train-test split guide: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- Cross-validation (advanced): https://scikit-learn.org/stable/modules/cross_validation.html

---

#### Simple Classification Example

**Task: Build your first classifier (15 min)**

**Dataset: Iris Flowers**
- Famous beginner dataset
- 150 samples, 4 features
- 3 flower species to classify
- Built into scikit-learn

**Steps:**

**1. Load the data**
- Import iris dataset
- Explore features and target
- Understand data shape

**2. Split train/test**
- 80/20 split
- random_state=42

**3. Train classifier**
- Use LogisticRegression
- Call .fit() on training data

**4. Make predictions**
- Use .predict() on test data

**5. Check accuracy**
- Compare predictions to actual
- Calculate accuracy score

**What to figure out:**
- How to load built-in datasets
- What X and y represent
- How to use train_test_split
- What .fit() does
- What .predict() returns
- How to calculate accuracy

**Expected outcome:**
- Accuracy around 95%+
- Understanding of basic workflow
- Confidence with scikit-learn API

---

#### Understanding Evaluation Metrics

**Accuracy**
- What percentage did we get right?
- Formula: Correct predictions / Total predictions
- Good starting point
- **Problem:** Misleading with imbalanced data

**Example:**
- 100 transactions: 95 legitimate, 5 fraud
- Model predicts "not fraud" for everything
- Accuracy = 95%! (Looks great!)
- But caught 0 fraud! (Actually terrible!)

**Better Metrics for Classification:**

**Precision**
- Of predicted positives, how many were correct?
- Formula: True Positives / (True Positives + False Positives)
- "When I say fraud, am I usually right?"

**Recall (Sensitivity)**
- Of actual positives, how many did we catch?
- Formula: True Positives / (True Positives + False Negatives)
- "Of all actual fraud, what % did I catch?"

**F1-Score**
- Harmonic mean of precision and recall
- Balances both metrics
- Good single number for imbalanced data

**Confusion Matrix**
- Shows all four outcomes
- True Positives, True Negatives
- False Positives, False Negatives
- Visual way to understand errors

**For Fraud Detection:**
- Recall is CRITICAL (must catch fraud!)
- Some false positives acceptable
- Missing fraud is very costly
- F1-Score good overall metric

**Resources:**
- Metrics guide: https://scikit-learn.org/stable/modules/model_evaluation.html
- Choosing metrics: https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/

---

#### Video Resources

**Video: "Scikit-learn Crash Course"**
- Link: https://www.youtube.com/watch?v=0B5eIE_1vpU
- Duration: 30:00
- Watch first 15-20 minutes
- Covers train/test split, basic classification

**Video: "Machine Learning with Scikit-learn"**
- Link: https://www.youtube.com/watch?v=pqNCD_5r0IU
- Duration: 10:00
- Quick overview of workflow

---

#### Reading Materials

**Official Scikit-learn Tutorial**
- Link: https://scikit-learn.org/stable/tutorial/basic/tutorial.html
- Duration: 20 min read
- Covers fundamentals with examples

**Article: "A Gentle Introduction to Scikit-learn"**
- Link: https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/
- Duration: 15 min read

---

#### Practice Exercise

**Build Iris Classifier (20 min)**

**Requirements:**
- Load iris dataset
- Split into train/test (80/20)
- Train LogisticRegression model
- Predict on test set
- Calculate accuracy
- Print classification report
- Create confusion matrix

**Success criteria:**
- Accuracy > 90%
- Understand each step
- Can explain what happened
- Code runs without errors

**What to observe:**
- Training is fast (milliseconds)
- Predictions are instant
- Model performs well
- Metrics make sense

---

### HOUR 2: Fraud Detection Project - Part 1

#### Project Setup

**Goal:** Build a fraud detection classifier using real transaction data

**What you'll learn:**
- Working with imbalanced data
- Feature preparation
- Model training on real problem
- Handling real-world challenges

---

#### Task 1: Get Dataset (10 min)

**Option A: Kaggle Credit Card Fraud Detection**
- Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- Most popular fraud dataset
- Real anonymized transactions
- Highly imbalanced (0.17% fraud)

**Option B: Synthetic Transaction Data**
- Create fake transactions if Kaggle unavailable
- Use pandas to generate
- Add fraud labels manually

**Dataset Requirements:**
- At least 1000 transactions
- Multiple features (amount, time, merchant, etc.)
- Binary fraud label (0=legitimate, 1=fraud)
- Imbalanced (more legitimate than fraud)

**Download and save:**
- Save as `transactions.csv`
- Place in project folder
- Verify file loads correctly

---

#### Task 2: Load and Explore (15 min)

**Requirements:**

**Load the data:**
- Use pandas read_csv
- Display first 10 rows
- Check data shape
- Inspect column names and types

**Exploratory questions to answer:**
- How many total transactions?
- How many features?
- How many fraudulent transactions?
- What's the fraud rate (%)?
- Any missing values?
- What's the range of transaction amounts?

**Data quality checks:**
- Check for nulls: .isnull().sum()
- Check for duplicates
- Check data types: .dtypes
- Get summary statistics: .describe()

**What to figure out:**
- Is this imbalanced data? (Yes!)
- What does imbalanced mean for modeling?
- Which features might be useful?
- Any obvious data issues?

**Expected findings:**
- Fraud rate likely 0.1% - 1%
- Highly imbalanced dataset
- This is realistic for fraud detection
- Will affect evaluation strategy

---

#### Task 3: Data Preparation (20 min)

**Clean the data:**

**Handle missing values:**
- Check each column for nulls
- Decide: drop or fill?
- For amounts: might fill with median
- For categories: might fill with "Unknown"
- Or drop rows if few missing

**Remove unnecessary columns:**
- Transaction IDs (not useful for prediction)
- Timestamps (for now - could engineer features later)
- Any columns that are all same value
- Keep: amount, merchant info, fraud label

**Separate features and target:**
- X = all columns except fraud label
- y = fraud label only
- Verify shapes match

**Handle categorical variables (if any):**
- If you have merchant names, categories, etc.
- For now, might drop them
- Or use simple encoding (0, 1, 2...)
- Advanced: one-hot encoding (optional)

**What to figure out:**
- What makes a good feature?
- When to drop vs transform?
- How to handle categorical data?
- Feature engineering opportunities

---

#### Task 4: Train/Test Split (5 min)

**Requirements:**

**Split the data:**
- 80% training, 20% testing
- Use train_test_split from sklearn
- Set random_state=42 for reproducibility
- Stratify by fraud label (important!)

**Why stratify?**
- Ensures both sets have similar fraud rates
- With rare events, random split might put all fraud in one set
- Stratify maintains class balance

**Verify split:**
- Check shapes of train and test sets
- Calculate fraud rate in each
- Should be similar (e.g., both ~0.5%)

**What to figure out:**
- How to use stratify parameter
- Why it matters for imbalanced data
- How to verify split worked correctly

---

#### Task 5: Feature Scaling (10 min)

**Why scale features?**

**Problem:**
- Transaction amount: $1 to $10,000
- Hour of day: 0 to 23
- Features on very different scales

**Impact:**
- Some algorithms sensitive to scale
- Large values dominate small values
- Model performs poorly

**Solution: StandardScaler**
- Transforms each feature
- Mean = 0, Standard deviation = 1
- All features on similar scale

**Important: Fit on train only!**
- Fit scaler on training data
- Transform both train and test
- Prevents data leakage
- Test set represents "future unseen data"

**What to figure out:**
- How to use StandardScaler
- Why fit_transform for train
- Why only transform for test
- When scaling is necessary

**Note:** Tree-based models (Random Forest) don't need scaling, but Logistic Regression does.

---

### HOUR 3: Fraud Detection Project - Part 2

#### Task 1: Train Classifier (15 min)

**Choose your algorithm:**

**Option 1: Logistic Regression (Recommended)**
- Simple and interpretable
- Good baseline model
- Fast training
- Works well with scaled features

**Option 2: Random Forest**
- More powerful
- Handles non-linear patterns
- Doesn't need feature scaling
- Takes longer to train

**Try both if time allows!**

**Training steps:**

**For Logistic Regression:**
- Import LogisticRegression
- Create instance
- Important: Set class_weight='balanced'
- Fit on training data
- Training completes in seconds

**For Random Forest:**
- Import RandomForestClassifier
- Set n_estimators (100 is good start)
- Set class_weight='balanced'
- Fit on training data
- May take longer than Logistic Regression

**Why class_weight='balanced'?**
- Handles imbalanced data
- Gives more weight to rare class (fraud)
- Helps model learn from minority examples
- Critical for fraud detection

**What to observe:**
- Training time
- Any warnings or errors
- Model learns patterns from training data
- Gradient descent happening (Logistic Regression)

**What to figure out:**
- What happens during .fit()?
- How does model learn patterns?
- What are model parameters?
- How long does training take?

---

#### Task 2: Make Predictions (10 min)

**Make predictions on test set:**

**Get predicted labels:**
- Use .predict() on test features
- Returns 0 or 1 for each transaction
- These are "hard" predictions

**Get prediction probabilities:**
- Use .predict_proba() on test features
- Returns probability for each class
- Probability of fraud (second column)
- Useful for setting custom thresholds

**What to figure out:**
- Difference between .predict() and .predict_proba()
- How to interpret probabilities
- When to use each method
- How to set custom thresholds

**Example:**
- Model predicts probability = 0.7 (70% fraud)
- Default threshold = 0.5
- Since 0.7 > 0.5, predict fraud (1)
- Could adjust threshold for more/fewer alerts

---

#### Task 3: Evaluate Performance (25 min)

**Calculate metrics:**

**Accuracy:**
- Simple: correct / total
- Expected: Very high (95%+)
- Why? Because most transactions are legitimate
- **Don't rely on accuracy alone!**

**Confusion Matrix:**
- True Negatives: Correctly identified legitimate
- False Positives: Wrongly flagged as fraud (false alarm)
- False Negatives: Missed fraud (dangerous!)
- True Positives: Correctly caught fraud

**Precision:**
- Of flagged transactions, how many were actually fraud?
- Low precision = too many false alarms
- Annoys customers with unnecessary blocks

**Recall:**
- Of actual fraud, what percentage did we catch?
- **Most important metric for fraud!**
- Low recall = missing fraud = losing money

**F1-Score:**
- Balance of precision and recall
- Good single metric for imbalanced data
- Higher is better

**Classification Report:**
- Shows all metrics together
- Breakdown by class (legitimate and fraud)
- Overall accuracy

**What to figure out:**
- How to interpret confusion matrix
- Which metric matters most for fraud?
- Tradeoff between precision and recall
- What's acceptable performance?

**Realistic expectations:**
- Recall: 60-80% (catching most fraud)
- Precision: 10-30% (lots of false alarms OK for fraud)
- Accuracy: 95%+ (due to class imbalance)
- F1-Score: 0.3-0.5 (typical for fraud detection)

**Why low precision is OK:**
- Better to review 10 false alarms
- Than miss 1 real fraud
- Human review can filter false positives
- Cost of missing fraud >> cost of false alarm

---

#### Task 4: Analyze Results (10 min)

**Detailed analysis:**

**Look at predictions:**
- How many transactions flagged as fraud?
- What's the alert rate?
- Is it realistic? (Should be low, like 1-3%)

**Examine false positives:**
- What legitimate transactions were flagged?
- Any patterns? (High amounts? Unusual merchants?)
- Could features be improved?

**Examine false negatives:**
- What fraud did we miss?
- Were they unusual cases?
- Any patterns to missed fraud?

**Feature importance (if using Random Forest):**
- Which features were most useful?
- Does it make sense?
- Amount often most important

**What to figure out:**
- Where is model strong?
- Where does it fail?
- What could improve performance?
- Is model ready for production?

---

#### Task 5: Try Improvements (Optional, if time)

**Ideas to try:**

**1. Adjust decision threshold:**
- Default is 0.5
- Lower to 0.3 → More alerts, better recall
- Raise to 0.7 → Fewer alerts, better precision
- Find optimal tradeoff

**2. Try different algorithm:**
- If used Logistic Regression, try Random Forest
- If used Random Forest, try Logistic Regression
- Compare results

**3. Feature engineering:**
- Create amount bins (small, medium, large)
- Add hour of day if timestamps available
- Interaction features (amount × merchant_type)

**4. Handle imbalance differently:**
- Try different class_weight values
- Use SMOTE for oversampling (advanced)
- Undersample majority class

**5. Ensemble methods:**
- Combine multiple models
- Average their predictions
- Often improves performance

**What to figure out:**
- What changes help vs hurt?
- Why might certain approaches work better?
- What's practical for production?

---

### Day7 Deliverables

**Scikit-learn Fundamentals:**
- ✅ Understand ML workflow (5 steps)
- ✅ Know train/test split purpose
- ✅ Built simple iris classifier
- ✅ Understand evaluation metrics
- ✅ Can use scikit-learn API

**Fraud Detection Project:**
- ✅ Loaded and explored fraud dataset
- ✅ Cleaned and prepared data
- ✅ Handled imbalanced data
- ✅ Split into train/test sets
- ✅ Scaled features appropriately
- ✅ Trained classifier with class_weight
- ✅ Made predictions on test set
- ✅ Evaluated with appropriate metrics

**Understanding:**
- ✅ Why accuracy is misleading for imbalanced data
- ✅ Why recall is critical for fraud detection
- ✅ What confusion matrix tells us
- ✅ How to interpret precision/recall tradeoff
- ✅ What "training" means
- ✅ Why we split train/test

**Jupyter Notebook:**
- ✅ Complete workflow documented
- ✅ Code well-commented
- ✅ Results clearly presented
- ✅ Insights and analysis included
- ✅ Next steps identified

---

### Key Insights

**About Fraud Detection:**
- Highly imbalanced problem (realistic!)
- Accuracy is misleading metric
- Recall more important than precision
- False positives acceptable, false negatives costly
- Real-world fraud detection is similar but more complex

**About Machine Learning:**
- Quality of data matters most
- Feature engineering is crucial
- Simple models often work well
- Evaluation is as important as training
- Production requires ongoing monitoring

**About Scikit-learn:**
- Consistent API across algorithms
- Easy to try different approaches
- Built-in tools for common tasks
- Great documentation and examples
- Industry standard for classical ML

---

### Connection to Future Learning

**Week 2 (APIs & FastAPI):**
- Wrap this classifier in API
- POST transaction → GET fraud score
- Real-time fraud detection endpoint

**Week 3 (LLMs):**
- Use LLM to extract features from transaction text
- "Coffee at Starbucks $5.50" → structured features
- Combine LLM + Classifier for powerful system

**Production Deployment:**
- This workflow is foundation
- Add database for transactions
- Add monitoring and alerting
- A/B test different models
- Retrain periodically with new data

---

### Troubleshooting Guide

**Issue: Very low recall (catching no fraud)**
- Check class_weight='balanced' is set
- Try adjusting decision threshold lower
- Verify train/test split was stratified
- Check if enough fraud examples in training

**Issue: Model predicts everything as not-fraud**
- Extreme class imbalance
- Ensure class_weight='balanced'
- Try SMOTE or undersampling
- Try different algorithm (Random Forest)

**Issue: High training time**
- Random Forest with many trees takes time
- Reduce n_estimators (try 50 instead of 100)
- Use Logistic Regression instead
- Reduce dataset size for testing

**Issue: ImportError or ModuleNotFoundError**
- Ensure scikit-learn installed: pip install scikit-learn
- Check version: sklearn.__version__
- Restart Jupyter kernel

**Issue: Poor performance across all metrics**
- Check data quality
- Verify features are meaningful
- Check for data leakage
- Try different features
- May need feature engineering

---

### Resources

**Scikit-learn Documentation:**
- Main docs: https://scikit-learn.org/stable/
- User guide: https://scikit-learn.org/stable/user_guide.html
- Tutorials: https://scikit-learn.org/stable/tutorial/index.html
- API reference: https://scikit-learn.org/stable/modules/classes.html

**Imbalanced Data:**
- imbalanced-learn library: https://imbalanced-learn.org/
- Techniques guide: https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/

**Evaluation Metrics:**
- Metrics guide: https://scikit-learn.org/stable/modules/model_evaluation.html
- Understanding metrics: https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/

**Fraud Detection:**
- Kaggle fraud detection competitions
- Real-world case studies
- Research papers on fraud ML

---

### Final Checklist

**Morning (Hour 1):**
- [ ] Watched scikit-learn tutorial video
- [ ] Read introduction documentation
- [ ] Understand ML workflow
- [ ] Built iris classifier example
- [ ] Understand train/test split
- [ ] Know basic evaluation metrics

**Afternoon (Hours 2-3):**
- [ ] Loaded fraud detection dataset
- [ ] Explored data (shape, fraud rate, features)
- [ ] Cleaned data (handled nulls, removed unnecessary columns)
- [ ] Separated features (X) and target (y)
- [ ] Split train/test with stratification
- [ ] Scaled features with StandardScaler
- [ ] Trained classifier with class_weight='balanced'
- [ ] Made predictions on test set
- [ ] Calculated all metrics (accuracy, precision, recall, F1)
- [ ] Created confusion matrix
- [ ] Analyzed results and identified strengths/weaknesses
- [ ] Tried at least one improvement
- [ ] Documented findings in notebook

**Understanding:**
- [ ] Can explain entire ML workflow
- [ ] Know why train/test split matters
- [ ] Understand imbalanced data challenges
- [ ] Know which metrics matter for fraud
- [ ] Can interpret confusion matrix
- [ ] Understand precision/recall tradeoff
- [ ] Ready to build more ML models

**Ready for Week 2!**