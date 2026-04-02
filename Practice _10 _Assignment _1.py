import pandas as pd

df = pd.read_csv("books.csv")

while True:
    print("\n1.Display All Books")
    print("2.Books by Author")
    print("3.Books by Publisher")
    print("4.Cheapest & Costliest Book")
    print("5.Sort by Year")
    print("6.Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        print(df)

    elif ch == '2':
        author = input("Enter author name: ")
        print(df[df['author'] == author])

    elif ch == '3':
        pub = input("Enter publisher name: ")
        print(df[df['publisher'] == pub])

    elif ch == '4':
        print("Cheapest Book:")
        print(df[df['price'] == df['price'].min()][['title', 'price']])
        print("\nCostliest Book:")
        print(df[df['price'] == df['price'].max()][['title', 'price']])

    elif ch == '5':
        print(df.sort_values(by='year'))

    elif ch == '6':
        break

    else:
        print("Invalid choice")
