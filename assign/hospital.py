class Patient:
    def __init__(self, patient_id, name, age, gender, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient_id, name, age, gender, contact_number):
        patient = Patient(patient_id, name, age, gender, contact_number)
        self.patients.append(patient)

    def display_patients(self):
        if not self.patients:
            print("No patients in the system.")
        else:
            print("Patient Details:")
            for patient in self.patients:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Contact: {patient.contact_number}")

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def delete_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} has been deleted.")
                return
        print(f"Patient with ID {patient_id} not found in the system.")

    def update_patient(self, patient_id, name, age, gender, contact_number):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.name = name
                patient.age = age
                patient.gender = gender
                patient.contact_number = contact_number
                print(f"Patient with ID {patient_id} has been updated.")
                return
        print(f"Patient with ID {patient_id} not found in the system.")

if __name__ == "__main__":
    hospital = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Search Patient by ID")
        print("4. Delete Patient by ID")
        print("5. Update Patient by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            contact_number = input("Enter Contact Number: ")
            hospital.add_patient(patient_id, name, age, gender, contact_number)
            print("Patient added successfully.")

        elif choice == '2':
            hospital.display_patients()

        elif choice == '3':
            patient_id = input("Enter ID to search: ")
            patient = hospital.search_patient(patient_id)
            if patient:
                print("Patient Details:")
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Contact: {patient.contact_number}")
            else:
                print("Patient not found.")

        elif choice == '4':
            patient_id = input("Enter ID to delete: ")
            hospital.delete_patient(patient_id)

        elif choice == '5':
            patient_id = input("Enter ID to update: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            contact_number = input("Enter Contact Number: ")
            hospital.update_patient(patient_id, name, age, gender, contact_number)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
