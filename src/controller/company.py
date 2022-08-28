from venv import create
from src.database.queries import create_company


def update_registry(company):
    if company.id is None:
        print('teste Bruno: ', company.id)
        result_company = create_company(company)
        return result_company.id

    return 0
