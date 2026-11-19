import pandas as pd
import os

#### Menu display and option selection
print("=============================== Chemical Inventory Management System ===============================")

menu = {
    1: "Add Chemical",
    2: "View Chemicals",
    3: "Search Chemical",
    4: "Record Chemical Consumption",
    5: "View Consumption",
    6: "Delete Chemical",
    7: "Exit"
}

class ChemicalTransaction:

    def __init__(self, chemical_name, current_stock, received_amount, consumed_amount):

        self.chemical_name = chemical_name
        self.current_stock = current_stock
        self.received_amount = received_amount
        self.consumed_amount = consumed_amount
        self.date_of_record = pd.Timestamp.now()



    @property # creates the getter. It retrieves the value.
    def current_stock(self): 
        return self._current_stock

    @current_stock.setter # creates the setter. It controls and stores the assigned value.
    def current_stock(self, value):
        if value < 0:
            raise ValueError("Current stock cannot be negative.")

        self._current_stock = value

    @property
    def received_amount(self):
        return self._received_amount

    @received_amount.setter
    def received_amount(self, value):
        if value < 0:
            raise ValueError("Received amount cannot be negative.")

        self._received_amount = value

    @property
    def consumed_amount(self):
        return self._consumed_amount

    @consumed_amount.setter
    def consumed_amount(self, value):
        if value < 0:
            raise ValueError("Consumed amount cannot be negative.")

        if value > self.current_stock + self.received_amount:
            raise ValueError("Consumption cannot exceed available stock.")

        self._consumed_amount = value

    @property
    def available_stock(self):
        return (self.current_stock + self.received_amount - self.consumed_amount)

    def to_dict(self):
        return {
            "Consumed Chemicals Name": self.chemical_name,
            "Available Stock": self.available_stock,
            "Received Amount": self.received_amount,
            "Consumed Amount": self.consumed_amount,
            "Date of Record": self.date_of_record
        }

    def __eq__(self, other):
        if not isinstance(other, ChemicalTransaction):
            return NotImplemented

        return (
            self.chemical_name == other.chemical_name
            and self.current_stock == other.current_stock
            and self.received_amount == other.received_amount
            and self.consumed_amount == other.consumed_amount
        )

class ChemicalInventory:

    @staticmethod
    def normalize_name(name):
        return name.strip().lower()

    @staticmethod
    def validate_quantity(quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    def __init__(self, filename="chemicals_inventory.csv"):

        self.file_name = filename
        self.file_name_consumption = "consumption_records.csv"
        self.excel_file = "chemicals_inventory.xlsx"


        self.columns_chem = [
            "Chemicals Name",
            "Chemicals ID",
            "Available Stock",
            "Unit",
            "Date of Entry"
        ]

        self.columns_consumption = [
            "Consumed Chemicals Name",
            "Available Stock",
            "Received Amount",
            "Consumed Amount",
            "Date of Record"
        ]

        # Load existing records if the file exists
        if os.path.exists(self.file_name):
            self.chem_df = pd.read_csv(self.file_name)
        else:
            self.chem_df = pd.DataFrame(columns=self.columns_chem)

        if os.path.exists(self.file_name_consumption):
            self.consumption_df = pd.read_csv(self.file_name_consumption)
        else:
            self.consumption_df = pd.DataFrame(columns=self.columns_consumption)

        # Generate the next chemical ID
        if not self.chem_df.empty:
            self.chemicals_id = (
                self.chem_df["Chemicals ID"]
                .str.replace("CH-", "", regex=False)
                .astype(int)
                .max() + 1
                # regex = False, Treat "CH-" as normal text, not as a regular expression.
                # astype(int), Convert the extracted string to an integer for numerical comparison.
            )
        else:
            self.chemicals_id = 1

    @classmethod
    def create_custom_inventory(cls, filename):
        return cls(filename)

    def enter_opening_stock(self):

        while True:

            try:
                opening_stock = float(input("Enter opening stock: "))

                self.validate_quantity(opening_stock)

            except ValueError as e:
                print(f"Error: {e}")

            else:
                print(f"Opening stock accepted: {opening_stock}")
                return opening_stock

    def add_chemical(self):

        chemicals_data = {
            "Chemicals Name": [],
            "Chemicals ID": [],
            "Available Stock": [],
            "Unit": [],
            "Date of Entry": []
        }

        while True:

            added_chemical = input("Enter chemical name: ")
            added_chemical_norm = self.normalize_name(added_chemical)

            if not added_chemical_norm:
                print("Chemical name cannot be empty.")
                continue

            existing_chemicals = (
                self.chem_df["Chemicals Name"].apply(self.normalize_name).tolist()
                    + [self.normalize_name(name) for name in chemicals_data["Chemicals Name"]]
            )

            if added_chemical_norm not in existing_chemicals:

                opening_stock = self.enter_opening_stock()

                available_stock = opening_stock  

                valid_units = ["grams", "kg", "litres", "bags"]

                while True:
                    unit = input("Enter unit (grams, kg, litres, bags): ").lower().strip()

                    if unit in valid_units:
                        break
                    else:
                        print("Invalid unit! Please enter a valid unit.")
            
                chemicals_data["Chemicals Name"].append(added_chemical.strip().title())
                chemicals_data["Chemicals ID"].append(f"CH-{self.chemicals_id:03d}")
                chemicals_data["Available Stock"].append(available_stock)
                chemicals_data["Unit"].append(unit)
                chemicals_data["Date of Entry"].append(pd.Timestamp.now())

                self.chemicals_id += 1

            else:
                print("This chemical already exists! \n" \
                "Please enter new chemical name.")
                continue

            another = input("Do you want to add another chemical? (yes/no): ")

            if another.lower().strip() != "yes":
                break

        # Convert newly entered records into a DataFrame
        new_df = pd.DataFrame(chemicals_data)

        # Combine old and new records
        self.chem_df = pd.concat([self.chem_df, new_df], ignore_index=True)

        # Save all records into CSV
        self.chem_df.to_csv(self.file_name, index=False)

        if chemicals_data["Chemicals Name"]:
            print("\nChemical added successfully!")

    def view_chemicals(self):

        if self.chem_df.empty:
            print("No chemicals found in the inventory.")
        else:
            print(self.chem_df.to_string(index=False))

            export = input("Do you want to export the inventory to Excel? (yes/no): ")

            if export.lower().strip() == "yes":
                self.chem_df.to_excel(self.excel_file, index=False)
                print("Excel file generated successfully!")

    def search_chemicals(self):

        search_chem = input("Enter the name of the chemical to search : ")
        search_chem_norm = self.normalize_name(search_chem)  # Remove leading/trailing whitespace

        if not search_chem_norm:
            print("Chemical name cannot be empty.")
            return

        chemical_names = self.chem_df["Chemicals Name"].apply(self.normalize_name)

        if not (chemical_names == search_chem_norm).any(): 
            # explicitly checks whether at least one row matches the search term.
            print(f"Chemical '{search_chem}' not found in the inventory.")
        else:
            matched_chemicals = self.chem_df[chemical_names == search_chem_norm]
            print(matched_chemicals.to_string(index=False))

    def validate_consumption_input(self):

        while True:
        
                    try:
                        received_amount = float(input("Enter the amount received: "))
                        self.validate_quantity(received_amount)
                                            
                        consumption_amount = float(input("Enter the amount consumed: "))
                        self.validate_quantity(consumption_amount)
        
                    except ValueError as e:
                        print(f"Error: {e}")
        
                    else:
                        print(f"Received amount accepted: {received_amount}")
                        print(f"Consumed amount accepted: {consumption_amount}")
                        return received_amount, consumption_amount
         
    def record_consumption(self):
      
        if self.chem_df.empty:
            print("No chemicals available in the inventory.")
            return
        
        while True:
            
            consume_chem = input("Enter the name of the chemical to record consumption: ")
            consume_chem_norm = self.normalize_name(consume_chem)  

            if not consume_chem_norm:
                print("Chemical name cannot be empty.")
                continue

            chemicals_name = self.chem_df["Chemicals Name"].apply(self.normalize_name)
     

            if not (chemicals_name == consume_chem_norm).any():
                print(f"Chemical '{consume_chem}' not found in the inventory.")
            
            else:
                
                actual_chemical_name = self.chem_df.loc[
                                    chemicals_name == consume_chem_norm, "Chemicals Name"].values[0]
                
                current_stock = self.chem_df.loc[chemicals_name == consume_chem_norm, "Available Stock"].values[0]

                while True:

                    received_amount, consumption_amount = self.validate_consumption_input()

                    if consumption_amount > received_amount + current_stock:
                        print(
                            f"Insufficient stock! Available stock after receipt: "
                            f"{current_stock + received_amount}"
                        )
                        continue

                    else:
                        break
                
                transaction = ChemicalTransaction(actual_chemical_name, current_stock, received_amount, consumption_amount)

                transaction_record = transaction.to_dict()

                new_record = pd.DataFrame([transaction_record])

                self.consumption_df = pd.concat([self.consumption_df, new_record], ignore_index=True)

                self.chem_df.loc[chemicals_name == consume_chem_norm, "Available Stock"] = transaction.available_stock

                self.chem_df.to_csv(self.file_name, index=False)

                self.consumption_df.to_csv(self.file_name_consumption, index=False)
                    
                print(f"Consumption input for '{consume_chem}' successful.")

            another = input("Do you want to record consumption for another chemical? (yes/no): ")
            
            if another.lower().strip() != "yes":
                break
             
        print("\nConsumption records saved successfully!")

    def view_consumption(self):

        if self.consumption_df.empty:
            print("No consumption records available.")
            return
        
        while True:

            search_view = input("Enter the name of the chemicals to view consumption record: ")
            search_view_norm = self.normalize_name(search_view)

            if not search_view_norm:
                print("Chemical name cannot be empty.")
                continue

            consump_view = self.consumption_df[
                self.consumption_df["Consumed Chemicals Name"].apply(self.normalize_name) == search_view_norm]
            
            if consump_view.empty:
                print(f"Consumption records for '{search_view}' not found.")
                    
            else:

                total_received = consump_view["Received Amount"].sum()
                total_consumed = consump_view["Consumed Amount"].sum()

                total_row = {"Consumed Chemicals Name": "TOTAL",
                            "Received Amount": total_received,
                            "Consumed Amount": total_consumed}

                consump_view = pd.concat([consump_view, pd.DataFrame([total_row])], ignore_index=True)

                print("\nConsumption History:")
                print(consump_view)

                consump_view.to_excel(f"{search_view_norm} consumption history.xlsx", index=False)
                print("Excel file generated successfully!")

                    
            another = input("Do you want to view consumption record of another chemical? (yes/no): ")
            
            if another.lower().strip() != "yes":
                break

    def delete_chemicals(self):

        delete_chem = input("Enter the name of the chemical to delete: ")
        delete_chem_norm = self.normalize_name(delete_chem) 

        if not delete_chem_norm:
            print("Chemical name cannot be empty.")
            return

        chemicals_name = self.chem_df["Chemicals Name"].apply(self.normalize_name)
        chemical_mask = chemicals_name == delete_chem_norm

        if not chemical_mask.any():
            print(f"Chemical '{delete_chem}' not found in the inventory.")
            
        
        else:
            self.chem_df = self.chem_df[self.chem_df["Chemicals Name"].apply(self.normalize_name) != delete_chem_norm]
            self.chem_df.to_csv(self.file_name, index=False)
            print(f"Chemical '{delete_chem}' deleted successfully from the inventory.")

def main_menu():

    ch_inventory = ChemicalInventory()

    while True:
        print("\nPlease select an option from the menu below:")
        print("===============================================================================================")
        for key, value in menu.items():
            print(f"{key}. {value}")

        print("\n")

        try:
            option = int(input("Enter your option (1-7): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:

            ch_inventory.add_chemical()

        elif option == 2:

            ch_inventory.view_chemicals()

        elif option == 3:

            ch_inventory.search_chemicals()

        elif option == 4:

            ch_inventory.record_consumption()

        elif option == 5:

            ch_inventory.view_consumption()

        elif option == 6:
        
            ch_inventory.delete_chemicals()
        
        elif option == 7:
        
            print("Exiting the program.")
            break
        
        else:
        
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main_menu()



