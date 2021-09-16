# Patient_abm type 2 diabetes module

## Description

This model is meant to show a simulation of patients in the NHS through the type 2 diabetes pathway.

Our model takes place in a fictional local area with two hospitals providing outpatient and inpatient services, and five GP practices.

Patient records will be constructed from scratch using a Bayesian network. Patients and environments will be added to the model using the JSON format. 

The model will run for a year with the first 500 patients and then the sensitivity of the initial set up (decisions made in each setting and their outcomes) will be evaluated. This is so the patients are in care settings that are relevant to their condition and it’s severity. 

After the first year that the model runs a further 9,500 patients will be added with the optimisation learning turned on with the output being recorded. 

Patients will exit the model if they develop end-stage kidney disease or liver disease.

### Creating patients

Dictionaries are used to input patients through patient_infos.json. Patient characteristics data were developed from PHE fingertips data (link)

Future versions of the model could use existing data sets (e.g. CPRD) to create a more accurate representation of 10,000 patients.