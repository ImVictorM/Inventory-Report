from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        now = datetime.today()
        valid_expiration_dates = [
            item["data_de_validade"]
            for item in inventory
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d") >= now
        ]
        manufacturing_dates = [
            item["data_de_fabricacao"] for item in inventory
        ]

        oldest_created_date = min(manufacturing_dates)

        closest_expiration_date = min(
            valid_expiration_dates,
            key=lambda date: abs(datetime.strptime(date, "%Y-%m-%d") - now),
        )

        company_products = {}

        for item in inventory:
            if item["nome_da_empresa"] in company_products:
                company_products[item["nome_da_empresa"]] += 1
            else:
                company_products[item["nome_da_empresa"]] = 1

        company_with_more_products = max(
            company_products, key=company_products.get
        )

        return (
            f"Data de fabricação mais antiga: {oldest_created_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
