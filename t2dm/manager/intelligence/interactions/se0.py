import datetime

# All the interactions for structured education
# "f2f_group_education",
# "ddpp",
# "online_lifestyle"

# Structured education interaction 1: Face to face group education

def f2f_group_education(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "f2f group education",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "f2f group education", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 203,                # Intervention cost from the DESMOND RCT, to be updated to a more recent figure
        "glucose": -1,              # dummy glucose impact, to be updated
        "carbon": 100,              # dummy carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.8, 29: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Structured education interaction 2: DDPP

def ddpp(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "ddpp_course",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "ddpp_course", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 150,                # Not aware of economic evaluation of DDP so far, to be updated
        "glucose": -1,              # dummy glucose value, to be updated
        "carbon": 100,              # dummy carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.8, 29: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Structured education interaction 3: Online lifestyle education 
def online_lifestyle(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "online lifestyle education",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "online lifestyle education", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 268,                # Intervention cost in NHS pilot for Liva app, Nuffield Trust
        "glucose": -1,              # dummy glucose impact, to be update
        "carbon": 100,              # dummy carbon impact, to be updated
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.8, 29: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )