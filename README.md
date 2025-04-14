Bitcoin Price Analysis and Classification Report

Project Objective:
The primary objective of this project was to analyze a decade of Bitcoin data (2010-07-27 to 2024-04-25), extract significant features, and classify market behavior into distinct clusters for better understanding of trends. Additionally, the model's performance was evaluated using advanced machine learning techniques.

1. Data Preprocessing
To prepare the dataset for analysis and modeling, the following steps were performed:

Handling Missing Values: Missing or incomplete data entries were removed or imputed to ensure data consistency.

Data Cleaning: Checked for anomalies and outliers in the Bitcoin dataset.

Feature Scaling: Features were normalized to avoid scale discrepancies and improve model performance.

2. Exploratory Data Analysis (EDA):
EDA was carried out to understand key trends and patterns in the data:

Historical Price Trends: Bitcoin price showed significant growth over the decade, with periods of high volatility corresponding to market events.

Volume Analysis: Trading volume varied significantly, indicating periods of low and high investor activity.

Key insights revealed the complexity of Bitcoin's price behavior, making it critical to extract informative features for classification.

3. Feature Engineering:
Significant features were derived to capture the behavior of the Bitcoin market:

Volatility: Measured as the variability in Bitcoin prices, reflecting market instability.

Impact: Quantified the influence of trading activity on price fluctuations.

Price to Volume: Examined the relationship between price changes and trading volume.

Rolling Standard Deviation: Captured the variability of prices over a defined period, providing a smoothed view of market behavior.

4. Clustering with K-Means:
The dataset was classified into two clusters using K-Means clustering:

Cluster 0: Represented periods of lower volatility and stable market conditions.

Cluster 1: Represented periods of higher volatility, indicating unstable and dynamic market conditions.

Clusters provided insights into market phases and their respective characteristics.

5. Machine Learning Model:
To evaluate the significance of features and classify the dataset:

Pipeline Construction:

MinMaxScaler: Normalized feature values for uniformity.

Random Forest Classifier: Used for robust classification and feature importance assessment.

Accuracy: The pipeline achieved an impressive 99.90% accuracy, reflecting its efficacy in separating the clusters and analyzing trends.

6. Insights and Conclusions:
Cluster analysis revealed distinct market behaviors, with Cluster 1 showing higher volatility and trading activity, making it the dominant cluster during significant events.

Feature importance analysis highlighted the relevance of rolling standard deviation and price-to-volume ratio in distinguishing market behaviors.

The model provides a strong foundation for further analysis and can be visualized in interactive dashboards like Power BI for real-time decision-making.
