import pandas as pd
box = {'Box': ['Box1', 'Box1','Box1','Box2','Box2','Box2'], 
         'Dimension': ['Length','Width','Height','Length','Width','Height'],
         'Value': [6,4,2,5,3,4]}
boxes = pd.DataFrame(box, columns = ['Box', 'Dimension', 'Value'])
tidyboxes = boxes.pivot_table(index = 'Box', columns = 'Dimension', values = 'Value')
tidyboxes['Volume'] =tidyboxes.Length*tidyboxes.Width*tidyboxes.Height
