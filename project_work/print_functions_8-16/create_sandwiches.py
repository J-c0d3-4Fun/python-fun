def sandwiches(*sandwich):
    """list what you wnat on your sandwich and print what was ordered"""
    for order in sandwich:
        print(f" - {order}")
    print(f"Is ready for pick up!")