import os
import random
import sys
from faker import Faker
from pyspark.sql import SparkSession
import pandas as pd


# =========================================================
# PYTHON CONFIGURATION FOR WINDOWS
# =========================================================

python_path = sys.executable

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

print("Python executable:", python_path)
print("PYSPARK_PYTHON:", os.environ["PYSPARK_PYTHON"])
print("PYSPARK_DRIVER_PYTHON:", os.environ["PYSPARK_DRIVER_PYTHON"])


# =========================================================
# SPARK SESSION
# =========================================================

spark = (
    SparkSession.builder
    .appName("FakerGenerator")
    .master("local[*]")
    .getOrCreate()
)

faker = Faker()


# =========================================================
# RECORD COUNTS
# =========================================================

num_departments = 16
num_providers = 300
num_patients = 3000
num_encounters = 10000
num_transactions = 50000


# =========================================================
# 1. DEPARTMENT DATA
# =========================================================

print("Department Data Generator Started")
print("----------------------------------")

department_names = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Oncology",
    "Dermatology",
    "General Medicine",
    "Emergency",
    "Radiology",
    "Gastroenterology",
    "Nephrology",
    "Urology",
    "Psychiatry",
    "ENT",
    "Ophthalmology",
    "Pulmonology"
]

department_locations = [
    "Block A",
    "Block B",
    "Block C",
    "Block D",
    "Block E"
]

departments = []

for i in range(1, num_departments + 1):

    dept_id = f"D{i:03d}"

    departments.append((
        dept_id,
        department_names[i - 1],
        random.choice(department_locations),
        department_names[i - 1]
    ))


department_schema = """
    DeptID string,
    Name string,
    Location string,
    Specialization string
"""

departments_df = spark.createDataFrame(
    departments,
    department_schema
)

print("\n===== DEPARTMENTS =====")
print("Total Departments:", departments_df.count())
print("===== END DEPARTMENTS =====")


# =========================================================
# 2. PROVIDER DATA
# =========================================================

print("\nProvider Data Generator Started")
print("----------------------------------")

specializations = [
    "Cardiologist",
    "Neurologist",
    "Orthopedic",
    "Pediatrician",
    "Oncologist",
    "Dermatologist",
    "General Physician",
    "Emergency Physician",
    "Radiologist",
    "Gastroenterologist",
    "Nephrologist",
    "Urologist",
    "Psychiatrist",
    "ENT Specialist",
    "Ophthalmologist",
    "Pulmonologist"
]

dept_ids = [row[0] for row in departments]

providers = []

for i in range(1, num_providers + 1):

    provider_id = f"P{i:04d}"

    providers.append((
        provider_id,
        faker.name(),
        random.choice(specializations),
        random.choice(dept_ids),
        faker.phone_number(),
        faker.email(),
        faker.date_between(
            start_date="-10y",
            end_date="today"
        )
    ))


provider_schema = """
    ProviderID string,
    ProviderName string,
    Specialization string,
    DeptID string,
    Phone string,
    Email string,
    HireDate date
"""

provider_df = spark.createDataFrame(
    providers,
    provider_schema
)

print("\n===== PROVIDERS =====")
print("Total Providers:", provider_df.count())
print("===== END PROVIDERS =====")


# =========================================================
# 3. PATIENT DATA
# =========================================================

print("\nPatient Data Generator Started")
print("----------------------------------")

genders = [
    "Male",
    "Female"
]

blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "O+",
    "O-",
    "AB+",
    "AB-"
]

insurance_types = [
    "Private",
    "Government",
    "Corporate",
    "Self-Pay"
]

patients = []

for i in range(1, num_patients + 1):

    patient_id = f"P{i:05d}"

    dob = faker.date_of_birth(
        minimum_age=2,
        maximum_age=100
    )

    reg_date = faker.date_between(
        start_date="-3y",
        end_date="today"
    )

    patients.append((
        patient_id,
        faker.name(),
        random.choice(genders),
        dob,
        faker.phone_number(),
        faker.email(),
        faker.address().replace("\n", ", "),
        random.choice(blood_groups),
        random.choice(insurance_types),
        reg_date
    ))


patients_schema = """
    PatientID string,
    PatientName string,
    Gender string,
    DateOfBirth date,
    Phone string,
    Email string,
    Address string,
    BloodGroup string,
    InsuranceType string,
    RegistrationDate date
"""

patients_df = spark.createDataFrame(
    patients,
    patients_schema
)

print("\n===== PATIENTS =====")
print("Total Patients:", patients_df.count())
print("===== END PATIENTS =====")


# =========================================================
# 4. ENCOUNTER DATA
# =========================================================

print("\nEncounters Data Generator Started")
print("----------------------------------")

encounter_types = [
    "OPD",
    "IPD",
    "Emergency",
    "Follow-up"
]

encounter_status = [
    "Completed",
    "Cancelled",
    "In Progress"
]

diagnoses = [
    "Hypertension",
    "Diabetes",
    "Fever",
    "Migraine",
    "Fracture",
    "Asthma",
    "Heart Disease",
    "Routine Checkup"
]

treatment_advice = [
    "Medication prescribed",
    "Rest and observation",
    "Follow-up required",
    "Diagnostic test recommended",
    "Hospital admission advised",
    "Lifestyle modification advised",
    "Surgery recommended"
]

patient_ids = [i[0] for i in patients]
provider_ids = [i[0] for i in providers]

encounters = []

for k in range(1, num_encounters + 1):

    encounter_id = f"E{k:05d}"

    encounter_date = faker.date_between(
        start_date="-3y",
        end_date="today"
    )

    followup_date = faker.date_between(
        start_date=encounter_date,
        end_date="+90d"
    )

    encounters.append((
        encounter_id,
        random.choice(patient_ids),
        random.choice(provider_ids),
        encounter_date,
        random.choice(encounter_types),
        random.choice(encounter_status),
        random.choice(diagnoses),
        random.choice(treatment_advice),
        followup_date
    ))


encounter_schema = """
    EncounterID string,
    PatientID string,
    ProviderID string,
    EncounterDate date,
    EncounterType string,
    Status string,
    Diagnosis string,
    TreatmentAdvice string,
    FollowUpDate date
"""

encounter_df = spark.createDataFrame(
    encounters,
    encounter_schema
)

print("\n===== ENCOUNTERS =====")
print("Total Encounters:", encounter_df.count())
print("===== END ENCOUNTERS =====")


# =========================================================
# 5. TRANSACTION DATA
# =========================================================

print("\nTransactions Data Generator Started")
print("----------------------------------")

transaction_types = [
    "Consultation",
    "Lab Test",
    "Medicine",
    "X-Ray",
    "MRI",
    "CT Scan",
    "Procedure"
]

payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "Insurance",
    "UPI"
]
# payment_statuses = [
#     "Paid",
#     "Pending",
#     "Failed"
# ]



encounter_ids = [i[0] for i in encounters]

transactions = []

for j in range(1, num_transactions + 1):

    transaction_id = f"T{j:07d}"

    transaction_date = faker.date_between(
        start_date="-3y",
        end_date="today"
    )

    amount = round(
         random.uniform(1000, 1000000),
       2
    )

    # insurance_amount = round(
    #     amount * random.uniform(0, 0.8),
    #     2
    # )

    # patient_amount = round(
    #     amount - insurance_amount,
    #     2
    # )

    transactions.append((
        transaction_id,
        random.choice(encounter_ids),
        transaction_date,
        random.choice(transaction_types),
        amount,
        random.choice(payment_methods),
        #random.choice(payment_statuses),
        #insurance_amount,
        #patient_amount
    ))


transaction_schema = """
    TransactionID string,
    EncounterID string,
    TransactionDate date,
    
    TransactionType string,
    Amount double,
    PaymentMethod string
"""

transaction_df = spark.createDataFrame(
    transactions,
    transaction_schema
)

print("\n===== TRANSACTIONS =====")
print("Total Transactions:", transaction_df.count())
print("===== END TRANSACTIONS =====")


# =========================================================
# WRITE CSV FILES
# =========================================================

output_path = r"D:\Git\SQL\healthcare-pyspark\datasets"

os.makedirs(output_path, exist_ok=True)

print("\n----------- CSV FILES -----------")


departments_df.toPandas().to_csv(
    f"{output_path}/departments.csv",
    index=False
)

print("departments.csv generated")


provider_df.toPandas().to_csv(
    f"{output_path}/providers.csv",
    index=False
)

print("providers.csv generated")


patients_df.toPandas().to_csv(
    f"{output_path}/patients.csv",
    index=False
)

print("patients.csv generated")


encounter_df.toPandas().to_csv(
    f"{output_path}/encounters.csv",
    index=False
)

print("encounters.csv generated")


transaction_df.toPandas().to_csv(
    f"{output_path}/transactions.csv",
    index=False
)

print("transactions.csv generated")




# =========================================================
# STOP SPARK
# =========================================================

spark.stop()

print("\n===================================")
print("ALL EMR DATA GENERATED SUCCESSFULLY")
print("===================================")