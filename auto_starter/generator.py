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
    
    # Generate module files with content
    for filename, details in analysis.module_names.items():
        file_path = Path(filename)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Fix: Access content from dictionary, not as attribute
        content = details['content'].replace('\\n', '\n').replace('\\"', '"')  # Unescape
        with open(file_path, 'w') as f:
            f.write(content)
    
    # Generate config files (use template if available, else placeholder)
    for config in analysis.config_files:
        config_path = Path(config)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            template_name = config.split('/')[-1] + '.j2'
            template = template_env.get_template(template_name)
            content = template.render(project_name=project_name)
        except jinja2.TemplateNotFound:
            content = '# Placeholder for ' + config
        with open(config_path, 'w') as f:
            f.write(content)
    
    # Generate entry points (if not in module_names, create basic)
    for entry in analysis.entry_points:
        if entry not in analysis.module_names:
            entry_path = Path(entry)
            entry_path.parent.mkdir(parents=True, exist_ok=True)
            content = '# Basic entry point for the app'  # Or language-specific
            with open(entry_path, 'w') as f:
                f.write(content)
    
    # Generate testing setup files (basic test code)
    for test_file in analysis.testing_setup:
        test_path = Path(test_file)
        test_path.parent.mkdir(parents=True, exist_ok=True)
        content = '# Placeholder test setup'  # Add basic import/test
        with open(test_path, 'w') as f:
            f.write(content)
    
    # Generate CI/CD files if present
    if analysis.ci_cd:
        for ci_file in analysis.ci_cd:
            ci_path = Path(ci_file)
            ci_path.parent.mkdir(parents=True, exist_ok=True)
            content = '# Placeholder CI/CD workflow'
            with open(ci_path, 'w') as f:
                f.write(content)
    
    # Generate Docker files (unescape)
    if hasattr(analysis.docker_setup, 'dockerfile') and analysis.docker_setup.dockerfile:
        dockerfile_content = analysis.docker_setup.dockerfile.replace('\\n', '\n').replace('\\"', '"')
        with open('Dockerfile', 'w') as f:
            f.write(dockerfile_content)
    if hasattr(analysis.docker_setup, 'compose_yaml') and analysis.docker_setup.compose_yaml:
        compose_content = analysis.docker_setup.compose_yaml.replace('\\n', '\n').replace('\\"', '"')
        with open('docker-compose.yml', 'w') as f:
            f.write(compose_content)
    
    # Dependencies and dev_dependencies (language-specific, use package_manager)
    for lang, deps in analysis.dependencies.items():
        if lang == "python":
            req_file = 'requirements.txt'
            with open(req_file, 'w') as f:
                f.write('\n'.join(deps))
            pm = getattr(analysis, 'package_manager', None) or 'pip'
            if pm == 'poetry':
                for dep in deps:
                    subprocess.run(["poetry", "add", dep], check=True)
            else:
                subprocess.run([pm, "install", "-r", req_file], check=True)
        elif lang == "js":
            pm = getattr(analysis, 'package_manager', None) or 'npm'
            deps_str = ','.join(f'"{pkg}": "latest"' for pkg in deps)
            with open('package.json', 'w') as f:
                f.write(f'{{"name": "{project_name}", "version": "1.0.0", "dependencies": {{{deps_str}}}}}')
            subprocess.run([pm, "install"], check=True)
    
    # Dev dependencies (similar, but as dev)
    for lang, dev_deps in analysis.dev_dependencies.items():
        if lang == "python":
            req_file = 'requirements-dev.txt'  # Separate for dev
            with open(req_file, 'w') as f:
                f.write('\n'.join(dev_deps))
            pm = getattr(analysis, 'package_manager', None) or 'pip'
            if pm == 'poetry':
                for dep in dev_deps:
                    subprocess.run(["poetry", "add", "--dev", dep], check=True)
            else:
                subprocess.run([pm, "install", "-r", req_file], check=True)
        elif lang == "js":
            pm = getattr(analysis, 'package_manager', None) or 'npm'
            dev_deps_str = ','.join(f'"{pkg}": "latest"' for pkg in dev_deps)
            # Read existing package.json and update it
            try:
                with open('package.json', 'r') as f:
                    import json
                    package_data = json.load(f)
                package_data['devDependencies'] = {pkg: "latest" for pkg in dev_deps}
                with open('package.json', 'w') as f:
                    json.dump(package_data, f, indent=2)
            except (FileNotFoundError, json.JSONDecodeError):
                # Create new package.json with dev dependencies
                with open('package.json', 'w') as f:
                    f.write(f'{{"name": "{project_name}", "version": "1.0.0", "devDependencies": {{{dev_deps_str}}}}}')
            subprocess.run([pm, "install", "--save-dev"], check=True)
    
    # Git init
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial scaffold"], check=True)
    
    # Third-party services in README (append if exists)
    if hasattr(analysis, 'third_party_services') and analysis.third_party_services:
        with open('README.md', 'a') as f:
            f.write("\n\nThird-party services:\n")
            for service in analysis.third_party_services:
                service_name = service.get('name', 'unknown') if isinstance(service, dict) else str(service)
                service_use = service.get('use', 'unknown') if isinstance(service, dict) else 'unknown'
                f.write(f"- {service_name}: {service_use}\n")
            f.write("\nSetup: docker-compose up\n")
    
    os.chdir("..")  # Back to original dir
    console.print(f"[green]Project {project_name} scaffolded successfully![/green]")