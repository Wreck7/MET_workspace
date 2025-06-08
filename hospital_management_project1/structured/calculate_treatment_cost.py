from store import hospital_data


def calculate_treatment_cost(patient_id):
    treatment_catalog = {
        "Basic Checkup": 100,
        "Surgery": 5000,
        "Physiotherapy": 300,
        "Dental Care": 200,
        "X-Ray": 150,
        "Blood Test": 80,
        "Consultation": 120,
        "Vaccination": 75,
        "Prescription": 50,
        "Emergency Care": 500,
    }

    num_treatments = int(input("How many treatments to add? "))
    treatments = []
    total_base_cost = 0

    # Collect all treatments first
    for i in range(num_treatments):
        print(f"\nEntering treatment {i + 1} of {num_treatments}")
        treatment_plan = input(
            f"Enter Treatment Plan ({', '.join(treatment_catalog.keys())}): "
        ).title()

        if treatment_plan not in treatment_catalog:
            print("Invalid treatment plan. Skipping this one.")
            continue

        base_cost = treatment_catalog[treatment_plan]
        treatments.append({"treatment": treatment_plan, "base_cost": base_cost})
        total_base_cost += base_cost

    # Apply single insurance discount to total
    discount_percent = float(
        input(
            f"\nTotal cost before insurance: ${total_base_cost}\n"
            "Enter Insurance Discount (%) [e.g., 10 for 10%]: "
        )
    )

    discount_amount = total_base_cost * (discount_percent / 100)
    total_final_cost = total_base_cost - discount_amount

    # Calculate proportional cost for each treatment
    if patient_id not in hospital_data["treatment_costs"]:
        hospital_data["treatment_costs"][patient_id] = []

    for treatment in treatments:
        # Calculate this treatment's share of the total final cost
        proportion = treatment["base_cost"] / total_base_cost
        treatment_final_cost = total_final_cost * proportion

        treatment_record = {
            "treatment": treatment["treatment"],
            "cost": round(treatment_final_cost, 2),
            "insurance": f"{discount_percent}% off total",
        }
        hospital_data["treatment_costs"][patient_id].append(treatment_record)

    print(f"\nTreatments added successfully!")
    print(f"Total base cost: ${total_base_cost}")
    print(f"Insurance discount: {discount_percent}% (${discount_amount:.2f})")
    print(f"Total final cost: ${total_final_cost:.2f}")

    print("\nPatient Treatment Cost Records:")
    print("-" * 50)
    for pid, treatments in hospital_data["treatment_costs"].items():
        print(f"Patient ID: {pid}")
        patient_total = sum(t["cost"] for t in treatments)
        for i, treatment in enumerate(treatments):
            print(f"  Treatment {i+1}:")
            print(f"    Plan      : {treatment['treatment']}")
            print(f"    Final Cost: ${treatment['cost']}")
            print(f"    Insurance : {treatment['insurance']}")
        print(f"  Total for Patient: ${patient_total:.2f}")
        print("-" * 50)