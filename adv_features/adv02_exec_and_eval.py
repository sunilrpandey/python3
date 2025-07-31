def demo_exec_and_eval():
    print("Demo: exec() and eval() in Python")

    # Use a local dictionary for exec/eval context
    local_ctx = {}

    # Easy exec: execute a simple statement
    code1 = "x = 5"
    exec(code1, {}, local_ctx)
    print("After exec('x = 5'), x =", local_ctx['x'])

    # Easy eval: evaluate a simple expression
    expr1 = "x + 10"
    result1 = eval(expr1, {}, local_ctx)
    print(f"eval('x + 10') = {result1}")

    # Medium exec: execute multiple lines
    code2 = """
y = 2
z = x * y
"""
    exec(code2, {}, local_ctx)
    print("After exec(multi-line), z =", local_ctx['z'])

    # Medium eval: evaluate a function call
    def square(n):
        return n * n
    local_ctx['square'] = square
    result2 = eval("square(7)", {}, local_ctx)
    print("eval('square(7)') =", result2)

    # Tricky exec: define a function dynamically
    code3 = """
def dynamic_add(a, b):
    return a + b
"""
    exec(code3, {}, local_ctx)
    print("dynamic_add(3, 4) =", local_ctx['dynamic_add'](3, 4))

    # Tricky eval: use globals and locals
    local_vars = {'a': 10, 'b': 20}
    result3 = eval("a * b", {}, local_vars)
    print("eval('a * b', {}, local_vars) =", result3)

if __name__ == "__main__":
    demo_exec_and_eval()