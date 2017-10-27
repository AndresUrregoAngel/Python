
import logging
from pydomo.datasets import DataSetRequest, Schema, Column, ColumnType, Policy
from pydomo.datasets import PolicyFilter, FilterOperator, PolicyType, Sorting
from pydomo import Domo

client_id = 'xx'
client_secret = 'xx'



def init_domo_client(client_id, client_secret, **kwargs):
    '''Create an API client on https://developer.domo.com
    Initialize the Domo SDK with your API client id/secret
    If you have multiple API clients you would like to use, simply
    initialize multiple Domo() instances
    Docs: https://developer.domo.com/docs/domo-apis/getting-started
    '''
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                                  '%(message)s')
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)

    return Domo(client_id, client_secret, logger_name='xx@xx.com',
                log_level=logging.INFO, **kwargs)




# Create an instance of the SDK Client
domo = init_domo_client(client_id, client_secret, api_host = 'api.domo.com')
datasets = domo.datasets

csv_file_path = './math.csv'
include_csv_header = True
csv_file = datasets.data_export_to_file('datasetid', csv_file_path,
                                        include_csv_header)
csv_file.close()

'''
dataset_name = 'Invoice DC inc + SAS NPD'
retrieved_dataset = datasets.get('datasetid')


result = retrieved_dataset['schema']['columns']
print(result)
'''
#print(retrieved_dataset)

'''
dataset_list = list(datasets.list(sort=Sorting.NAME))
domo.logger.info("Retrieved a list containing {} DataSet(s)".format(len(dataset_list)))
for v in dataset_list:
    print(v)
'''