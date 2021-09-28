# SynPath_Diabetes
Demonstration of using SynPath version 1.0.0 for creating a diabetes pathway.  This repo sits as a module inside the `templates` folder as https://github.com/nhsx/SynPath/tree/main/template/t2dm

See Readme in https://github.com/nhsx/SynPath for SynPath documentation.

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

# Usage

### Roadmap

See the [open issues](https://github.com/nhsx/SynPath_Diabetes/issues) for a list of proposed features (and known issues).

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

_See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance._

### License

Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._

### Contact

To find out more about the [Analytics Unit](https://www.nhsx.nhs.uk/key-tools-and-info/nhsx-analytics-unit/) visit our [project website](https://nhsx.github.io/AnalyticsUnit/projects.html) or get in touch at [analytics-unit@nhsx.nhs.uk](mailto:analytics-unit@nhsx.nhs.uk).

### Acknowledgements

