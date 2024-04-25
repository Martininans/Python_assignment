def main():
    print("Hello, Kindly Enter card details to verify:")
    card_number = input()
    digit_length = len(card_number)
    
    if is_valid_credit_card(card_number):
        card_type = get_credit_card_type(card_number)
        print("Credit card type:", card_type)
        print("Credit card Number:", card_number)
        print("Credit card Digits Length:", digit_length)
        print("Validity: Valid")
    else:
        print("Validity: Invalid")

def is_valid_credit_card(card_number):
    if len(card_number) < 13 or len(card_number) > 16:
        return False

    if card_number.startswith(("4", "5", "37", "6")):
        return True

    return False

def get_credit_card_type(card_number):
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith("5"):
        return "MasterCard"
    elif card_number.startswith("37"):
        return "American Express"
    elif card_number.startswith("6"):
        return "Discover"
    else:
        return "Unknown"

main()
