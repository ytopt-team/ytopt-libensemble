import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

dataframe = pandas.read_csv("results.csv")
array = dataframe.values
x = array[:,5]

print("Performance (accuracy) summary based on", len(array), "evaluations:")
print("Min: ", -1 * x.max())
print("Max: ", -1 * x.min())
print("Mean: ", -1 * x.mean())
print("The best configurations (for the smallest -accuracy) of P0 P1 P2 P3 P4 is:\n")
print("P0  P1  P2 P3 P4  -accuracy	     elapsed time\n")
mn = x.min()
for i in range(len(array)): 
   if x[i] == mn:
    print (*array[i,:])