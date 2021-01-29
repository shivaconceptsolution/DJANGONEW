from django.shortcuts import render

def index(request):
	return render(request,"si/index.html")

def silogic(request):
	p = request.GET["txtp"]
	r = request.GET["txtr"]
	t = request.GET["txtt"]
	si = (float(p)*float(r)*float(t))/100
	return render(request,"si/index.html",{"key":si})


def addition(request):
	return render(request,"si/addition.html")

def additionlogic(request):
	num1 = request.GET["txtnum1"]
	num2 = request.GET["txtnum2"]
	num3= int(num1)+int(num2)
	return render(request,"si/addition.html",{"key":num3})	

