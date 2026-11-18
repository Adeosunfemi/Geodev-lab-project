
import pandas as pd

# Load the ward information
wards = pd.read_csv("month-03/week-10/wards_table.csv")

# Load the ward population data
pop = pd.read_csv("data/raw/ward_population.csv")

# Display the first 5 records
print("Wards table:")
print(wards.head())

print("\nPopulation table:")
print(pop.head())



# First attempt: join without cleaning
first_try = wards.merge(
    pop,
    left_on="ward_name",
    right_on="ward",
    how="left"
)

matched = first_try["population_2024"].notna().sum()

print("\nFirst attempt:")
print("Matched:", matched, "of", len(wards))



# Function to clean ward names
def clean_name(name):
    return name.strip().upper().replace("-", " ")

# Clean both tables
wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

# Join using the cleaned ward names
joined = wards.merge(
    pop,
    on="join_key",
    how="left"
)

# Count successful matches
matched = joined["population_2024"].notna().sum()

print("\nAfter cleaning:")
print("Matched:", matched, "of", len(wards))

print(joined[["ward_name", "population_2024"]])
