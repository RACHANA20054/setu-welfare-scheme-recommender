def check_eligibility(citizen, scheme):
    """
    Checks whether a citizen is eligible for a given scheme.
    Returns a tuple: (is_eligible: bool, reasons: list of str)
    """
    reasons = []
    eligible = True
    citizen_state = "Karnataka"  # Hardcoded for now - SETU currently only supports Karnataka citizens


    # --- Age check ---
    if scheme.min_age is not None:
        if citizen.age >= scheme.min_age:
            reasons.append(f"Age {citizen.age} meets minimum age {scheme.min_age}")
        else:
            reasons.append(f"Age {citizen.age} is below minimum age {scheme.min_age}")
            eligible = False

    if scheme.max_age is not None:
        if citizen.age <= scheme.max_age:
            reasons.append(f"Age {citizen.age} is within maximum age {scheme.max_age}")
        else:
            reasons.append(f"Age {citizen.age} exceeds maximum age {scheme.max_age}")
            eligible = False

    # --- Income check ---
    if scheme.max_income is not None:
        if citizen.income <= scheme.max_income:
            reasons.append(f"Income ₹{citizen.income:.0f} is within limit ₹{scheme.max_income:.0f}")
        else:
            reasons.append(f"Income ₹{citizen.income:.0f} exceeds limit ₹{scheme.max_income:.0f}")
            eligible = False

    # --- Occupation check ---
    if scheme.occupation is not None:
        if citizen.occupation.strip().lower() == scheme.occupation.strip().lower():
            reasons.append(f"Occupation '{citizen.occupation}' matches required '{scheme.occupation}'")
        else:
            reasons.append(f"Occupation '{citizen.occupation}' does not match required '{scheme.occupation}'")
            eligible = False

    # --- Gender check ---
    if scheme.gender is not None and scheme.gender.strip().lower() != "any":
        if citizen.gender.strip().lower() == scheme.gender.strip().lower():
            reasons.append(f"Gender '{citizen.gender}' matches requirement")
        else:
            reasons.append(f"Gender '{citizen.gender}' does not match required '{scheme.gender}'")
            eligible = False

    # --- Caste category check ---
    if scheme.caste_category is not None and scheme.caste_category.strip().lower() != "any":
        allowed_categories = [c.strip().lower() for c in scheme.caste_category.split("/")]
        if citizen.caste_category.strip().lower() in allowed_categories:
            reasons.append(f"Category '{citizen.caste_category}' is eligible under '{scheme.caste_category}'")
        else:
            reasons.append(f"Category '{citizen.caste_category}' does not match required '{scheme.caste_category}'")
            eligible = False
# --- State applicability check ---
    if scheme.state_applicability.strip().lower() != "all india":
        if citizen_state.strip().lower() != scheme.state_applicability.strip().lower():
            reasons.append(f"Not applicable in your state")
            eligible = False
# --- State applicability check ---
    if scheme.state_applicability.strip().lower() != "all india":
        if citizen_state.strip().lower() != scheme.state_applicability.strip().lower():
            reasons.append("This scheme is not applicable in your state")
            eligible = False

    return eligible, reasons

    return eligible, reasons