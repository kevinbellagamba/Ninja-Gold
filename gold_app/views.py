from django.shortcuts import redirect, render
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    context = {
        "activities":request.session['activities']
    }
    return render(request, "index.html", context)

def process_money(request):
    if request.method == 'POST':
        myGold = request.session['gold']
        activities = request.session['activities']
        location = request.POST['location']
        if location == 'farm':
            #Earn 10-20 Gold
            goldThisTurn = round(random.random() * 10 + 10)
        elif location == 'cave':
            #Earn 5-10 Gold
            goldThisTurn = round(random.random() * 5 + 5)
        elif location == 'house':
            #Earn 2-25 Gold
            goldThisTurn = round(random.random() * 23 + 2)
        else:
            winOrLose = round(random.random())
            if winOrLose == 1:
                goldThisTurn = round(random.random() * 50)
            else:
                goldThisTurn = round(random.random() * 50 * -1)



        time = strftime("%A, %B %dth %Y at %H:%M:%S %p", gmtime())
        myGold += goldThisTurn
        request.session['gold'] = myGold


        if goldThisTurn >= 0:
            str = f"Earned {goldThisTurn} from the {location} on {time}"            
        else:
            goldThisTurn *= -1
            str = f"Lost {goldThisTurn} from the {location} on {time}"
        
        activities.insert(0, str)
        request.session['activities'] = activities

    return redirect("/")
