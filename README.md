## Ultimate Stock Analyzer 

A data science project build to analyze financial markets
and filter out systemic market panic from true, company specific signals.

## Current Milestones - June 19th 2026
* [x] Set up Git & GitHub repository architecture
* [x] Import historical stock data arrays using NumPy
* [x] Apply multi-dimensional array slicing to isolate specifc trading windows
* [x] Implement core statistical metrics (mean, volatility, standard deviation) 

## Goals - June 20th 2026 
* [x] - Convert calculated metrics to plain English 
* [x] - Incorporate matplotlib(maybe) with the project 

## Milestones - June 26th 2026 
* [x] - 'Clean Slate' ingestion pipeline: Correctly read the local CSV file so that each dtype is in its correct format. 

## Milestones - June 28th 2026
* [] - Feature engineering & Clean target subsetting: isolate the target columns you need for the analyzer (Close and Daily Return), calculate your risk metrics, and cleanly separate your data without triggering Pandas errors. 
* [] - Apply the control structure learned yesterday: Write a small script/function that takes the stock's data and flags high-risk/warning message (e.g: stock's daily '%' change) 
* [] - Take the logical "Brain" you built in Milestone 1 and scale it up to handle massive chunks of data effortlessly using your new looping powers.
