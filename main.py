"""
This is a code demonstration of the function point estimation developed by Allan Albrecht
The estimation is based on the team project of the module of Software Engineering Project Management June 2022 (University of Essex Online)
"""

def calculate_function_point():
    #Assumption of the 5 user function categories with average weighing factors
    function_categories = {
    "number_of_user_inputs" : 7*4,
    "number_of_user_outputs" : 5*5,
    "number_of_user_enquiries" : 0*4,
    "number_of_user_files" : 1*10,
    "number_of_external_interfaces" : 0*7
    }

    #Assumption of the 14 complexity factors (ci)
    #Each factor is multiplied by its degree of influence (From 1-5)
    complexity_factors = {
    "data_communications" : 1*3,
    "distributed_data_processing" : 1*3,
    "performance" : 1*3,
    "heavily_used_configuration" : 1*3,
    "transaction_rate" : 1*3,
    "online_data_entry" : 1*3,
    "end_user_efficiency" : 1*3,
    "online_update" : 1*3,
    "complex_processing" : 1*3,
    "reusability" : 1*3,
    "installation_ease" : 1*3,
    "operational_ease" : 1*3,
    "multiple_sites" : 1*3,
    "facilitate_change" : 1*3,
    }

    ufp = 0
    tdi = 0
    for x in function_categories.values():
        ufp += x
    
    print(f'Function Categories have {ufp}')
    
    for x in complexity_factors.values():
        tdi += x
    
    vaf = 0.65 + (0.01 * tdi)
    print(f'Value add factor is {vaf}')

    fp = ufp*vaf
    print(f'Calculated function point is {fp}')

calculate_function_point()