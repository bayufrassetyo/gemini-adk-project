# Gemini Multi-Agent Productivity Assistant

A multi-agent productivity assistant built for the Google Cloud Gemini APAC Hackathon. This project explores how AI agents can help users manage tasks, analyze issues, interact with a database, and support productivity workflows.

## Overview

This project demonstrates a Python-based multi-agent assistant powered by Gemini. The assistant is designed to process user requests, interact with structured data, and return useful responses for productivity and issue management use cases.

## Problem

Many productivity workflows require users to switch between notes, databases, task lists, and manual analysis. This creates friction and reduces efficiency.

This project explores how AI agents can reduce that friction by helping users interact with information more naturally.

## Solution

The assistant uses multiple components to process requests, query data, and return relevant responses. It combines AI reasoning, database interaction, and modular Python tools.

## Features

- AI-powered assistant workflow
- SQLite database integration
- Issue or task data processing
- Modular Python components
- Docker support for containerized execution
- Experimental MCP tool integration

## Tech Stack

- Python
- Gemini
- SQLite
- Docker
- MCP Tooling

## Project Structure

```txt
gemini-adk-project/
├── agent.py
├── ai_sql.py
├── database.py
├── main.py
├── mcp_tool.py
├── issues.db
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## How to Run
1. Clone repository
git clone https://github.com/bayufrassetyo/gemini-adk-project.git
cd gemini-adk-project

2. Install dependencies
pip install -r requirements.txt

3. Run the app
python main.py

## Use Case

This project can be extended into:

- Productivity assistant
- Issue tracking assistant
- AI-powered task manager
- SQL/database assistant
- Internal workflow automation tool

## Future Improvements

- Add clearer agent architecture diagram
- Improve user interface
- Add API endpoint
- Add authentication
- Deploy to cloud platform
- Add sample prompts and demo screenshots

## Author

Bayu Frassetyo Wibowo
GitHub: https://github.com/bayufrassetyo
