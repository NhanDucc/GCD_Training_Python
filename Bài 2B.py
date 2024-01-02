import math

x = float(input('Nhập giá trị của x: '))
formula_str = 'sin^2x + cos^2x'
clear_formula = formula_str.replace('sin^2x', 'math.sin(x)**2').replace('cos^2x', 'math.cos(x)**2')
formula = math.ceil(eval(clear_formula))

print(f'sin^2x + cos^2x = {formula}')