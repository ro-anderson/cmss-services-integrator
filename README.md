# CMMS System Integrator

A detailed exploration into the integration of Computerized Maintenance Management Systems (CMMS) using Python.

## Overview

This project dives deep into the intricacies and potential techniques of integrating with various CMMS services. It showcases optimization tasks, the development of Python functions, and a proposal for a component architecture that can be adopted for similar integrations.

## Performed Tasks

1. **[Code Optimization](./docs/code_optimization.md):** Dive into the provided code in `to_be_optimized.py` to understand its operations and explore avenues for optimization.

2. **[Data Transformation Functions](./docs/data_transformation_functions.md):** Develop and understand Python functions for various data transformation operations and design a main function to invoke them.

3. **[Component Architecture Design](./docs/component_architecture_design.md):** Delve into creating an efficient design to integrate with web services, exploring its limitations and features.


## Repository Structure

```
.
├── Makefile                              # Automation scripts for building and testing
├── README.md                             # Project documentation and setup guide
├── concurrent_notifier                   # Concurrent notifier library
│   ├── __init__.py
│   ├── observer.py                       # Observer implementation for the pattern
│   ├── subject.py                        # Subject implementation for the pattern
│   └── utils
│       ├── __init__.py
│       └── threading_utils.py            # Utility functions for multithreading
├── concurrent_observer_pattern.py        # Demonstration of the observer pattern
├── data_transformation                   # Data transformation library
│   ├── __init__.py
│   ├── strategies
│   │   ├── __init__.py
│   │   ├── add_strategy.py               # Strategy to add numbers
│   │   ├── base_strategy.py              # Base strategy class
│   │   ├── subtract_strategy.py          # Strategy to subtract numbers
│   │   └── to_lowercase_strategy.py      # Strategy to convert strings to lowercase
│   └── utils
│       ├── __init__.py
│       └── data_transformer.py           # Transformer utility using strategies
├── docs
│   └── diagrams
│       └── images
│           └── cmms_integration_architecture.png  # Integration architecture diagram
├── images                                # Directory for miscellaneous images
├── main.py                               # Main execution file
├── poetry.lock                           # Lock file for dependencies (used by Poetry)
├── pyproject.toml                        # Python project metadata and dependencies
├── tests                                 # Unit tests directory
│   ├── __init__.py
│   ├── test_data_transformation.py       # Tests for data transformation functions
│   └── test_main.py                      # Main test file
└── to_be_optimized.py                    # Sample code for optimization
```

## Getting Started

1. **Clone the Repository**;

2. **Install Dependencies:**

Using [Poetry](https://python-poetry.org/):

```bash
make init
```

3. **Run the Tests:**

```bash
make test
```
