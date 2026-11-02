"""Command line interface for prompt-ast-pruner."""
import sys
from .pruner import prune_python_code

def main():
    sample = 'def add(a: int, b: int) -> int:\n    """Add two numbers."""\n    return a + b\n'
    pruned = prune_python_code(sample)
    print("Pruned Python code:\n", pruned)

if __name__ == "__main__":
    main()
