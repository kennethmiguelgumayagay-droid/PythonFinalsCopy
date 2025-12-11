# parser.py
import re
import math
from operations import add, subtract, multiply, divide, power, modulus, sqrt, absolute, sin, cos, tan
from constants import CONSTANTS

FUNCTIONS = {
    "sqrt": sqrt,
    "abs": absolute,
    "sin": sin,
    "cos": cos,
    "tan": tan,
}

BINARY_OPERATORS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulus,
}

def evaluate_expression(expr: str) -> float:
    """Safely evaluate a mathematical expression."""
    # Replace constants
    for k, v in CONSTANTS.items():
        expr = expr.replace(k, str(v))

    try:
        # Python-safe parsing using ast
        import ast
        tree = ast.parse(expr, mode='eval')
        return _eval_ast(tree.body)
    except Exception:
        raise ValueError("Invalid expression format.")

def _eval_ast(node):
    import ast

    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)

        op_type = type(node.op)

        op_map = {
            ast.Add: BINARY_OPERATORS["+"],
            ast.Sub: BINARY_OPERATORS["-"],
            ast.Mult: BINARY_OPERATORS["*"],
            ast.Div: BINARY_OPERATORS["/"],
            ast.Pow: BINARY_OPERATORS["^"],
            ast.Mod: BINARY_OPERATORS["%"],
        }

        if op_type not in op_map:
            raise ValueError("Unsupported operator.")
        return op_map[op_type](left, right)

    elif isinstance(node, ast.Num):
        return node.n

    elif isinstance(node, ast.UnaryOp):
        operand = _eval_ast(node.operand)
        if isinstance(node.op, ast.UAdd):
            return operand
        elif isinstance(node.op, ast.USub):
            return -operand

    elif isinstance(node, ast.Call):
        func_name = node.func.id
        if func_name not in FUNCTIONS:
            raise ValueError(f"Unknown function '{func_name}'.")
        args = [_eval_ast(arg) for arg in node.args]
        return FUNCTIONS[func_name](*args)

    else:
        raise ValueError("Invalid or unsupported expression.")
