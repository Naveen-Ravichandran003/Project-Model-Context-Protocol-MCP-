# Project: Automated VWO Login Validation (Playwright MCP + JIRA)

Empowering automated test execution and professional reporting using Model Context Protocol (MCP) and Playwright.

## 🚀 Overview

This project automates the validation of the VWO Login page across multiple scenarios, integrates with JIRA for professional bug tracking, and generates high-fidelity HTML reports for stakeholders. It leverages the **RICEPOT METHOD** for structured test case design and execution.

---

## 📊 Quick Links

- 🚀 **[Launch Full Test Execution Report](./Test_Execution_Report.html)**
- 📋 **[Test Cases Document (PDF/Excel Source)](./Test%20Cases/VWO_Login_TestCases_RICEPOT%20METHOD.xlsx)**
- 🐛 **[Live JIRA Bug (KAN-246)](https://naveen-workflow.atlassian.net/browse/KAN-246)**

---

## 📋 Detailed Test Cases

| ID | Scenario | Expected Result | Status |
|:---|:---|:---|:---|
| **TC_001** | Password Visibility Toggle | Password becomes visible on eye-icon click | ✅ PASS |
| **TC_002** | Valid Email + Wrong Pwd | Error: 'Your email, password... did not match' | ✅ PASS |
| **TC_003** | Invalid Email + Valid Pwd | Error: 'Your email, password... did not match' | ✅ PASS |
| **TC_004** | Forgot Password Link | Redirect to /forgot-password page | ✅ PASS |
| **TC_005** | Credential Error (FAIL) | User redirected to dashboard | ❌ FAIL |

*For full steps and data, refer to [the detailed markdown](./Test%20Cases/VWO_Login_TestCases_RICEPOT%20METHOD.md).*

---

## 🛠️ Tech Stack & Methodology

- **Framework**: Model Context Protocol (MCP)
- **Automation Engine**: Playwright MCP
- **Bug Tracking**: JIRA MCP (Atlassian)
- **Reporting**: Custom Styled HTML/CSS Project Dashboard (RICEPOT Output)

## 📁 Project Structure

```text
Project 2 - MCP + Playwright + JIRA Workflow/
├── screenshots/               # Folder: Evidence & JIRA screenshots
├── Test Cases/                # Folder: Detailed Test Specifications (.md, .xlsx)
├── Prompts/                   # Folder: RICEPOT requirement & execution prompts
├── Test_Execution_Report.html # Professional Dashboard (Launch this!)
└── README.md                  # Project documentation (this file)
```

---
*Created with ❤️ using Super Agent Workflow*
