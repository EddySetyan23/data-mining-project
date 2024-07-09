from collections import Counter
from itertools import combinations

def apriori_frequent_pairs(transactions, min_support):
    # Count individual items
    item_counts = Counter(item for transaction in transactions for item in transaction)
    
    # Filter items based on min_support
    frequent_items = {item for item, count in item_counts.items() if count >= min_support}
    
    # Find and count pairs
    pair_counts = Counter()
    for transaction in transactions:
        frequent_transaction = [item for item in transaction if item in frequent_items]
        for pair in combinations(frequent_transaction, 2):
            pair_counts[pair] += 1
            
    # Filter pairs based on min_support
    frequent_pairs = {pair for pair, count in pair_counts.items() if count >= min_support}
    
    return frequent_pairs

# Load transactions from the dataset
with open("retail.dat.txt", "r") as f:
    transactions = [line.strip().split() for line in f.readlines()]

# Finding frequent pairs with a sample min_support (you can change this value)
frequent_pairs = apriori_frequent_pairs(transactions, min_support=100)

print(frequent_pairs)
