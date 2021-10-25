from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
import pymongo
from pymongo import MongoClient
from django.conf import settings

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')


connect_string = 'mongodb://127.0.0.1:27017/Contact?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false' 

my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['Contact']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["Details"]
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host='127.0.0.1',
                      port=int('27017'),
                      username='',
                      password=''
                     )
 db_handle = client['Contact']
 return db_handle, client 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        #date = request.POST.get(datetime.today())
        #contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        #contact.save()
        contact = {
            name : name, email : email, phone : phone, desc : desc, "date": datetime.today()
        }
        collection_name.insert_one(contact)
        #print(contact)
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

