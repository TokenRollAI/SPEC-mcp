# -*-coding:utf-8 -*-
from pathlib import Path
from typing import Annotated

from fastmcp import FastMCP
from pydantic import Field

from prompts import *

mcp = FastMCP("spec-mcp")


@mcp.tool
def generate_spec(
    root_path: Annotated[str, Field(
        description="Full path of the project root directory, e.g. /Users/username/project_name (in windows, it should be "
                    "D:/username/project_name)")],
):
    # create specdir : root/spec, use pathlib to create
    # create specdir/requirements.md
    # create specdir/design.md
    # create specdir/attention.md
    # create specdir/todos.md

    specdir = Path(root_path) / "spec"
    specdir.mkdir(parents=True, exist_ok=True)
    requirements = specdir / "requirements.md"
    design = specdir / "design.md"
    attention = specdir / "attention.md"
    todos = specdir / "todos.md"

    requirements.write_text(GEN_REQUIREMENTS, encoding="utf-8")
    design.write_text(GEN_DESIGN, encoding="utf-8")
    attention.write_text(GEN_MISTAKES, encoding="utf-8")
    todos.write_text(GEN_TODOS, encoding="utf-8")

    return (f"if user want to generate spec, Make sure user had said what user want, if not ask user to say what user want. Spec files have been "
            f"generated on {specdir}, now read all files under {specdir} and follow the instructions in theses md. The squence is requirements -> "
            f"design -> attention -> todos.")


@mcp.tool
def get_spec():
    pass


@mcp.prompt
def update_tasks():
    pass


if __name__ == "__main__":
    if __name__ == "__main__":
        mcp.run(
            transport="sse",
            host="127.0.0.1",
            port=4200,
            log_level="debug",
            path="/spec-mcp",
        )
