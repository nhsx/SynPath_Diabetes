import datetime  # enables the start time elements in date and time format

# Mental health interaction 1: Psychological assessment

def psychol_assessment(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "psychological assessment",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "psychological assessment", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96,         # NHS Ref cost for IAPT - PSSRU
        "glucose": 0,       # dummy glucose impact, to be updated
        "carbon": 50,       # update for accurate carbon
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 14: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        14: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Mental health interaction 2: IAPT

def iapt(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "iapt",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "iapt", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96,         # NHS Ref cost for IAPT - PSSRU
        "glucose": 0,       # dummy glucose impact, to be updated
        "carbon": 50,       # update for accurate carbon
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 14: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        14: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Mental health interaction 3: Community mental health for severe mental illness

def cmh_for_smi(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "cmh for smi",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "cmh for smi", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96,             # NHS Ref cost for IAPT - PSSRU
        "glucose": 0,           # dummy glucose impact, to be updated
        "carbon": 50,           # update for accurate carbon 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 14: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        14: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
