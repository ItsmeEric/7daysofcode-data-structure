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
    def __init__(self, id, name, health_status):
        self.id = id
        self.name = name
        self.health_status = health_status
        self.next_patient = None

# Defining the Patients list to represent the linked list
class PatientList:
    def __init__(self):
        self.head = None
    

    def find_patient(self, id):
        actual_patient = self.head
        while actual_patient is not None:
            if actual_patient.id == id:
                return actual_patient
            actual_patient = actual_patient.next_patient
        return None

    def add_patient(self, id, name, health_status):
        new_patient = Patient(id, name, health_status)
        if self.head is None:
            # If the list is empty, new_patient is added as the list head
            self.head = new_patient
        else:
            # Check if a patient with the same ID already exists
            if self.find_patient(id):
                print("Patient with the same ID already exists.")
                return
            # Otherwise, he is added to the end of the list
            actual_patient = self.head
            while actual_patient.next_patient is not None:
                actual_patient = actual_patient.next_patient
            actual_patient.next_patient = new_patient
            
    # Remove patient from the list, receives the id to remove as a parameter
    def remove_patient(self, id):
        if self.head is None:
            # If the list is empty, cancel the operation
            return
        elif self.head.id == id:
            # If the patient to remove is the head, move the pointer to the next patient
            self.head = self.head.next_patient
            return
        else:
            # Otherwise, iterate over the list until we find the id we're looking for
            actual_patient = self.head
            while actual_patient.next_patient is not None:
                if actual_patient.next_patient.id == id:
                    # If found, update the previous patient's next_patient pointer
                    actual_patient.next_patient = actual_patient.next_patient.next_patient
                    return
                actual_patient = actual_patient.next_patient
        
    # Method to print all patients in the list
    def list_patients(self):
        if self.head is None:
            print("There is no patients in this list!!")
        else:
            actual_patient = self.head
            while actual_patient is not None:
                print(f"Name: {actual_patient.name}, ID: {actual_patient.id}, Health status: {actual_patient.health_status}")
                actual_patient = actual_patient.next_patient


patients_list = PatientList()

patients_list.add_patient(1, "Giovanna", "Stable")
patients_list.add_patient(2, "Angela", "Intensive care")
patients_list.add_patient(3, "Marietta", "Critical")
patients_list.add_patient(4, "Eric", "Stable")

patients_list.list_patients()

patients_list.remove_patient(1)

patients_list.list_patients()