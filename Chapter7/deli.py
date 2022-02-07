sandwhich_orders = [ "Pistrami", "Reuben", "Bacon Lettuce & Tomato", "Peanut Butter & Jelly", "Chicken Backon Melt", "Pistrami", "Toast", "Tunafish", "Pistrami", "Reuben", "Steak"]
finished_sandwhiches = []

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("I made your", current_sandwhich.title(), "sandwhich")
    finished_sandwhiches.append(current_sandwhich)

print("Sandwiches that were made today include:")
for sandwhich in finished_sandwhiches:
    print(sandwhich.title())

print()
sandwhich_orders = [ "Pistrami", "Reuben", "Bacon Lettuce & Tomato", "Peanut Butter & Jelly", "Chicken Backon Melt", "Pistrami", "Toast", "Tunafish", "Pistrami", "Reuben", "Steak"]
finished_sandwhiches = []

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    if current_sandwhich != "Pistrami":
        print("I made your", current_sandwhich.title(), "sandwhich")
        finished_sandwhiches.append(current_sandwhich)
    else:
        print("I am sorry, we are out of pastrami!!!")

print("Sandwiches that were made today include:")
for sandwhich in finished_sandwhiches:
    print(sandwhich.title())
