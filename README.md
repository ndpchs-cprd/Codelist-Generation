# **Comprehensive Medical Codelist Management System**

## Description
This project provides a suite of tools for researchers and healthcare professionals to manage and utilize medical codelists effectively. It integrates multiple sources, including the NHS PCD refset, HDRUK phenotype library, AIM RSF codelists, CALIBER project codelists, and Opencodelists.org, facilitating robust search capabilities and conversion to proprietary formats like CPRD Aurum's MedCodeIDs. These tools streamline the process of defining conditions, diseases, treatments, and medications for data extraction and research purposes.

## Features
* Codelist Searcher: Search through multiple pre-existing codelists using disease or condition names.
* Codelist Converter: Convert standard SNOMED codelists to CPRD Aurum-specific MedCodeIDs.
* EMIS Dictionary Searcher: Perform advanced searches on the EMIS medical dictionary to locate similar terms using a variety of techniques.

## Installation

Clone the repository:
```python
git clone https://github.com/yourusername/medical-codelist-management.git
```

Install required packages:
```python
pip install -r requirements.txt
```

##Usage

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
NHS PCD refset
HDRUK phenotype library
AIM RSF codelists
CALIBER project
Opencodelists.org
