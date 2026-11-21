def remove_duplicates(transactions):

    unique = []

    seen = set()

    for transaction in transactions:

        if transaction not in seen:

            unique.append(transaction)

            seen.add(transaction)

    return unique


transactions = [101, 102, 103, 101, 104, 102, 105]

result = remove_duplicates(transactions)

print("Unique transactions:", result)