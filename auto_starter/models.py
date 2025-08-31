from typing import List, Literal, Optional, Dict
from pydantic import BaseModel

class ProjectInputs(BaseModel):
    project_name: str
    project_type: Literal["frontend", "backend", "fullstack"]
    tech_stack: List[str]  # e.g. ["react", "typescript", "node", "fastapi"]
    design_pattern: Literal["mvc", "feature-based", "clean-architecture", "hexagonal"]
    features: List[str]  # e.g. ["auth", "users", "posts", "comments"]
    database: Optional[str] = None  # e.g. "postgres", "mongodb"
    testing_framework: Optional[str] = None  # e.g. "jest", "pytest"
    package_manager: Optional[str] = None  # e.g. "npm", "yarn", "pip", "poetry"

class DockerSetup(BaseModel):
    dockerfile: str
    compose_yaml: Optional[str] = None

class ProjectAnalysis(BaseModel):
    folder_structure: List[str]  # directory tree (flattened or nested)
    config_files: List[str]  # list of config files to include
    dependencies: Dict[str, List[str]]  # runtime deps
    dev_dependencies: Dict[str, List[str]]  # linting, testing, etc.
    entry_points: List[str]  # e.g. ["src/index.ts", "src/main.py", "src/App.tsx"]
    module_names: Dict[str, Dict[str, str]]  # feature -> related files
    testing_setup: List[str]  # test framework files/config
    ci_cd: Optional[List[str]] = None  # optional GitHub Actions, Docker, etc.
    docker_setup: DockerSetup