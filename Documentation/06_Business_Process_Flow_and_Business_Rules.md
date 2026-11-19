# 06. Business Process Flow and Business Rules

## 1. Purpose

This document describes the business processes involved in managing chemical inventory and defines the business rules that govern inventory transactions.

## 2. Business Process Overview

The Chemical Inventory Management System supports the following key business processes:

1. Adding new chemicals to inventory.
2. Viewing available chemical stock.
3. Searching for chemicals.
4. Recording chemical receipts and consumption.
5. Monitoring available stock.
6. Reviewing consumption history.
7. Generating inventory and consumption reports.
8. Deleting chemicals from the current inventory.

## 3. Chemical Inventory Process Flow

### 3.1 Add New Chemical

1. User selects the Add Chemical option.
2. User enters the chemical name.
3. System checks whether the chemical name is blank or already exists.
4. User enters the opening stock quantity and unit.
5. System validates the opening stock quantity.
6. System generates a unique chemical ID.
7. System saves the chemical information.
8. The new chemical becomes available in the inventory.

### 3.2 Record Chemical Consumption

1. User selects the Record Consumption option.
2. User selects or identifies the chemical.
3. User enters the received quantity, if applicable, and consumed quantity.
4. System validates the entered quantities.
5. System checks whether the consumed quantity exceeds the available stock after considering any new receipt.
6. System updates the available stock.
7. System records the consumption transaction.
8. Updated inventory information becomes available.

### 3.3 View and Search Inventory

1. User selects View Inventory or Search Chemical.
2. System retrieves the available inventory records.
3. System displays the relevant chemical information.
4. User reviews the stock information.

### 3.4 Generate Reports

1. User selects the relevant report option.
2. System retrieves the current inventory or consumption records.
3. System generates an Excel report.
4. User can access the generated report for review and analysis.

## 4. Business Rules

| Rule ID | Business Rule | Description |
|---|---|---|
| BRULE-01 | Unique Chemical Name | A chemical name must not be duplicated in the current inventory. |
| BRULE-02 | Unique Chemical ID | Each newly added chemical must receive an automatically generated chemical ID. |
| BRULE-03 | Non-Negative Opening Stock | Opening stock quantity must not be negative. |
| BRULE-04 | Non-Negative Received Quantity | Received quantity must not be negative. |
| BRULE-05 | Positive Consumption Quantity | A consumption transaction must have a positive consumed quantity. |
| BRULE-06 | Stock Availability | Consumption must not exceed the available stock after accounting for any quantity received in the transaction. |
| BRULE-07 | Stock Calculation | Available stock = Previous Available Stock + Received Quantity - Consumed Quantity. |
| BRULE-08 | Consumption History | Recorded consumption transactions should be retained for historical reference. |
| BRULE-09 | Chemical Deletion | Deleting a chemical removes it from the current inventory but does not automatically delete its historical consumption records. |

## 5. Process Control and Validation

The system applies validation controls to reduce inventory errors, including:

- Checking for blank and duplicate chemical names.
- Validating stock quantities.
- Preventing consumption beyond available stock.
- Maintaining chemical identification numbers.
- Recording consumption transaction dates.
- Updating available stock after transactions.

## 6. Process Improvement Opportunities

The following improvements may be considered for future development:

- Low-stock notifications.
- Chemical batch and expiry-date tracking.
- Supplier and purchase order management.
- User authentication and authorization.
- Automated inventory reconciliation.
- Database integration for improved data management.

## 7. Conclusion

The defined process flows and business rules establish a consistent approach to chemical inventory management. They help ensure accurate stock monitoring, controlled consumption, and reliable inventory records.
