# JIRA Bug Report — KAN-245

## Summary
**[VWO] Login Page - 'Sign in with Passkey' option should not be displayed**

| Attribute | Value |
|---|---|
| **Issue Key** | [KAN-245](https://naveen-workflow.atlassian.net/browse/KAN-245) |
| **Project** | KAN |
| **Status** | Updated |
| **Severity** | Medium |
| **Environment** | Production |

## Detailed Description
**URL:** [https://app.vwo.com/#/login](https://app.vwo.com/#/login)

**Bug Summary:**
The 'Sign in with Passkey' option is currently visible on the VWO login page. According to the product requirements, this option should not be displayed to users. Its presence causes confusion as it is not a supported or expected authentication method for VWO users.

**Steps to Reproduce:**
1. Navigate to [https://app.vwo.com](https://app.vwo.com)
2. Observe the login page
3. Scroll down below the 'Sign in' button

**Expected Result:**
The 'Sign in with Passkey' option should NOT be visible on the login page.

**Actual Result:**
The 'Sign in with Passkey' button is displayed alongside 'Sign in with Google' and 'Sign in using SSO'.

---

## Evidence

### 1. VWO Login Page Issue
![VWO Login Screenshot](Login_Screenshot_Test.png)

### 2. JIRA Issue Status (KAN-245)
![JIRA Board Screenshot](KAN-245 bug.png)
