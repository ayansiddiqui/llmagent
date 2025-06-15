# LLM Agent Starter

This project provides a scaffold for building domain-driven LLM powered agents with FastAPI and Azure integration.

## Features

- **Clean Architecture** with separate domain, application, infrastructure and API layers.
- **OpenAI integration** through `openai` library.
- **Plugin system** for domain tools (retrievers, summarizers).
- **Azure placeholders** for Key Vault, Blob Storage and Service Bus.
- **FastAPI** web interface.
- **Data** folder with sample queries.
- **Notebooks and scripts** for data processing and training.
- **GitHub Actions** workflow for CI.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your environment variables (e.g. `OPENAI_API_KEY`).
3. Run the API server:
   ```bash
   python scripts/start_server.py
   ```
4. Send a request:
   ```bash
   curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' -d '{"user": "you", "content": "Hello"}'
   ```

## Roadmap

- Implement real Azure service integrations.
- Add more domain tools and example plugins.
- Extend training scripts for fine-tuning models on domain data.
- Provide a rich frontend interface.

## Contributing

1. Fork the repo and create your feature branch.
2. Commit your changes with descriptive messages.
3. Push to the branch and open a pull request.
4. Ensure `pytest` passes and CI is green.

