##################################################################################
# Nothing to see here, only the printing stuff.
# (C) Color Code setting, 
# (CS) to start, (CE) to end, (CW) start without triangle
# (CR) red color, (CL) line draw, 
# More information : https://en.wikipedia.org/wiki/ANSI_escape_code
CCS= '\x1b[35m'+u'\u1405' # Ascii ESC Magenta color + Unicode triangle symbol 
CCW= '\x1b[35m'           # Ascii ESC Magenta color
CCR= '\x1b[31m'+u'\u1405' # Ascii ESC Red color + Unicode triangle symbol
CCE= '\x1b[0m'            # Ascii reset all attributes
CCL= u'\u2550'*100        # Ascii continius 10- char horizontal line
CUB= '\033[4m'            # Ascii underline
CUE= '\033[0m'            # Ascii reset underline
# For the Braille community
CCB= u'\u2803'+u'\u280a'+u'\u281b'+' '+u'\u2819'+u'\u2801'+u'\u281e'+u'\u2801'
#
# H for Header, U for Underline, V for Variable, 
# P for Point, E for Exponent, EH for EndHeader
##################################################################################
def var():
    print( CCS, 'General Functions Version =', CCE, 3.0)

def Print_1H(TheFirstHeader):
    print( CCS, TheFirstHeader, CUE)
def Print_1H_U(TheFirstHeader):
    print( CCS, CUB, TheFirstHeader, CUE)

def Print_1H_1V_U(TheFirstHeader, TheFirstVariable):
    print( CCS, CUB, TheFirstHeader, CUE, TheFirstVariable)

def Print_1H_1V(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable)
def Print_2H_2V(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable)
def Print_3H_3V(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, TheThirdHeader, CCE, TheThirdVariable)

def Print_1H_1V_1P(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable))
def Print_2H_2V_1P(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.1f}".format(TheSecondVariable))
def Print_3H_3V_1P(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.1f}".format(TheSecondVariable), CCW, TheThirdHeader, CCE, "{:8.1f}".format(TheThirdVariable))
def Print_3H_3V_2P(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.2f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.2f}".format(TheSecondVariable), CCW, TheThirdHeader, CCE, "{:8.2f}".format(TheThirdVariable))
def Print_3H_3V_3P(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.3f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.3f}".format(TheSecondVariable), CCW, TheThirdHeader, CCE, "{:8.3f}".format(TheThirdVariable))

def Print_4H_1V_0P_3V_3P(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable, TheFourthHeader, TheFourthVariable):
    print( CCS, TheFirstHeader, CCE, "{:4.0f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.3f}".format(TheSecondVariable), CCW, TheThirdHeader, CCE, "{:8.3f}".format(TheThirdVariable),
           CCW, TheFourthHeader, CCE, "{:8.3f}".format(TheFourthVariable))

def Print_1H_1V_2E(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, "{:.2e}".format(TheFirstVariable))
    
def Print_1H_1V_EH(TheFirstHeader, TheFirstVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, EndHeader, CCE)
def Print_2H_2V_EH(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, EndHeader, CCE)
def Print_3H_3V_EH(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, TheThirdHeader, CCE, TheThirdVariable, CCW, EndHeader, CCE)
