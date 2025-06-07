from store import hospital_data

def process_billing():
    patient_id = input("Enter patient ID: ").strip()
    if patient_id not in hospital_data["patients"]:
        return "Patient ID not found."

    patient = hospital_data["patients"][patient_id]
    patient_name = patient["name"]
    admission_date = input("Enter admission date (e.g., March 15, 2025): ").strip()
    discharge_date = input("Enter discharge date (e.g., March 18, 2025): ").strip()
    num_services = int(input("How many services do you want to enter? "))

    services = []
    total_cost = 0

    for i in range(num_services):
        desc = input(f"Enter description for service {i+1}: ").strip().capitalize()
        cost_str = input(f"Enter cost for '{desc}': ").strip()
        cost = float(cost_str)
        services.append({"description": desc, "cost": cost})
        total_cost += cost

    insurance_str = input("Enter insurance coverage percentage (e.g., 10): ").strip()
    insurance_coverage = float(insurance_str)
    discount = (insurance_coverage / 100) * total_cost
    final_cost = total_cost - discount

    billing_info = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "admission_date": admission_date,
        "discharge_date": discharge_date,
        "services": services,
        "total_cost": total_cost,
        "insurance_coverage": insurance_coverage,
        "final_cost": final_cost,
    }
    hospital_data["billing"].append(billing_info)

    print("\n=== BILLING SUMMARY ===")
    print("Patient:", patient_name)
    print("Admission Date:", admission_date)
    print("Discharge Date:", discharge_date)
    print("Service Charges:")
    for service in services:
        print(f"{service['description']}: ₹{service['cost']}")
    print(f"Total Cost: ₹{total_cost}")
    print(f"Insurance Coverage: {insurance_coverage}%")
    print(f"Final Amount Payable: ₹{final_cost}")
    print("-" * 50)

    return "Billing processed successfully."
