# Petrol Purchase System

A Python object-oriented program that simulates a petrol purchase system with comprehensive class implementation and financial calculations.

## Program Description
This program implements a complete petrol purchase management system using Object-Oriented Programming (OOP) principles:
- Petrol purchase tracking with all essential attributes
- Automatic cost calculations and discount applications
- Interactive user input for purchase details
- Professional receipt generation with formatted output

## Features
- Complete class implementation with accessor and mutator methods
- Real-time cost calculations (total cost, discounts, final price)
- Interactive purchase modification system
- Professional string representation (`__str__` and `__repr__` methods)
- Formatted financial output with proper currency formatting
- Dynamic purchase updates with additional quantities

## Files
- `Toh Qi Hao_lab_5.py` - Main Python program implementing the PetrolPurchase class system
- 
## Technologies Used
- Python 3
- Object-Oriented Programming
- Accessor/Mutator methods
- Special methods (__str__, __repr__)
- Financial calculations
- User input handling

## Author
Toh Qi Hao

## How to Run
```bash
python "Toh Qi Hao_lab_5.py"

Enter the station: Shell Station
Enter quantities in litres: 20
Enter type of petrol: Premium 95
Enter price of petrol: 2.50
Enter discount: 10

Summary of purchase
    Station: Shell Station
    Quantities: 20.00
    Type of petrol: Premium 95
    Unit price: 2.50
    Discount: 10.00%
    Total cost: 50.00
    Total discount: (10.00%): $5.00
    Final payment: $45.00

Additional quantity: 5

Final Summary of purchase
    Station: Shell Station
    Quantities: 25.00
    Type of petrol: Premium 95
    Unit price: 2.50
    Discount: 10.00%
    Total cost: 62.50
    Total discount: (10.00%): $6.25
    Final payment: $56.25

The object was constructed according to:
PetrolPurchase("Shell Station", 25.0, "Premium 95", 2.5, 10.0)
