# 07. Use Case Specification – Record Chemical Consumption

## 1. Use Case Overview

| Attribute | Description |
|---|---|
| Use Case ID | UC-01 |
| Use Case Name | Record Chemical Consumption |
| Primary Actor | Storekeeper / Inventory Officer |
| Supporting Actor | None |
| System | Chemical Inventory Management System |
| Priority | High |
| Related Requirements | FR-07, FR-08, FR-09, FR-10 |

## 2. Use Case Description

This use case describes how an inventory officer records chemical consumption in the system. The system validates the transaction, updates the available stock, and maintains a historical consumption record.

## 3. Preconditions

- The application must be running.
- The chemical must already exist in the inventory.
- The user must have the necessary chemical and transaction information.

## 4. Trigger

The inventory officer needs to record chemical consumption following a production or operational activity.

## 5. Main Success Scenario

| Step | Actor Action | System Response |
|---|---|---|
| 1 | Selects the Record Consumption option. | Displays the chemical selection and transaction input process. |
| 2 | Selects or identifies the required chemical. | Retrieves the selected chemical's current stock information. |
| 3 | Enters the received quantity, if applicable. | Accepts the received quantity for validation. |
| 4 | Enters the consumed quantity. | Validates the entered quantities. |
| 5 | Confirms the transaction inputs. | Checks stock availability and calculates the updated stock. |
| 6 | Completes the transaction. | Updates available stock and records the consumption transaction. |
| 7 | Reviews the result. | Displays the transaction outcome and updated stock information. |

## 6. Alternative and Exception Flows

### A1: Invalid Quantity

- The user enters a negative or otherwise invalid quantity.
- The system displays an appropriate error message.
- The user must enter a valid quantity.

### A2: Consumption Exceeds Available Stock

- The user enters a consumed quantity greater than the available stock after accounting for any new receipt.
- The system rejects the transaction.
- The user must correct the quantity.

### A3: Chemical Not Found

- The selected chemical cannot be found in the inventory.
- The system displays an appropriate message.
- The user must select an existing chemical.

## 7. Postconditions

### Successful Transaction
- Available stock is updated.
- A consumption transaction record is maintained.
- The transaction date is recorded.

### Unsuccessful Transaction
- Invalid transactions are rejected.
- The existing available stock remains unchanged.

## 8. Business Rules

- Consumption quantity must be greater than zero.
- Consumption must not exceed available stock after considering any received quantity.
- Available stock must be updated after a successful transaction.
- Consumption history must be retained for future reference.

## 9. Expected Outcome

The system successfully records chemical consumption, updates available stock, and maintains an accurate transaction history.

## 10. Implementation Note

This use case represents the current inventory application workflow. The Storekeeper / Inventory Officer is an intended business actor; the current application does not implement user authentication or role-based access control.
