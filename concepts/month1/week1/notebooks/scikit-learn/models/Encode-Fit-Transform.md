
# **When Only Features are Text**

## PHASE 1: ENCODING (Text → Numbers)
### ------------------------------------
    encoder.fit(training_data)                    # Learn: Visa=2, Mastercard=1, Amex=0
    encoder.transform(training_data)              # Apply to training
    encoder.transform(test_data)                  # Apply to test (same mapping!)


## PHASE 2: TRAINING (Learning Patterns)
### ------------------------------------
    model.fit(encoded_training_data, y_train)     # Learn fraud patterns from training


## PHASE 3: EVALUATION (Testing Performance)
### ------------------------------------
    model.predict(encoded_test_data)              # Main goal: How well does it work?


## PHASE 4: PRODUCTION (Real Usage)
### ------------------------------------
    encoder.transform(new_data)                   # NO fit! Use learned mapping
    model.predict(encoded_new_data)               # NO fit! Use learned patterns


## OPTIONAL DIAGNOSTIC (Not part of main workflow)
### ------------------------------------
    model.predict(encoded_training_data)          # Check if model learned
                                              # (Training accuracy should be high)


# **When Features and Targer both are Text**

## PHASE 1: ENCODING FEATURES (X):
======================
encoder_X.fit(training features) = Learn text-to-number mapping for features
encoder_X.transform(training features) = Encode training features
encoder_X.transform(test features) = Encode test features
encoder_X.transform(new features) = Encode new features (NO fit!)


## PHASE 2: ENCODING TARGET (y) - IF TEXT:
===============================
encoder_y.fit(training target) = Learn text-to-number mapping for target
encoder_y.transform(training target) = Encode training target
encoder_y.transform(test target) = Encode test target (for evaluation)

⚠️ IMPORTANT: You DON'T transform new y values in production!
   (You're trying to PREDICT them, not encode known values!)


## PHASE 3: TRAINING:
=========
model.fit(encoded X training, encoded y training) = Learn patterns


## PHASE 4: PREDICTION:
===========
encoded_predictions = model.predict(encoded X new)
text_predictions = encoder_y.inverse_transform(encoded_predictions)
                   ↑ Convert numbers back to text!


## COMPLETE FLOW:
==============
Training:
  1. encoder_X.fit() + transform() on X_train
  2. encoder_y.fit() + transform() on y_train  ← NEW!
  3. model.fit(encoded X, encoded y)

Testing:
  1. encoder_X.transform() on X_test (NO fit!)
  2. encoder_y.transform() on y_test (for comparison only)
  3. model.predict() returns encoded predictions
  4. encoder_y.inverse_transform() to get text predictions

Production:
  1. encoder_X.transform() on X_new (NO fit!)
  2. model.predict() returns encoded predictions
  3. encoder_y.inverse_transform() to get text predictions  ← NEW!


THREE ENCODERS:
===============
encoder_X = LabelEncoder()       # For features (X)
encoder_y = LabelEncoder()       # For target (y)  ← NEW!
model = RandomForestClassifier() # For learning patterns

encoder_X.fit() = Learn feature encoding
encoder_y.fit() = Learn target encoding  ← NEW!
model.fit() = Learn patterns
```

## Level 6: Visual Diagram
```
┌────────────────────────────────────────────────────────┐
│  TRAINING WITH TEXT TARGET                             │
└────────────────────────────────────────────────────────┘

Training Data:
  X: ['Visa', 'Mastercard', ...]
  y: ['Fraud', 'Normal', ...]  ← TEXT!
        ↓
encoder_X.fit(X_train)
        ↓
X_encoded = encoder_X.transform(X_train)
        ↓
encoder_y.fit(y_train)  ← NEW! Encode target
        ↓
y_encoded = encoder_y.transform(y_train)
        ↓
model.fit(X_encoded, y_encoded)  ← Both encoded!
        ↓
Trained Model


┌────────────────────────────────────────────────────────┐
│  PREDICTION WITH TEXT TARGET                           │
└────────────────────────────────────────────────────────┘

New Data:
  X: ['Amex', 'Visa']
  y: ???  ← We want to predict this!
        ↓
X_encoded = encoder_X.transform(X_new)
        ↓
predictions_encoded = model.predict(X_encoded)
  Result: [0, 1]  ← Numbers!
        ↓
predictions_text = encoder_y.inverse_transform(predictions_encoded)
  Result: ['Fraud', 'Normal']  ← Text!
        ↓
Return human-readable predictions