# pandas-npi
NPI validation made easy with Pandas

# Installation
pip install pandas-npi

# Basic Usage

### Update definitions

    import pandas_npi
    
    pandas_npi.update_definitions()
    
    #------------------------------additional details------------------------------
    
    #CMS updates the NPPES dataset about once per month. Running the above code
    #on a monthly basis will ensure that you are using the most up-to-date information.
    
    #Note that the function above has no parameters. Just run the function, and it will
    #notify you when the update is complete.
    
### Validate NPI

    import pandas as pd
    import pandas_npi
    
    df = pd.read_csv("your_dataset_here.csv")
    
    df = pandas_npi.validate(df, "npi_field_here")
    
    #------------------------------additional details------------------------------
    
    #The validate function takes care of cleaning/standardizing your npi. No need to
    #preprocess on your end! Even special characters and letters are removed.
    
    #Your dataset will be compared against the NPPES dataset. Four new fields will
    #be added to your dataset: nppes_name, nppes_type, nppes_status, and nppes_deactivation_date.
    #For full description of new fields, see below:
    
* nppes_name - gives the provider or facility name for the given NPI
* nppes_type - shows whether the NPI is a provider or facility NPI. Be aware that sole proprietors 
are not required to bill under a facility NPI
* nppes_status - shows whether an NPI is active or deactivated
* nppes_deactivation_date - If the NPI has been deactivated, lists the deactivation date. Else is NaN.
* **A final note - If an NPI does not exist now, and has never existed, nppes_name, nppes_type, and
nppes_status will all be labeled "invalid".**
    

    
