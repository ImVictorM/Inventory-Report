from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    GREEN = "\033[32m"
    RESET = "\033[0m"
    BLUE = "\033[36m"
    RED = "\033[31m"

    product_list = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
    ]

    # COLORED INTRODUCTORY CLAUSES
    OLDEST_PRODUCT = f"{GREEN}Data de fabricação mais antiga:{RESET}"
    CLOSEST_EXPIRATION = f"{GREEN}Data de validade mais próxima:{RESET}"
    COMPANY_WITH_MORE_PRODUCTS = f"{GREEN}Empresa com mais produtos:{RESET}"

    p1 = product_list[0]

    expected_report = (
        f"{OLDEST_PRODUCT} {BLUE}{p1['data_de_fabricacao']}{RESET}\n"
        f"{CLOSEST_EXPIRATION} {BLUE}{p1['data_de_validade']}{RESET}\n"
        f"{COMPANY_WITH_MORE_PRODUCTS} {RED}{p1['nome_da_empresa']}{RESET}"
    )

    report = ColoredReport(SimpleReport).generate(product_list)

    assert report == expected_report
