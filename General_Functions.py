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
##################################################################################

def ThePrint_1Header(TheFirstHeader):
    print( CCS, TheFirstHeader, CUE)
def ThePrint_1Header_Underline(TheFirstHeader):
    print( CCS, CUB, TheFirstHeader, CUE)

def ThePrint_1Header_1Variable_Underline(TheFirstHeader, TheFirstVariable):
    print( CCS, CUB, TheFirstHeader, CUE, TheFirstVariable)

def ThePrint_1Header_1Variable(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable)
def ThePrint_2Header_2Variable(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable)
def ThePrint_3Header_3Variable(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, TheThirdHeader, CCE, TheThirdVariable)

def ThePrint_1Header_1Variable_Point1(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable))
def ThePrint_2Header_2Variable_Point1(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.1f}".format(TheSecondVariable))
def ThePrint_3Header_3Variable_Point1(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable):
    print( CCS, TheFirstHeader, CCE, "{:8.1f}".format(TheFirstVariable), CCW, TheSecondHeader, 
           CCE, "{:8.1f}".format(TheSecondVariable), CCW, TheThirdHeader, CCE, "{:8.1f}".format(TheThirdVariable))

def ThePrint_1Header_1Variable_Exponent2(TheFirstHeader, TheFirstVariable):
    print( CCS, TheFirstHeader, CCE, "{:.2e}".format(TheFirstVariable))
    
def ThePrint_1Header_1Variable_EndHeader(TheFirstHeader, TheFirstVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, EndHeader, CCE)
def ThePrint_2Header_2Variable_EndHeader(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, EndHeader, CCE)
def ThePrint_3Header_3Variable_EndHeader(TheFirstHeader, TheFirstVariable, TheSecondHeader, TheSecondVariable, TheThirdHeader, TheThirdVariable, EndHeader):
    print( CCS, TheFirstHeader, CCE, TheFirstVariable, CCW, TheSecondHeader, CCE, TheSecondVariable, CCW, TheThirdHeader, CCE, TheThirdVariable, CCW, EndHeader, CCE)
