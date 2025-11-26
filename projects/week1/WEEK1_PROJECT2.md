## **📋 CREDIT CARD DEFAULT PREDICTION - PROJECT REQUIREMENTS**

---

## **PROJECT GOAL**

Build a machine learning model to predict which credit card customers will default on their next payment using real banking data.

---

## **DATASET**

**Source:** UCI Machine Learning Repository - "Default of Credit Card Clients"

**Download Links:**
- Main page: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
- Direct download: https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls

**Format:** Excel file (.xls)
**Size:** 30,000 customer records
**Note:** Skip the first row when loading (it's a description row)

---

## **PHASE 1: DATA LOADING & EXPLORATION (30 minutes)**

### **Requirements:**

**1.1 Load the Dataset**
- Load Excel file using pandas
- Skip first row (header is in row 2)
- Remove first column (ID column)

**1.2 Initial Exploration**
- Display first 5 rows
- Display last 5 rows
- Show dataset shape (rows, columns)
- Display all column names
- Show data types of each column

**1.3 Statistical Summary**
- Get summary statistics for all numerical columns
- Show count, mean, std, min, 25%, 50%, 75%, max

**1.4 Missing Values Check**
- Check for missing values in each column
- Display count of missing values per column
- Calculate percentage of missing values

**1.5 Target Variable Analysis**
- Count how many defaults vs non-defaults
- Calculate default rate (percentage)
- Create a bar chart showing distribution

**Deliverable:** Written summary answering:
- How many customers are in the dataset?
- How many features are available?
- What's the default rate?
- Are there any missing values?
- Is the dataset balanced or imbalanced?

---

## **PHASE 2: FEATURE ENGINEERING (30 minutes)**

### **Requirements:**

Create 5 new features based on banking domain knowledge:

**2.1 Payment Trend Feature**
- Calculate: Most recent payment status MINUS oldest payment status
- Name: `payment_trend`
- Purpose: Did payment behavior get worse (positive) or better (negative)?
- Use columns: PAY_0 and PAY_6

**2.2 Bill Amount Volatility Feature**
- Calculate: Standard deviation across all 6 monthly bill amounts
- Name: `bill_volatility`
- Purpose: How unstable is their spending?
- Use columns: BILL_AMT1 through BILL_AMT6

**2.3 Payment Ratio Feature**
- Calculate: Most recent payment amount divided by most recent bill amount
- Name: `payment_ratio`
- Purpose: Are they paying off their bills?
- Use columns: PAY_AMT1 and BILL_AMT1
- Handle division by zero (add 1 to denominator)

**2.4 Credit Utilization Feature**
- Calculate: Most recent bill amount divided by credit limit
- Name: `utilization`
- Purpose: How much of credit limit are they using?
- Use columns: BILL_AMT1 and LIMIT_BAL

**2.5 Number of Delays Feature**
- Calculate: Count how many months had payment delays (value > 0)
- Name: `num_delays`
- Purpose: Pattern of consistent delays
- Use columns: PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6

**Verification:**
- Display first 10 rows of new features
- Check for any infinite values
- Check for any NaN values created
- Show min and max values of each new feature

**Deliverable:** Brief explanation of why each feature might predict default

---

## **PHASE 3: DATA PREPARATION (20 minutes)**

### **Requirements:**

**3.1 Feature Selection**
Select exactly these 12 features for the model:
- LIMIT_BAL (credit limit)
- AGE (customer age)
- PAY_0 (most recent payment status)
- PAY_2 (payment status 2 months ago)
- PAY_3 (payment status 3 months ago)
- BILL_AMT1 (most recent bill)
- PAY_AMT1 (most recent payment)
- payment_trend (your engineered feature)
- bill_volatility (your engineered feature)
- payment_ratio (your engineered feature)
- utilization (your engineered feature)
- num_delays (your engineered feature)

**3.2 Create Feature Matrix (X)**
- Extract the 12 selected features into matrix X
- Display shape of X

**3.3 Create Target Variable (y)**
- Extract the target column: 'default.payment.next.month'
- Display shape of y
- Verify values are only 0 and 1

**3.4 Handle Any Issues**
- Replace any infinite values with NaN
- Fill NaN values with median of that column
- Verify no missing values remain

**3.5 Train-Test Split**
- Split data: 80% training, 20% testing
- Use random_state=42 for reproducibility
- Use stratify on target variable (keeps same default rate in both sets)
- Display shapes of: X_train, X_test, y_train, y_test
- Display default rate in training set
- Display default rate in test set

**Deliverable:** Confirmation that:
- Training set has ~24,000 samples
- Test set has ~6,000 samples
- Default rates match in both sets
- No missing values in any set

---

## **PHASE 4: MODEL TRAINING (20 minutes)**

### **Requirements:**

**4.1 Feature Scaling**
- Create StandardScaler
- Fit scaler on X_train only
- Transform X_train using fitted scaler
- Transform X_test using same scaler (do not fit again!)
- Verify scaled data has mean ~0 and std ~1

**4.2 Model Training**
- Create Logistic Regression model with:
  - class_weight='balanced' (handles imbalanced data)
  - random_state=42
  - max_iter=1000
- Train model on scaled training data
- Display confirmation that training completed

**4.3 Generate Predictions**
- Predict on scaled test set (binary predictions: 0 or 1)
- Get probability predictions on scaled test set (probabilities: 0.0 to 1.0)
- Display first 10 predictions alongside actual values
- Display first 10 probability predictions

**Deliverable:** 
- Trained model object
- Test set predictions (binary)
- Test set probabilities

---

## **PHASE 5: MODEL EVALUATION (40 minutes)**

### **Requirements:**

**5.1 Confusion Matrix**
- Calculate confusion matrix
- Display as 2x2 matrix showing:
  - True Negatives (top-left)
  - False Positives (top-right)
  - False Negatives (bottom-left)
  - True Positives (bottom-right)
- Create visualization (heatmap) of confusion matrix
- Label axes clearly (Actual vs Predicted)

**5.2 Classification Report**
- Generate full classification report showing:
  - Precision for each class
  - Recall for each class
  - F1-score for each class
  - Support for each class

**5.3 Manual Metric Calculation**
Extract from confusion matrix:
- True Positives (TP)
- False Negatives (FN)
- False Positives (FP)
- True Negatives (TN)

Calculate manually:
- Recall = TP / (TP + FN)
- Precision = TP / (TP + FP)
- Accuracy = (TP + TN) / Total

Display in business terms:
- "We caught X% of all defaults" (recall)
- "X% of our alerts were correct" (precision)
- "We missed X defaults" (false negatives)
- "We had X false alarms" (false positives)

**5.4 Model Performance Analysis**
Answer these questions:
- Is recall high enough to catch most defaults?
- Is precision acceptable (too many false alarms)?
- Which error is more costly: missing a default (FN) or false alarm (FP)?
- Would you recommend this model for production use?

**Deliverable:** 
- Confusion matrix visualization
- Classification report
- Written analysis (3-5 sentences) on model performance
- Recommendation: Deploy or improve?

---

## **PHASE 6: BUSINESS INSIGHTS (20 minutes)**

### **Requirements:**

**6.1 Feature Importance Analysis**
- Extract model coefficients
- Match coefficients to feature names
- Sort features by absolute coefficient value (highest to lowest)
- Display top 10 most important features
- Create horizontal bar chart showing top 10 features

**6.2 Business Impact Calculation**
Assumptions:
- Average loss per default = $5,000
- Test set represents one month of customers

Calculate:
- Total defaults in test set
- Defaults caught by model (True Positives)
- Defaults missed by model (False Negatives)
- Money saved = Defaults caught × $5,000
- Money lost = Defaults missed × $5,000
- Net impact = Money saved - Money lost

Display as a business report

**6.3 Threshold Analysis**
For each threshold [0.3, 0.4, 0.5, 0.6, 0.7]:
- Predict using that probability threshold
- Calculate confusion matrix
- Calculate recall and precision
- Calculate missed defaults (FN)
- Display in table format

**6.4 Recommendations**
Write recommendations addressing:
- Which threshold should the bank use and why?
- Which customers should be flagged for intervention?
- Which features are strongest predictors (top 3)?
- What actions should bank take with high-risk customers?
- What's the estimated monthly value of this model?

**Deliverable:**
- Feature importance chart
- Business impact summary ($$ saved/lost)
- Threshold comparison table
- Written recommendations (5-7 bullet points)

---

## **FINAL DELIVERABLES**

### **Required Outputs:**

**1. Jupyter Notebook** containing:
- All code with clear markdown explanations
- All visualizations (confusion matrix, feature importance)
- Analysis and insights as markdown cells

**2. Summary Document** (markdown or text) answering:
- What problem did you solve?
- What was your approach?
- What were the key findings?
- What features matter most?
- What's your recommendation?
- What's the business value?

**3. Results Summary:**
- Final model recall: ___%
- Final model precision: ___%
- Recommended threshold: ___
- Top 3 predictive features: ___, ___, ___
- Estimated monthly savings: $___
- Number of customers to flag: ___

---

## **SUCCESS CRITERIA**

You've successfully completed this project if:

✅ Model achieves recall > 50% (catching at least half of defaults)
✅ You can explain confusion matrix in business terms
✅ You can identify top 3 most important features
✅ You can recommend a threshold with business justification
✅ You can calculate ROI/business impact
✅ You can explain the project in a 2-minute interview answer

---

## **INTERVIEW PREPARATION**

Prepare to answer:

**Q1:** "Walk me through this project"
- 2-3 minute summary covering problem, approach, results

**Q2:** "Why did you choose these features?"
- Explain domain knowledge reasoning

**Q3:** "What's precision vs recall?"
- Define both and explain which matters more for defaults

**Q4:** "What would you improve?"
- Discuss: more features, different models, threshold tuning, cost-sensitive learning

**Q5:** "What's the business value?"
- Quote your money saved calculation

---

## **TIME ALLOCATION**

- Phase 1 (Exploration): 30 min ⏰
- Phase 2 (Feature Engineering): 30 min ⏰
- Phase 3 (Preparation): 20 min ⏰
- Phase 4 (Training): 20 min ⏰
- Phase 5 (Evaluation): 40 min ⏰
- Phase 6 (Business Insights): 20 min ⏰
- Documentation: 20 min ⏰

**Total: 3 hours**

---

## **OPTIONAL EXTENSIONS (If Time Permits)**

- Create visualizations of feature distributions (default vs non-default)
- Analyze which demographics default most
- Compare performance across different age groups
- Create a "risk score" formula based on top 3 features
