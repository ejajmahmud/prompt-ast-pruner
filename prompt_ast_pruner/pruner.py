"""Python code AST minifier and comment stripper."""
import ast

class DocstringRemover(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body.pop(0)
        return node

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body.pop(0)
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body.pop(0)
        return node

def prune_python_code(code: str) -> str:
    try:
        parsed = ast.parse(code)
        transformer = DocstringRemover()
        modified = transformer.visit(parsed)
        ast.fix_missing_locations(modified)
        return ast.unparse(modified)
    except Exception:
        # Fallback to returning stripped code if not valid Python
        return "\n".join(line for line in code.splitlines() if line.strip() and not line.strip().startswith("#"))
