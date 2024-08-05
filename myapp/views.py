from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def rsvp_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        attending = request.POST.get('attending')
        
        # Lakukan sesuatu dengan data yang dikirim, misalnya menyimpannya ke database
        
        return render(request, 'thank_you.html', {'name': name, 'email': email, 'attending': attending})
    else:
        return redirect('/')