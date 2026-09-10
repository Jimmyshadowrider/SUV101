import math


def formula_1(vals, target):
    """v = u + a·t"""
    if target == 'v': return vals['u'] + vals['a'] * vals['t']
    if target == 'u': return vals['v'] - vals['a'] * vals['t']
    if target == 'a':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return (vals['v'] - vals['u']) / vals['t']
    if target == 't':
        if vals['a'] == 0: raise ValueError("a cannot be zero")
        return (vals['v'] - vals['u']) / vals['a']


def formula_2(vals, target):
    """s = ((u + v) / 2) · t"""
    if target == 's': return (vals['u'] + vals['v']) / 2 * vals['t']
    if target == 'u':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return (2 * vals['s'] / vals['t']) - vals['v']
    if target == 'v':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return (2 * vals['s'] / vals['t']) - vals['u']
    if target == 't':
        if (vals['u'] + vals['v']) == 0: raise ValueError("u + v cannot be zero")
        return 2 * vals['s'] / (vals['u'] + vals['v'])


def formula_3(vals, target):
    """s = u·t + ½·a·t²"""
    if target == 's': return vals['u'] * vals['t'] + 0.5 * vals['a'] * vals['t'] ** 2
    if target == 'u':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return (vals['s'] - 0.5 * vals['a'] * vals['t'] ** 2) / vals['t']
    if target == 'a':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return 2 * (vals['s'] - vals['u'] * vals['t']) / vals['t'] ** 2
    if target == 't':
        A, B, C = 0.5 * vals['a'], vals['u'], -vals['s']
        return _quadratic(A, B, C)


def formula_4(vals, target):
    """s = v·t − ½·a·t²"""
    if target == 's': return vals['v'] * vals['t'] - 0.5 * vals['a'] * vals['t'] ** 2
    if target == 'v':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return (vals['s'] + 0.5 * vals['a'] * vals['t'] ** 2) / vals['t']
    if target == 'a':
        if vals['t'] == 0: raise ValueError("t cannot be zero")
        return 2 * (vals['v'] * vals['t'] - vals['s']) / vals['t'] ** 2
    if target == 't':
        # s = v·t − ½·a·t²  →  −½·a·t² + v·t − s = 0
        A, B, C = -0.5 * vals['a'], vals['v'], -vals['s']
        return _quadratic(A, B, C)


def formula_5(vals, target):
    """v² = u² + 2·a·s"""
    if target == 'v': return math.sqrt(vals['u'] ** 2 + 2 * vals['a'] * vals['s'])
    if target == 'u': return math.sqrt(vals['v'] ** 2 - 2 * vals['a'] * vals['s'])
    if target == 'a':
        if vals['s'] == 0: raise ValueError("s cannot be zero")
        return (vals['v'] ** 2 - vals['u'] ** 2) / (2 * vals['s'])
    if target == 's':
        if vals['a'] == 0: raise ValueError("a cannot be zero")
        return (vals['v'] ** 2 - vals['u'] ** 2) / (2 * vals['a'])


def _quadratic(A, B, C):
    """Solve A·x² + B·x + C = 0, return list of real non-negative roots."""
    disc = B * B - 4 * A * C
    if disc < 0:
        return []
    if A == 0:
        return [-C / B] if B != 0 else []
    roots = [(-B + math.sqrt(disc)) / (2 * A),
             (-B - math.sqrt(disc)) / (2 * A)]
    return [r for r in roots if r >= 0]



FORMULAS = {
    '1': ("v = u + a·t",            formula_1, "uvat"),
    '2': ("s = ((u+v)/2)·t",        formula_2, "suvt"),
    '3': ("s = u·t + ½·a·t²",       formula_3, "suat"),
    '4': ("s = v·t − ½·a·t²",       formula_4, "svat"),
    '5': ("v² = u² + 2·a·s",        formula_5, "uvas"),
}

# def main():
#     print("Available formulas:")
#     for key, (desc, _, vars_) in FORMULAS.items():
#         print(f"  {key}) {desc:<22}  (variables: {', '.join(vars_)})")
#     print()

#     choice = input("Choose a formula (1-5): ").strip()
#     if choice not in FORMULAS:
#         print("Invalid choice.")
#         return

#     desc, func, variables = FORMULAS[choice]
#     print(f"\nUsing: {desc}")
#     print(f"Variables involved: {', '.join(variables)}\n")

#     target = input(f"Which variable to find? ({'/'.join(variables)}): ").strip().lower()
#     if target not in variables:
#         print("Invalid target.")
#         return

#     vals = {}
#     for name in variables:
#         if name == target:
#             continue
#         try:
#             vals[name] = float(input(f"Enter value of {name}: "))
#         except ValueError:
#             print(f"Invalid number for {name}.")
#             return

#     # Compute
#     try:
#         result = func(vals, target)
#     except ValueError as e:
#         print(f"Error: {e}")
#         return

#     if isinstance(result, list):
#         if not result:
#             print("No real non-negative solution.")
#         else:
#             for r in result:
#                 print(f"{target} = {r}")
#     else:
#         print(f"{target} = {result}")


# if __name__ == "__main__":
#     main()