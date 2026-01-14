import numpy as np

def calcualte(l):
    a=np.array(l)
    if len(a)!=9:
        raise ValueError("List must contain nine numbers.")
    a=a.reshape(3,3)
    return {
        'mean': [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a)],
        'variance': [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a)],
        'standard deviation': [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a)],
        'max': [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a)],
        'min': [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a)],
        'sum': [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a)]
    }

a=input("Enter nine numbers separated by spaces: ")
l=[int(i) for i in a.split()]
result=calcualte(l)
print(result)