# Flowcharts

This folder contains flowcharts that illustrate the various processes and workflows in the **Project Nexus E-Commerce Backend**. Flowcharts help visualize the logic and sequence of actions, making it easier for developers and stakeholders to understand system behavior.

## User Authentication Flowchart

The **User Authentication Flowchart** demonstrates the step-by-step process that occurs when a user attempts to log in:

1. **User accesses Login Page:**  
   The process starts when a user navigates to the login page of the application.

2. **Enter Credentials:**  
   The user enters their login credentials (e.g., username and password).

3. **Validation Check:**  
   A conditional check is performed to verify if the provided credentials are valid.
   - **If valid:**  
     The system generates a JWT token for the user.
   - **If not valid:**  
     The system returns an error message, prompting the user to retry.

4. **Token Generation and Return:**  
   Upon successful validation, a JWT token is generated and sent back to the user. This token is used for subsequent authenticated requests.

5. **Error Handling:**  
   If the credentials are invalid, the user is notified of the error and prompted to try logging in again.

---

