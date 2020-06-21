from umongo.document import MetaDocumentImplementation, DocumentImplementation
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def convert_to_mongo_document(object_to_convert: object, mongo_entity: MetaDocumentImplementation) -> [DocumentImplementation, None]:
    entity_db = mongo_entity()
    list_attr = list(object_to_convert.__dict__.keys())
    list_values = list(object_to_convert.__dict__.values())
    logger.info(f"Converting from {object_to_convert.__class__.__name__} to {mongo_entity.__name__}")
    try:
        [entity_db.__setattr__(list_attr[item], list_values[item]) for item in range(0, len(list_attr))]

    except AttributeError:
        logger.error(f"Error when converting from {object_to_convert.__class__.__name__} to {mongo_entity.__name__}")
        return None

    return entity_db
