# Covid19 Forecasting
Coronavirus is a large family of viruses. This is a disease that was detected in 1960, with several varieties. The virus, which is seen mostly in animals, has also been seen in humans for the first time. The current outbreak first appeared in Wuhan, China, in December 2019.The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face.

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available.

This project is about daily case estimation using multiple data sources. Basically, Time Series and Random Forest Regressor were used in this project.

## Table of Contents

* [World COVID-19 Cases](#section-one)
* [Global Deaths Heat Map](#section-two)
* [Active, Recovered, Deaths in Hotspot Countries](#section-three)
* [US Heatmap(Confirmed Cases)](#section-four)
* [Average Age Distribution of Cases in Countries](#section-four-1)
* [Turkey](#section-five)
    * [Top 5 Cities with the Highest Number of Cases](#section-five-one)
    * [Turkey Heatmap (Number of Case)](#section-five-two)
    * [10 Cities with the Lowest Number of Cases](#section-five-three)
* [Turkey COVID-19 Forecasting](#section-six)
     * [Confirmed Case in Time Intervals](#section-six-one)
     * [Fatalities Case in Time Intervals](#section-six-two)
     * [Time Series Model](#section-six-four)
         * [Importing Libraries](#section-six-four-1)
         * [Prepearing Data](#section-six-four-2)
         * [Spliting Data for Training and Validation](#section-six-four-3)
         * [Determine Rolling Stats](#section-six-four-4)
         * [Check for Stationary](#section-six-four-5)
         * [Log scale tranformation](#section-six-four-6)
         * [Exponential Decay Transformation](#section-six-four-7)
         * [ADCF Test](#section-six-four-8)
         * [Time Shift Transformation](#section-six-four-9)
         * [Decomposition](#section-six-four-10)
         * [Building Model](#section-six-four-11)
         * [Prediction & Reverse Transformations](#section-six-four-12)
         * [Validation](#section-six-four-13)
         * [Test Forecasting](#section-six-four-14)
         * [ARIMA PDQ Param Tuning](#section-six-four-15) 
* [REFERENCES](#section-five)
