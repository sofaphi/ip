from django import views
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Gallery(View):
    def get(self, request):
        if (request.GET.get('type') == 'certificate'):
            achievementsList = Certificate.objects.all()

            return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
            })
        elif (request.GET.get('type') == 'work'):
            achievementsList = Work.objects.all()

            return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
            })
        elif (request.GET.get('type') == 'project'):
            achievementsList = Project.objects.all()

            return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
            })
        elif (request.GET.get('type') == 'tourtaiment'):
            achievementsList = Tourtaiment.objects.all()

            return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
            })
        else:
            achievementsList = Certificate.objects.all()

            return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
            })


class AchievementItem(View):
    def get(self, request, pk):
        if (request.GET.get('type') == 'certificate'):
            return render(request, 'gallery-item.html', context={
                'item': Certificate.objects.get(pk=pk),
            })
        elif (request.GET.get('type') == 'work'):
            return render(request, 'gallery-item.html', context={
                'item': Work.objects.get(pk=pk),
            })
        elif (request.GET.get('type') == 'project'):
            return render(request, 'gallery-item.html', context={
                'item': Project.objects.get(pk=pk),
            })
        elif (request.GET.get('type') == 'tourtaiment'):
            return render(request, 'gallery-item.html', context={
                'item': Tourtaiment.objects.get(pk=pk),
            })
        else:
            return render(request, 'gallery-item.html', context={
                'item': Certificate.objects.get(pk=pk),
            })


class AchievementCreate(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):

        if (request.GET.get('type') == 'certificate'):

            achievement = Certificate(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                date=request.POST.get('date'),
                preview=request.FILES.get('preview'),
            )
            achievement.save()
        elif (request.GET.get('type') == 'tourtaiment'):
            achievement = Tourtaiment(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                date=request.POST.get('date'),
                preview=request.FILES.get('preview'),
            )
            achievement.save()
        elif (request.GET.get('type') == 'work'):
            achievement = Work(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                dateStart=request.POST.get('dateStart'),
                dateEnd=request.POST.get('dateEnd'),
                preview=request.FILES.get('preview'),
            )
            achievement.save()
        elif (request.GET.get('type') == 'project'):
            achievement = Project(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                dateStart=request.POST.get('dateStart'),
                dateEnd=request.POST.get('dateEnd'),
                preview=request.FILES.get('preview'),
            )
            achievement.save()


        return redirect('gallery')
