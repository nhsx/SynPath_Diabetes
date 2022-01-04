import datetime

# Interactions for inpatient care
# "review_and_consultation",
# "bd_hypoglycaemic_ep",
# "bd_hyperglycaemic_ep",
# "bd_lower_limb_compl",
# "enhanced_independence",
# "retinal_procedure",
# "amputation"

# Inpatient interaction 1: Inpatient review and consultation (might take out if not in spell) 

def review_and_consultation(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "review and consultation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "review and consultation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,       # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 5032,     # carbon impact, PSSRU 2018-19
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 2: Hypoglycaemic episode bed day

def bd_hypoglycaemic_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "hypoglycaemic ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "hypoglycaemic ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,       # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 5032,     # carbon impact, PSSRU 2018-19
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 3: Hyperglycaemic episode bed day

def bd_hyperglycaemic_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "hyperglycaemic ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "hyperglycaemic ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,       # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 5032,     # carbon impact, PSSRU 2018-19
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 4: Lower limb complications bed day

def bd_lower_limb_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "lower limb ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "lower limb ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,           # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,          # dummy glucose impact, to be updated
        "carbon": 5032,         # carbon impact, to be updated   
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 5: Enhanced independence

def enhanced_indep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "enhanced independence",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "enhanced independence", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,           # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,          # dummy glucose impact, to be updated
        "carbon": 5032,         # carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 6: Retinal procedure

def retinal_procedure(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "retinal procedure",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "retinal procedure", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,           # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,          # dummy glucose impact, to be updated
        "carbon": 5032,         # carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Inpatient interaction 7: Amputation

def amputation(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "amputation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "amputation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053,           # NEL long stay from PSSRU 2018-19 - to be updated
        "glucose": -1,          # dummy glucose impact, to be updated
        "carbon": 5032,         # carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.3, 40: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
        40: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )