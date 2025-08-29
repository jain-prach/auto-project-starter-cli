import os
import subprocess
from pathlib import Path
import jinja2
from rich.console import Console
from .models import ProjectAnalysis

console = Console()
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


def scaffold_project(project_name: str, analysis: ProjectAnalysis):
    project_path = Path(project_name)
    if project_path.exists():
        console.print("[red]Project directory already exists! Aborting.[/red]")
        return
    
    # Create root dir
    project_path.mkdir()
    os.chdir(project_path)  # Change to project dir for relative paths
    
    # Create folders
    for folder in analysis.folder_structure:
        Path(folder).mkdir(parents=True, exist_ok=True)
    
    # Generate module files with content (single loop, with unescape)
    for filename, details in analysis.module_names.items():
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        content = details.get('content', '# Placeholder for ' + details.get('purpose', 'unknown purpose'))  # Safe get to avoid KeyError
        content = content.replace('\\n', '\n').replace('\\"', '"')  # Unescape
        with open(filename, 'w') as f:
            f.write(content)
    
    # Generate Docker files (with unescape)
    if analysis.docker_setup.dockerfile:
        dockerfile_content = analysis.docker_setup.dockerfile.replace('\\n', '\n').replace('\\"', '"')
        with open('Dockerfile', 'w') as f:
            f.write(dockerfile_content)
    if analysis.docker_setup.compose_yaml:
        compose_content = analysis.docker_setup.compose_yaml.replace('\\n', '\n').replace('\\"', '"')
        with open('docker-compose.yml', 'w') as f:
            f.write(compose_content)
    
    # Template files: e.g., .gitignore (removed unnecessary if-check)
    gitignore_template = template_env.get_template('gitignore.j2')
    with open('.gitignore', 'w') as f:
        f.write(gitignore_template.render(project_name=project_name))
    
    # Dependencies (now Dict, so language-specific)
    for lang, deps in analysis.dependencies.items():
        if lang == "python":
            with open('requirements.txt', 'w') as f:
                f.write('\n'.join(deps))
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        elif lang == "js":
            deps_str = ','.join(f'"{pkg}": "latest"' for pkg in deps)
            with open('package.json', 'w') as f:
                f.write(f'{{"name": "{project_name}", "version": "1.0.0", "dependencies": {{{deps_str}}}}}')
            subprocess.run(["npm", "install"], check=True)
    
    # Git init
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial scaffold"], check=True)
    
    # Third-party in README
    with open('README.md', 'w') as f:
        f.write(f"# {project_name}\n\nThird-party services:\n")
        for service in analysis.third_party_services:
            f.write(f"- {service.get('name', 'unknown')}: {service.get('use', 'unknown')}\n")  # Safe get
        f.write("\nSetup: docker-compose up\n")
    
    os.chdir("..")  # Back to original dir
    console.print(f"[green]Project {project_name} scaffolded successfully![/green]")