#!/usr/bin/env python
# coding: utf-8

# Codelist generator

import pandas as pd
import os
import glob
import re
from datetime import datetime
from collections import defaultdict

# Configuration of repository pathways - do not alter these ##
folder_paths = [
    r"C:\Users\Micheal\Desktop\Work\CPRD\Codelists\Sources\Complete_Repo"
]

# User input here: specify the location of the EMIS medical dictionary if using "MedCodeID"
emis_dictionary_path = r"C:\Users\Micheal\Desktop\Work\CPRD\Codelists\Sources\EMISMedicalDictionary_2022.txt"

# User input here: set your output folder to the location of your project
output_folder = r"C:\Users\Micheal\Desktop\Work\CPRD\Codelists\Test"

# User input here: set the search term here; most commonly this is condition name to take advantage of established codelists
search_terms = ['cancer']

# User input here: specify the coding system to use, "MedCodeID" or "Snomed"
coding_system = "MedCodeID"



search_mode = 'partial'  # Options: 'exact', 'partial', 'regex', 'all_partial'
column_to_search = None  # Specify column or None for full document search
exclusion_terms = ['Does not', 'No H/O', 'Family History']  # Specify your exclusion terms here

def create_output_folder(base_folder, search_term):
    base_name = search_term
    output_folder = os.path.join(base_folder, base_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        base_output_folder = output_folder
        index = 1
        while os.path.exists(output_folder):
            timestamp = datetime.now().strftime("%Y%m%d")
            output_folder = f"{base_output_folder}_{timestamp}_{index}"
            index += 1
        os.makedirs(output_folder)
    return output_folder

def save_results(df, output_folder, search_term, source_path):
    source_name = os.path.basename(source_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_folder, f"{source_name}_{search_term}_{timestamp}.csv")
    df.to_csv(output_file, index=False)
    print(f"Results for '{search_term}' from {source_name} saved to {output_file}")

def clean_dataframe(df):
    expected_columns = ['SNOMED_CT_Concept_ID', 'Med_Code_ID', 'Description', 'Search Term', 'Original_Source', 'Codelist_Name']
    df = df.reindex(columns=expected_columns)
    df.dropna(axis=1, how='all', inplace=True)
    return df

def drop_duplicates_based_on_snomed(df):
    return df.drop_duplicates(subset=['SNOMED_CT_Concept_ID'], keep='first')

def filter_empty_snomed_ids(df):
    return df[df['SNOMED_CT_Concept_ID'].notna()]

def apply_search(data, terms, search_mode):
    data_str = str(data).lower()
    matched_terms = []

    if search_mode == 'exact':
        matched_terms = [term for term in terms if term.lower() == data_str]
    elif search_mode == 'partial' or search_mode == 'all_partial':
        for term in terms:
            if term.lower() in data_str:
                matched_terms.append(term)
        if search_mode == 'all_partial' and len(matched_terms) != len(terms):
            matched_terms = []
    elif search_mode == 'regex':
        matched_terms = [term for term in terms if re.search(term.lower(), data_str, flags=re.IGNORECASE)]

    return ', '.join(matched_terms) if matched_terms else None

def search_files(search_term, folder_paths, output_folder, search_mode='exact', column=None):
    for folder_path in folder_paths:
        print(f"Searching in {folder_path}")
        consolidated_results = []

        for file_path in glob.glob(os.path.join(folder_path, '*.csv')):
            print(f"Processing {file_path}")
            df = pd.read_csv(file_path, dtype=str, encoding='utf-8')
            df = clean_dataframe(df)
            df = filter_empty_snomed_ids(df)

            if column and column in df.columns:
                df['matches'] = df[column].apply(lambda cell: apply_search(cell, search_terms, search_mode))
            else:
                df['matches'] = df.applymap(lambda cell: apply_search(cell, search_terms, search_mode)).any(axis=1)

            matched_df = df[df['matches']].drop('matches', axis=1)
            matched_df = drop_duplicates_based_on_snomed(matched_df)

            if not matched_df.empty:
                matched_df['Source'] = os.path.basename(file_path)
                matched_df['Search Term'] = ', '.join(search_terms)
                consolidated_results.append(matched_df)

        for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
            with open(file_path, 'r', encoding='utf-8') as file:
                df = pd.DataFrame([line.strip() for line in file], columns=['Content'])
                df = clean_dataframe(df)
                df = filter_empty_snomed_ids(df)

                df['matches'] = df['Content'].apply(lambda line: apply_search(line, search_term, search_mode))
                matched_df = df[df['matches']].drop('matches', axis=1)
                matched_df = drop_duplicates_based_on_snomed(matched_df)

                if not matched_df.empty:
                    matched_df['Source'] = os.path.basename(file_path)
                    matched_df['Search Term'] = search_term
                    save_results(matched_df, output_folder, search_term, file_path)

        if consolidated_results:
            all_matches = pd.concat(consolidated_results, ignore_index=True)
            all_matches = drop_duplicates_based_on_snomed(all_matches)
            save_results(all_matches, output_folder, " and ".join(search_terms), folder_path)

def combine_csv_files_by_search_term(folder_location, exclusion_terms=None):
    csv_files = glob.glob(os.path.join(folder_location, '**/*.csv'), recursive=True)
    combined_data_by_search_term = defaultdict(pd.DataFrame)
    columns_to_select = ['Med_Code_ID', 'Description', 'SNOMED_CT_Concept_ID', 'Search Term', 'Original_Source', 'Codelist_Name']
    
    for file_path in csv_files:
        print(f"Processing {file_path}")
        df = pd.read_csv(file_path, usecols=lambda column: column in columns_to_select, dtype=str)
        
        if exclusion_terms:
            pattern = '|'.join(exclusion_terms)
            df = df[~df['Description'].str.contains(pattern, case=False, na=False)]
        
        search_term = os.path.basename(os.path.dirname(file_path))
        combined_data_by_search_term[search_term] = pd.concat(
            [combined_data_by_search_term[search_term], df],
            ignore_index=True
        ).drop_duplicates(subset=['SNOMED_CT_Concept_ID'], keep='first')
        
        unique_ids_count = combined_data_by_search_term[search_term]['SNOMED_CT_Concept_ID'].nunique()
        print(f"Unique 'SNOMED_CT_Concept_ID' count for '{search_term}': {unique_ids_count}")
    
    for search_term, combined_df in combined_data_by_search_term.items():
        output_filename = f'combined_output_{search_term}.csv'
        combined_df.to_csv(os.path.join(folder_location, output_filename), index=False)
        print(f"Combined DataFrame for '{search_term}' saved to '{output_filename}'")
    
    return combined_data_by_search_term

def finalize_output(df, output_folder, search_terms):
    final_columns = ['Description', 'SNOMED_CT_Concept_ID', 'Med_Code_ID', 'Source_Codelist', 'Codelist_Name', 'Original_Source', 'Source', 'Search Term']
    df = df.reindex(columns=final_columns)
    df.fillna('', inplace=True)
    if coding_system == "Snomed":
        df['SNOMED_CT_Concept_ID'] = 'b' + df['SNOMED_CT_Concept_ID'].astype(str)  # Prepend 'b' to SNOMED codes
    df['Med_Code_ID'] = 'a' + df['Med_Code_ID'].astype(str)  # Prepend 'a' to MedCodeIDs
    final_filename = f"Final_Processed_File_{'_'.join(search_terms)}.csv"
    df.to_csv(os.path.join(output_folder, final_filename), index=False)
    print(f"Final file saved as {final_filename}")

def detect_delimiter(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        if '\t' in first_line:
            return '\t'
        else:
            return ','

def match_to_emis_dictionary(df, emis_dict_path):
    try:
        delimiter = detect_delimiter(emis_dict_path)
        emis_df = pd.read_csv(emis_dict_path, dtype=str, delimiter=delimiter)
        emis_df.columns = emis_df.columns.str.strip()  # Remove any leading/trailing whitespace
        print("EMIS dictionary columns:", emis_df.columns)  # Debug print
    except pd.errors.ParserError as e:
        print(f"Error reading EMIS dictionary file: {e}")
        return df
    
    print("Search results columns:", df.columns)  # Debug print
    df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace

    # Prepend 'b' to SNOMED codes before matching
    df['SNOMED_CT_Concept_ID'] = 'b' + df['SNOMED_CT_Concept_ID'].astype(str)

    if 'Med_Code_ID' not in df.columns:
        print("Med_Code_ID column missing in search results DataFrame.")
        return df
    if 'Med_Code_Id' not in emis_df.columns:
        print("Med_Code_Id column missing in EMIS dictionary DataFrame.")
        return df
    
    merged_df = df.merge(emis_df, left_on='Med_Code_ID', right_on='Med_Code_Id', how='left', suffixes=('', '_EMIS'))
    return merged_df

if __name__ == "__main__":
    for term in search_terms:
        term_output_folder = create_output_folder(output_folder, term)
        search_files(term, folder_paths, term_output_folder, search_mode, column_to_search)
    
    combined_data = combine_csv_files_by_search_term(output_folder, exclusion_terms)
    for search_term, df in combined_data.items():
        if coding_system == "MedCodeID":
            df = match_to_emis_dictionary(df, emis_dictionary_path)
        finalize_output(df, output_folder, [search_term])