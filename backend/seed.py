from database import Base, engine, SessionLocal
from models import Scheme

# Step A: Create all tables defined in our models (based on Base)
Base.metadata.create_all(bind=engine)

# Step B: Open a session (our workspace to talk to the database)
db = SessionLocal()

# Step C: Define all 28 schemes as a list of Scheme objects
schemes = [
    Scheme(name="PM-KISAN", description="Income support for farmer families.",
           category="Agriculture", level="Central", min_age=18, max_age=None,
           max_income=None, occupation="Farmer", gender="Any", caste_category="Any",
           state_applicability="All India", benefits="₹6,000/year direct transfer",
           official_link="https://pmkisan.gov.in/"),

    Scheme(name="Ayushman Bharat (PM-JAY)", description="Health insurance cover for economically vulnerable families.",
           category="Health", level="Central", min_age=None, max_age=None,
           max_income=250000, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="Up to ₹5 lakh health cover/year",
           official_link="https://pmjay.gov.in/"),

    Scheme(name="PM Awas Yojana (Urban)", description="Housing subsidy for urban poor and middle-income families.",
           category="Housing", level="Central", min_age=18, max_age=None,
           max_income=300000, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="Housing subsidy for urban poor",
           official_link="https://pmaymis.gov.in/"),

    Scheme(name="National Scholarship (Post-Matric)", description="Scholarship support for SC/ST/OBC students after matriculation.",
           category="Education", level="Central", min_age=None, max_age=30,
           max_income=250000, occupation="Student", gender="Any", caste_category="SC/ST/OBC",
           state_applicability="All India", benefits="Tuition + maintenance scholarship",
           official_link="https://scholarships.gov.in/"),

    Scheme(name="Sukanya Samriddhi Yojana", description="High-interest savings scheme for the girl child.",
           category="Women & Child", level="Central", min_age=0, max_age=10,
           max_income=None, occupation=None, gender="Female", caste_category="Any",
           state_applicability="All India", benefits="High-interest savings account for girl child",
           official_link="https://www.india.gov.in/sukanya-samriddhi-yojana"),

    Scheme(name="Atal Pension Yojana", description="Guaranteed pension scheme for unorganised sector workers.",
           category="Pension", level="Central", min_age=18, max_age=40,
           max_income=None, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="Guaranteed pension after age 60",
           official_link="https://npscra.nsdl.co.in/scheme-details.php"),

    Scheme(name="PM Mudra Yojana", description="Collateral-free loans for small business owners and entrepreneurs.",
           category="Employment/Business", level="Central", min_age=18, max_age=None,
           max_income=None, occupation="Self-employed/Entrepreneur", gender="Any", caste_category="Any",
           state_applicability="All India", benefits="Collateral-free business loan",
           official_link="https://www.mudra.org.in/"),

    Scheme(name="PM Ujjwala Yojana", description="Free LPG gas connections for women from poor households.",
           category="Welfare", level="Central", min_age=18, max_age=None,
           max_income=100000, occupation=None, gender="Female", caste_category="Any",
           state_applicability="All India", benefits="Free LPG gas connection",
           official_link="https://pmuy.gov.in/"),

    Scheme(name="Gruha Lakshmi", description="Monthly financial assistance to women heads of households in Karnataka.",
           category="Welfare", level="State", min_age=18, max_age=None,
           max_income=None, occupation=None, gender="Female", caste_category="Any",
           state_applicability="Karnataka", benefits="₹2,000/month to woman head of household",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Gruha Jyothi", description="Free electricity up to 200 units per month for Karnataka households.",
           category="Welfare", level="State", min_age=None, max_age=None,
           max_income=None, occupation=None, gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Free electricity up to 200 units/month",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Anna Bhagya", description="Free rice distribution scheme for BPL families in Karnataka.",
           category="Food Security", level="State", min_age=None, max_age=None,
           max_income=100000, occupation=None, gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="10kg free rice/month per BPL family member",
           official_link="https://ahara.kar.nic.in/"),

    Scheme(name="Yuva Nidhi", description="Monthly unemployment allowance for unemployed graduates/diploma holders in Karnataka.",
           category="Employment", level="State", min_age=18, max_age=35,
           max_income=None, occupation="Unemployed graduate/diploma holder", gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Monthly unemployment allowance",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Vidyasiri Scholarship", description="Hostel and scholarship support for SC/ST/OBC/minority students in Karnataka.",
           category="Education", level="State", min_age=17, max_age=25,
           max_income=250000, occupation="Student", gender="Any", caste_category="SC/ST/OBC/Minority",
           state_applicability="Karnataka", benefits="Hostel/scholarship support",
           official_link="https://vidyasiri.karnataka.gov.in/"),

    Scheme(name="Shadi Bhagya", description="Marriage assistance grant for minority women in Karnataka.",
           category="Welfare", level="State", min_age=18, max_age=None,
           max_income=100000, occupation=None, gender="Female", caste_category="Minority",
           state_applicability="Karnataka", benefits="Marriage assistance grant",
           official_link="https://mmdcdomt.karnataka.gov.in/"),

    Scheme(name="Karnataka Vidyarthi Vetan (Post-Matric)", description="Monthly stipend for SC/ST post-matric students in Karnataka.",
           category="Education", level="State", min_age=None, max_age=25,
           max_income=250000, occupation="Student", gender="Any", caste_category="SC/ST",
           state_applicability="Karnataka", benefits="Monthly stipend for students",
           official_link="https://sw.kar.nic.in/"),

    Scheme(name="Krishi Bhagya", description="Subsidy for farm ponds and irrigation infrastructure for Karnataka farmers.",
           category="Agriculture", level="State", min_age=18, max_age=None,
           max_income=None, occupation="Farmer", gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Farm pond/irrigation subsidy",
           official_link="https://raitamitra.karnataka.gov.in/"),

    Scheme(name="Karnataka Widow Pension", description="Monthly pension for widows in Karnataka.",
           category="Pension", level="State", min_age=18, max_age=None,
           max_income=200000, occupation=None, gender="Female", caste_category="Any",
           state_applicability="Karnataka", benefits="Monthly pension",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Karnataka Disability Pension", description="Monthly pension for persons with disability in Karnataka.",
           category="Pension", level="State", min_age=18, max_age=None,
           max_income=200000, occupation=None, gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Monthly pension for persons with disability",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Karnataka Old Age Pension (Sandhya Suraksha)", description="Monthly pension for elderly poor citizens in Karnataka.",
           category="Pension", level="State", min_age=60, max_age=None,
           max_income=200000, occupation=None, gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Monthly pension for elderly poor",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Karnataka Artisan Credit Card", description="Low-interest credit facility for artisans and craftspersons in Karnataka.",
           category="Employment/Business", level="State", min_age=18, max_age=None,
           max_income=None, occupation="Artisan/Craftsperson", gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Low-interest credit for artisans",
           official_link="https://kavika.karnataka.gov.in/"),

    Scheme(name="Matsya Ashraya (Fisheries Housing)", description="Housing assistance for fishing families in Karnataka.",
           category="Housing", level="State", min_age=18, max_age=None,
           max_income=200000, occupation="Fisherperson", gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Housing assistance for fishing families",
           official_link="https://fisheries.karnataka.gov.in/"),

    Scheme(name="Karnataka Sericulture Subsidy", description="Subsidy for silk farming equipment for Karnataka sericulture farmers.",
           category="Agriculture", level="State", min_age=18, max_age=None,
           max_income=None, occupation="Farmer (Sericulture)", gender="Any", caste_category="Any",
           state_applicability="Karnataka", benefits="Subsidy for silk farming equipment",
           official_link="https://sericulture.karnataka.gov.in/"),

    Scheme(name="PM Jan Dhan Yojana", description="Zero-balance bank account scheme for financial inclusion.",
           category="Financial Inclusion", level="Central", min_age=10, max_age=None,
           max_income=None, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="Free zero-balance bank account",
           official_link="https://pmjdy.gov.in/"),

    Scheme(name="PM Suraksha Bima Yojana", description="Accident insurance scheme with a very low annual premium.",
           category="Insurance", level="Central", min_age=18, max_age=70,
           max_income=None, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="₹2 lakh accident insurance, ₹20/year premium",
           official_link="https://jansuraksha.gov.in/"),

    Scheme(name="PM Jeevan Jyoti Bima Yojana", description="Life insurance scheme with a low annual premium.",
           category="Insurance", level="Central", min_age=18, max_age=50,
           max_income=None, occupation=None, gender="Any", caste_category="Any",
           state_applicability="All India", benefits="₹2 lakh life insurance, low annual premium",
           official_link="https://jansuraksha.gov.in/"),

    Scheme(name="Karnataka Disabled Persons Marriage Incentive", description="One-time marriage incentive grant for persons with disability in Karnataka.",
           category="Welfare", level="State", min_age=18, max_age=None,
           max_income=None, occupation=None, gender="Any", caste_category="Any (Person with Disability)",
           state_applicability="Karnataka", benefits="One-time marriage incentive grant",
           official_link="https://sevasindhu.karnataka.gov.in/"),

    Scheme(name="Karnataka Minority Pre-Matric Scholarship", description="Scholarship for school-level minority students in Karnataka.",
           category="Education", level="State", min_age=None, max_age=17,
           max_income=100000, occupation="Student", gender="Any", caste_category="Minority",
           state_applicability="Karnataka", benefits="Scholarship for school-level minority students",
           official_link="https://minoritywelfare.karnataka.gov.in/"),

    Scheme(name="National Family Benefit Scheme", description="One-time financial assistance to BPL households on death of the primary earning member.",
           category="Welfare", level="Central", min_age=None, max_age=None,
           max_income=200000, occupation="Any (BPL household, on death of earning member)", gender="Any", caste_category="Any",
           state_applicability="All India", benefits="One-time ₹20,000 financial assistance",
           official_link="https://nsap.nic.in/"),
]

# Step D: Add all schemes to the session, then commit (save) them to the database
db.add_all(schemes)
db.commit()

print(f"Successfully inserted {len(schemes)} schemes into the database.")

# Step E: Close the session
db.close()