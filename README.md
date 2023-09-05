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
├── Makefile
├── README.md
├── concurrent_notifier
│   ├── __init__.py
│   ├── observer.py
│   ├── subject.py
│   └── utils
│       ├── __init__.py
│       └── threading_utils.py
├── concurrent_observer_pattern.py
├── data_transformation
│   ├── __init__.py
│   ├── strategies
│   │   ├── __init__.py
│   │   ├── add_strategy.py
│   │   ├── base_strategy.py
│   │   ├── subtract_strategy.py
│   │   └── to_lowercase_strategy.py
│   └── utils
│       ├── __init__.py
│       └── data_transformer.py
├── docs
│   └── diagrams
│       └── images
│           └── cmms_integration_architecture.png
├── images
├── main.py
├── poetry.lock
├── pyproject.toml
├── tests
│   ├── __init__.py
│   ├── test_data_transformation.py
│   └── test_main.py
└── to_be_optimized.py
```

## Getting Started

1. **Clone the Repository;

2. **Install Dependencies:**

Using [Poetry](https://python-poetry.org/):

```bash
make init
```

3. **Run the Tests:**

```bash
make test
```
