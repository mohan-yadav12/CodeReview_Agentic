import ast


def parse_file(filepath):

    with open(
        filepath,
        encoding="utf8"
    ) as f:

        source = f.read()

    tree = ast.parse(source)

    data = {

        "file": filepath,

        "functions": [],

        "classes": [],

        "imports": []
    }

    for node in ast.walk(tree):

        if isinstance(
            node,
            ast.FunctionDef
        ):

            data[
                "functions"
            ].append(
                node.name
            )

        elif isinstance(
            node,
            ast.ClassDef
        ):

            data[
                "classes"
            ].append(
                node.name
            )

        elif isinstance(
            node,
            ast.Import
        ):

            for i in node.names:

                data[
                    "imports"
                ].append(
                    i.name
                )

    return data