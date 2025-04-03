# Function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function and print the result
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or original price
if final_price == original_price:
    print(f"No discount applied. The final price is: ${final_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
