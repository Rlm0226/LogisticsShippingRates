# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shippping Cost: {shipping_cost} USD")
