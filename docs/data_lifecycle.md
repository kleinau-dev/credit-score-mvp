# Data Lifecycle

This document describes how user data flows through the system.

## 1. User Registration
The user creates an account using email and password.

## 2. Authentication
The user authenticates and receives a JWT access token.

## 3. Consent
The user explicitly accepts the current consent version before sensitive operations.

## 4. Financial Data Submission
The user submits financial information used for credit score calculation.

## 5. Credit Score Calculation
The system calculates a credit score based on enabled rules and stores:
- Score value
- Rule snapshot
- Engine version
- Timestamp

## 6. History
Each score calculation is preserved and accessible to the user.

## 7. Data Export
The user can export all personal and financial data.

## 8. Data Deletion
The user can permanently delete their data from the system.

All sensitive actions are logged in the audit system.