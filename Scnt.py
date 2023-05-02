def scnt_mthd(f, x0, x1, tol=1e-6, max_iter=100):
   
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if (fx1 - fx0)!=0:
         x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
         if abs(x_next - x1) < tol:
            return x_next
         x0 = x1
         x1 = x_next
        else:
            return x1
    
    raise RuntimeError("The secant method failed to converge.")



