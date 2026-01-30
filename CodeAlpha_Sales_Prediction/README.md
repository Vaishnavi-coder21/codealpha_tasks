# Sales Prediction Using Advertising Data (CodeAlpha – Task 4)

## Project Overview
This project focuses on predicting future product sales based on
advertising expenditure using Python. The analysis helps understand
how different advertising channels influence sales outcomes and
supports data-driven marketing decisions.

## Objective
- Predict sales based on advertising spend
- Prepare data through cleaning and exploration
- Use regression modeling to forecast sales
- Analyze the impact of advertising on sales performance
- Provide actionable insights for marketing strategy

## Dataset
File Name: Advertising.csv

The dataset contains the following columns:
- TV: Advertising budget spent on TV
- Radio: Advertising budget spent on Radio
- Newspaper: Advertising budget spent on Newspaper
- Sales: Product sales

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Project Structure
CodeAlpha_Sales_Prediction/
- sales_prediction.py
- Advertising.csv
- README.md

## Steps Performed
1. Loaded the dataset using Pandas.
2. Removed unnecessary columns.
3. Checked and handled missing values.
4. Performed exploratory data analysis using pair plots.
5. Selected advertising features (TV, Radio, Newspaper).
6. Split the data into training and testing sets.
7. Trained a Linear Regression model.
8. Evaluated the model using MAE, MSE, and R² score.
9. Visualized actual vs predicted sales.
10. Analyzed the impact of advertising spend on sales.

## Key Insights
- TV advertising has the strongest influence on sales.
- Radio advertising shows moderate impact.
- Newspaper advertising has comparatively lower effect.
- Higher advertising investment generally leads to increased sales.

## Business & Marketing Insights
- Companies should invest more in high-impact advertising channels.
- Marketing budgets can be optimized using predictive analysis.
- Data-driven strategies improve return on investment (ROI).

## How to Run the Project
1. Place Advertising.csv in the project folder.
2. Open terminal in the project directory.
3. Run the command:
   python sales_prediction.py

## Conclusion
This project demonstrates how sales can be effectively predicted
using regression analysis and advertising data, enabling better
marketing and business decisions.

## Author
Vaishnavi Narendra Patil  
CodeAlpha Data Science Intern
