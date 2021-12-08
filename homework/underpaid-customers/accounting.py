melon_cost = 1.00

def print_pmt_status(payment_data_filename):
    """ Calc cost of Melons to see who underpaid"""
    pmt_data = open(payment_data_filename)

    for line in pmt_data:
        order = line.split('|')
        full_name = order[1]
        first_name = full_name.split(" ")[0]
        melons_qty = float(order[2])
        amt_paid = float(order[3])
        expected_price = melons_qty * melon_cost

        print(f"{full_name} paid ${amt_paid:.2f}, expected", f"${expected_price:.2f}")

        if expected_price > amt_paid:
            print(f"{first_name} has overpaid for their melons.")
        elif expected_price > amt_paid:
            print(f"{first_name} has underpaid for their melons.")

    pmt_data.close()

print_pmt_status("customer-orders.txt")