> **Easier project setup with LLMs.**  
> Scaffold frontend, backend, or fullstack projects instantly using your chosen tech stack, design patterns, and features.

---

## ✨ Why This Project?

I’m not an experienced developer who knows every detail about setting up projects.  
But I found that project setup is one of the biggest blockers that delays building real features.  

This project exists to:
- **Reduce project setup time** by generating folders, configs, and boilerplate instantly.  
- **Let developers focus on building** instead of fighting with initial setup.  
- **Enable the community to collaborate** and refine scaffolding patterns (best practices, templates, CI/CD).  

If this helps others to get past the painful “day-1 setup” and actually start building, then it has done its job.

---

## 🛠 How It Works

1. You run the CLI and answer prompts about your project:
   - Frontend & Backend tech (e.g., React, FastAPI)
   - Project type (frontend, backend, fullstack)
   - Design pattern (MVC, Clean Architecture, Feature-based, etc.)
   - Key features (auth, users, posts, etc.)
   - Database, testing framework, package manager

2. The tool sends these inputs to an LLM (Ollama or OpenAI).  
3. The LLM generates a structured JSON (`ProjectAnalysis`) describing:
   - Folder structure
   - Dependencies & configs
   - Boilerplate module files
   - Docker setup
   - CI/CD configs

4. The generator uses this JSON to scaffold the full project locally:
   - Creates folders and files
   - Writes configs (`.gitignore`, `package.json`, `requirements.txt`, etc.)
   - Sets up Docker (if needed)
   - Initializes Git