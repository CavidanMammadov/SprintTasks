import pandas as pd
#1) 10, 20, 30, 40 elementlərindən ibarət s1 adlı series/vector yaradın

s1 = pd.Series([10, 20, 30, 40])

s1.index = ['w', 'x', 'y', 'z']

#3) Python: {'p': 5, 'q': 10, 'r': 15} dictionary-dən s2 adlı Series yaradın
   # R: list(p = 5, q = 10, r = 15) listindən v2 adlı named vektor yaradın


s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})
print(s2['q'])
print(s1[s1 > 25])
print(s1[s1 > 20] / 10)



df1 = pd.DataFrame([(1, 2), (3, 4)])
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df2[df2['A'] > 1])


