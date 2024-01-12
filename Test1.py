import json

class SATResult:
    def __init__(self, name, address, city, country, pincode, sat_score):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.pincode = pincode
        self.sat_score = sat_score
        self.Result = "Pass" if sat_score > 30 else "Fail"

class SATSystem:
    def __init__(self):
        self.data = []

    def insert_data(self):
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        country = input("Enter Country: ")
        pincode = input("Enter Pincode: ")
        sat_score = int(input("Enter SAT Score: "))

        result = SATResult(name, address, city, country, pincode, sat_score)
        self.data.append(result)
        print("Data inserted successfully!")

    def view_all_data(self):
        for result in self.data:
            print(json.dumps(result.__dict__, indent=2)) #converts dictanory to json data and indent will do proper arrangments

    def get_rank(self, name):
        sorted_data = sorted(self.data, key=lambda x: x.sat_score, reverse=True)
        rank = [result.name for result in sorted_data].index(name) + 1
        print(f"{name}'s rank is {rank}")

    def update_score(self, name):
        for result in self.data:
            if result.name == name:
                new_score = int(input(f"Enter new SAT Score for {name}: "))
                result.sat_score = new_score
                result.passed = "Pass" if new_score > 30 else "Fail"
                print(f"SAT Score updated for {name}!")

    def delete_record(self, name):
        self.data = [result for result in self.data if result.name != name]
        print(f"{name}'s record deleted successfully!")

    def save_to_file(self):
        with open("sat_results.json", "w") as file:
            json.dump([result.__dict__ for result in self.data], file, indent=2)
        print("Data saved to 'sat_results.json' file.")

def main():
    sat_system = SATSystem()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save to file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sat_system.insert_data()
        elif choice == "2":
            sat_system.view_all_data()
        elif choice == "3":
            name = input("Enter name to get rank: ")
            sat_system.get_rank(name)
        elif choice == "4":
            name = input("Enter name to update score: ")
            sat_system.update_score(name)
        elif choice == "5":
            name = input("Enter name to delete record: ")
            sat_system.delete_record(name)
        elif choice == "6":
            sat_system.save_to_file()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
