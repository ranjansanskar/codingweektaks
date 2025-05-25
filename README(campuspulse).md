# CampusPulse Notebook

## Overview

In this notebook a classification task using student data to predict relationship status (`romantic`). It involved data preprocessing, model training, and interpretation using machine learning tools.

## Structure & Flow

1. **Data Loading and Preprocessing**

   * Import libraries and load dataset.
   * Handle missing values and encode categorical variables.
   * Feature selection:

     * Feature\_1: Age
     * Feature\_2: Study Time
     * Feature\_3: Extrovertedness
2. **Data Cleaning
   
   *replaced missing feature values using different imputation strategies
   
3. **Exploratory Data Analysis**

   * Basic summary statistics.
   * Visualizations to understand feature distributions and target balance.

4. **Modeling**

   * Use `RandomForestClassifier`  to train a predictive model.
   * Evaluate performance using accuracy and confusion matrix.
   * Also used logistic regression model to check if accuracy increases and checked important features affecting models prediction


5. **Interpretability**

   * Use SHAP (SHapley Additive exPlanations) to interpret feature importance and model behavior.

## Notes

* The notebook is structured for experimentation and explanation.
* Primary target: `romantic` (relationship status).

