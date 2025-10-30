# Contributing to SweepGraph

Thanks for your interest in contributing! This guide explains how to propose improvements, report bugs, and submit pull requests so we can integrate your work smoothly.

## Getting Started

- Review the [README](README.md) to understand project goals, architecture, and workflows.
- Set up a local environment using the Quick Start instructions or the detailed guides in `docs/guides/`.
- If you're planning a substantial change, open a discussion or issue first so we can align on scope and approach.

## Ways to Contribute

- **Report bugs:** Use GitHub Issues and include reproduction steps, expected vs. actual behaviour, and environment details.
- **Improve documentation:** Clarify procedures, add diagrams, share real-world examples, or contribute sweep templates and prompts.
- **Enhance code:** Optimise performance, extend the Streamlit frontend, add validation utilities, or implement domain-specific sweep pipelines.
- **Share use cases:** Document how you used SweepGraph in your research or organisation to help others learn.

## Pull Request Checklist

Before opening a PR:

1. Fork the repository and create a feature branch (`git checkout -b feature/your-change`).
2. Keep changes focused and scoped; separate unrelated work into individual PRs.
3. Follow existing coding style and add concise comments only when they clarify non-obvious logic.
4. Add or update documentation and tests relevant to your change.
5. Run any applicable scripts or checks to verify your updates locally.
6. Describe the motivation, solution, and validation steps clearly in the PR description.

## Coding Standards

- Use Python 3.11+ and keep dependencies minimal.
- Prefer deterministic behaviour in scripts; make network calls optional where possible.
- Ensure generated JSON adheres to the documented schemas (nodes, relationships, enrichments).
- When introducing prompts or sweeps, include validation steps and sample outputs.

## Community Expectations

We aim to maintain a collaborative and respectful environment. Be welcoming, stay constructive, and help others succeed. If you encounter any issues or have questions, start a discussion—our goal is to make SweepGraph useful for researchers, developers, and analysts alike.

Happy graph building!
