import argparse
import logging
import sys

logger = logging.getLogger("MatchNames")
# logger.setLevel(logging.INFO)
# or you can set the following level
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def get_db():
    return []


def find_in_db(db, company_name):
    return []


def match_vectors(vector, vector_db):
    return True


def run_matching(company_vector):
    logger.info("Try to find matching vector...")
    db = []
    for row in db:
        match = match_vectors(company_vector, row.vector)
        if match:
            return row.instance


def get_company_instance_names(instance):
    # return db.get_name_from_instance(instance)
    return []


def search_company_instance(company_name):
    # company_vectors = berta.make_vector()
    company_vector = [1, 1, 1]

    instance = run_matching(company_vector)
    if not instance:
        logger.info("Dont find matching company's in database. Creating new instance")
        # db.create(company_name, company_vector)
        return 0

    logger.info("Find this company before, by names")
    names = get_company_instance_names(instance)
    for name in names:
        logger.info(name)


def run_company_matches(company_name):
    db = get_db()
    logger.info("Checking company existence in db")
    existed_in_db = find_in_db(db, company_name)

    if existed_in_db:
        logger.info("Find this company in db. Other names:")
        other_names = get_company_instance_names(existed_in_db)
        for name in other_names:
            logger.info(name)

        return 1

    logger.info(f"Previous company's dont use name {company_name}. Starting matching process")
    search_company_instance(company_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('company_name', type=str,
                        help='A name of studied company')

    args = parser.parse_args()
    # print(args.company_name)
    logger.info(f"Get company name: {args.company_name}")
    run_company_matches(args.company_name)
    logger.info(f"Shutting down")
