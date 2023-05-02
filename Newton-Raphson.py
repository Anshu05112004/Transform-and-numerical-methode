def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
   
    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1
    raise Exception("Maximum number of iterations reached")







def f(x):
    return x**3-5*x+1

def df(x):
    return 3*x**2-5



print("The root is:", newton_raphson(f, df, 1))
