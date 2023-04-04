def convert_RADEC_degrees(degrees=False,hms=True):
    """convert RA/DEC in either sexagesimal or degrees 

    Author: Houda Haidar
    Date: 4/4/23
    """
    import numpy as np
    import math
    
    if degrees == True:

        # Get user input for RA and DEC in h:mm:ss and d:mm:ss format
        RA = input("Enter RA in h:mm:ss format: ")
        DEC = input("Enter DEC in d:mm:ss format: ")

        # Split the RA and DEC into separate components
        RA_hours, RA_minutes, RA_seconds = map(float, RA.split(':'))
        DEC_degrees, DEC_minutes, DEC_seconds = map(float, DEC.split(':'))

        # Convert the RA from h:mm:ss to decimal degrees
        RA_degrees = (RA_hours * 15) + (RA_minutes * 0.25) + (RA_seconds * 0.00416667)

        # Convert the DEC from d:mm:ss to decimal degrees
        DEC_degrees = DEC_degrees - (DEC_minutes / 60) - (DEC_seconds / 3600)

        print("RA: {:.5f} degrees".format(RA_degrees))
        print("DEC: {:.5f} degrees".format(DEC_degrees))

        # Return the converted RA and DEC values as a tuple
        return RA_degrees, DEC_degrees
    
    elif hms == True:
        print("bug in this code")
        RA_dec = float(input("Enter RA in decimal degrees: "))
        DEC_dec = float(input("Enter DEC in decimal degrees: "))
        
        RA_hours = RA_dec / 15.0
        RA_minutes = (RA_hours - int(RA_hours)) * 60.0
        RA_seconds = (RA_minutes - int(RA_minutes)) * 60.0
        RA = "{:02.0f}:{:02.0f}:{:.2f}".format(int(RA_hours), int(RA_minutes), RA_seconds)

        DEC_hours   = math.floor(abs(DEC_dec))
        DEC_minutes = math.floor((abs(DEC_dec) - DEC_hours) * 60)
        DEC_seconds =  (abs(DEC_dec) - DEC_hours - DEC_minutes/60) * 3600

        DEC = "{:02.0f}:{:02.0f}:{:.2f}".format(DEC_hours, DEC_minutes, DEC_seconds)
        
        print("RA: ", RA)
        print("DEC ", DEC)
        return RA,DEC

        
    else:
        raise ValueError("Sorry! Code can only convert to degrees or to hh:mm:ss")

# Call the function and print the result
RA, DEC = convert_RADEC_degrees()
