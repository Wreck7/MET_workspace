from store import hospital_data


def calculate_treatment_cost(patient_id):
    treatment_catalog = {
        "Basic Checkup": 100,
        "Surgery": 5000,
        "Physiotherapy": 300,
        "Dental Care": 200,
    }
    num_treatments = int(input("How many treatments to add? "))
    if patient_id not in hospital_data["treatment_costs"]:
        hospital_data["treatment_costs"][patient_id] = []
    for i in range(num_treatments):
        print(f"\nEntering treatment {i + 1} of {num_treatments}")
        treatment_plan = input(
            f"Enter Treatment Plan ({', '.join(treatment_catalog.keys())}): "
        ).title()

        if treatment_plan not in treatment_catalog:
            print("Invalid treatment plan. Skipping this one.")
            continue
        base_cost = treatment_catalog[treatment_plan]
        discount_percent = float(
            input("Enter Insurance Discount (%) [e.g., 10 for 10%]: ")
        )
        discount_amount = base_cost * (discount_percent / 100)
        final_cost = base_cost - discount_amount

        treatment_record = {
            "treatment": treatment_plan,
            "cost": round(final_cost, 2),
            "insurance": f"{discount_percent}% off",
        }
        hospital_data["treatment_costs"][patient_id].append(treatment_record)
        print("Treatment added.\n")
    print("\nPatient Treatment Cost Records:")
    print("-" * 50)
    for pid, treatments in hospital_data["treatment_costs"].items():
        print(f"Patient ID: {pid}")
        for i, info in enumerate(treatments, 1):
            print(f"  Treatment {i}:")
            print(f"    Plan      : {info['treatment']}")
            print(f"    Final Cost: ${info['cost']}")
            print(f"    Insurance : {info['insurance']}")
        print("-" * 50)
