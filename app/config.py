from app.model.tax_slab import TaxSlabs, Slab

MAX_TAX_EXEMPTION = 450000

base_male_slab = Slab(name="1st Slab", amount=350000, percent=0)
base_female_slab = Slab(name="1st Slab", amount=400000, percent=0)


slabs = [
    Slab(name="2nd Slab", amount=100000, percent=5),
    Slab(name="3rd Slab", amount=400000, percent=10),
    Slab(name="4th Slab", amount=500000, percent=15),
    Slab(name="5th Slab", amount=500000, percent=20),
    Slab(name="6th Slab", amount=2000000, percent=25),
    Slab(name="max", amount=0, percent=30)
]

tax_slab_for_male = TaxSlabs(slabs=[base_male_slab] + slabs)
tax_slab_for_female = TaxSlabs(slabs=[base_female_slab] + slabs)


def get_gender_specific_tax_slab(gender: str):
    if gender.lower() == "male":
        return tax_slab_for_male
    if gender.lower() == "female":
        return tax_slab_for_male
