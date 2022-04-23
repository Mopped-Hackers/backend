"""services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.api import game_api
import pandas as pd
from sklearn.neighbors import KDTree

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/getGames/', game_api.gameList, name='getGames'),
    path('api/v1/uploadData/', game_api.uploadData, name='uploadData'),
    path('api/v1/dummy/', game_api.getDummyData, name='dummy'),
    path('api/v1/createPrediction', game_api.createPrediction, name='createPrediction')
]

def loadModel():
    items = pd.read_csv("../KNN_dataset.csv")
    columns = items.columns[2:]
    X = items[columns]
    tree = KDTree(X)
    return tree
MODEL_TREE = loadModel()
KNN_DATA = pd.read_csv("KNN_dataset.csv")
COLUMNS = KNN_DATA.columns[2:]