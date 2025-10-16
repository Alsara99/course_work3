from api_handler import get_employers, get_vacancies
from db_setup import create_connection, create_tables, insert_employer, insert_vacancy
from UI import user_interface


def load_data_to_database() -> None:
    """Загружает данные о работодателях и вакансиях в базу данных"""
    employer_ids = [1740, 78638, 3529, 10965, 15478, 907345, 3779, 1455, 4181, 2345]
    employers = get_employers(employer_ids)
    conn = create_connection()
    create_tables(conn)
    for employer in employers:
        insert_employer(conn, employer)
        vacancies = get_vacancies(employer["id"])
        for vacancy in vacancies:
            insert_vacancy(conn, vacancy)
    conn.close()


def main() -> None:
    """Основная функция для запуска программы"""
    load_data_to_database()
    user_interface()


if __name__ == "__main__":
    main()