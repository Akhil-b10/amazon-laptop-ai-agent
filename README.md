# Amazon Laptop AI Agent

A command-line tool that scrapes Amazon India for laptops, filters by rating, and summarizes the best affordable options using GPT-4o via LangChain.

## Features
- Web scraping using Selenium
- Filters by user-defined rating
- Summarizes top results with GPT-4o
- Fully interactive CLI

## Setup

```bash
pip install -r requirements.txt

Set your OpenAI key in .env:

OPENAI_API_KEY=your-key-here

## Run

python agent.py
