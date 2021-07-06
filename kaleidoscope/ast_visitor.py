from kaleidoscope.ast import ASTNode


class ASTVisitor:
    """
    A node visitor base class that walks the abstract syntax tree and calls a
    visitor function for every node found.  This function may return a value
    which is forwarded by the `visit` method.

    Modified from the implementation in ast.py in the Python standard library
    """

    def visit(self, node: ASTNode):
        """Visit a node."""
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: ASTNode):
        """Called if no explicit visitor function exists for a node."""
        for _, value in node.__dict__.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ASTNode):
                        self.visit(item)
            elif isinstance(value, ASTNode):
                self.visit(value)
