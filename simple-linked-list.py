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
# class Patient:
#     def __init__(self, id, name, health_status):
#         self.id = id
#         self.name = name
#         self.health_status = health_status
#         self.next_patient = None
