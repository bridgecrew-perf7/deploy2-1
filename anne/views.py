from django.shortcuts import render
from .forms import SearchVideoForm
from anne import models

def searchUser(request):
    obj = models.Item.objects.all()
    site_d = models.SiteDesc.objects.all()
    return render(request,'anne/index.html', {'obj':obj, 'site_des':set(site_d)})

def videoPlayer(request):
    obj = models.Item.objects.all()
    video_id = request.GET['video_id']
    video = models.Item.objects.get(id=video_id)
    return render(request, 'anne/video_player.html', {'obj':obj, 'my_video':video})

def searchVideo(request):
    if request.method=='POST':
        form = SearchVideoForm(request.POST)
        desc = form.data['desc']
        items = models.Item.objects.filter(desc=desc)
        res = render(request,'anne/search_video.html',{'form':form,'items':items})
        return res
