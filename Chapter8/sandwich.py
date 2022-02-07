def make_sandwhich(*ingredients):
    print(f"Making a sandwhich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwhich("bun", "toast", "bun")
make_sandwhich("bun", "russian dressing", "swiss cheese", "sauerkraut", "corned beef", "bun")
make_sandwhich("bun", "mayonaise", "egg, over-easy", "bacon", "cheddar cheese", "burger", "bun")