# apidjango

#first create folder (name project) them in cmd run the following command
pip install virtualenv

#them
virtualenv venv

#activate virtual environment(in windows, these environments are recommended to be able to work different versions of python on the same computer y framework):
.\venv\Scripts\activate  (for exit write: deactivate)

#or in linux
./venv/Scripts/activate

#note: default console commando venv your key press F1 select interpreter (recommended), them you have active venv in this folder with vscode

#install:
pip install django 

#module api framework or rest framework
pip install djangorestframework

note: documentations 
https://www.django-rest-framework.org/

#initialize project (end with point, allow create folder the same level)
django-admin startproject restdjango . 

#after create app (I add z in the beginning because with alphabetical order, it would be above the main project visually I think it looks better like this)
python manage.py startapp zprojectapp 

#do you need add in setting.py, in the end INSTALLED_APPS = [
  
 'zprojectapp', 
 'rest_framework',

#make the models in zprojectapp

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  technology = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)

note: django automatically create migration of models 
#make file migration (default migration)
python manage.py makemigrations

#execute all migration
python manage.py migrate

# create file of rest serializers.py

from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    # fields = '__all__' TODO: below other form
    fields = ('id','title','description','technology','created_at')
    read_only_fields = ('created_at',)

# create secund file api.py

from zprojectapp.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer


# third step create route 

from rest_framework import routers
from .api import ProjectViewSet 

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls




# four step add route app to main urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zprojectapp.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#note upload project with python

git init 

#after you create .gitignore and write in this name the files than ignore

db.sqlite3
venv
__pycache__

# them add new file than upload with command
 
git add .

#below check the commit and automatically upload the file 

git commit -m “second commit”
