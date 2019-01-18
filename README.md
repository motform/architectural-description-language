# Paraphs
Turns your poems into many diffirent, but relatively similar, early modernist artworks!

## Installation
Getting dependances set up for Paraphs requires a bit of extra work. If you use pipenv, then the pipfile contains all the neccecary information. Otherwise, the modules required are:

* NLTK
* Pycario
* Textblob

Additionaly, if you want to build the project, you'll also need:

* pip
* setuptools
* wheel

Pycario requires Cairo to be installed. Instructions for this can be found on https://www.cairographics.org

If you have never used the NLTK before, it might require you to download additional data. For example, this project uses NLTK stopwords. To download these, run a python interpreter and input the following:

```py
import nltk
nltk.download('stopwords')
```

## Usage
If you decide to build the project with ```pip install -e .``` , then just run it using the Paraphs alias. You can also run it directly with the Python interpreter, using ```python __init__.py [arguments]```

Paraphs requires at least two arguments to work: 1. an input file 2. an outpute filename or an output file type. For all the possible arguments, consult the ```--help``` flag. Regular useage might look something like this:

```paraphs sample_1.txt -f pdf -s```

## About
This project was built as a final examination for Linneuniversitete's course _Programming for Digital Humanities_.
