# 11. Portfolio Case Study – Chemical Inventory Management System

## 1. Project Overview

The Chemical Inventory Management System is a Python-based application developed to improve the management and monitoring of chemical inventory in an industrial environment.

The project demonstrates practical Business Analysis activities, including business problem identification, stakeholder analysis, requirements engineering, process documentation, gap analysis, and software testing.

The application was developed using Python and pandas, with CSV-based data storage and Excel reporting capabilities.

## 2. Business Problem

In industrial operations, effective chemical inventory management is essential for maintaining production continuity, controlling operational costs, and ensuring the availability of critical chemicals.

Manual inventory management or poorly structured recordkeeping can lead to:

- Inaccurate stock information.
- Difficulty tracking chemical consumption.
- Delayed identification of stock shortages.
- Inefficient retrieval of inventory records.
- Limited visibility of historical consumption.
- Increased risk of inventory discrepancies.

A structured inventory management solution was therefore identified as a practical way to address these challenges.

## 3. Project Objectives

The main objectives were to:

1. Develop a structured system for maintaining chemical inventory records.
2. Track chemical receipts and consumption.
3. Automatically calculate available stock.
4. Maintain historical consumption records.
5. Improve inventory information retrieval.
6. Generate inventory and consumption reports.
7. Apply validation controls to reduce data entry errors.

## 4. Stakeholder Analysis

The following business stakeholders were identified:

| Stakeholder | Interest / Responsibility |
|---|---|
| Storekeeper / Inventory Officer | Maintains chemical inventory and records transactions. |
| Production / Operations Officer | Requires accurate information about chemical availability and consumption. |
| Department Manager | Uses inventory information for operational planning and decision-making. |
| System Administrator / Developer | Maintains and improves the application. |

These represent intended business stakeholders. The current application does not implement separate user accounts or role-based permissions.

## 5. Business Analysis Activities

The following Business Analysis activities were performed:

### 5.1 Business Problem Identification

Identified common challenges associated with chemical inventory monitoring and consumption tracking.

### 5.2 Stakeholder Identification

Identified key stakeholders and documented their responsibilities and information needs.

### 5.3 Requirements Elicitation and Documentation

Developed business requirements, functional requirements, and non-functional requirements to define the expected system capabilities.

### 5.4 Business Process Analysis

Documented the chemical inventory management workflow and established business rules for stock transactions.

### 5.5 Use Case Analysis

Prepared use case documentation and a use case diagram to describe interactions between intended users and the application.

### 5.6 Gap Analysis

Compared current application capabilities with potential future business needs and identified improvement opportunities.

### 5.7 Testing and Validation

Prepared test cases and manually tested the core application functions to verify expected system behavior.

## 6. Proposed Solution

A menu-driven Chemical Inventory Management System was developed using Python.

The application provides the following features:

- Add new chemicals with automatically generated chemical IDs.
- View chemical inventory.
- Search chemicals by name.
- Record received and consumed quantities.
- Automatically update available stock.
- Maintain consumption history.
- Delete chemicals from current inventory.
- Generate Excel inventory reports.
- Generate Excel consumption reports.
- Validate user inputs and prevent invalid stock transactions.

## 7. Business Process Logic

The available stock is calculated using the following formula:

**Available Stock = Previous Available Stock + Received Quantity − Consumed Quantity**

The system validates each transaction to prevent consumption beyond the available stock.

## 8. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Application development |
| pandas | Inventory and transaction data management |
| CSV | Data storage |
| Excel | Inventory and consumption reporting |
| GitHub | Source code management and portfolio documentation |

## 9. Testing and Validation

Manual testing was performed to verify the major application functions.

Testing covered:

- Chemical registration.
- Duplicate and blank chemical validation.
- Chemical ID generation.
- Inventory viewing and searching.
- Chemical consumption recording.
- Stock calculation.
- Invalid transaction handling.
- Consumption history.
- Chemical deletion.
- Excel report generation.

The documented test scenarios were successfully completed.

## 10. Project Outcomes

The project resulted in:

- A functional chemical inventory management application.
- Structured inventory and consumption records.
- Automated chemical ID generation.
- Improved stock visibility through automatic stock calculations.
- Validation controls to reduce inventory transaction errors.
- Excel reporting for inventory monitoring.
- Business Analysis documentation supporting the development process.

## 11. Limitations

The current application has some limitations:

- CSV-based data storage.
- No user authentication or role-based access control.
- No automated low-stock notifications.
- No batch or expiry-date tracking.
- No supplier or purchase order management.
- No automated testing framework.
- No advanced analytical dashboard.

## 12. Future Recommendations

Future development may include:

1. Database integration using SQLite or PostgreSQL.
2. User authentication and role-based access control.
3. Low-stock alerts and replenishment notifications.
4. Batch and expiry-date tracking.
5. Supplier and procurement management.
6. Analytical dashboards for consumption trends.
7. Automated backup and audit trail functionality.

## 13. Conclusion

The Chemical Inventory Management System demonstrates how Business Analysis techniques can be applied to identify operational problems, define business needs, document system requirements, and develop a practical software solution.

The project combines industrial chemical inventory management knowledge with Python programming and structured Business Analysis documentation.

It provides a foundation for further development into a more comprehensive inventory management solution.
