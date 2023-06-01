from django.shortcuts import render,redirect
from webapp.models import catdb,prodb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def indexpage(req):
    return render(req,"index.html")
def categorypage(req):
    return render(req,"AddCategory.html")
def savecat(req):
    if req.method=="POST":
        na=req.POST.get('name')
        img=req.FILES['image']
        ds=req.POST.get('des')
        obj=catdb(Cat_Name=na,Image=img,Description=ds)
        obj.save()
        messages.success(req,"Category Saved Succesfully  ")
        return redirect(categorypage)
def catdisplay(req):
    data=catdb.objects.all()
    return render(req,"DisplayPage.html",{'data':data})
def editcat(req,dataid):
    data=catdb.objects.get(id=dataid)
    return render(req,"EditPage.html",{'data':data})
def Updatecat(req,dataid):
    if req.method=="POST":
        na=req.POST.get('name')
        ds = req.POST.get('des')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Cat_Name=na,Image=file,Description=ds)
        messages.success(req,"Category Updated")
        return redirect(catdisplay)


def delcat(req,dataid):
        data = catdb.objects.filter(id=dataid)
        data.delete()
        messages.error(req,"Category Deleted")
        return redirect(catdisplay)

def productpage(req):
    data=catdb.objects.all()
    return render(req,"AddProduct.html",{'data':data})
def saveproduct(request):
    if request.method=="POST":
        cna=request.POST.get('cname')
        pna=request.POST.get('pname')
        qty=request.POST.get('quantity')
        pr=request.POST.get('price')
        dr=request.POST.get('description')
        im=request.FILES['pimage']
        obj1=prodb(Category_Name=cna,Product_Name=pna,Product_Quantity=qty,Product_Price=pr,Product_descrption=dr,Product_Image=im)
        obj1.save()
        messages.success(request,"Product Saved Successfully")
        return redirect(productpage)
def prodisplay(req):
    data=prodb.objects.all()
    return render(req,"DisplayProduct.html",{'data':data})
def proedit(req,dataid):
    data=catdb.objects.all()
    products=prodb.objects.get(id=dataid)
    return render(req,"EditProduct.html",{'data':data,'products':products})
def proupdate(req,dataid):
    if req.method=="POST":
        cna=req.POST.get('cname')
        pna=req.POST.get('pname')
        qty=req.POST.get('quantity')
        pr=req.POST.get('price')
        dr=req.POST.get('description')
        try:
            img = req.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=dataid).Image
        prodb.objects.filter(id=dataid).update(Category_Name=cna,Product_Name=pna,Product_Quantity=qty,Product_Price=pr,Product_descrption=dr,Product_Image=file)
        messages.success(req,"Updated Successfully")
        return redirect(prodisplay)

def prodel(req, dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Data Deleted")
    return redirect(prodisplay)

def adminpage(req):
    return render(req,"AdminLogin.html")
def adminlogin(request):
    if request.method=="POST":
        username_p=request.POST.get('username')
        password_p=request.POST.get('password')
        if User.objects.filter(username__contains=username_p).exists():
            user=authenticate(username=username_p,password=password_p)
            if user is not None:
                login (request,user)
                request.session['username']=username_p
                request.session['password']=password_p
                return redirect(indexpage)
            else:
                return redirect(adminpage)
        else:
            return redirect(adminpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminpage)
