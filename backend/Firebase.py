import firebase_admin
from firebase_admin import credentials, storage, firestore
import datetime
import pandas as pd
import json
import csv

cred = credentials.Certificate("C:\\Users\\rrohi\OneDrive\\Desktop\\HTN\\pricematch-326403-firebase-adminsdk-qbsjj-00d3c2cbad.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'pricematch-326403.appspot.com', 'databaseURL': 'https: // pricematch-326403.firebaseio.com /'})

def getImage():
    bucket = storage.bucket()
    blob = bucket.blob('maggi.jpg') 
    url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    return url

def convertToCSV(d):
    f = open('data.csv', 'w', newline="")
    csv_file = csv.writer(f)
    key = list(d.keys())
    val = list(d.values())
    csv_file.writerow(key)
    csv_file.writerow(val)
    f.close()

def uploadOutput():
    db = firestore.client()
    doc_ref = db.collection(u'applications')
    df = pd.read_csv('data.csv')
    tmp = df.to_dict(orient='records')
    list(map(lambda x: doc_ref.add(x), tmp))

    docs = doc_ref.stream()
    for doc in docs:
        print(f'{doc.id}= > {doc.to_dict()}')

