
import os
from datetime import datetime
from urllib.request import urlopen
import logging

logger = logging.getLogger(__name__)
logger.info('Logging has started')
logger.setLevel(logging.DEBUG)


def main():
    lambda_handler('','')



def lambda_handler(event, context):

    sites = ['https://www.google.com', 'http://www.yahoo.com', 'https://www.google.com/webhp?hl=en', ' http://www.google.com/ncr']

    for site in sites:
        check_url(site)


def check_url(site):

    logger.info('Checking {}'.format(site))
    try:
        response = urlopen(site)
    except:
        logger.error('Check failed!')
    else:
        # logger.info(response.code)
        # logger.info(response.headers)
        logger.info('Check passed!')

    finally:
        print('Check complete at {}'.format(str(datetime.now())))




if __name__ == '__main__':
    main()






# def lambda_handler_s3_getter(event, context):
#     #print("Received event: " + json.dumps(event, indent=2))

#     # Get the object from the event and show its content type
#     bucket = event['Records'][0]['s3']['bucket']['name']
#     key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
#     try:
#         response = s3.get_object(Bucket=bucket, Key=key)
#         print("CONTENT TYPE: " + response['ContentType'])
#         return response['ContentType']
#     except Exception as e:
#         print(e)
#         print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
#         raise e
