# code to be executed

import itertools
import time
from collections import defaultdict

# Sample dataset (small transactions for testing)
# as computataion takes too long for Online Retail dataset
transactions = [
    ["Milk", "Bread", "Butter"],
    ["Milk", "Diapers", "Beer", "Bread"],
    ["Milk", "Diapers", "Beer", "Cola"],
    ["Bread", "Butter", "Diapers"],
    ["Milk", "Bread", "Butter", "Diapers"],
    ["Cola", "Diapers", "Beer"],
    ["Milk", "Bread", "Diapers", "Butter"],
    ["Beer", "Bread"],
    ["Milk", "Bread", "Butter"],
    ["Milk", "Diapers", "Beer", "Cola"],
]

# Minimum support threshold
min_support = 2


# Function to generate frequent 1-itemsets
def get_frequent_1_itemsets(transactions, min_support):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1
    return {
        frozenset([item]): count
        for item, count in item_counts.items()
        if count >= min_support
    }


# Function to generate candidate itemsets
def generate_candidates(frequent_itemsets, k):
    return {
        frozenset(a | b)
        for a in frequent_itemsets
        for b in frequent_itemsets
        if len(a | b) == k
    }


# Function to calculate support of itemsets
def get_frequent_itemsets(transactions, candidates, min_support):
    itemset_counts = defaultdict(int)
    for transaction in transactions:
        for candidate in candidates:
            if candidate.issubset(transaction):
                itemset_counts[candidate] += 1
    return {
        itemset: count
        for itemset, count in itemset_counts.items()
        if count >= min_support
    }


# Basic Apriori Algorithm
def apriori_basic(transactions, min_support):
    start_time = time.time()
    frequent_itemsets = get_frequent_1_itemsets(transactions, min_support)
    all_frequent_itemsets = frequent_itemsets.copy()

    k = 2
    while frequent_itemsets:
        candidates = generate_candidates(frequent_itemsets, k)
        frequent_itemsets = get_frequent_itemsets(transactions, candidates, min_support)
        all_frequent_itemsets.update(frequent_itemsets)
        k += 1

    return all_frequent_itemsets, time.time() - start_time


# Apriori with Transaction Reduction
def apriori_transaction_reduction(transactions, min_support):
    start_time = time.time()
    frequent_itemsets = get_frequent_1_itemsets(transactions, min_support)
    all_frequent_itemsets = frequent_itemsets.copy()

    k = 2
    while frequent_itemsets:
        candidates = generate_candidates(frequent_itemsets, k)
        reduced_transactions = [
            t
            for t in transactions
            if any(itemset.issubset(t) for itemset in frequent_itemsets)
        ]
        frequent_itemsets = get_frequent_itemsets(
            reduced_transactions, candidates, min_support
        )
        all_frequent_itemsets.update(frequent_itemsets)
        k += 1

    return all_frequent_itemsets, time.time() - start_time


# Apriori with Hash-Based Candidate Generation
def apriori_hash_based(transactions, min_support):
    start_time = time.time()
    frequent_itemsets = get_frequent_1_itemsets(transactions, min_support)
    all_frequent_itemsets = frequent_itemsets.copy()

    k = 2
    while frequent_itemsets:
        hash_table = defaultdict(int)
        candidate_itemsets = set()

        for transaction in transactions:
            for itemset in itertools.combinations(transaction, k):
                hash_table[itemset] += 1

        for itemset, count in hash_table.items():
            if count >= min_support:
                candidate_itemsets.add(frozenset(itemset))

        frequent_itemsets = get_frequent_itemsets(
            transactions, candidate_itemsets, min_support
        )
        all_frequent_itemsets.update(frequent_itemsets)
        k += 1

    return all_frequent_itemsets, time.time() - start_time


# Running all three algorithms
basic_result, basic_time = apriori_basic(transactions, min_support)
tr_result, tr_time = apriori_transaction_reduction(transactions, min_support)
hash_result, hash_time = apriori_hash_based(transactions, min_support)

# Calculate accuracy comparison
accuracy_tr = len(tr_result) / len(basic_result) * 100 if len(basic_result) > 0 else 0
accuracy_hash = (
    len(hash_result) / len(basic_result) * 100 if len(basic_result) > 0 else 0
)

# Print final results
print("\nComparison of Apriori Algorithms:")
print(f"Basic Apriori Execution Time: {basic_time:.6f} seconds")
print(f"Transaction Reduction Execution Time: {tr_time:.6f} seconds")
print(f"Hash-Based Execution Time: {hash_time:.6f} seconds")
print(f"Transaction Reduction Accuracy: {accuracy_tr:.2f}%")
print(f"Hash-Based Candidate Generation Accuracy: {accuracy_hash:.2f}%")


# Comparison of Apriori Algorithms:
# Basic Apriori Execution Time: 0.000278 seconds
# Transaction Reduction Execution Time: 0.000326 seconds
# Hash-Based Execution Time: 0.000198 seconds
# Transaction Reduction Accuracy: 100.00%
# Hash-Based Candidate Generation Accuracy: 92.86%