# Practical AI Workflows with Model Context Protocol (MCP)

This repository contains real-world, automated workflows powered by the **Model Context Protocol (MCP)**. It demonstrates how AI can interact with developer tools like **Playwright** (for browser automation) and **JIRA** (for bug tracking) to create seamless, hands-free QA and reporting pipelines.

---

## 📁 Repository Structure

### 1️⃣ [Project 1: MCP Basics](./Project%201%20-MCP%20Basics/)
**Goal:** Establish the fundamental connection between AI, a browser, and an issue tracker.
- **Playwright MCP:** Used to navigate to the VWO login page and perform a visual audit.
- **JIRA MCP:** Used to automatically log a bug (KAN-245) when an unexpected UI element ("Sign in with Passkey") was discovered during the audit.
- **Highlights:** Demonstrates zero-touch visual inspection and automated bug ticket creation with screenshot evidence.

### 2️⃣ [Project 2: MCP + Playwright + JIRA Workflow](./Project%202%20-%20MCP%20%2B%20Playwright%20%2B%20JIRA%20Workflow/)
**Goal:** Execute a structured, multi-scenario test suite and generate professional execution reports.
- **RICEPOT Method:** Utilized a structured prompt methodology to generate detailed test cases.
- **Execution:** The AI agent autonomously executed 5 distinct login test cases (validating UI toggles, error boundaries, and navigation) using Playwright.
- **Reporting:** 
  - Automatically logged a verified failure into JIRA (KAN-246) with professional phrasing.
  - Generated a stunning, dark-mode **[HTML Test Execution Report](https://htmlpreview.github.io/?https://github.com/Naveen-Ravichandran003/Project-Model-Context-Protocol-MCP-/blob/main/Project%202%20-%20MCP%20+%20Playwright%20+%20JIRA%20Workflow/Test_Execution_Report.html)** complete with dynamic badges and lightbox screenshots.

---

## ⚙️ How It Works (The Tech Stack)

- **AI Agents:** Powered by advanced language models communicating via MCP.
- **Playwright MCP (`@playwright/mcp`):** Allows the AI to read the browser's accessibility tree, find elements, click, type, and capture visual proof.
- **JIRA MCP (`mcp-atlassian`):** Allows the AI to securely access Jira Cloud, create issues, attach files, and transition statuses.

## 🚀 Getting Started

If you are cloning this repository to run it locally with your own agent (like Claude Desktop, Cursor, or Windsurf), ensure you have your `.vscode/mcp.json` configured with your specific Jira API credentials and Playwright environment.

*Detailed configuration steps can be found inside the respective project folders.*

## 🧪 Run MCP servers locally

Quick instructions to run the sample MCP servers in this repo.

- From the project root (`Project 3 - MCP Creation`) you can run the calculator server:

```powershell
cd "Project 3 - MCP Creation"
fastmcp run calculator_mcp.py --no-banner
```

- To run the file reader server using STDIO (the terminal will be owned by the server):

```powershell
cd "Project 3 - MCP Creation"
fastmcp run file_reader_mcp.py --transport stdio --no-banner
```

Keep that terminal dedicated to the MCP process and then connect with the MCP Inspector (Transport: STDIO).

- Alternatively, run the file reader over HTTP so the Inspector can connect remotely:

```powershell
cd "Project 3 - MCP Creation"
fastmcp run file_reader_mcp.py --transport http --host 127.0.0.1 --port 8000 --no-banner
```

Then open the MCP Inspector and point it to `http://127.0.0.1:8000/mcp/`.

### VS Code config

This repo includes an example VS Code MCP config at `.vscode/mcp.json` with entries for `calculator` and `file_reader`. Use those to launch servers from the Inspector or adjust args to match your preferred transport.

