{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

```
The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make setup` or `make clean`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── metadata       <- Information about the tables given : Schema, Headers, etc.
│   ├── mock_data
│   │   ├── interim    <- Intermediate data that has been transformed.
│   │   ├── processed  <- The final, canonical data sets for modeling.
│   │   └── raw        <- The original, immutable data dump.
│   └── scripts        <- SQL scripts used to create the datasets
│
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│   └── template.ipynb
│                         
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── config      <- Specifications used to determine fields, parameters etc. for preprocessing, 
│   │                  modeling etc.
│   │
│   ├── utilities      <- Scripts for common functions used. The scripts can be split into company 
│   │   │                 functions (functions used across all projects) and local functions (functions 
│   │   │                 used only in this project)
│   │   └── e.g. company_func.py
│   │   └── e.g. project_func.py
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling : e.g. encoding, type conversion 
│   │                     steps.
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── train_model.py
│   │   └── predict_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
│
├── tests              <- Unittests, end-to-end testing etc. with mock data to check code.
│
└── .env               <- Environment File to load all necessary environment variables for local testing
```

--------
