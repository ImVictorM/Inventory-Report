from inventory_report.inventory.product import Product


def test_relatorio_produto():
    PRODUCT_ID = 1
    PRODUCT_NAME = "farinha"
    COMPANY_NAME = "Farinini"
    MANUFACTURING_DATE = "2021-02-18"
    EXPIRATION_DATE = "2023-09-17"
    SERIAL_NUMBER = "CR25 1551 4467 2549 4402 1"
    STORAGE_INSTRUCTION = "ao abrigo de luz"

    product = Product(
        PRODUCT_ID,
        PRODUCT_NAME,
        COMPANY_NAME,
        MANUFACTURING_DATE,
        EXPIRATION_DATE,
        SERIAL_NUMBER,
        STORAGE_INSTRUCTION,
    )

    expected_report = (
            f"O produto {PRODUCT_NAME}"
            f" fabricado em {MANUFACTURING_DATE}"
            f" por {COMPANY_NAME} com validade"
            f" até {EXPIRATION_DATE}"
            f" precisa ser armazenado {STORAGE_INSTRUCTION}."
        )

    assert repr(product) == expected_report
