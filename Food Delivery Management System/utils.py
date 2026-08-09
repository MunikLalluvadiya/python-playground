
DELIVERY_CHARGE = 40.0
GST_RATE = 0.05  # 5%


def calculate_bill(subtotal):
    
    delivery_charge = DELIVERY_CHARGE
    gst_amount = subtotal * GST_RATE
    grand_total = subtotal + delivery_charge + gst_amount
    return delivery_charge, gst_amount, grand_total