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
        elif (request.GET.get('type') == 'work'):
            achievementsList = Work.objects.all()
        elif (request.GET.get('type') == 'project'):
            achievementsList = Project.objects.all()
        elif (request.GET.get('type') == 'tourtaiment'):
            achievementsList = Tourtaiment.objects.all()
        elif (request.GET.get('type') == 'hackaton'):
            achievementsList = Hackaton.objects.all()
        elif (request.GET.get('type') == 'course'):
            achievementsList = Course.objects.all()
        else:
            achievementsList = Certificate.objects.all()

        return render(request, 'gallery.html', context={
                'achievementsList': achievementsList,
                'achievementsListCount': len(achievementsList),
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
        elif (request.GET.get('type') == 'hackaton'):
            return render(request, 'gallery-item.html', context={
                'item': Hackaton.objects.get(pk=pk),
            })
        elif (request.GET.get('type') == 'course'):
            return render(request, 'gallery-item.html', context={
                'item': Course.objects.get(pk=pk),
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
        elif (request.GET.get('type') == 'tourtaiment'):
            achievement = Tourtaiment(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                date=request.POST.get('date'),
                preview=request.FILES.get('preview'),
            )
        elif (request.GET.get('type') == 'work'):
            achievement = Work(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                dateStart=request.POST.get('dateStart'),
                dateEnd=request.POST.get('dateEnd'),
                preview=request.FILES.get('preview'),
            )
        elif (request.GET.get('type') == 'project'):
            achievement = Project(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                dateStart=request.POST.get('dateStart'),
                dateEnd=request.POST.get('dateEnd'),
                preview=request.FILES.get('preview'),
            )
        elif (request.GET.get('type') == 'course'):
            achievement = Course(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                dateStart=request.POST.get('dateStart'),
                dateEnd=request.POST.get('dateEnd'),
                preview=request.FILES.get('preview'),
            )
        elif (request.GET.get('type') == 'hackaton'):
            achievement = Hackaton(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                date=request.POST.get('date'),
                preview=request.FILES.get('preview'),
            )
            achievement.save()
            
        achievement.save()
        return redirect('gallery')


class DeleteAchievement(View):
    def get(self, request, pk):

        if (request.GET.get('type') == 'certificate'):
            Certificate.objects.get(pk=pk).delete()
        elif (request.GET.get('type') == 'project'):
            Project.objects.get(pk=pk).delete()
        elif (request.GET.get('type') == 'work'):
            Work.objects.get(pk=pk).delete()
        elif (request.GET.get('type') == 'tourtaiment'):
            Tourtaiment.objects.get(pk=pk).delete()
        elif (request.GET.get('type') == 'hackaton'):
            Hackaton.objects.get(pk=pk).delete()
        elif (request.GET.get('type') == 'course'):
            Course.objects.get(pk=pk).delete()
        else:
            Certificate.objects.get(pk=pk).delete()

        return redirect('gallery')

class ChangeAchievement(View):
    def get(self, request, pk):
        if (request.GET.get('type') == 'certificate'):
            item = Certificate.objects.get(pk=pk)
        elif (request.GET.get('type') == 'work'):
            item = Work.objects.get(pk=pk)
        elif (request.GET.get('type') == 'project'):
            item = Project.objects.get(pk=pk)
        elif (request.GET.get('type') == 'tourtaiment'):
            item = Tourtaiment.objects.get(pk=pk)
        elif (request.GET.get('type') == 'hackaton'):
            item = Hackaton.objects.get(pk=pk)
        elif (request.GET.get('type') == 'course'):
            item = Course.objects.get(pk=pk)
        else:
            item = Certificate.objects.get(pk=pk)

        return render(request, 'form.html', context={
            'item': item,
        })

    def post(self, request, pk):
        if (request.GET.get('type') == 'certificate'):
            achievement = Certificate.objects.get(pk=pk)
        elif (request.GET.get('type') == 'tourtaiment'):
            achievement = Tourtaiment.objects.get(pk=pk)
        elif (request.GET.get('type') == 'work'):
            achievement = Work.objects.get(pk=pk)
        elif (request.GET.get('type') == 'project'):
            achievement = Project.objects.get(pk=pk)
        elif (request.GET.get('type') == 'course'):
            achievement = Course.objects.get(pk=pk)
        elif (request.GET.get('type') == 'hackaton'):
            achievement = Hackaton.objects.get(pk=pk)
        else:
            achievement = Certificate.objects.get(pk=pk)
            
        achievement.title = request.POST.get('title')
        achievement.description = request.POST.get('description')
        achievement.preview = request.FILES.get('preview')
        
        try: 
            achievement.date = request.POST.get('date')
        except:
            achievement.dateStart = request.POST.get('dateStart')
            achievement.dateEnd = request.POST.get('dateEnd')

        achievement.save()

        return redirect('gallery')