from datasets import load_dataset

multi_lexsum = load_dataset("allenai/multi_lexsum", name="v20230518", trust_remote_code=True)
# Download multi_lexsum locally and load it as a Dataset object 

example = multi_lexsum["validation"][0] # The first instance of the dev set 
example["sources"] # A list of source document text for the case

# for sum_len in ["long", "short", "tiny"]:
#     print(example["summary/" + sum_len]) # Summaries of three lengths

#     print(example['case_metadata']) # The corresponding metadata for a case in a dict 


# # Load the dataset
# dataset = load_dataset("allenai/multi_lexsum")

train_data = multi_lexsum["train"]

train_data = multi_lexsum["train"].remove_columns(["sources", 'sources_metadata'])

# print(len(multi_lexsum['validation'])+len(multi_lexsum['test'])+len(train_data))




# print(multi_lexsum.column_names)
print(train_data.column_names)  # Displays the column names
# print(len(train_data))
print(train_data[15])           # Displays the nth record

from collections import Counter

# Initialize a Counter for case_type values
case_type_counter = Counter()

# Iterate through the dataset
for example in multi_lexsum["train"]:
    # Access case_metadata and case_type if they exist
    case_metadata = example.get("case_metadata", {})
    case_type = case_metadata.get("case_type")
    
    # Count case_type occurrences
    if case_type:
        case_type_counter[case_type] += 1

# Display the unique case types and their counts
print("\nUnique case types:")
for case_type, count in case_type_counter.items():
    print(f"{case_type}: {count}")

# Initialize a Counter for causes_of_action values
causes_of_action_counter = Counter()

# Iterate through the dataset
for example in multi_lexsum["train"]:
    # Access case_metadata and causes_of_action if they exist
    case_metadata = example.get("case_metadata", {})
    causes_of_action = case_metadata.get("causes_of_action", [])
    
    # Count causes_of_action occurrences
    causes_of_action_counter.update(causes_of_action)

# Display the unique causes_of_action and their counts
print("\nUnique causes_of_action:")
for causes_of_action, count in causes_of_action_counter.items():
    print(f"{causes_of_action}: {count}")

    # Initialize a Counter for constitutional_clauses values
constitutional_clauses_counter = Counter()

# Iterate through the dataset
for example in multi_lexsum["train"]:
    # Access case_metadata and constitutional_clauses if they exist
    case_metadata = example.get("case_metadata", {})
    constitutional_clauses = case_metadata.get("constitutional_clauses", [])
    
    # Count constitutional_clauses occurrences
    constitutional_clauses_counter.update(constitutional_clauses)

# Display the unique constitutional_clauses and their counts
print("\nUnique constitutional_clauses:")
for constitutional_clause, count in constitutional_clauses_counter.items():
    print(f"{constitutional_clause}: {count}")