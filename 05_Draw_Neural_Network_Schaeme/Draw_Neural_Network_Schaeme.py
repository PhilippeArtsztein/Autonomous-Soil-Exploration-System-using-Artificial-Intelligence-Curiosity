import matplotlib.pyplot as plt
from math import cos, sin, atan

class Neuron():
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def Draw(self, NeuronRadius, NeuronColor):
        Circle= plt.Circle((self.x, self.y), radius=NeuronRadius, fill=False, 
                           linewidth=0.6, color=NeuronColor)
        plt.gca().add_patch(Circle)
        return(self.x)


class Layer():
    def __init__(self, Network, NumberOfNeuronsInThisLayer, WidestLayer, Appearance, HDBL=6, VDBL=2):
        self.HorizontalDistanceBetweenLayers= HDBL    # 6
        self.VerticalDistanceBetweenNeurons = VDBL    # 2
        self.NeuronRadius                   = 0.3
        self.WidestLayer                    = WidestLayer
        self.PreviousLayer                  = self.Get_Previous_Layer(Network)
        self.x                              = self.Calculate_Layer_X_Position()
        self.Neurons                        = self.Intialise_Neurons(NumberOfNeuronsInThisLayer)
        self.Appearance            = Appearance

    def Intialise_Neurons(self, NumberOfNeuronsInThisLayer):
        Neurons= []
        yy= self.Calculate_Bottom_Margin_So_Layer_Is_Centered(NumberOfNeuronsInThisLayer)
        for iteration in range(NumberOfNeuronsInThisLayer):
            NewNeuron= Neuron(self.x, yy)
            Neurons.append(NewNeuron)
            yy+= self.VerticalDistanceBetweenNeurons
        return(Neurons)

    def Calculate_Bottom_Margin_So_Layer_Is_Centered(self, NumberOfNeuronsInThisLayer):
        return(self.VerticalDistanceBetweenNeurons* 
               (self.WidestLayer-NumberOfNeuronsInThisLayer)/2)

    def Calculate_Layer_X_Position(self):
        if(self.PreviousLayer):
            return(self.PreviousLayer.x+self.HorizontalDistanceBetweenLayers)
        else:
            return(0)

    def Get_Previous_Layer(self, Network):
        if(len(Network.Layers)>0):
            return(Network.Layers[-1])
        else:
            return(None)

    def Line_Between_Two_Neurons(self, Neuron1, Neuron2):
        Angle       = atan((Neuron2.y-Neuron1.y)/float(Neuron2.x-Neuron1.x))
        x_adjustment= self.NeuronRadius*cos(Angle)
        y_adjustment= self.NeuronRadius*sin(Angle)
        Line        = plt.Line2D((Neuron1.x-x_adjustment, Neuron2.x+x_adjustment),
                                 (Neuron1.y-y_adjustment, Neuron2.y+y_adjustment),
                                 linewidth=0.4, color=self.Appearance["NetColor"])
        plt.gca().add_line(Line)

    def Draw(self, ActivationFunction, layerType=0):
        for neuron in self.Neurons:
            neuron.Draw(self.NeuronRadius, self.Appearance["NeuronsColor"])
            if self.PreviousLayer:
                for previous_layer_neuron in self.PreviousLayer.Neurons:
                    self.Line_Between_Two_Neurons(neuron, previous_layer_neuron)

        x_text = self.WidestLayer*self.VerticalDistanceBetweenNeurons
        if(layerType==0):
            plt.text(self.x, 
                     self.Neurons[0].y-self.VerticalDistanceBetweenNeurons/2, 
                     'Input Layer',
                     horizontalalignment='center',
                     verticalalignment  ='top',
                     rotation           ='vertical',
                     fontsize           = 8,
                     color              = self.Appearance["LeyersNameColor"])
            plt.text(self.x+self.HorizontalDistanceBetweenLayers/2, -self.VerticalDistanceBetweenNeurons/4,
                     'Activation\nFunction\n'+ActivationFunction,
                     horizontalalignment='center',
                     verticalalignment  ='top',
                     rotation           ='horizontal',
                     fontsize           = 10)
        elif(layerType==-1):
            plt.text(self.x, 
                     self.Neurons[0].y-self.VerticalDistanceBetweenNeurons/2, 
                     'Output Layer', 
                     horizontalalignment='center',
                     verticalalignment  ='top', 
                     rotation           ='vertical', 
                     fontsize           = 8,
                     color              = self.Appearance["LeyersNameColor"])
        else:
            plt.text(self.x, 
                     self.Neurons[0].y-self.VerticalDistanceBetweenNeurons/2, 
                     'Hidden Layer '+str(layerType), 
                     horizontalalignment='center',
                     verticalalignment  ='top', 
                     rotation           ='vertical', 
                     fontsize           = 8,
                     color              = self.Appearance["LeyersNameColor"])
            plt.text(self.x+self.HorizontalDistanceBetweenLayers/2, -self.VerticalDistanceBetweenNeurons/4,
                     'Activation\nFunction\n'+ActivationFunction,
                     horizontalalignment='center',
                     verticalalignment  ='top',
                     rotation           ='horizontal',
                     fontsize           = 10)
            

class NeuralNetworkBuilder():
    def __init__(self, WidestLayer, ActivationFunctionList, HDBL, Appearance):
        self.WidestLayer           = WidestLayer
        self.ActivationFunctionList= ActivationFunctionList
        self.HDBL                  = HDBL
        self.Layers                = []
        self.Layertype             = 0
        self.Appearance            = Appearance

    def Add_Layer(self, NumberOfNeuronsInThisLayer ):
        layer= Layer(self, NumberOfNeuronsInThisLayer, self.WidestLayer, self.Appearance, HDBL=self.HDBL)
        self.Layers.append(layer)

    def Draw(self, TheFileName):
        plt.figure()
        for iii in range(len(self.Layers)):
            Layer= self.Layers[iii]
            if(iii== len(self.Layers)-1):
                iii= -1
            Layer.Draw(self.ActivationFunctionList[iii], iii)
        plt.axis("scaled")
        plt.axis("off")
        plt.title("Neural Network Schaeme", fontsize=12, 
                  color=self.Appearance["TitleColor"])
        if(TheFileName):
            plt.savefig(TheFileName)
        plt.show()
        
class NeuralNetworkDisplay():
    def __init__(self, LeyersList, ActivationFunctionList):
        self.LeyersList            = LeyersList
        self.WidestLayer           = max(LeyersList)
        self.ActivationFunctionList= ActivationFunctionList
        self.HDBL                  = (self.WidestLayer*4)/len(LeyersList)
        self.Appearance            = dict(NeuronsColor="darkred", NetColor="tab:blue", 
                                          TitleColor="darkred", LeyersNameColor="black")
        
    def SetAppearance(self, NeuronsColor="darkred", NetColor="tab:blue", 
                         TitleColor="darkred", LeyersNameColor="black"):
        self.Appearance["NeuronsColor"]   = NeuronsColor
        self.Appearance["NetColor"]       = NetColor
        self.Appearance["TitleColor"]     = TitleColor
        self.Appearance["LeyersNameColor"]= LeyersNameColor

    def Draw( self, TheFileName=None):
        Network= NeuralNetworkBuilder(self.WidestLayer, 
                               self.ActivationFunctionList, 
                               self.HDBL, 
                               self.Appearance)
        for lll in self.LeyersList:
            Network.Add_Layer(lll)
        Network.Draw(TheFileName)