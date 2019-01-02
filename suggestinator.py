def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Need more that 3 chars")
    return product_idea + "inator"