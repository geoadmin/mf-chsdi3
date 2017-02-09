#!/usr/bin/env python

# This script replace scales in all KML files in the production bucket
# public.geo.admin.ch from a begin date to now.
# It saves the KML tested in tmp/kml_tested folder and save the KML modified in
# tmp/kml_replaced.
# Files are stored in gzip format with the same name as in the bucket
import sys
import boto3

import botocore.session
from botocore.exceptions import ClientError


import boto3
from botocore.client import Config


import datetime
import pytz
import gzip
import re
import hashlib
import base64
import time

utc=pytz.UTC


begin_naive = datetime.datetime(2017,01,26)
#end_naive = datetime.datetime(2017,01,27)

begin_naive = datetime.datetime(2016,10,25)
end_naive = datetime.datetime(2017,01,27)


begin = utc.localize(begin_naive) 
end = utc.localize(end_naive) 



import boto3.session
dev = boto3.session.Session(profile_name='geoadmin_filestorage')
  
s3 = dev.resource('s3')

bucket = s3.Bucket('public.geo.admin.ch')

# To test the replace
bucketInt = s3.Bucket('public.int.bgdi.ch')

start_time = time.time()

for objSummary in bucket.objects.all():
    
    # if objSummary.last_modified > begin and objSummary.key == 'H-3eRDgiSN2pZTTYxU7DOQ' and objSummary.last_modified < end:
    if objSummary.last_modified > begin: # and objSummary.key == '3f2YaEnTSFmv-tNqfVN_0g':
        obj = objSummary.Object();
        try : 
            # Get file content
            with open('tmp/kml_tested/' + obj.key, 'wb') as data:
                obj.download_fileobj(data)
            gzf = gzip.GzipFile(fileobj=open('tmp/kml_tested/' + obj.key, 'rb'))
            file_content = gzf.read()
            gzf.close()
            
            # Search scales to replace
            m = re.search('(<scale>0\.25</scale>|<scale>0\.5625</scale>|<scale>2\.25</scale>|<scale>4</scale>)', file_content)
            if m is not None:
              
                # Replace scales
                #print file_content
                file_content = re.sub('<scale>0\.25</scale>', '<scale>0.5</scale>', file_content);
                file_content = re.sub('<scale>0\.5625</scale>', '<scale>0.75</scale>', file_content);
                file_content = re.sub('<scale>2\.25</scale>', '<scale>1.5</scale>', file_content);
                file_content = re.sub('<scale>4</scale>', '<scale>2</scale>', file_content);
                #print file_content
                #print m.group(0)
                #print obj.key, obj.last_modified
              
                # Zip content
                f = gzip.open('tmp/kml_replaced/' + obj.key, 'wb')
                f.write(file_content)
                f.close();


                md5 = hashlib.md5()
                md5.update(file_content) 
                # Send to int bucket
                f = open('tmp/kml_replaced/' + obj.key, 'rb')
                f.seek(0)
                bucket.delete_objects(
                   Delete={
                       'Objects': [{
                            'Key': obj.key
                        }]
                   }
                )
                bucket.put_object(
                    Key=obj.key,
                    Body=f,
                    # ContentMD5=base64.encodestring(md5.digest()),
                    ContentEncoding='gzip',
                    ContentType='application/vnd.google-earth.kml+xml'
                )
                f.close();
                print "Before http://map.geo.admin.ch/?layers=KML||http://public.geo.admin.ch/" + obj.key 
                print "After  http://mf-geoadmin3.int.bgdi.ch/?layers=KML||http://public.int.bgdi.ch/" + obj.key
                print "\n"
        except:
            print objSummary.key
            print objSummary.last_modified 
            print "Error: ", sys.exc_info()[0] 

sec = round(time.time() - start_time)
(min, sec) = divmod(sec,60)
(hour, min) = divmod(min,60) 
print('Time passed: {} hour: {} min: {} sec'.format(hour,min,sec))
