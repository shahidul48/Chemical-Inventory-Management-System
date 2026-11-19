# 09. Test Case Documentation

## 1. Purpose

This document describes the test cases designed to verify the functionality, data validation, and accuracy of the Chemical Inventory Management System.

## 2. Testing Approach

The application was tested manually using different input scenarios to verify that its core functions operate as expected.

The testing covered:

- Chemical registration.
- Chemical identification number generation.
- Input validation.
- Inventory viewing and searching.
- Chemical consumption recording.
- Available stock calculation.
- Consumption history.
- Chemical deletion.
- Excel report generation.

## 3. Test Cases

| Test Case ID | Test Scenario | Test Steps / Input | Expected Result | Status |
|---|---|---|---|---|
| TC-01 | Add a new chemical | Enter a valid chemical name, opening stock, and unit. | Chemical is added successfully with a unique ID. | Passed |
| TC-02 | Add duplicate chemical | Enter a chemical name that already exists. | System rejects the duplicate entry. | Passed |
| TC-03 | Enter blank chemical name | Submit an empty chemical name. | System requests a valid chemical name. | Passed |
| TC-04 | Enter negative opening stock | Enter a negative opening stock quantity. | System rejects the invalid quantity. | Passed |
| TC-05 | View inventory | Select the View Inventory option. | Current inventory records are displayed. | Passed |
| TC-06 | Search chemical | Search using an existing chemical name. | Matching chemical information is displayed. | Passed |
| TC-07 | Record valid consumption | Enter a valid received quantity, if applicable, and consumed quantity. | Stock is updated and consumption is recorded. | Passed |
| TC-08 | Record excessive consumption | Enter a consumed quantity exceeding available stock. | System rejects the transaction. | Passed |
| TC-09 | Enter negative consumption | Enter a negative consumption quantity. | System rejects the invalid quantity. | Passed |
| TC-10 | View consumption history | Select the View Consumption option. | Historical consumption records are displayed. | Passed |
| TC-11 | Delete a chemical | Select an existing chemical for deletion. | Chemical is removed from current inventory. | Passed |
| TC-12 | Generate inventory report | Select the inventory Excel export option. | Inventory report is generated successfully. | Passed |
| TC-13 | Generate consumption report | Select the consumption Excel export option. | Consumption report is generated successfully. | Passed |

## 4. Test Results Summary

| Test Metric | Result |
|---|---|
| Total Test Cases | 13 |
| Passed | 13 |
| Failed | 0 |
| Testing Type | Manual Testing |

## 5. Testing Observations

The manual testing process verified the following:

- Chemical records can be added and retrieved.
- Duplicate and invalid chemical entries are rejected.
- Chemical IDs are generated automatically.
- Available stock is updated following valid transactions.
- Consumption exceeding available stock is prevented.
- Consumption history is maintained.
- Inventory and consumption reports can be generated in Excel format.

## 6. Limitations

- Testing was performed manually.
- Automated unit and integration testing have not been implemented.
- Performance and security testing have not been formally conducted.
- Test results represent the tested application version and scenarios.

## 7. Conclusion

The tested application successfully completed the documented test scenarios. The results indicate that the core inventory management functions and validation controls operate as expected under the tested conditions.
