import argparse
import logging
import sys
import db.data_base as data_base
import models.quaterion_model as working_model

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
    return data_base.get_qdrant_client_()


def find_in_db(db_client, company_name):
    return db_client.check_for_name_in_db(company_name)


def print_company_instance_names(results):
    for result in results:
        logger.info(result)


def search_company_instance(company_name, db_client, threshold, limit):
    search_result = working_model.inference(company_name, db_client, threshold, limit=limit, preproc_text=True)
    return search_result


def run_company_matches(args):
    company_name = args.company_name
    threshold = args.threshold_value
    limit = args.limit

    logger.info("Getting db client...")
    db_client = get_db()

    try:
        res = db_client.get_collection()
        if not res:
            logger.error("Db client dont return collection")
            return 0
    except Exception:
        logger.error("Error during database client initialisation")
        return 1

    logger.info("Get dbase client!")

    logger.info("Checking company existence in db")
    status, company = find_in_db(db_client, company_name)

    if status == 0:
        logger.info(f"Find this company in db. We worked with company '{company}'. They don't change company name.")
        return 0
    elif status == 1:
        logger.info(f"Don't find exact company in db. However, find close one by name:'{company}'. Starting matching "
                    f"with threshold {threshold} process to search better matching.")
    else:
        logger.info(f"Dont find company '{company_name}' in db. Starting matching process with threshold {threshold}")

    search_result = search_company_instance(company_name, db_client, threshold, limit)
    print_company_instance_names(search_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('company_name', type=str,
                        help='A name of studied company')

    parser.add_argument('threshold_value', type=float,
                        help='Matching threshold, between 0 and 1, where = 1 means total matching.')

    parser.add_argument('--limit', '-l', type=int, default=10,
                        help='Limit of number for search names',dest='limit')

    args = parser.parse_args()
    # print(args.company_name)
    logger.info(f"Get company name: {args.company_name}")
    run_company_matches(args)
    logger.info(f"Shutting down")
