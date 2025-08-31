# Auto Starter CLI

**Intelligent Project Scaffolding Tool** - Generate complete, production-ready project structures with AI-powered analysis.

Auto Starter CLI uses Large Language Models to analyze your project requirements and automatically generate a comprehensive folder structure, boilerplate code, configuration files, and development environment setup.

## Features

- **AI-Powered Analysis**: Uses LLMs (Ollama/OpenAI) to understand your project needs
- **Multi-Stack Support**: Frontend, Backend, and Fullstack projects
- **Design Pattern Aware**: MVC, Feature-based, Clean Architecture, Hexagonal
- **Complete Setup**: Dependencies, dev tools, Docker, CI/CD, and testing
- **Technology Agnostic**: Supports React, Vue, FastAPI, Django, and more
- **Instant Development**: Ready-to-code projects with proper structure

## Prerequisites

### For Ollama (Recommended - Free)
1. **Docker** - Install from [docker.com](https://docker.com)
2. **Ollama** - We'll guide you through the setup

### For OpenAI
- OpenAI API key with credits

## Installation

```bash
# Clone the repository
git clone https://github.com/jain-prach/auto-project-starter-cli.git
cd auto-starter-cli

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Option 1: Using Ollama (Free, Local)

1. **Start Ollama with Docker:**
```bash
# Pull and run Ollama container
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# The tool will automatically pull qwen2.5:3b model on first use
```

2. **Generate your project:**
```bash
python -m auto_starter.main myapp --llm=ollama --model=qwen2.5:3b
```

### Option 2: Using OpenAI

```bash
# Set your API key
export OPENAI_API_KEY="your-api-key-here"

# Generate project
python -m auto_starter.main myapp --llm=openai --model=gpt-4o-mini
```

## 🎯 Usage

When you run the command, you'll be prompted for:

```
Project name? myapp
Project type (frontend, backend, fullstack)? fullstack
Design patterns (e.g., MVC, feature-based, clean-architecture, hexagonal)? feature-based
Key features (comma-separated)? auth, users, posts, comments
Frontend tech (e.g., React, Vue)? react
Backend tech (e.g., FastAPI, Django)? fastapi
Database (e.g., Postgres, MongoDB)? postgres
Testing framework (e.g., Jest, Pytest)? pytest
Package manager (e.g., npm, yarn, pip, poetry)? npm
```

## What Gets Generated

The tool creates a complete project structure including:

### **Folder Structure**
- Organized directories following your chosen design pattern
- Feature-based modules for scalable architecture
- Separation of concerns (frontend/backend for fullstack)

### **Configuration Files**
- `package.json` / `requirements.txt` - Dependencies
- `.gitignore` - Git ignore patterns
- `README.md` - Project documentation
- Framework-specific configs (e.g., `tsconfig.json`, `pyproject.toml`)

### **Docker Setup**
- `Dockerfile` - Container configuration
- `docker-compose.yml` - Multi-service orchestration
- Database and service configurations

### **Testing Setup**
- Test framework configuration
- Sample test files
- Testing utilities and helpers

### **Development Tools**
- CI/CD workflows (GitHub Actions)
- Linting and formatting configs
- Development dependencies

### **Boilerplate Code**
- Entry point files with basic setup
- Feature modules with standard patterns
- API routes and components
- Database models and connections

## Supported Technologies

### Frontend
- React, Vue, Angular
- TypeScript, JavaScript
- Tailwind CSS, Styled Components

### Backend
- FastAPI, Django, Flask
- Node.js, Express
- Python, JavaScript/TypeScript

### Databases
- PostgreSQL, MongoDB, MySQL
- SQLite for development

### Design Patterns
- **MVC**: Model-View-Controller separation
- **Feature-based**: Organized by business features
- **Clean Architecture**: Dependency inversion principles
- **Hexagonal**: Ports and adapters pattern

## Advanced Configuration

### Custom Models

```bash
# Use different Ollama model
python -m auto_starter.main myapp --llm=ollama --model=llama2:7b

# Use different OpenAI model
python -m auto_starter.main myapp --llm=openai --model=gpt-4
```

### Environment Variables

```bash
# OpenAI API Key
export OPENAI_API_KEY="your-key"

# Ollama endpoint (if not default)
export OLLAMA_HOST="http://custom-host:11434"
```

## Troubleshooting

### Ollama Issues
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama container
docker restart ollama

# Pull model manually
docker exec -it ollama ollama pull qwen2.5:3b
```

### Common Errors
- **"Project directory already exists"**: Choose a different name or remove existing directory
- **"Ollama not detected"**: Ensure Docker container is running on port 11434
- **"Invalid JSON"**: Model output parsing failed - try again or use different model

## Project Analysis Process

The tool follows this workflow:

1. **Input Collection**: Gathers your project requirements
2. **LLM Analysis**: AI analyzes requirements and generates project structure
3. **Structure Creation**: Creates folders and files based on analysis
4. **Code Generation**: Generates boilerplate code for each module
5. **Configuration**: Sets up development environment and tools
6. **Git Initialization**: Initializes repository with initial commit

## 🌟 Example Output

For a fullstack React + FastAPI project with authentication:

```
myapp/
├── frontend/
│   ├── src/
│   │   ├── features/
│   │   │   └── auth/
│   │   │       ├── components/
│   │   │       ├── hooks/
│   │   │       └── services/
│   │   └── components/
│   ├── package.json
│   └── tsconfig.json
├── backend/
│   ├── features/
│   │   └── auth/
│   │       ├── models.py
│   │       ├── routes.py
│   │       └── services.py
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

[LICENSE.md](LICENSE.md)

## Acknowledgments

- Powered by Ollama and OpenAI
- Built with Python, Typer, and Rich
- Template engine: Jinja2

---

**Ready to scaffold your next project? Run the command and watch the magic happen!** 
