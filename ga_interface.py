import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton

class Variable_Parameters(BaseWidget):

    def __init__(self):
        super(Variable_Parameters,self).__init__('Variable Parameters')

        #Definition of the forms fields
        self._No_of_variables = ControlText('No of variables')
        self._Variable1_Min_constraint    = ControlText('Variable1_Min_constraint')
        self._Variable1_Max_constraint   = ControlText('Variable1_Max_constraint')
        self._Variable2_Min_constraint     = ControlText('Variable2_Min_constraint')
        self._Variable2_Max_constraint     = ControlText('Variable2_Max_constraint')
        self._Variable3_Min_constraint     = ControlText('Variable3_Min_constraint')
        self._Variable3_Max_constraint     = ControlText('Variable3_Max_constraint')

        self._enter_equation = ControlText('the equation should be in terms of x1, x2, x3')

#Execute the application
if __name__ == "__main__":   pyforms.startApp( Variable_Parameters )
