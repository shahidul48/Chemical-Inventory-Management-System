# 04. Functional Requirements

## 1. Purpose

This document defines the functional requirements of the Chemical Inventory Management System. Functional requirements describe the specific operations and features that the system must provide to meet the identified business requirements.

## 2. Functional Requirements

| Requirement ID | Functional Requirement | Description | Related Business Requirement |
|---|---|---|---|
| FR-01 | Add Chemical | The system shall allow users to add new chemicals by entering the chemical name, opening stock quantity, and unit. | BR-01, BR-02 |
| FR-02 | Generate Chemical ID | The system shall automatically generate a unique chemical identification number for each newly added chemical. | BR-02 |
| FR-03 | Validate Chemical Information | The system shall prevent users from adding blank or duplicate chemical names. | BR-01 |
| FR-04 | Validate Opening Stock | The system shall prevent users from entering negative opening stock quantities. | BR-01, BR-09 |
| FR-05 | View Chemical Inventory | The system shall display the list of chemicals along with their IDs, available stock quantities, units, and entry dates. | BR-01, BR-05 |
| FR-06 | Search Chemical | The system shall allow users to search for chemicals using their names. | BR-07 |
| FR-07 | Record Chemical Consumption | The system shall allow users to record chemical consumption by selecting a chemical and entering the consumed quantity. | BR-04, BR-06 |
| FR-08 | Validate Consumption Quantity | The system shall prevent negative consumption quantities and consumption exceeding the available stock. | BR-09 |
| FR-09 | Update Available Stock | The system shall automatically update the available stock after recording chemical receipts or consumption. | BR-03, BR-04, BR-05 |
| FR-10 | Maintain Consumption Records | The system shall maintain a history of chemical consumption, including chemical identification, consumed quantity, unit, and transaction date. | BR-06 |
| FR-11 | View Consumption History | The system shall allow users to view historical chemical consumption records. | BR-06 |
| FR-12 | Delete Chemical | The system shall allow users to delete a chemical from the current inventory. | BR-01 |
| FR-13 | Export Inventory Report | The system shall allow users to generate an Excel report containing current chemical inventory information. | BR-08 |
| FR-14 | Export Consumption Report | The system shall allow users to generate an Excel report containing chemical consumption records. | BR-08 |

## 3. Input and Output Requirements

### Inputs
- Chemical name
- Opening stock quantity
- Chemical unit
- Chemical selection
- Received quantity
- Consumed quantity

### Outputs
- Chemical inventory list
- Chemical identification numbers
- Updated available stock
- Chemical consumption history
- Excel inventory report
- Excel consumption report

## 4. Business Rules and Validations

The system shall enforce the following rules:

1. Chemical names must not be blank.
2. Duplicate chemical names are not permitted.
3. Chemical identification numbers must be generated automatically.
4. Opening stock and received quantities must not be negative.
5. Consumption quantities must be greater than zero.
6. Consumption must not exceed the available stock, including any quantity received in the same transaction.
7. Available stock must be calculated by considering opening stock, received quantities, and consumed quantities.

## 5. Requirement Traceability

Each functional requirement is linked to one or more business requirements to ensure that the system functions support the identified business needs.

## 6. Implementation Status

The current application implements the core inventory management, validation, consumption tracking, reporting, and deletion functions described in this document.
