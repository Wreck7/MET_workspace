from store import hospital_data

def track_medication_inventory(med_id):
    if med_id in hospital_data["inventory"]:
        print(f"\nMedication '{med_id}': {hospital_data["inventory"][med_id]["name"]} already exists in the inventory.")
        add_qty = int(input("Enter quantity to add: "))
        hospital_data["inventory"][med_id]["quantity"] += add_qty
        print(
            f"Updated quantity for '{med_id}': {hospital_data["inventory"][med_id]["name"]} is now {hospital_data['inventory'][med_id]['quantity']}.\n"
        )
    else:
        name = input("Enter Medication Name: ").title()
        quantity = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
        supplier = input("Enter Supplier Name: ")
        hospital_data["inventory"][med_id] = {
            "name": name,
            "quantity": quantity,
            "expiry": expiry,
            "supplier": supplier,
        }
        print(f"\nMedication '{med_id}' added successfully.\n")

    print("Current Medication Inventory:")
    print("-" * 50)
    for med, info in hospital_data["inventory"].items():
        print(f"ID: {med}")
        print(f"  Name     : {info['name']}")
        print(f"  Quantity : {info['quantity']}")
        print(f"  Expiry   : {info['expiry']}")
        print(f"  Supplier : {info['supplier']}")
        print("-" * 50)
