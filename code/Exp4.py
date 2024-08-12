print("Gautam Kumar")
print("21BCS5998")
def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    x_k_minus_1 = x0
    x_k = x1

    for k in range(max_iter):
        f_k_minus_1 = func(x_k_minus_1)
        f_k = func(x_k)

        if f_k == f_k_minus_1:
            raise ValueError("Division by zero in Secant method.")

        x_k_plus_1 = x_k - f_k * (x_k - x_k_minus_1) / (f_k - f_k_minus_1)

        if abs(x_k_plus_1 - x_k) < tol:
            return x_k_plus_1, k + 1  # Return the root and the number of iterations

        x_k_minus_1 = x_k
        x_k = x_k_plus_1

    raise ValueError("Secant method did not converge within the maximum number of iterations.")

# Example usage:
if __name__ == "__main__":
    # Define the function for finding the square root of a number
    def target_function(x):
        return x**3 - x*2 - 4

    # Initial guesses
    x0 = 1.0
    x1 = 3.0

    # Call the Secant method function
    root, iterations = secant_method(target_function, x0, x1)

    print(f"Root found: {root}")
    print(f"Iterations: {iterations}")
