# Crossformer Model Reproduction

This repository aims to:
1. Reproduce the results presented in the original paper. | Status: Done | Progress: We were able to reproduce the results.
2. Use the Crossformer model presented in the paper on stock price data and predict result for 1 time_stamp out. | Status: Done | Progress: Done with the setup and got results on AKM 2023 stock price data
3. Fine tune hyperparameters to improve on results. | Status: On going |  Progress: Working on building a dynamic grid<>search for different stocks

## Introduction

The Crossformer model is a state-of-the-art approach for time series analysis and prediction. In this repository, we provide the necessary code and instructions to reproduce the results reported in the original paper.

## Getting Started

To get started with reproducing the results, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Download the dataset used in the original paper and place it in the appropriate directory.
4. Run the provided scripts to train and evaluate the Crossformer model.

## Directory Structure

Here is the directory structure for this project - 

1. `OrginalPaperCode/` contains the original code for the paper [link](https://openreview.net/forum?id=vSVLM2j9eie). 
2. `progress/` contains reports, screenshots, logs about what all have been achieved so far!
2. `scripts/` contains the scripts to preporcess our stock data & plot final results.

## Results

In this section, we will showcase the results obtained by reproducing the Crossformer model. We will provide details on the performance metrics achieved and compare them with the results reported in the original paper.

Results 8 June 2024:
![Results 8 June 2024](./crossformer/progress/Results_8_June_2024.png)
[Full Report](./crossformer/progress/Progress_v1_8_June_2024.pdf)

Plots:

Result 3 - ETTH data plot:
![Result3](./crossformer/progress/R3_ETTH_plot.png)

Result 4 - AKAM data plot:
![Result4](./crossformer/progress/R4_AKAM_plot.png)

## Changes and Updates

As we make progress in reproducing the Crossformer model, we will document any changes or updates made to the code or methodology. This section will serve as a log of our work and provide transparency in the reproduction process.


## License

This project is licensed under the [MIT License](LICENSE).
