from typing import List
import typer
from rich.console import Console
from rich.prompt import Prompt
from .generator import scaffold_project

from .llm_services import OllamaService, OpenAIService
from .models import ProjectInputs

app = typer.Typer()
console = Console()

@app.command()
def new(project_name: str, llm: str = "ollama", model: str = "gemma:2b"):
    console.print(f"[bold green]Starting new project: {project_name}[/bold green]")

    # Always needed
    project_name = Prompt.ask("Project name?")
    project_type = Prompt.ask("Project type (frontend, backend, fullstack)?")
    design_pattern = Prompt.ask("Design patterns (e.g., MVC, feature-based, clean-architecture, hexagonal)?")
    features = Prompt.ask("Key features (comma-separated)?")

    # Collect tech stack conditionally
    tech_stack: List[str] = []
    if project_type.lower() in ["frontend", "fullstack"]:
        frontend = Prompt.ask("Frontend tech (e.g., React, Vue)?")
        if frontend:
            tech_stack.append(frontend.lower())

    if project_type.lower() in ["backend", "fullstack"]:
        backend = Prompt.ask("Backend tech (e.g., FastAPI, Django)?")
        if backend:
            tech_stack.append(backend.lower())

    # Optional extras
    database = None
    if project_type.lower() in ["backend", "fullstack"]:
        database = Prompt.ask("Database (e.g., Postgres, MongoDB)?", default="")

    testing_framework = Prompt.ask("Testing framework (e.g., Jest, Pytest)?", default="")
    package_manager = Prompt.ask("Package manager (e.g., npm, yarn, pip, poetry)?", default="")

    # Build ProjectInputs
    inputs = ProjectInputs(
        project_name=project_name,
        project_type=project_type.lower(),
        tech_stack=tech_stack,
        design_pattern=design_pattern.lower(),
        features=[f.strip() for f in features.split(",")],
        database=database.lower() if database else None,
        testing_framework=testing_framework.lower() if testing_framework else None,
        package_manager=package_manager.lower() if package_manager else None
    )
    print(inputs.model_dump_json(indent=2))
    
    if llm == "ollama":
        service = OllamaService(model=model if model else None)
    elif llm == "openai":
        service = OpenAIService(model=model if model else None)
    else:
        raise ValueError("Invalid LLM choice")
    
    console.print("[blue]Analyzing with LLM...[/blue]")
    analysis = service.analyze_project(inputs)
    
    console.print(f"[green]Analysis: {analysis.model_dump_json(indent=2)}[/green]")

    # TODO: Generate files/dirs, including Docker
    console.print("[blue]Scaffolding project...[/blue]")
    scaffold_project(project_name, analysis)
    console.print("[yellow]Project scaffolded! (Placeholder)[/yellow]")

if __name__ == "__main__":
    app()