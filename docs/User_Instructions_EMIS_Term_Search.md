# Working Instructions for Medical Term Search Tool

# General Summary

The Medical Term Search Tool is a sophisticated yet user-friendly tool designed for researchers and professionals working with medical data. It allows for efficient searching of terms within a medical product dictionary, leveraging various search modes to cater to the specific needs of the user. This tool not only facilitates exact, partial, and regex-based searches but also enables users to specify the search column within the dictionary. With functionalities for refining search results and exporting them, this tool streamlines the process of medical data analysis.

The EMIS term search script is located in the folder at:

"C:\\Example\\Codelist_Generator\\Codelist Generation Scripts\\EMIS Term Search\\EMIS_Dictionary_Term_Search_20240411.ipynb"

# Step-by-Step Instructions

## Starting Jupyter

1. Launch the Terminal or Command Prompt: Access the terminal (Mac/Linux) or command prompt (Windows).  
    2\. Navigate to Your Project Directory: Use the \`cd\` command followed by the path to the directory containing your script. For example, \`cd C:\\Users\\YourName\\Documents\\MedicalSearchTool\`.  
    3\. Start Jupyter: Type \`jupyter notebook\` (or \`jupyter lab\` if you prefer) and press Enter. This will open Jupyter in your default web browser.

## Preparing the script

Prior to entering the search terms the script will require the file pathways to be set up. Find the source file and save this to your local system.

Once located copy the file pathway of the “202202_EMISMedicalDictionary_Alpha.txt" and replace this in the script at cell 2 line 2. The file pathway should look like the following example:

"C:\\Users\\ExampleUser\\Codelist_Generator\\Codelist Generation Scripts\\Sources\\EMIS Medical Dictionary\\202202_EMISMedicalDictionary_Alpha.txt"

![image](https://github.com/ndpchs-cprd/Codelist-Generation/assets/167761988/f0855004-1a5e-4d06-8113-0106841f546e)

Establish a folder for you search usually named after the condition you will be searching such as "C:\\Users\\Example_User\\Medical_Project\\Diabetes"

## Interacting with the Script

Follow the on-screen prompts to input your search terms, select the search column, and specify other search criteria as the script progresses. This section provides detailed guidance for each interaction with the script.

1. **Run Each Cell**: Execute the cells sequentially by selecting them and pressing Shift+Enter or using the run button in the toolbar.
2. **Input Method**:
    - The script will ask if you want to input search terms manually or use a file.
    - **For manual input**: Type **1** and press Enter. Then, input your search terms separated by commas, e.g., “**diabetes, asthma**, cough”
    - **For file input**: Type **2** and press Enter. Provide the full path to the file containing your search terms, one per line, e.g., **C:\\Data\\search_terms.txt**.
3. **Selecting the Search Column**:
    - The script will display the column headers from your dictionary. Each will be numbered.
    - Type the number corresponding to the column you wish to search in and press Enter.
4. **Choosing Search Type**:
    - You'll be prompted to select the search type. Type the number corresponding to your choice (e.g., **1** for exact match) and press Enter. The default choice is partial match, so you can press Enter directly to proceed with this option. Unless you have a specific search in mind always use the default here/
5. **Refining Search Results (Optional)**:
    - After the initial search, you can refine the results by adding more search terms or applying exclusions.
    - To add more terms, input them separated by commas when prompted.
    - To apply exclusions, input the terms you wish to exclude from the results, separated by commas.
6. **Viewing Results**:
    - The script will offer an option to view the search results directly. Type **y** and press Enter to view, or **n** to skip.

## Exporting Results

1. **Set Output Folder**: Input the full path to the folder where you want the results to be saved. This will be the folder you created for your condition in the preparing the script stage. The script will create the folder if it doesn't exist.
2. **Name Your File**: Enter the desired filename for the results file when prompted. Do not include the file extension; the script will handle it.

## Closing Jupyter

Go to "File" > "Save and Checkpoint", then "File" > "Close and Halt". Return to the terminal or command prompt window where Jupyter is running. Press \`Ctrl+C\` twice to shut it down.
