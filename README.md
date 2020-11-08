# Covid19 Forecasting
Coronavirus is a large family of viruses. This is a disease that was detected in 1960, with several varieties. The virus, which is seen mostly in animals, has also been seen in humans for the first time. The current outbreak first appeared in Wuhan, China, in December 2019.The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face.

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available.

This project is about daily case estimation using multiple data sources. Basically, Time Series and Random Forest Regressor were used in this project.
You can see the project in the most detailed way on my Kaggle link.
https://www.kaggle.com/thepinokyo/esin-covid19-forecasting-capstone

## Multiple Data Source:
- COVID19 Global Forecasting (Week 5)
- COVID-19 in Turkey
- COVID-19 useful features by country
- COVID19 Daily Updates
- Novel Corona Virus 2019 Dataset
- Number of Covid-19 cases in the cities of Turkey
- Python Folium Country Boundaries
- Turkey Geoplot
I received the "World COVID-19 Cases" from the following github links to study its worldwide spread and effects. It contains all cases until 23/9/2020. https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

## Table of Contents

* World COVID-19 Cases
* Global Deaths Heat Map
* Active, Recovered, Deaths in Hotspot Countries
* US Heatmap(Confirmed Cases)
* Average Age Distribution of Cases in Countries
* Turkey
    * Top 5 Cities with the Highest Number of Cases
    * Turkey Heatmap (Number of Case)
    * 10 Cities with the Lowest Number of Cases
* Turkey COVID-19 Forecasting
     * Confirmed Case in Time Intervals
     * Fatalities Case in Time Intervals
     * Time Series Model
         * Importing Libraries
         * Prepearing Data
         * Spliting Data for Training and Validation
         * Determine Rolling Stats
         * Check for Stationary
         * Log scale tranformation
         * Exponential Decay Transformation
         * ADCF Test
         * Time Shift Transformation
         * Decomposition
         * Building Model
         * Prediction & Reverse Transformations
         * Validation
         * Test Forecasting
         * ARIMA PDQ Param Tuning
* REFERENCES
