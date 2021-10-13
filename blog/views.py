from django.shortcuts import render

posts = [
    {'author': 'Mark',
    'title': 'BMS Builder',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, assumenda nemo eveniet libero ab molestiae, sunt animi aperiam quibusdam provident fugiat voluptates quis earum. Minima quo perferendis animi beatae repellat!',
    'date': '12/01/2020'},

    {'author': 'Jean',
    'title': 'Commercial Setup Teams',
    'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, assumenda nemo eveniet libero ab molestiae, sunt animi aperiam quibusdam provident fugiat voluptates quis earum. Minima quo perferendis animi beatae repellat!',
    'date': '01/02/2020'}
]


def home(request):
    context ={'posts': posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
