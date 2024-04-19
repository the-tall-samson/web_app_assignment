import os
import requests


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    print("Main Menu")
    print("1. Login")
    print("2. Issue API call w/o login (simulate anonymous user)")
    print("3. Exit")


def api_menu():
    print("API Menu")
    print("1. Get Product")
    print("2. Get Products")
    print("3. Add Product")
    print("4. Logout")


def unauth_api_menu():
    print("Unauthorized API Menu")
    print("1. Get Product")
    print("2. Get Products")
    print("3. Add Product")
    print("4. Main Menu")


def login(username, password):
    url = 'http://localhost:5000/login'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()['token']
    else:
        return None


def get_product(product_id, token):
    url = f'http://localhost:5000/get-product/{product_id}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response


def get_products(token):
    url = 'http://localhost:5000/get-products'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response


def add_product(name, price, token):
    url = 'http://localhost:5000/add-product'
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {'name': name, 'price': price}
    response = requests.post(url, json=data, headers=headers)
    return response


def handle_choice(choice):
    if choice == '1':
        clear_screen()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        token = login(username, password)
        if token:
            print("\nLogin successful!")
            input("\nPress Enter to continue...")
            clear_screen()
            api_menu()
            choice = input("\nEnter your choice: ")
            handle_api_choice(choice, token)
        else:
            print("\nLogin failed. Invalid username or password.")
            input("\nPress Enter to return to main menu...")
    elif choice == '2':
        clear_screen()
        unauth_api_menu()
        sub_choice = input("\nEnter your choice: ")
        handle_unauthorized_api(sub_choice)
    elif choice == '3':
        clear_screen()
        print("Exiting...")
        exit()
    else:
        clear_screen()
        print("Invalid choice")


def handle_unauthorized_api(choice):
    token = None
    if choice == '1':
        clear_screen()
        product_id = input("Enter the product ID: ")
        response = get_product(product_id, token)
        if response.status_code != 200:
            print("Failed to get product details. Error:", response.status_code)
        else:
            print('API call should not be allowed, contact developers.')
        input("\nPress Enter to return to Unauthorized API menu...")
        clear_screen()
        unauth_api_menu()
        choice = input("\nEnter your choice: ")
        handle_unauthorized_api(choice)
    elif choice == '2':
        clear_screen()
        response = get_products(token)
        if response.status_code != 200:
            print("Failed to get product list. Error:", response.status_code)
        else:
            print('API call should not be allowed, contact developers.')
        input("\nPress Enter to return to Unauthorized API menu...")
        clear_screen()
        unauth_api_menu()
        choice = input("\nEnter your choice: ")
        handle_unauthorized_api(choice)
    elif choice == '3':
        clear_screen()
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        response = add_product(name, price, token)
        if response.status_code != 201:
            print("Failed to add product. Error:", response.status_code)
        else:
            print('API call should not be allowed, contact developers.')
        input("\nPress Enter to return to Unauthorized API menu...")
        clear_screen()
        unauth_api_menu()
        choice = input("\nEnter your choice: ")
        handle_unauthorized_api(choice)
    elif choice == '4':
        clear_screen()
        print("Going back to Main Menu...")
        input("\nPress Enter to return to main menu...")
        clear_screen()
        main_menu()
        choice = input("\nEnter your choice: ")
        handle_choice(choice)
    else:
        clear_screen()
        print("Invalid choice")


def handle_api_choice(choice, token):
    if choice == '1':
        clear_screen()
        product_id = input("Enter the product ID: ")
        response = get_product(product_id, token)
        content_type = response.headers.get('Content-Type', '')
        if response.status_code == 200:
            clear_screen()
            product = response.json()
            print("Product details:")
            print("-" * 20)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print("-" * 20)
            print("\nRaw response details:")
            print(f'\nContent-Type: {content_type}')
            print(f"\nResponse: {response.text}")
        else:
            print("Failed to get product details. Error:", response.status_code)
        input("\nPress Enter to return to API menu...")
        clear_screen()
        api_menu()
        choice = input("\nEnter your choice: ")
        handle_api_choice(choice, token)
    elif choice == '2':
        clear_screen()
        response = get_products(token)
        if response.status_code == 200:
            products = response.json()
            print("Product list:")
            print("-" * 20)
            for product in products:
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: {product['price']}")
                print("-" * 20)
        else:
            print("Failed to get products. Error:", response.status_code)
        input("\nPress Enter to return to API menu...")
        clear_screen()
        api_menu()
        choice = input("\nEnter your choice: ")
        handle_api_choice(choice, token)
    elif choice == '3':
        clear_screen()
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        response = add_product(name, price, token)
        if response.status_code == 201:
            product = response.json()['product']
            print("\nProduct added successfully:")
            print("-" * 20)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print("-" * 20)
        else:
            print("\nFailed to add product. Error:", response.status_code)
        input("\nPress Enter to return to API menu...")
        clear_screen()
        api_menu()
        choice = input("\nEnter your choice: ")
        handle_api_choice(choice, token)
    elif choice == '4':
        clear_screen()
        print("Logging out...")
        token = None
        input("\nPress Enter to return to main menu...")
        clear_screen()
        main_menu()
        choice = input("\nEnter your choice: ")
        handle_choice(choice)
    else:
        clear_screen()
        print("Invalid choice")


def main():
    while True:
        clear_screen()
        main_menu()
        choice = input("\nEnter your choice: ")
        handle_choice(choice)


if __name__ == "__main__":
    main()
