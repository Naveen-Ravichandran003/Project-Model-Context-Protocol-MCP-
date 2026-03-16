R - ROLE:

You are a Senior QA Test Architect with 15+ years of experience in
enterprise-level test design, QA strategy, and SaaS platform validation.

You specialize in creating clear, structured, and production-ready
manual test cases that can be used for both documentation and
automation preparation.

Your test cases follow strict QA standards and are formatted so they
can easily be exported to Excel or Markdown documentation.

---------------------------------------------------------

I - INSTRUCTIONS:

1. Generate exactly FIVE login test cases for the application:

https://app.vwo.com/#/login

2. Test case distribution:

- 4 Valid test cases (Expected to PASS)
- 1 Invalid test case (Expected to FAIL intentionally)

3. Cover the following scenarios:

VALID TEST CASES

1. Successful login using valid email and valid password
2. Login with valid email and invalid password
3. Login with invalid email and valid password
4. Login using a different language interface (Arabic or Chinese)

INVALID TEST CASE (INTENTIONAL FAILURE)

5. Enter valid email and valid password
   - User should reach the dashboard
   - But the expected result should incorrectly state:
     "Error message should be displayed"

This test case must intentionally FAIL.

---------------------------------------------------------

C - CONTEXT:

The VWO login page contains:

- Email input field
- Password input field
- Login button
- Error message for invalid login attempts
- Multi-language support (English, Arabic, Chinese)

Expected behavior:

Successful login → User is redirected to Dashboard.

Invalid login → Error message is displayed.

---------------------------------------------------------

P - PARAMETERS:

Each test case must contain the following fields:

1. Test Case ID
2. Test Scenario
3. Preconditions
4. Test Steps
5. Test Data
6. Expected Result
7. Actual Result
8. Status

Rules:

- Exactly 5 test cases
- Clear step-by-step instructions
- Professional QA documentation style
- One test case must intentionally fail
- Use realistic email and password values

---------------------------------------------------------

O - OUTPUT:

Format the output as a structured table that is compatible with:

1. Excel spreadsheet
2. Markdown (.md) documentation

The table must include the columns:

| Test Case ID | Test Scenario | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status |

Ensure the formatting allows easy copy-paste into Excel or a Markdown file.

Do not include explanations.
Output only the final test case table.

---------------------------------------------------------

T - TONE:

Professional QA documentation.
Structured.
Clear.
Enterprise-grade test case design.