import datetime

# Smoking service interaction 1: Smoking cessation
# For people who smoke (Y), 20% chance of successfully stopping smoking if they go to the service


def smoking_cessation(patient, environment, patient_time):
   encounter = {
       "resource_type": "Encounter",
       "name": "smoking cessation",
       "start": patient_time,
    }

   entry = {
        "resource_type": "Condition",
        "name": "stop_smoking",
        "start": patient_time,
        "cost": 140,            # PSSRU Unit cost 2018-19 for male patients (female patients £135)
        "glucose": -1,          # dummy glucose impact, to be updated
        "carbon": 22,           # PSSRU 2018-19 value for outpatient visit carbon impact
    } 
    
   new_patient_record_entries = [encounter, entry]

   next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

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