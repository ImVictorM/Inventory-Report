from datetime import datetime


class SimpleReport:
    inventory = []

    @classmethod
    def get_oldest_created_date(cls):
        manufacturing_dates = [
            item["data_de_fabricacao"] for item in cls.inventory
        ]
        oldest_created_date = min(manufacturing_dates)
        return oldest_created_date

    @classmethod
    def get_closest_expiration_date(cls):
        now = datetime.today()

        valid_expiration_dates = [
            item["data_de_validade"]
            for item in cls.inventory
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d") >= now
        ]

        closest_expiration_date = min(
            valid_expiration_dates,
            key=lambda date: abs(datetime.strptime(date, "%Y-%m-%d") - now),
        )

        return closest_expiration_date

    @classmethod
    def company_products_quantity(cls, inventory=[]):
        company_products = {}
        inventory_to_use = inventory if inventory else cls.inventory

        for item in inventory_to_use:
            if item["nome_da_empresa"] in company_products:
                company_products[item["nome_da_empresa"]] += 1
            else:
                company_products[item["nome_da_empresa"]] = 1

        return company_products

    @classmethod
    def get_company_with_more_products(cls):
        company_products = cls.company_products_quantity()

        company_with_more_products = max(
            company_products, key=company_products.get
        )

        return company_with_more_products

    @classmethod
    def generate(cls, inventory):
        cls.inventory = inventory

        oldest_created_date = cls.get_oldest_created_date()
        closest_expiration_date = cls.get_closest_expiration_date()
        company_with_more_products = cls.get_company_with_more_products()

        return (
            f"Data de fabricação mais antiga: {oldest_created_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
