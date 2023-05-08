from inventory_report.inventory.product import Product


def test_cria_produto():
    PRODUCT_ID = 1
    PRODUCT_NAME = "Nicotine Polacrilex"
    COMPANY_NAME = "Target Corporation"
    MANUFACTURING_DATE = "2021-02-18"
    EXPIRATION_DATE = "2023-09-17"
    SERIAL_NUMBER = "CR25 1551 4467 2549 4402 1"
    STORAGE_INSTRUCTION = "instrucao 1"

    product = Product(
        PRODUCT_ID,
        PRODUCT_NAME,
        COMPANY_NAME,
        MANUFACTURING_DATE,
        EXPIRATION_DATE,
        SERIAL_NUMBER,
        STORAGE_INSTRUCTION,
    )

    assert product.id == PRODUCT_ID
    assert product.nome_do_produto == PRODUCT_NAME
    assert product.nome_da_empresa == COMPANY_NAME
    assert product.data_de_fabricacao == MANUFACTURING_DATE
    assert product.data_de_validade == EXPIRATION_DATE
    assert product.numero_de_serie == SERIAL_NUMBER
    assert product.instrucoes_de_armazenamento == STORAGE_INSTRUCTION
