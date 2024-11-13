from django.shortcuts import render,HttpResponse,redirect
from .models import*
import random
from django.core.mail import send_mail
from django.core.paginator import Paginator
import razorpay
from  django.contrib import messages
from django.utils import timezone
# Create your views here.

def index(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        con={"uid":uid}
        return render(request,"index.html",con)
    else:
        return redirect("login")
        

def shop(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        cid = Categorie.objects.all()
        pid = Product.objects.all().order_by("-id")
        cat2=request.GET.get("cat2")
        S = request.GET.get("sort")
        wishlist_color = Wishlist.objects.filter(user_id=uid)
        l1=[]
        for i in wishlist_color:
            l1.append(i.product_id.id)

        if cat2:
            pid = Product.objects.filter(Categorie_id=cat2)
        elif S == 'lth':
            pid = Product.objects.all().order_by("price")
        elif S == 'htl':
            pid = Product.objects.all().order_by("-price") 
        elif S == 'atz':
            pid = Product.objects.all().order_by("name") 
        elif S == 'zta':
            pid = Product.objects.all().order_by("-name")              
        else:
            pid = Product.objects.all().order_by("-id")

        paginator=Paginator(pid,2)
        page_number=request.GET.get("page",1)
        print(type(page_number))
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1

        pid=paginator.get_page(page_number)
      
        show_page = paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=2)
        

        print(show_page)

        con={"uid":uid,"cid":cid,"pid":pid,"l1":l1,"wishlist_color":wishlist_color,"show_page":show_page}
        return render(request,"shop.html",con)
    else:
        return redirect("login")
    
from django.urls import reverse
def rating(request):
    if 'email' in request.session:
        uid=Register.objects.get(email=request.session["email"])
        if request.POST:
            name = request.POST['name']
            email = request.POST['email']
            review = request.POST['review']
            stars = request.POST['stars']
            product_id = request.POST['product_id']
            datetime = timezone.localtime(timezone.now()).date()

            reverse_url = reverse('shop_detail1',kwargs={'id':product_id})
            pid = Product.objects.get(id=product_id)

            Rating.objects.create(product_id=pid,name=name,email=email,review=review,rating=stars,datetime=datetime)
            return redirect(reverse_url)
    else:
        return redirect('login')






def price_filter(request):
    if request.POST:
        max=request.POST['max']
        pid=Product.objects.filter(price__lte=max)
        con={"max":max,"pid":pid}
        return render(request,"shop.html",con)
    else:

        return render(request,"shop.html")
    
def search(request):
    if "email" in request.session:
        srh = request.GET.get("srh")
        pid = Product.objects.all()
        if srh:
            pid = Product.objects.filter(name__icontains = srh)
            print(pid)
            con={"pid":pid,"srh":srh}
            return render(request,"shop.html",con)
        else:
            return redirect("shop")
    else:    
        return redirect("login")



def shop_detail(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        cid = Categorie.objects.all()
        pid = Product.objects.all()


        con={"uid":uid,"cid":cid,"pid":pid}
        return render(request,"shop_detail.html",con)
    else:
        return redirect("login")
    

import math
def shop_detail1(request,id):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        cid = Categorie.objects.all()
        pid = Product.objects.get(id=id)    
        rate_id = Rating.objects.filter(product_id = pid)

        # totaluser = sum(i.user_id for i in Rating)
        # totalstar = sum(i.star for i in Rating)
        # avg = totalstar/totaluser

        l1 = []
        for i in rate_id:
            l1.append(i.rating)

        print(l1)

        if rate_id.count() > 0:
            a = sum(l1)/rate_id.count()#start count and sum: total stars/total reviews
            print(a)
            a1 = math.ceil(a)  # for half star
            print(a1)
            pid.rating1 = a
            pid.halfrating = a1
            pid.save()
        else:
            a = 0
            a1 = 0
            print("No ratings available")

        con={"uid":uid,"cid":cid,"pid":pid,"rate_id":rate_id,"a":a,"a1":a1}
        return render(request,"shop_detail.html",con)
    else:
        return redirect("login")

def testimonial(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        con={"uid":uid}
        return render(request,"testimonial.html",con)
    else:
        return redirect("login")

def contact(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
      

        if request.POST:
                name = request.POST['name']
                email = request.POST['email']
                message = request.POST['message']

                Contact.objects.create(name=name,email=email,message=message)
                return redirect("contact")

        else:
            return render(request,"contact.html")
    else:
       
        return render(request,"login.html")



def Checkout(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        pid = Product.objects.all()    
        cart_items = CartItem.objects.filter(user_id=uid)
        shipping = 50
        subtotal= sum(i.total_price for i in cart_items)
        total = subtotal + shipping
        

   
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            companyname = request.POST['companyname']
            address = request.POST['address']
            city = request.POST['city']
            country = request.POST['country']
            zip = request.POST['zip']
            mobile = request.POST['mobile']
            email = request.POST['email']

            checkout.objects.create(firstname=firstname,lastname=lastname,companyname=companyname,
                                    address=address,city=city,country=country,zip=zip,mobile=mobile,email=email)
            

            # send items which are ordered in the order model 
            for item in cart_items:
                    order.objects.create(
                        user_id=uid,
                        product_id=item.product_id,
                        name=item.name,
                        image=item.image,
                        price=item.price,
                        quantity=item.quantity,
                        total_price=item.quantity * item.price
                    )
                    item.delete()  # Clear the cart

            return redirect('emptycart')
            
        else:
            # payment
            amount = max(total, 1) * 100
            client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
            response = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})
            print(response,"******")
            con={"uid":uid,"cart_items":cart_items,"shipping":shipping,"subtotal":subtotal,"total":total,"response":response}
            return render(request,"checkout.html",con)
       
    else:
        return redirect("login")
def emptycart(request):
    
    return render(request,"emptycart.html")

def orders(request):
    if "email" in request.session:
        uid = Register.objects.get(email = request.session['email'])
        oid = order.objects.filter(user_id=uid)
        con={"uid":uid,"oid":oid}
        return render(request,"orders.html",con) 
    else:
        return redirect("login")
    
def orderhandle(request,id):
    if 'email' in request.session:
        cart_id = order.objects.get(id=id)
        cart_id.delete()
        return redirect('orders')
    else:
        return redirect('login')

    
def cart(request):
    if "email" in request.session:
        uid = Register.objects.get(email = request.session['email'])
        cid1 = CartItem.objects.filter(user_id=uid)
        count = CartItem.objects.filter(user_id=uid).count()

        if cid1:
            shipping = 50
            subtotal = sum(i.total_price for i in cid1)
            total = shipping + subtotal

            con={"cid1":cid1,"total":total,"subtotal":subtotal,"shipping":shipping,"count":count}
            return render(request,"cart.html",con)
        else:
            return redirect("emptycart")
    else:
        return redirect("login")



def add_to_cart(request,id):
    if "email" in request.session:
        uid = Register.objects.get(email = request.session['email'])
        pid = Product.objects.get(id=id)
        cid1 = CartItem.objects.filter(product_id=pid,user_id=uid).first()
        
        if cid1:
            cid1.quantity=cid1.quantity+1
            cid1.total_price=cid1.quantity*cid1.price
            cid1.save()
        else:    
            CartItem.objects.create(product_id=pid,user_id=uid,
                                    name=pid.name,
                                    image=pid.image,
                                    price=pid.price,
                                    quantity=pid.quantity,
                                    total_price=pid.quantity*pid.price)
        
        return redirect("cart")
    else:
        return redirect("login")

def increment(request,id):
    if "email" in request.session:
        try:
            cart_id = CartItem.objects.get(id=id)
            cart_id.quantity += 1
            cart_id.total_price = cart_id.quantity*cart_id.price
            cart_id.save()
            return redirect("cart")
        except CartItem.DoesNotExist:
            return render(request,"cart.html")
    else:
        return redirect("login")


def decrement(request,id):
    if "email" in request.session:
        try:
            cart_id = CartItem.objects.get(id=id)
            cart_id.quantity -= 1
            if cart_id.quantity < 1 :
                cart_id.delete()
                return redirect('cart')

            else:
                cart_id.total_price = cart_id.total_price-cart_id.price
                cart_id.save()
                return redirect('cart')
                    
        except CartItem.DoesNotExist:
            return redirect("cart")
    return render(request,"cart.html")

def handle(request,id):
    if 'email' in request.session:
        cart_id = CartItem.objects.get(id=id)
        cart_id.delete()
        return redirect('cart')
    else:
        return redirect('login')

    

def error(request):
    if "email" in request.session:
        uid=Register.objects.get(email=request.session["email"])
        con={"uid":uid}
        return render(request,"error.html",con)
    else:
        return redirect("login")
import requests
def register(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        conpass = request.POST['conpass']
        response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=6089bc4afeb248cfbae263ac6dd99ef8&email={email}")
        try:
            uid = Register.objects.get(email=email)
            if uid.email == email:
                con={"e_msg":"this email already exist"}
                return render(request,"register.html",con)
        except:
                if response.status_code == 200:
                    data = response.json()
                    if data["deliverability"] == "DELIVERABLE":
                        if password == conpass:
                            Register.objects.create(name=name,email=email,password=password)
                            return redirect("login")
                        else:
                            con={"e_msg":"Password do not match"}
                            return render(request,"register.html",con)
                    else:
                        con={"e_msg":"this email is not found in server"}
                        return render(request,"register.html",con)
                else:
                    return render(request,"register.html")       
    else:        
        return render(request,"register.html")

def login(request):
    if "email" in request.session:
        return render(request,"index.html")
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            uid = Register.objects.get(email=email)
            if uid.email == email:
                request.session["email"]=uid.email
                if uid.password == password:
                    return redirect("index")
                else:
                    con={"e_msg":"password does not match"}
                    return render(request,"login.html",con)  
            else:
                return render(request,"login.html")
        except Register.DoesNotExist:
            con={"e_msg":"user does not match"}
            return render(request,"login.html",con)

    else:             
        # con={"e_msg":"user does not match"}
        return render(request,"login.html")
    
  
def logout(request):
    if "email" in request.session:
        
        del request.session["email"]
        return redirect("login")

    else:    
        return redirect("login")
    

def forget(request):
    if request.POST:
        email = request.POST['email']
        otp=random.randint(1111,9999)
        try:
            uid = Register.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail("Django",f"your OTP is {otp}",'aayrin.imscit21@gmail.com',[email])
            con={"email":email}
            return render(request,"confirm_password.html",con)
            
        except :
            con={"e_msg":"This email doesn't exixts"}
            return render(request,"forget.html",con)

        # if uid.email != email:
        #     con={"e_msg":"This email doesn't exists"}
        #     return render(request,"forget.html",con)
        # else:
        #     return redirect("confirm_password")
    
    return render(request,"forget.html") 

def confirm_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        conpass = request.POST['conpass']
        uid = Register.objects.get(email=email)
        try:
            if uid.otp == int(otp):
                if password == conpass:
                    uid.password = password
                    uid.save()
                    return redirect("login")
                else:
                    con = {"e_msg":"passwords does not match"}
                    return render(request,"confirm_password.html",con)
            else:
                con={"e_msg":"otp is not correct"}
                return render(request,"confirm_password.html",con) 
        except:
            con={"e_msg":"something went wrong"}
            return render(request,"confirm_password.html",con) 

    return render(request,"confirm_password.html")

def wishlist(request,id):
    if 'email' in request.session:
        uid = Register.objects.get(email=request.session['email'])
        pid = Product.objects.get(id=id)
        wid = Wishlist.objects.filter(product_id=pid,user_id=uid).first()
        
        if wid:  
            wid.delete()
            messages.info(request,"your item is been deleted")
            return redirect("shop")
        
        
        else:
            Wishlist.objects.create(user_id=uid,product_id=pid,image=pid.image,name=pid.name,
                                     price=pid.price)  
            messages.info(request,"your item is added to wishlist")
         
        return redirect("shop")
    

    else:
        return redirect("login")
    
def show_wishlist(request):
    if 'email' in request.session:
        uid = Register.objects.get(email=request.session['email'])
        wid = Wishlist.objects.filter(user_id=uid)

        con = {"uid":uid,"wid":wid}
        return render(request,"wishlist.html",con)
    else:
        return redirect("login")
    

def wishlist_handle(request,id):
    if 'email' in request.session:
        item = Wishlist.objects.get(id=id)
        item.delete()
        return redirect('show_wishlist')
    else:
        return redirect('login')



# def profile1(request,id):
#     if 'email' in request.session:
#         uid =Register.objects.get(email=request.session['email'])
    
#     if request.POST:
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
        
#         if "image" in request.FILES:
#             image = request.FILES['image']
#             uid.image = image
#             uid.name = name
#             uid.email = email
#             uid.phone = phone
#             uid.address = address  
#             request.session['email'] = email
#             uid.save()
#             return render('profile',id=uid.id) 
            
#         else:    
#             uid.name = name
#             uid.email = email
#             uid.phone = phone
#             uid.address = address  
#             request.session['email'] = email
#             uid.save()
#             return render('profile',id=uid.id)           

#     context = {"uid": uid}
#     return render(request, 'profile.html', context)

def profile(request):
    if 'email' in request.session:
        uid =Register.objects.get(email=request.session['email'])

        if request.POST:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            if "image" in request.FILES:
                image = request.FILES['image']
                uid.name = name
                uid.email = email
                uid.phone = phone
                uid.address = address
                request.session['email'] = email
                uid.save()
                return redirect("profile")
            else:
                uid.name = name
                uid.email = email
                uid.phone = phone
                uid.address = address
                request.session['email'] = email
                uid.save()
                return redirect("profile")

        con = {"uid":uid}
        return render(request,"profile.html",con)
    
    else:
        return redirect('login')

def password(request):
    if 'email' in request.session:
        uid =Register.objects.get(email=request.session['email'])    
        if request.POST:
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            newpassword = request.POST['newpassword']

        if uid.password == password:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                return redirect("profile")
            else:
                con={'e_msg':'pls enter same password'}
                return render(request,'profile.html',con)
        else:
            con={'e_msg':'pls enter same  password'}
            return render(request,'profile.html',con)
    else:
        return redirect('login')
    