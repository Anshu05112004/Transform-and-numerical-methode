def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    
    
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("The function has the same sign at both endpoints.")
    
    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise RuntimeError("The regula falsi method failed to converge.")


