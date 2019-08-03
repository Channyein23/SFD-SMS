import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import handler

class FIS(handler.AbstractHandler):
    def __init__(self, ctrl, ante, cons):
        self.ctrl = ctrl
        self.ante = ante
        self.cons = cons
        self.simulation = control.ControlSystemSimulation(self.ctrl)
        
    def compute(self, temp, humid):
        self.simulation.reset()
        # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
        # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
        self.simulation.input['temperature'] = temp
        self.simulation.input['humidity'] = humid
        # Crunch the numbers
        self.simulation.compute()
        return self.simulation.output['result']
    
    def handle(self, request):
        if self.check(request):
            request['threat'] = self.compute(request['temp'], request['humid'])
        print('Fuzzy :', request)
        super().handle(request)
    
    def check(self, request):
        return 'threat' not in request
    
    @classmethod
    def instance(cls):
        temperature = control.Antecedent(np.arange(20, 101, 1), 'temperature')
        humidity = control.Antecedent(np.arange(0, 101, 1), 'humidity')
        result = control.Consequent(np.arange(0, 101, 1), 'result', defuzzify_method='centroid')
        
        temperature['normal'] = fuzz.trapmf(temperature.universe, [20, 20, 30, 40])
        temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 50])
        temperature['veryhot'] = fuzz.trapmf(temperature.universe, [40, 50, 100, 100])
        humidity['dry'] = fuzz.trapmf(humidity.universe, [0, 0, 20, 40])
        humidity['medium'] = fuzz.trimf(humidity.universe, [20, 40, 60])
        humidity['wet'] = fuzz.trapmf(humidity.universe, [40, 60, 100, 100])
        result['low'] = fuzz.trapmf(result.universe, [0, 0, 20, 40])
        result['medium'] = fuzz.trimf(result.universe, [20, 40, 60])
        result['high'] = fuzz.trapmf(result.universe, [40, 60, 100, 100])
        
        rule1 = control.Rule(temperature['normal'] & humidity['wet'], result['low'])
        rule2 = control.Rule(temperature['veryhot'], result['high'])
        rule3 = control.Rule(temperature['hot'] & humidity['medium'], result['medium'])
        rule4 = control.Rule(temperature['normal'] & humidity['dry'], result['medium'])
        resulting_ctrl = control.ControlSystem([rule1, rule2, rule3, rule4])
        
        return cls(resulting_ctrl, [temperature, humidity], result)