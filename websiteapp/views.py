from django.shortcuts import render,redirect
from webapp.models import catdb,prodb,contactdb,userdb,cartdb
from django.contrib import messages

# Create your views here.
def webindexpage(req):
    data=catdb.objects.all()
    return render(req,"webindex.html",{'data':data})

def aboutpage(req):
    return render(req,"AboutPage.html")
def brandpage(req,catg):
    products=prodb.objects.filter(Category_Name=catg)
    return render(req,"products.html",{'products':products})
def singleproduct(req,dataid):
    data=prodb.objects.get(id=dataid)
    return render(req,"Pro_details.html",{'data':data})
def contactpage(req):
    return render(req,"contact.html")
def savecontact(req):
    if req.method=="POST":
        na=req.POST.get('Name')
        em=req.POST.get('Email')
        ph=req.POST.get('Phone')
        me=req.POST.get('Message')
        obj2=contactdb(Name=na,Email=em,Phone=ph,Message=me)
        obj2.save()
        return redirect(contactpage)
def contactdisplay(req):
    data=contactdb.objects.all()
    return render(req,"contact.html",{'data':data})
def login(req):
    return render(req,"login.html")
def user_reg(request):
    if request.method=="POST":
        em=request.POST.get('email')
        un=request.POST.get('username')
        pa=request.POST.get('password')
        pas=request.POST.get('cpassword')
        obj3=userdb(usermail=em,user=un,passw=pa,con_passw=pas)
        obj3.save()
        return redirect(login)
def userlogin(request):
    if request.method=="POST":
        username_p=request.POST.get('username')
        password_p=request.POST.get('password')
        if userdb.objects.filter(user=username_p,passw=password_p).exists():

            request.session['usernamep']=username_p
            request.session['passwordp']=password_p

            return redirect(webindexpage)
        else:
            return redirect(login)
        return redirect(login)

def userlogout(request):
    del request.session['usernamep']
    del request.session['passwordp']
    return redirect(login)


def cart(req):
    cartt = cartdb.objects.filter(User=req.session['usernamep'])
    return render(req, "cart.html", {'cartt': cartt})

def cartpage(req):
    if req.method=="POST":
        n=req.POST.get('proname')
        u=req.POST.get('username')
        q=req.POST.get('quantity')
        p=req.POST.get('tprice')
        obj=cartdb(proname=n,proquantity=q,proprice=p,User=u)
        obj.save()
        messages.success(req, "Added to Cart")
        return redirect(cart)





