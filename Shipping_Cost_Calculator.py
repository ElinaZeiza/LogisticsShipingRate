# Shipping Cost Calculator

## Input package weight and shipping rate
wight = float(input("Enter the package weight in kilograms:"))
rate = float(input("Enter the shipping rate per kilogram:"))

## Calculate shaipping cost
shipping_cost = weight * rate

##Display the result
print(f"Shipping Cost: {shipping_cost} USD")
