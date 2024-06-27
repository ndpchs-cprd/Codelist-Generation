# **Comprehensive Medical Codelist Management System**

## Description
This project provides tools for researchers and healthcare professionals to make CPRD medical codelists effectively and efficiently. It integrates codelists from multiple sources, including the NHS PCD refset, HDRUK phenotype library, AIM RSF codelists, CALIBER project codelists, and Opencodelists.org. It also offers search capabilities with relavent terms for the creation of new codelists and the option to combine these with existing codelists.  These tools streamline the process of defining conditions, diseases, treatments, and medications for data extraction and research purposes. The tool gives you the option to create codelists of SNOMED CT Concept IDs, CPRD Aurum Medcode IDs or both.

## Features
* Codelist Searcher: Search through repositories described above using disease or condition names.
* Codelist Converter: Convert standard SNOMED codelists to CPRD Aurum-specific MedCodeIDs.
* EMIS Dictionary Searcher: Perform tailored searches on the EMIS medical dictionary using relevant search terms. Options include exact match, partial match, starts with, ends with, and/or, and exlude.

## Installation

1. Download the codelist repository, scripts and documentation:

Click here: 

![image](https://github.com/ndpchs-cprd/Codelist-Generation/assets/167761988/e9b58933-80e1-4371-95a6-571cd6d576ec)

Select "Download Zip":


![image](https://github.com/ndpchs-cprd/Codelist-Generation/assets/167761988/61096b0b-2f7c-4bd5-b862-8b0b1bdeb912)



Navigate to downloaded zip folder and extract. 

Unzip folder in desired location. 

OR: 

If familiar with github, clone the repository directly from your terminal:

```python
git clone https://github.com/yourusername/medical-codelist-management.git
```



## Installing Anaconda

Download Anaconda at: [Anaconda Download Link](https://www.anaconda.com/download) and follow the install instructions provided at: [Anaconda Instructions](https://docs.anaconda.com/anaconda/install/windows/)

OR

If familiar with github. Install required packages from the terminal:

```python
pip install -r requirements.txt
```

## Running Jupyter Notebook from Anaconda

Follow the instructions provided to begin using Jupter Notebooks directly from Anaconda: [Jupyter Instuctions](https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/jupyter/)

more detailed instuctions and examples can be found at the [Jupyter official documentation](https://docs.jupyter.org/en/latest/)

## Usage

Here’s how to use the tools provided in the repository:

Searching Codelists:
```python
codelist_searcher.py "diabetes"
```

Converting to MedCodeIDs:

```python
codelist_converter.py "inputfile.csv"
```

Searching EMIS Dictionary:

```python
emis_searcher.py "hypertension"
```

## Contributing
Contributions are welcome! Please read the CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
* NHS PCD refset
* HDRUK phenotype library
* AIM RSF codelists
* CALIBER project
* Opencodelists.org
