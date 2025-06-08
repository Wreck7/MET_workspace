from store import hospital_data


def process_billing(patient_id):
    if patient_id not in hospital_data.get("patients", {}):
        print(f"Patient ID {patient_id} not found in the system.")
        return

    if patient_id not in hospital_data.get("treatment_costs", {}):
        print(f"\nNo treatment costs found for Patient ID: {patient_id}")
        print("Please add treatment costs first using the treatment cost")
        return
    patient_info = hospital_data["patients"][patient_id]
    treatments = hospital_data["treatment_costs"][patient_id]

    total_treatment_cost = 0
    for treatment in treatments:
        total_treatment_cost += treatment["cost"]

    additional_charges = {
        "Room Charges": 0,
        "Pharmacy": 0,
        "Lab Fees": 0,
        "Administrative Fee": 50,
    }
    print(f"\n--- Processing Bill for Patient: {patient_info['name']} ---")
    print(f"Patient ID: {patient_id}")
    date = input("Enter current date (YYYY-MM-DD): ").strip()
    add_extra = input("\nDo you want to add additional charges? (y/n): ").lower()
    if add_extra == "y":
        for charge_type in ["Room Charges", "Pharmacy", "Lab Fees"]:
            amount = float(input(f"Enter {charge_type} amount (0 if none): $"))
            additional_charges[charge_type] += amount
    total_additional = sum(additional_charges.values())
    grand_total = total_treatment_cost + total_additional

    print("\n" + "=" * 50)
    print("                    HOSPITAL BILL")
    print("=" * 50)
    print(f"Patient Name: {patient_info['name']}")
    print(f"Patient ID  : {patient_id}")
    print(f"Phone       : {patient_info.get('age', 'N/A')}")
    print(f"Address     : {patient_info.get('gender', 'N/A')}")
    print("-" * 50)
    print("TREATMENT COSTS:")
    print("-" * 50)
    i = 1
    for treatment in treatments:
        print(f"{i}. {treatment['treatment']} ${treatment['cost']}")
        print(f"   Insurance: {treatment['insurance']}")
        i += 1
    print(f"Subtotal (Treatments): ${total_treatment_cost}")
    print("-" * 50)
    print("ADDITIONAL CHARGES:")
    print("-" * 50)
    for charge_type, amount in additional_charges.items():
        if amount > 0:
            print(f"{charge_type}: ${amount}")
    print(f"Subtotal (Additional): ${total_additional}")
    print("=" * 50)
    print(f"GRAND TOTAL: ${grand_total}")
    print("=" * 50)

    billing_record = {
        "patient_id": patient_id,
        "patient_name": patient_info["name"],
        "treatments": treatments.copy(),
        "additional_charges": additional_charges.copy(),
        "total_treatment_cost": total_treatment_cost,
        "total_additional_cost": total_additional,
        "grand_total": grand_total,
        "billing_date": date,
    }
    hospital_data["billing"][patient_id] = billing_record
    print(f"\nBilling record saved for Patient ID: {patient_id}")
