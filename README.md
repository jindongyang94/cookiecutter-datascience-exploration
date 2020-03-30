# Cookiecutter Data Science - AIDA

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)

### Requirements to use the cookiecutter template:

-----------

 - Python 2.7 or 3.7
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:

------------

    cookiecutter https://github.com/jindongyang94/cookiecutter-data-science-custom.git


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure

------------

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
│   │                     predictions
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

### Installing development requirements

------------

'''python
    pip install -r requirements.txt
'''