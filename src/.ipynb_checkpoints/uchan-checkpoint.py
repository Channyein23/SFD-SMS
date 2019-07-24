import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
temperature = ctrl.Antecedent(np.arange(20, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
result = ctrl.Consequent(np.arange(0, 101, 1), 'result', defuzzify_method='centroid')
temperature['normal'] = fuzz.trapmf(temperature.universe, [20, 20, 30, 40])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 50])
temperature['veryhot'] = fuzz.trapmf(temperature.universe, [40, 50, 100, 100])
humidity['dry'] = fuzz.trapmf(humidity.universe, [0, 0, 20, 40])
humidity['medium'] = fuzz.trimf(humidity.universe, [20, 40, 60])
humidity['wet'] = fuzz.trapmf(humidity.universe, [40, 60, 100, 100])
result['low'] = fuzz.trapmf(result.universe, [0, 0, 20, 40])
result['medium'] = fuzz.trimf(result.universe, [20, 40, 60])
result['high'] = fuzz.trapmf(result.universe, [40, 60, 100, 100])
temperature.view()
humidity.view()
result.view()
rule1 = ctrl.Rule(temperature['normal'] & humidity['wet'], result['low'])
rule2 = ctrl.Rule(temperature['veryhot'], result['high'])
rule3 = ctrl.Rule(temperature['hot'] & humidity['medium'], result['medium'])
rule4 = ctrl.Rule(temperature['normal'] & humidity['dry'], result['medium'])
rule1.view()
resulting_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
resulting = ctrl.ControlSystemSimulation(resulting_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
resulting.input['temperature'] = 44
resulting.input['humidity'] = 43
# Crunch the numbers
resulting.compute()
print(resulting.output['result'])
result.view(sim=resulting)