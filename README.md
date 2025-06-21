# Travel Review Rating - Project by Group 12

In today’s world, focus has shifted from word-of-mouth to word-of-reviews. For any business to thrive, positive customer reviews and experiences are essential.

Our project aims to support small business owners in a city by helping them understand what customers value most. It also enables them to identify and engage with users who are likely to support their business and leave positive reviews—ultimately boosting their visibility and growth.

## Dataset Used

We used the dataset from UC Irvine - Machine Learning Repository that contains below information.

Google reviews on attractions from 24 categories across Europe are considered. Google user rating ranges from 1 to 5 and average user rating per category is calculated.

[Visit UCI - ML Repository](https://archive.ics.uci.edu/dataset/485/tarvel+review+ratings)

## Implementation Overview

We conducted comprehensive machine learning analysis on the dataset to derive statistical insights and to cluster and identify user groups that businesses should consider targeting. 

**Details are as below:**

1. Install the required Libraries
2. Data Aquisition from UCI - ML Repository
3. Generate User Demographics Data using Faker Library - Which eventually would be replaced with real user demographic
4. Perform Exploratory Data Analysis as below:

    1. Categorization of Age to Age Group like Youth, Adult & Senior
    2. Categorization of the Rating by each Location like Entertainment , Food, Natural & Art Category
    3. Perform Descriptive Statistical Analysis like Mean, Median, IQR, etc
    4. Data Cleansing using Null, Duplicate check etc.
5. Data Distribution Plot using KDE & Histogram to derive the inference on skewness

6. Data Distribution using Normal, Gamma & Beta 
7. Hypothesis Testing on Influence of Gender on Specific Category
8. Statiscally check if user only reviewing Positive Experiance or Negative Experiances
9. Influence of Age Group on various entertainment Category was checked
10. Confidence Interval on each user to check how much review a particular user is likely going to give.
11. Identify Top 5 Users who has tendancy to likely give positive reviews overall.
12. Statistically check if the Age Group + Gender combined has an influence on reviewing a category.
13. Perform K-Means Clustering to group users into 4 clusters - co-relate with 4 categories
14. Perform the Linear Regression of Average Reviews by Categories
15. User Classification - Random Forect Classifier to create a model and estimate accuracy of this model.
16. Perform Bootstrapping to estimate Confidence Interval of User rating in Entertainment Category and Hypothetical Testing on influence of Gender in this Category

## Conclusion

This project provides businesses with a method to identify and target specific users by analyzing various factors and user ratings. It also incorporates statistical analysis to help determine which user segments are most likely to engage with and support the business.




