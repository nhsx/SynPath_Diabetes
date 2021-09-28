import datetime

# Interactions for eye care services in the community
# "retinopathy_screening"

# Eye care 1: Retinopathy service
# Appointments for screening and advice within a specialist antenatal service

def retinopathy_screening(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "retinopathy screening",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "retinopathy screening", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 74,     # NHS Ref costs
        "glucose": 0,   # dummy glucose impact, to be updated
        "carbon": 22,   # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {23: 0.5, 27: 0.5} # afilbercept and inpatient for retinal procedure

    next_environment_id_to_time = {
        23: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Eye care 2: Afilbercept prescription for AMD (high cost drug)
# Drug used to treat wet age-related macular degeneration
def aflibercept_prescription(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "afilbercept prescription",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "afilbercept prescription", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 809,    # NHS Ref costs
        "glucose": 0,   # dummy glucose impact, to be updated
        "carbon": 22,   # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} # gp and inpatient for retinal procedure

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )