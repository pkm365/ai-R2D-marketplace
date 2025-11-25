# AI R2D Marketplace

A curated collection of Claude Code plugins to streamline your Requirement-to-Diagram (R2D) workflow.

## 🚀 Quick Start

To use the plugins in this marketplace with Claude Code, you must first install the marketplace. You can then browse available plugins and install them directly from Claude Code.

### Installation

Run the command to add the ai-R2D-marketplace to Claude Code.

```bash
/plugin marketplace add [https://github.com/pkm365/ai-R2D-marketplace.git](https://github.com/pkm365/ai-R2D-marketplace.git)
```

You can then browse available plugins interactively by running /plugin.

## 📦 Available Plugins

**[NOTE]** Each plugin has its own set of requirements! Please refer to the plugin's README for more information.

### Flowchart Architect

A comprehensive plugin for analyzing business requirements, managing standard assets, and generating brand-compliant Draw.io flowcharts with AI assistance.

**REQUIREMENTS:**
This plugin relies on a specific folder structure and standard assets. Please refer to the plugin's README for setup instructions.

**Features:**

- Interactive Requirement Solicitation: Acts as a consultant to clarify business logic and user needs using a professional checklist.

- Asset Library Integration: Searches and retrieves existing standard process templates ("Pre-made dishes") to avoid reinventing the wheel.

- Gap Analysis: Automatically compares new requirements against standard baselines to identify and confirm logical deviations.

- Draw.io XML Generation: Calculates coordinates and generates valid .drawio files strictly following brand guidelines (colors, fonts, layout).

- Automated QA: Built-in XML Auditor to check for syntax errors and brand compliance loops.

View Plugin →

## 🛠️ Plugin Structure

Each plugin in this marketplace follows a consistent structure designed for the R2D workflow:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── README.md                 # Plugin documentation
├── skills/                   # Claude Code skills (Orchestration, Generation, Analysis)
├── agents/                   # Agent definitions (Analyst, Auditor, Librarian)
├── references/               # Static knowledge (Brand Guidelines, Templates)
└── assets/                   # Standard process library (optional)
```

## 👤 Author

- GitHub: @pkm365

## 🔗 Related Projects

Flowchart Architect Scaffolding - The core implementation of the R2D workflow.

---

Made with ❤️ for the R2D AI OS for LinkedData