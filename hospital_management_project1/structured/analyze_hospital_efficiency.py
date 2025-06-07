from store import hospital_data


def analyze_hospital_efficiency():
    metric = {
        "total_patients": len(hospital_data["patients"]),
        "admitted_patients": sum(1 for p in hospital_data["patients"]),
        "emergency_count": len(hospital_data["emergency_cases"]),
    }
    print(f"\n{'-'*35}\n    Hospital Efficiency\n")
    print(f"Total Patients Registered  : {metric['total_patients']}")
    print(f"Currently Admitted Patients: {metric['admitted_patients']}")
    print(f"Emergency Cases            : {metric['emergency_count']}")
    print("-" * 35)