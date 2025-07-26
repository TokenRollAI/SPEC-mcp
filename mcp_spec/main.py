# -*-coding:utf-8 -*-
from pathlib import Path
from typing import Annotated

from fastmcp import FastMCP
from pydantic import Field

from .prompts import *

mcp = FastMCP("spec_mcp")


@mcp.tool
def generate_spec(
    root_path: Annotated[str, Field(
        description="Full path of the project root directory, e.g. /Users/username/project_name (in windows, it should be "
                    "D:/username/project_name)")],
):
    specdir = Path(root_path) / ".spec"
    specdir.mkdir(parents=True, exist_ok=True)
    requirements = specdir / "requirements.md"
    design = specdir / "design.md"
    attention = specdir / "attention.md"
    todos = specdir / "todos.md"

    requirements.write_text(GEN_REQUIREMENTS, encoding="utf-8")
    design.write_text(GEN_DESIGN, encoding="utf-8")
    attention.write_text(GEN_MISTAKES, encoding="utf-8")
    todos.write_text(GEN_TODOS, encoding="utf-8")

    return (f"""
ATTENTION: The relevant documents have now been created in the {specdir} directory.

Here’s what you need to do next:
1. Confirm that you understand the user's requirements. If the user's description is too brief, ask for more details.
2. Once you’re confident you’ve grasped the requirements, follow the instructions in {requirements} to generate the requirements document. The content should be written into {requirements}main.py.
3. Proceed with the same instructions to execute the content in {design}, generating the design document. The content should be written into {design}. Follow the instructions in {attention} to generate the precautions document, with content written into {attention}.
4. Finally, continue with the same instructions to execute the content in {todos}, generating the to-do list document. The content should be written into {todos}.
5. Note: Your output language must match the user's input language!

The most important thing: Before writing each document, comprehensively consider the content of all preceding documents to ensure consistency.
""")


@mcp.tool
def get_spec(
    root_path: Annotated[str, Field(
        description="Full path of the project root directory, e.g. /Users/username/project_name (in windows, it should be "
                    "D:/username/project_name)")], ) -> str:
    specdir = Path(root_path) / ".spec"
    return f"""
You now need to carefully read all the documents in the {specdir} directory.

These include:

* requirements.md: The user's requirements document
* design.md: The technical design document
* attention.md: The precautions document
* todos.md: The to-do list document


Then, you should follow the tasks listed in {specdir / 'todos.md'} and complete each one sequentially(EveryTime you complete a task, you should write the results to the corresponding document.)
Please note:

Your output language should match the user's input language!
After completing each task, you should write the results to the corresponding document.

**If the user makes any changes to the requirements/design/precautions/to-do list, you should update the corresponding document accordingly.**
    """

def main():
    mcp.run()

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="127.0.0.1",
        port=4200,
        log_level="debug",
        path="/spec",
    )
