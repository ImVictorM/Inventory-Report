from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        company_products = super().company_products_quantity(inventory)

        additional_report = 'Produtos estocados por empresa:\n'
        for company in company_products.items():
            additional_report += f'- {company[0]}: {company[1]}\n'

        return (
            f"{simple_report}\n"
            f"{additional_report}"
        )
