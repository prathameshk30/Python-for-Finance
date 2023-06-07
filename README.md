# This Repository contains projects related to Finance domain. 

### Project 1:-

#### Using Python for Quantitative Risk Analysis
This project was done as a part of my Graduate Research Assistant project. The project helped to study the effect of public sentiment on stock’s price before and after Covid-19. Using python-built Risk models (Fama French factors) for various dummy portfolio and provided insights on the risk. Further forecasted risk using VaR technique by implementing a Monte Carlo Simulation for the given portfolio. Lastly, using sentiment analysis (NLP) tried to check causation between stock pricing and people’s sentiment. Worked on web scraping automation for companies’ review text data using API, Selenium, Octoparse tools from websites such as Facebook, Yelp and Twitter.

Methodology:- 
Develope a VaR (Value at Risk) model using the Covariance matrix of the potfolio stock and run the Monte Carlo simuation for a definite window of period upto where we want o visualize the risk. Develope Regression model (OLS lib) in python to check the factors associated with risk. Download the Fama French data (3 Factors) for the dummy portfolios from Website. https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Finally use the scraped data from website such as Yahoo finance, Facebook, Twitter API to develope a sentiment analysis model and compare the stock price movement of some risk stocks with sentiment analysis score derived from text data. Use Granger causality test to check the interpretability of the sentiment score.

Part 1:- Run VaR model

https://github.com/prathameshk30/Python-for-Finance/blob/main/Monte_Carlo_Simulation_Stock_Prediction.ipynb

Part 2:- develope a  Fama French model

Part 3:- Use sentiment analysis to check the causality.

https://github.com/prathameshk30/Python-for-Finance/blob/main/FinBERT_%26_WandB.ipynb

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Project 2:- 

#### Fraud Analytics
The project was done as a part of graded assisgnment to find fraud for a retail comapny using transaction and customer data. The problem was to find fraudulent customers for a retail company using past data. Two tables were provided, transaction and customer identity for identifying AML patterns among customers. Feature engineering on the transactional data to generate features. Used unsupervised learning Isolation Forest for verification of anomalies in transaction data. Trained and selected GBM, KNN classification model on various provided labels (Fraud, Type- 1, Type-2) to identify the fraudulent customer. Further used API to fetch location data using IP address, to cross verify with given residential address for fraudulent customer.

Link:- https://github.com/prathameshk30/Python-for-Finance/blob/main/Transactional%20Fraud%20Analytics%20.ipynb

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Project 3:-

#### Lease Renewal Statistical Analysis
A project done on lease renewal risk analysis. Used various statistical tests such as Chi squared (goodness of fit), G-test, Monte Carlo simulation method to check the risk of customers that were not renewing the lease. Finally, used Kmodes clustering algorithm to group the customer to find common groups of retractor and detractor.Before starting my analysis I would like to explain my methodology and process: - Analyzing the given data that has all the variables in categorical format, it is highly imbalanced consisting of only 19.59 % of renewed vs 80.41 % of non-renewed lease. Therefore, this bias is also reflected in all my probability calculations as well as in ML algorithms output. The main question that has been answered in this report in that is a given variable/feature causing lease renewal or not, so I have only considered the ‘Yes’ counts to determine the lease renewal process that means if the feature is not present it is of no concern to answer the question of being promoter/ detractors.

Process:- To analysis is divided into two part :-

Inferential statistics
ML Algorithm output
In inferential statistics, I made a contingency table (2x2) and calculated the conditional probability of lease renewal for each case. Then further validated the relevance of the given variable to lease renewal process using statistical test such as Chi squared test for independence and Fisher’s test for exact. Further to check if the variable is a promoter and detractor used G test for goodness of fit to check if the ratio will hold true always.

In ML Algorithm part, I have used a Kmode clustering algorithm to check the similar characteristic of customer who renewed and not renewed. My theory is that as I have been given a sample of data it might totally be biased from the population and the values will be different in main database. Therefore, this analysis will only help me to figure out the behavioral pattern of customers and give insights related to it. If there would have been some numerical data then a strong conclusion can also be made.

Link:- https://github.com/prathameshk30/Python-for-Finance/blob/main/House%20Leasing%20Statistical%20Study%20(1).ipynb








