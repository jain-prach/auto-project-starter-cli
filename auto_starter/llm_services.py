import os
import json
import ollama
from openai import OpenAI
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from rich.console import Console
from .models import ProjectInputs, ProjectAnalysis
from .prompts import ollama_prompt, open_ai_prompt
from .helper import repair_json

load_dotenv()  # For OPENAI_API_KEY
console = Console()

class LLMService(ABC):
    @abstractmethod
    def analyze_project(self, inputs: ProjectInputs) -> ProjectAnalysis:
        pass

class OllamaService(LLMService):
    def __init__(self, model: str = "gemma:2b"):
        self.model = model
        try:
            ollama.list()
        except Exception:
            console.print("[red]Ollama not detected at http://localhost:11434.[/red]")
            console.print("[yellow]Setup guide: Run Docker container as per docs, then 'ollama pull {self.model}' inside it.[/yellow]")
            raise
        if model not in [m['model'] for m in ollama.list()['models']]:
            console.print(f"[yellow]Pulling {model}... This may take time.[/yellow]")
            ollama.pull(model)

    def analyze_project(self, inputs: ProjectInputs) -> ProjectAnalysis:
        prompt = ollama_prompt.format(inputs=inputs)
        response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
        json_str = response['message']['content'].strip()
        json_str = repair_json(json_str)
        print(json_str)
        return ProjectAnalysis.model_validate_json(json_str)  # Parse and validate

class OpenAIService(LLMService):
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if not self.client.api_key:
            key = console.input("[yellow]Enter OpenAI API key: [/yellow]")
            os.environ["OPENAI_API_KEY"] = key
            self.client = OpenAI(api_key=key)
        self.model = model

    def analyze_project(self, inputs: ProjectInputs) -> ProjectAnalysis:
        prompt = open_ai_prompt.format(inputs=inputs)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        json_str = response.choices[0].message.content
        json_str = repair_json(json_str)
        print(json_str)
        return ProjectAnalysis.model_validate_json(json_str)