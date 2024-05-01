[![codecov](https://codecov.io/gh/arturogonzalezm/temperature_predictions/graph/badge.svg?token=U18KTIAC7R)](https://codecov.io/gh/arturogonzalezm/temperature_predictions)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://github.com/arturogonzalezm/temperature_predictions/blob/master/LICENSE)
[![Documentation](https://img.shields.io/badge/docs-pdf-blue.svg)](https://github.com/arturogonzalezm/temperature_predictions/blob/master/docs/temperature-predictions-English.pdf)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Temperature Predictions - HackerRank Challenge

This repository contains the solution to the HackerRank challenge "Temperature Predictions". 
The challenge consists of predicting the temperature of a given day based on the temperatures of the previous days. 
The solution is implemented in Python and the code is documented in the file `temperature_predictions.py`. 
The documentation of the code is available in the file `temperature-predictions-English.pdf`.

## Overview
This Python script reads climate data from standard input, processes this data to interpolate missing values, and prints the interpolated values. It's designed for use directly from the command line and is built to handle tabular data effectively.

## Installation

### Prerequisites
- Python (3.x recommended)
- Pandas library

To install Pandas, you can use pip:

```bash
pip intsall -r requirements.txt
```

# Climate Data Processor Flow

This diagram illustrates the sequence of operations in the Climate Data Processor script:

```mermaid
flowchart TD
    A[Start] --> B[Create Instance]
    B --> C{Singleton Check}
    C -- "If None" --> D[Create New Instance]
    C -- "If Exists" --> E[Use Existing Instance]
    D --> F[Initialize Data]
    E --> F
    F --> G[Read Input]
    G --> H[Process Data]
    H --> I[Print Interpolated Values]
    I --> J[End]

    classDef className fill:#f9f,stroke:#333,stroke-width:2px;
    class B,C,D,E,F,G,H,I className;
```
