import datetime

# Interactions for diabetes footcare
# "prevent_foot_community",
# "manage_foot_community",

# Community footcare 1: Preventing foot problems in the community
# Caring for feet with chiropody etc with footcare in the community (prevention)

def prevent_foot_community(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare prevention in community",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare prevention in community", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 43,     # NHS Ref costs
        "glucose": -1,  # dummy glucose impact, to be updated
        "carbon": 25,   # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 28: 0.2, 36: 0.3} # gp, inpatient, outpatient footcare

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        28: datetime.timedelta(days=20),
        36: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Community footcare 2: Managing foot problems in the community
# Caring for feet problems such as foot ulcers with footcare in the community (management)

def manage_foot_community(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare management in community",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare management in community", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 54,     # NHS Ref costs
        "glucose": -1,  # dummy glucose impact, to be updated
        "carbon": 25,   # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 28: 0.2, 36: 0.3} # gp, inpatient, outpatient footcare

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        28: datetime.timedelta(days=20),
        36: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
