# from openpyxl import Workbook

# workbook = Workbook()
# sheet = workbook.active

# sheet["A1"] = "hello"
# sheet["B1"] = "world!"

# workbook.save(filename="hello_world.xlsx")

import pandas as pd

data = pd.read_csv(r'hello.xlsx')
df = pd.DataFrame(data, columns= ['First Name',	'Last Name', 'Age', 'Phone Number'])

print(df)
