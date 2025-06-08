from register_patient import register_patient
from add_medical_staff import add_medical_staff
from schedule_appointment import schedule_appointment
from create_medical_record import create_medical_record
from process_billing import process_billing
from manage_emergency_admission import manage_emergency_admission
from track_medication_inventory import track_medication_inventory
from assign_room import assign_room
from calculate_treatment_cost import calculate_treatment_cost
from generate_patient_report import generate_patient_report
from analyze_hospital_efficiency import analyze_hospital_efficiency
from manage_discharge_process import manage_discharge_process
from store import hospital_data
from registration import registration


def main():
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Register Patient")
        print("2. Add Medical Staff")
        print("3. Schedule Appointment")
        print("4. Create Medical Record")
        print("5. Process Billing")
        print("6. Emergency Admission")
        print("7. Track Medication Inventory")
        print("8. Assign Room")
        print("9. Calculate Treatment Cost")
        print("10. Generate Patient Report")
        print("11. Analyze Hospital Efficiency")
        print("12. Manage Discharge Process")
        print("13. Exit\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            registration()

        elif choice == "2":
            staff_id = f"{len(hospital_data['staff'])+1}"
            role = input("Enter role: ").capitalize()
            name = input("Enter name: ").title()
            specialization = input("Enter specialization: ").capitalize()
            start_time = input("Enter shift start time: ")
            end_time = input("Enter shift end time: ")
            phone = input("Enter phone number: ")
            print(
                add_medical_staff(
                    staff_id, role, name, specialization, start_time, end_time, phone
                )
            )

        elif choice == "3":
            patient_id = input("Enter patient ID: ").strip()
            doctor_id = input("Enter doctor ID: ").strip()
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ").strip()
            appointment_time = input(
                "Enter appointment time (HH:MM, 24-hour format): "
            ).strip()
            appointment_type = input("Enter appointment type: ").strip().capitalize()
            print(
                schedule_appointment(
                    patient_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    appointment_type,
                )
            )

        elif choice == "4":
            patient_id = input("Enter patient ID: ").strip()
            doctor_id = input("Enter doctor ID: ").strip()
            diagnosis = input("Enter diagnosis: ").capitalize()
            treatment = input("Enter treatment: ").capitalize()
            prescription = input("Enter prescription: ").capitalize()
            record_date = input("Enter date of record (YYYY-MM-DD): ").strip()
            print(
                create_medical_record(
                    patient_id,
                    doctor_id,
                    diagnosis,
                    treatment,
                    prescription,
                    record_date,
                )
            )

        elif choice == "5":
            print(process_billing())

        elif choice == "6":
            patient_id = input("Enter patient ID: ")
            emergency_type = input("Enter emergency type: ")
            severity_level = input("Enter severity level: ")
            print(
                manage_emergency_admission(patient_id, emergency_type, severity_level)
            )

        elif choice == "7":
            med_id = input("Enter Medication ID: ")
            track_medication_inventory(med_id)

        elif choice == "8":
            patient_id = input("Enter Patient ID: ")
            assign_room(patient_id)

        elif choice == "9":
            patient_id = input("Enter Patient ID: ")
            calculate_treatment_cost(patient_id)

        elif choice == "10":
            patient_id = input("Enter patient ID: ").strip()
            report_type = input("Enter report type (e.g., Blood Test, X-Ray): ").strip()
            print(generate_patient_report(patient_id, report_type))

        elif choice == "11":
            analyze_hospital_efficiency()

        elif choice == "12":
            patient_id = input("Enter patient ID: ").strip()
            discharge_date = input("Enter discharge date (YYYY-MM-DD): ").strip()
            follow_up_instructions = input("Enter follow-up instructions: ").strip()
            print(
                manage_discharge_process(
                    patient_id, discharge_date, follow_up_instructions
                )
            )

        elif choice == "13":
            print("Exiting system.")
            break

        else:
            print("Invalid option. Try again.")


main()
