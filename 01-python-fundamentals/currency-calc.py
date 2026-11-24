print("Welcome to the Currency Calculator!")
try:
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency you want to convert from (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, GBP): ").upper()
    usd_to_ngn = 1500
    gbp_to_ngn = 2000
    eur_to_ngn = 1600
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    else:    
        if from_currency == "USD" and to_currency == "NGN":
            converted_amount = amount * usd_to_ngn
            print(f"{amount:,.2f} {from_currency} = {converted_amount} {to_currency}")
        elif from_currency == "GBP" and to_currency == "NGN":
            converted_amount = amount * gbp_to_ngn
            print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
        elif from_currency == "EUR" and to_currency == "NGN":
            converted_amount = amount * eur_to_ngn
            print(f"{amount:,.2f} {from_currency} = {converted_amount} {to_currency}")
        elif from_currency == "NGN" and to_currency == "USD":
            converted_amount = amount / usd_to_ngn
            print(f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")
        elif from_currency == "NGN" and to_currency == "GBP":
            converted_amount = amount / gbp_to_ngn
            print(f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")
        elif from_currency == "NGN" and to_currency == "EUR":
            converted_amount = amount / eur_to_ngn
            print(f"{amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")
        else:
         print("Invalid currency conversion. Please try again.")
except ValueError:
    print("Invalid input. Please enter a number.")