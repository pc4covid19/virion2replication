 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Virus Replication---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.virion_uncoating_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name3 = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.uncoated_to_RNA_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name4 = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.protein_synthesis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.virion_assembly_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Virus Adsorption and Export---', disabled=True, layout=divider_button_layout)

        param_name6 = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.virion_export_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Visualization Options---', disabled=True, layout=divider_button_layout)

        param_name7 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.color_variable = Text(
          value='assembled virion',
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='rate at which an internalized virion is uncoated' , tooltip='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='rate at which uncoated virion makes its mRNA available' , tooltip='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='rate at mRNA creates complete set of proteins' , tooltip='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='rate at which viral proteins are assembled into complete virion' , tooltip='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='rate at which a virion is exported from a live cell' , tooltip='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button18 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.virion_uncoating_rate, units_button3, desc_button2] 
        row3 = [param_name3, self.uncoated_to_RNA_rate, units_button4, desc_button3] 
        row4 = [param_name4, self.protein_synthesis_rate, units_button5, desc_button4] 
        row5 = [param_name5, self.virion_assembly_rate, units_button6, desc_button5] 
        row6 = [param_name6, self.virion_export_rate, units_button8, desc_button6] 
        row18 = [param_name7, self.color_variable, units_button10, desc_button18] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          box4,
          box5,
          div_row2,
          box6,
          div_row3,
          box18,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.virion_uncoating_rate.value = float(uep.find('.//virion_uncoating_rate').text)
        self.uncoated_to_RNA_rate.value = float(uep.find('.//uncoated_to_RNA_rate').text)
        self.protein_synthesis_rate.value = float(uep.find('.//protein_synthesis_rate').text)
        self.virion_assembly_rate.value = float(uep.find('.//virion_assembly_rate').text)
        self.virion_export_rate.value = float(uep.find('.//virion_export_rate').text)
        self.color_variable.value = (uep.find('.//color_variable').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//virion_uncoating_rate').text = str(self.virion_uncoating_rate.value)
        uep.find('.//uncoated_to_RNA_rate').text = str(self.uncoated_to_RNA_rate.value)
        uep.find('.//protein_synthesis_rate').text = str(self.protein_synthesis_rate.value)
        uep.find('.//virion_assembly_rate').text = str(self.virion_assembly_rate.value)
        uep.find('.//virion_export_rate').text = str(self.virion_export_rate.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
