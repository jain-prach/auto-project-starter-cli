import json

string_json = r"""
{
    "folder_structure": [
        "src/features/auth",
        "src/components/atoms"
    ],
    "config_files": [
        ".gitignore",
        "README.md",
        "pyproject.toml"
    ],
    "dependencies": {
        "python": [
        "fastapi",
        "react"
        ],
        "js": [
        "pytest",
        "eslint"
        ]
    },
    "dev_dependencies": {
        "pytest": [
        "pytest",
        "python-dotenv"
        ],
        "eslint": [
        "eslint",
        "eslint-plugin-yaml"
        ]
    },
    "entry_points": [
        "src/main.py",
        "src/index.js"
    ],
    "module_names": {
        "features/auth/service.py": {
        "purpose": "Authenticate user",
        "content": "from fastapi import login"
        },
        "src/atoms/Button.js": {
        "purpose": "Button functionality",
        "content": "import React from 'react';\nconst Button = () => <div>Button clicked!</div>;\nexport default Button;"
        }
    },
    "third_party_services": [
        {
        "name": "database",
        "use": "sqlite3"
        }
    ],
    "testing_setup": [
        "pytest.ini"
    ],
    "ci_cd": {
        "production-ready": [
        "docker-compose run backend:build",
        "docker-compose run frontend:build"
        ]
    }
}
"""
data = json.loads(string_json)
print(json.dumps(data, indent=4))