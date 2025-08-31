# Contributing to Auto Starter CLI

Thank you for your interest in contributing to Auto Starter CLI! This project is built for the developer community, by the developer community. We believe in making project scaffolding accessible, intelligent, and helpful for developers of all backgrounds.

## Our Mission

Auto Starter CLI exists to **democratize project setup** and eliminate the repetitive, time-consuming task of creating project boilerplate. We want this tool to be:

1. **Universally Helpful** - Supporting frontend, backend, and fullstack developers across all major technologies
2. **Community-Driven** - Open source, free, and improved by developers who use it
3. **Rapidly Deployable** - Getting developers from idea to coding as fast as possible

This is **not a commercial product** - it's a tool built by developers, for developers, to solve a common pain point we all face.

## How You Can Help

### High Priority Contributions

We need your help to make this tool production-ready and widely useful:

#### 1. **Technology Support Expansion**
- Add support for new frameworks (Svelte, SolidJS, Spring Boot, .NET, etc.)
- Improve existing technology integrations
- Add mobile development support (React Native, Flutter)

#### 2. **Template Quality & Variety**
- Create better boilerplate code templates
- Add industry-specific templates (e-commerce, SaaS, APIs)
- Improve code quality and best practices in generated files

#### 3. **LLM Provider Support**
- Add support for other providers (Anthropic Claude, Google Gemini, local models)
- Improve prompt engineering for better project analysis
- Add model-specific optimizations

#### 4. **Developer Experience**
- Better error handling and user feedback
- Interactive project configuration wizard
- Project preview before generation

#### 5. **Testing & Reliability**
- Unit tests for core functionality
- Integration tests with different LLM providers
- End-to-end testing of generated projects

## Development Setup

### Prerequisites
- Python 3.8+
- Docker (for Ollama testing)
- Git

### Local Development

1. **Fork and Clone**
```bash
git clone https://github.com/jain-prach/auto-project-starter-cli.git
cd auto-starter-cli
```

2. **Setup Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. **Setup Ollama for Testing**
```bash
# Start Ollama container
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Pull test model
docker exec -it ollama ollama pull qwen2.5:3b
```

4. **Test Your Setup**
```bash
# Run a test generation
python -m auto_starter.main test-project --llm=ollama --model=qwen2.5:3b
```

## Contribution Guidelines

### Workflow

1. **Create an Issue** - Discuss your idea before implementing
2. **Fork & Branch** - Create a feature branch from `main`
3. **Develop** - Make your changes with tests
4. **Test** - Ensure everything works with different configurations
5. **Pull Request** - Submit with clear description

### Testing Your Changes

Before submitting, test with multiple scenarios:

```bash
# Test different project types
python -m auto_starter.main frontend-app --llm=ollama
python -m auto_starter.main backend-api --llm=ollama  
python -m auto_starter.main fullstack-app --llm=ollama

# Test different tech stacks
# (React + FastAPI, Vue + Django, etc.)
```

## Specific Areas We Need Help

### **Template Development**
**Skills Needed**: Knowledge of specific frameworks/technologies
**Impact**: High - directly improves generated project quality

- Create Jinja2 templates in `/templates/` directory
- Add support for new package managers
- Improve existing boilerplate code quality

### **LLM Integration**
**Skills Needed**: Python, API integration, prompt engineering
**Impact**: High - expands tool capabilities

- Add new LLM providers in `llm_services.py`
- Improve prompt engineering in `prompts.py`
- Add fallback mechanisms for API failures

### **Framework Support**
**Skills Needed**: Framework expertise (React, Vue, Django, etc.)
**Impact**: High - makes tool useful for more developers

- Add framework-specific logic in generator
- Create proper dependency lists
- Add framework-specific folder structures

### **Architecture Improvements**
**Skills Needed**: Python, software architecture
**Impact**: Medium - improves maintainability

- Refactor code organization
- Add plugin system for extensibility
- Improve error handling

### **Documentation**
**Skills Needed**: Technical writing
**Impact**: Medium - helps adoption

- Improve inline documentation
- Create tutorial videos/guides
- Add example project showcases

## Adding New Technology Support

### Example: Adding Svelte Support

1. **Update Models** (`models.py`):
```python
# Add to tech_stack validation if needed
```

2. **Update Prompts** (`prompts.py`):
```python
# Add Svelte-specific examples in prompt
```

3. **Add Templates** (`templates/`):
```
templates/
├── svelte.config.js.j2
├── vite.config.js.j2
└── package.json.j2
```

4. **Update Generator** (`generator.py`):
```python
# Add Svelte-specific logic if needed
```

## Bug Reports

### Before Reporting
- Check existing issues
- Test with latest version
- Try with different models/providers

### What to Include
- Command used
- Error message/output
- System info (OS, Python version)
- LLM provider and model
- Expected vs actual behavior

## Feature Requests

We love new ideas! Before suggesting:

1. **Check Issues** - Might already be planned
2. **Consider Scope** - Does it fit our mission?
3. **Think Implementation** - How would it work?

### Good Feature Requests
- "Add support for Rust web frameworks"
- "Generate API documentation automatically"  
- "Add mobile app project types"

## Getting Help

- **Questions**: Open a GitHub issue with `question` label
- **Discussions**: Use GitHub Discussions for broader topics
- **Bugs**: Follow bug report template

## Development Priorities

### Short Term
- [ ] Add comprehensive testing suite
- [ ] Improve error handling and user feedback
- [ ] Add more framework templates (Svelte, SolidJS)
- [ ] Better Docker configurations

### Medium Term
- [ ] Plugin system for custom templates
- [ ] Web interface for non-CLI users
- [ ] Project update/migration capabilities
- [ ] Integration with popular IDEs

### Long Term
- [ ] AI-powered code generation beyond boilerplate
- [ ] Project analytics and recommendations
- [ ] Team collaboration features

## Community Values

We're building this together! Our community values:

- **Inclusivity** - All skill levels and backgrounds welcome
- **Collaboration** - We learn from each other
- **Quality** - Code that actually helps developers
- **Openness** - Transparent development process
- **Impact** - Features that make real difference

## Code of Conduct

Be respectful, constructive, and collaborative. We're all here to build something useful together.

---

**Ready to contribute? Pick an issue, fork the repo, and let's build something amazing!**

*Remember: This tool is meant to save developers time and eliminate repetitive setup work. Every contribution brings us closer to that goal.*