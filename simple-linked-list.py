'''
Implement a patient management system in a hospital using simply linked list

    # Patient details
        a. Name
        b. Identification number
        c. Health status/condition [stable, in intensive care, in critical condition, and many more]

    # The system must accept to add new patients
    # Remove existing patients
    # List all patients in order of arrival
        
    # Create a class named Patient(representing one node)
    # Create a class name PatientList(representing the list)

    # Node structure
        a. Must keep patient information
        b. Have a pointer to the next patient node in the list

    # Patient list structure
        a. Write functions to add and remove patient
        b. These functions must create or remove one node from the linked list e adjust the pointers
    
    # Write a function to list all the patients
        a. It must iterate over the linked list
        b. Display each patient information
    
    # Think of special cases
        a. Adding or removing the first node in the list
        b. Try to remove a patient that does not exist in the list
    
    ### Test the code ###

    # EXTRA
        a. Try using only the "head" property without the "tail" property 
'''

# Defining the Patient class to represent the list node
class Patient:
    def __init__(self, patient_id, name, health_status):
        self.id = patient_id
        self.name = name
        self.health_status = health_status
        self.next_patient = None

# Defining the Patients list to represent the linked list
class PatientList:
    def __init__(self):
        self.head = None
    

    def add_patient(self, patient_id, name, health_status):
        new_patient = Patient(patient_id, name, health_status)

        if self.head is None:
            # If the list is empty, new_patient is added as the list head
            self.head = new_patient
        else:
            # Otherwise, he is added to the end of the list
            current_patient = self.head
            while current_patient.next_patient is not None:
                if current_patient.id == patient_id:
                    raise ValueError("Patient with the same ID already exists.")
                current_patient = current_patient.next_patient
            if current_patient.id == patient_id:
                raise ValueError("Patient with the same ID already exists.")
            current_patient.next_patient = new_patient
            
    # Remove patient from the list, receives the id to remove as a parameter
    def remove_patient(self, patient_id):
        if self.head is None:
            # If the list is empty, cancel the operation
            print("There are no patients in this list")
            return
        
        elif self.head.id == patient_id:
            # If the patient to remove is the head, move the pointer to the next patient
            self.head = self.head.next_patient
            return
        else:
            # Otherwise, iterate over the list until we find the id we're looking for
            current_patient = self.head
            while current_patient.next_patient is not None:
                if current_patient.next_patient.id == patient_id:
                    # If found, update the previous patient's next_patient pointer
                    removed_patient = current_patient.next_patient
                    current_patient.next_patient = removed_patient.next_patient
                    removed_patient.next_patient = None # Detach the removed patient
                    return
                current_patient = current_patient.next_patient
            # Patient with the given ID was not found in the list
            print("Patient not found")

    # Method to print all patients in the list
    def list_patients(self):
        if self.head is None:
            print("There is no patients in this list!!")
        else:
            current_patient = self.head
            while current_patient is not None:
                print(f"Name: {current_patient.name}, ID: {current_patient.id}, Health status: {current_patient.health_status}")
                current_patient = current_patient.next_patient

patients_list = PatientList()

patients_list.add_patient(1, "Giovanna", "Stable")
patients_list.add_patient(2, "Angela", "Intensive care")
patients_list.add_patient(3, "Marietta", "Critical")
patients_list.add_patient(4, "Eric", "Stable")

patients_list.list_patients()

patients_list.remove_patient(1)

patients_list.list_patients()