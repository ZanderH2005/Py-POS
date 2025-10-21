import os # Laat you toe om clear_screen funksie te gebruik
import time # Laat time.sleep funksie toe om 'n kort pouse te skep

# Huidige voorraad en pryse van items
INVENTORY = {
    "melk": 20.60,
    "brood": 12.20,
    "botter": 45.70,
    "dosyn eiers": 35.50 
}

def clear_screen(): # Funksie om die skerm skoon te maak
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_subtotal(cart): # Berken die subtotaal van items in die mandjie
    return sum(INVENTORY[item] * quantity for item, quantity in cart.items())

def calculate_tax(subtotal, tax_rate=0.15): # Bereken die belasting (BTW) op die subtotaal
    return subtotal * tax_rate

def calculate_total(subtotal, tax): # Bereken die finaale totaal 
    return subtotal + tax

def display_menu(): # Vertoon die beskikbaare items en hul pryse vir die gebruiker
    print("Beskikbare Items")
    print("---------------------")
    for item, price in INVENTORY.items(): 
        print(f"* {item.capitalize()}: R{price:.2f}")
    print("-----------------------")

def display_cart(cart): # Vertoon die items in die mandjie met hul hoeveelhied en pryse
    if not cart:
        print("Die mandjie is leeg.")
    else:
        print("--- Jou mandjie ---")
        for item, quantity in cart.items():
            price = INVENTORY[item]
            print(f"{item.capitalize()} (x{quantity}): R{price * quantity:.2f}")
        print("-----------------")

def process_payment(total): # Beheer die betalingsproses en bereken die kleingeld
    print(f"Die totaal is: R{total:.2f}")
    while True:
        try:
            amount_paid = float(input("Tik in u bedrag: R"))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Kleingeld: R{change:.2f}")
                print("Betaaling suksessvol!")
                return True
            else:
                print("Onvoldoenbaare bedrag. Tik asseblief 'n groter bedrag in.")
        except ValueError:
            print("Verkeerde toevoer. Gee asseblief 'n nommer.")

def main(): # Hooffunksie om die POS stelsel te bestuur
    cart = {}
    clear_screen()
    
    while True:
        print("\n--- Welkom by die POS Stelsel ---\n")
        display_menu()
        
        choice = input("\nTik die item naam om dit in u mandjie te sit (of 'betaal' om te betaal, 'stop' om POS te verlaat): ").lower()
        
        clear_screen() # Maak die skerm skoon na elke toevoer

        if choice == 'stop':
            print("Dankie om die POS stelsel te gebruik het!")
            break
        elif choice == 'betaal':
            if not cart:
                print("Die mandjie is leeg... Sit asseblief items in voor u betaal.")
                continue
            
            subtotal = calculate_subtotal(cart)
            tax = calculate_tax(subtotal)
            total = calculate_total(subtotal, tax)
            
            print("--- Rekening ---")
            display_cart(cart)
            print(f"Subtotal: R{subtotal:.2f}")
            print(f"Tax(15%):      R{tax:.2f}")
            print(f"Total:    R{total:.2f}")
            print("---------------")
            
            if process_payment(total):
                cart = {}  # Maak die mandjie skoon na 'n suksesvolle betaling
            input("\nDruk 'Enter' om terug te keer na die tuisblad...")
            clear_screen()
            continue
        
        # Kyk of die item in die voorraad is, indien nie, vra om item uit die lys te kies
        if choice in INVENTORY:
            try:
                quantity = int(input(f"Skakel die hoeveelheid vir {choice.capitalize()}: "))
                if quantity > 0:
                    cart[choice] = cart.get(choice, 0) + quantity
                    print(f"{quantity} x {choice.capitalize()} in mandjie geplaas.")
                else:
                    print("Hoeveelhied moet 'n posatiewe waarde wees.")
            except ValueError:
                print("Verkeerde toevoer. Gee asseblief 'n toelaatbare nommer.")
        else:
            print("Item nie beskikbaar nie. Kies asseblief van die lys.")
        
        time.sleep(1.5)  # Pause skerm vir 'n oomblik as jy jou item en hoeveelheid intik
        clear_screen()

if __name__ == "__main__": # Laat die POS stelsel hardloop
    main()
