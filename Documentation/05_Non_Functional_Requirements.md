# 05. Non-Functional Requirements

## 1. Purpose

This document defines the non-functional requirements (NFRs) of the Chemical Inventory Management System. These requirements describe the quality attributes, operational expectations, and performance characteristics of the system.

## 2. Non-Functional Requirements

| Requirement ID | Category | Non-Functional Requirement | Description |
|---|---|---|---|
| NFR-01 | Usability | User-Friendly Interface | The system should provide a simple and understandable menu-driven interface to help users perform inventory operations easily. |
| NFR-02 | Performance | Efficient Processing | The system should process common inventory operations, such as adding, searching, viewing, and recording consumption, within a reasonable time. |
| NFR-03 | Data Integrity | Accurate Stock Calculation | The system should maintain accurate stock balances by correctly accounting for opening stock, received quantities, and consumed quantities. |
| NFR-04 | Reliability | Consistent Data Storage | The system should save inventory and consumption records so that data remains available after the application is closed and restarted. |
| NFR-05 | Maintainability | Structured Code | The application should use a structured, modular design to make future updates, troubleshooting, and maintenance easier. |
| NFR-06 | Compatibility | Platform Compatibility | The application should run in a compatible Python environment with the required dependencies installed. |
| NFR-07 | Data Validation | Input Validation | The system should validate user inputs and provide understandable error messages for invalid entries. |
| NFR-08 | Reporting | Report Accessibility | The system should generate Excel reports that users can access for review and further analysis. |
| NFR-09 | Data Backup | Data Protection | Inventory and consumption CSV files should be backed up regularly to reduce the risk of data loss. |

## 3. Security Considerations

The current application is designed for basic inventory management and does not include:

- User authentication.
- Role-based access control.
- Data encryption.
- Audit trails for user activities.

These capabilities may be considered for future development if the system is deployed in a multi-user business environment.

## 4. Operational Considerations

- Users should enter accurate inventory and consumption information.
- Required Python libraries should be installed before running the application.
- Inventory and consumption data files should be maintained and backed up regularly.
- Excel reports should be reviewed to support inventory monitoring and decision-making.

## 5. Implementation Considerations

The current application provides a basic menu-driven interface, input validation, CSV-based data persistence, and Excel reporting.

Advanced security, automated backup, and measurable performance targets have not been implemented or formally tested. These can be addressed in future development.

## 6. Conclusion

The non-functional requirements establish the expected quality and operational characteristics of the Chemical Inventory Management System. They provide a foundation for evaluating the system beyond its core functional capabilities.
