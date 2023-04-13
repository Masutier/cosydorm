@login_required(login_url='loginPage')
def editProfile(request):
    cities = []

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        form.user  = request.POST.get(request.user)

        if form.is_valid():
            print('yess')
            pform = form.save(commit=False)
            pform.user  = request.POST.get(request.user)
            pform.phone  = request.POST.get('phone')
            pform.institute = request.POST.get('institute')
            pform.address1 = request.POST.get('address1')
            pform.address2 = request.POST.get('address2')
            pform.city = request.POST.get('city')
            pform.state = request.POST.get('state')
            pform.zip = request.POST.get('zip')

            print(request.POST.get(request.user))

            #pform.save()

            messages.success(request, f'Modifications was saved successfuly')
            return redirect('userProfile')
        else:

            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        user = request.user.profile
        profile = ProfileForm(instance=user)

        with open('static/json/us_states_and_cities.json') as statesFile:
            states = json.load(statesFile)

            for j in states['Florida']:
                cities.append(j)
            cities.sort()

    context = {'title':'Register Profile', "banner": "Register Profile", 'profile':profile, 'cities':cities}
    return render(request, 'users/edit_profile.html', context)