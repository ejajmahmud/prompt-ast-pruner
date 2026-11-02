"""Unit tests for prompt_ast_pruner."""
import unittest
import ast
from prompt_ast_pruner.pruner import prune_python_code

class TestPromptPruner(unittest.TestCase):
    def test_docstring_removal(self):
        source = 'def greet(name: str) -> str:\n    """Docstring to strip."""\n    return f"Hello {name}"\n'
        pruned = prune_python_code(source)
        self.assertNotIn("Docstring to strip", pruned)
        # Verify valid syntax
        self.assertIsNotNone(ast.parse(pruned))

if __name__ == "__main__":
    unittest.main()
