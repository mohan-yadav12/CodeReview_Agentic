import ast

def parse_file(path):
    with open(
        path,
        encoding="utf8"
    ) as f:
        src = f.read()
    tree = ast.parse(
        src
    )
    out = []
    for node in ast.walk(
        tree
    ):
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.ClassDef
            )
        ):
            code = (
                ast.get_source_segment(
                    src,
                    node
                )
            )
            out.append({
                "name":
                node.name,

                "type":
                node.__class__.__name__,

                "code":
                code
            })
    return out