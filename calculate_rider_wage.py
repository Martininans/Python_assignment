def main():
    successful_deliveries = 25
    rider_wage = calculate_rider_wage(successful_deliveries)
    print("Rider's wage for the day: N{}".format(rider_wage))

def calculate_rider_wage(successful_deliveries):
    base_pay = 5000
    amount_per_parcel = 0

    if successful_deliveries < 50:
        amount_per_parcel = 160
    elif 50 <= successful_deliveries < 60:
        amount_per_parcel = 200
    elif 60 <= successful_deliveries < 70:
        amount_per_parcel = 250
    elif successful_deliveries >= 70:
        amount_per_parcel = 500

    rider_wage = base_pay + (successful_deliveries * amount_per_parcel)
    return rider_wage

main()
