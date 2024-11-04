import argparse
import json

from app.config import MAX_TAX_EXEMPTION, tax_slab_for_male, get_gender_specific_tax_slab
from app.model.information import Information
from app.model.tax_slab import TaxSlabs


def read_input(input_path: str) -> str:
    with open(input_path, 'r') as file:
        json_data = json.load(file)

    return json_data


def calculate_total_salary(info: Information) -> float:
    total = 0
    for salary in info.income.salaries:
        total += salary.amount * salary.times

    return total


def calculate_total_bonus(info: Information) -> float:
    total = 0
    for bonus in info.income.bonuses:
        total += bonus.amount

    return total


def calculate_total_profit_from_investments(info: Information) -> float:
    total = 0
    for profit in info.income.profitFromInvestments:
        total += profit.amount

    return total


def calculate_tax_exemption(total_income: float) -> float:
    tax_exempted_option_1 = total_income * (1/3)
    if tax_exempted_option_1 > MAX_TAX_EXEMPTION:
        return float(MAX_TAX_EXEMPTION)

    return tax_exempted_option_1


def calculate_tax_leviable(taxable_income: float, tax_slabs: TaxSlabs) -> float:
    temp_taxable_income = taxable_income
    total_tax = 0
    print("-"*30)
    for slab in tax_slabs.slabs:
        if temp_taxable_income >= slab.amount:
            slab_tax = (slab.amount * (slab.percent/100))
            total_tax += slab_tax
            print(f"{slab.name} \t| {slab_tax}")
            print("-" * 30)
            temp_taxable_income -= slab.amount
        elif slab.amount >= temp_taxable_income > 0:
            slab_tax = (temp_taxable_income * (slab.percent/100))
            total_tax += slab_tax
            print(f"{slab.name} \t| {slab_tax}")
            print("-" * 30)
            temp_taxable_income -= slab.amount

    return total_tax


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path of the json file", type=str)

    args = parser.parse_args()

    input_path = args.path
    data = read_input(input_path)

    info = Information(**data)

    total_salary = calculate_total_salary(info)
    print(f"Total Salary: {total_salary}")

    total_bonus = calculate_total_bonus(info)
    print(f"Total Bonus: {total_bonus}")

    total_salary_with_bonus = total_salary + total_bonus
    print(f"Total Salary with Bonus: {total_salary_with_bonus}")

    total_profit_from_investments = calculate_total_profit_from_investments(info)
    print(f"Total Profit from Investments: {total_profit_from_investments}")

    total_income = total_salary_with_bonus + total_profit_from_investments
    print(f"Total Taxable Income: {total_income}")

    tax_exempted = calculate_tax_exemption(total_income)
    print(f"Tax Exempted: {tax_exempted}")

    total_taxable_income = total_income - tax_exempted
    print(f"Total Taxable Income: {total_taxable_income}")

    tax_slab = get_gender_specific_tax_slab(info.gender)
    total_tax_leviable = calculate_tax_leviable(total_taxable_income, tax_slab)
    print(f"Total Tax Leviable: {total_tax_leviable}")
