from matching_engine import check_eligibility

# A simple fake "citizen" using a basic object - just for testing
class FakeCitizen:
    age = 25
    income = 200000
    occupation = "Farmer"
    gender = "Male"
    caste_category = "General"

# A simple fake "scheme" mimicking PM-KISAN's rules
class FakeScheme:
    min_age = 18
    max_age = None
    max_income = None
    occupation = "Farmer"
    gender = "Any"
    caste_category = "Any"

citizen = FakeCitizen()
scheme = FakeScheme()

eligible, reasons = check_eligibility(citizen, scheme)

print("Eligible:", eligible)
for r in reasons:
    print(" -", r)