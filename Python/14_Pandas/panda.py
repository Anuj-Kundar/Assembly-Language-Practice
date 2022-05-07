import pandas as pd

import pandas as pd
personset={
    'Name':['ajay','manoj','vijay','sanjay'],
    'age':[20,27,32,22]
}
p=pd.DataFrame(personset,index=['n1','n2','n3','n4'])
print(p)



import pandas as pd
a=['rose','lily','tulips']
x=pd.Series(a)
print(x)


import pandas as pd
a=['rose','lily','tulips']
x=pd.Series(a,index=['flower1','flower2','flower3'])
print(x)
print(a[0])

# Creating pandas from directory
import pandas as pd
flowerset={'flower1':'rose','flower1':'lily','flower1':'tulips'}
x=pd.Series(flowerset)
print(x)


import pandas as pd
flowerset={'flower1':'rose','flower1':'lily','flower1':'tulips'}
x=pd.Series(flowerset,index=['flower1','flower2'])
print(x)


import pandas as pd
df=pd.read_csv('data.csv')
df=pd.read_csv("iris_csv.csv")
print(df.info())


import pandas as pd
df=pd.read_json('iris_json.json')
print(df)

import pandas as pd
df=pd.read_csv('IRIS.csv')
print(df.tail())

df.info()

df.describe()

df.sample(20)

df.columns()

df.shape()

print(df[40:51])