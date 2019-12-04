import pandas as pd

a = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80,95,79]}
b = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85,81,83]}
c = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90,79,93]}
d = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93,89,88]}

Math = pd.DataFrame(a, columns = ['Student', 'Math'])
Elecs = pd.DataFrame(b, columns = ['Student','Electronics'])
Geas = pd.DataFrame(c, columns = ['Student','GEAS'])
Esat = pd.DataFrame(d, columns = ['Student','ESAT'])

bearmerge=pd.merge(pd.merge(Math,Elecs, on = 'Student'),pd.merge(Geas, Esat, on = 'Student') , on = 'Student')
bearlong=pd.melt(bearmerge, id_vars = ['Student'], var_name = 'Subject', value_name = 'Grades')