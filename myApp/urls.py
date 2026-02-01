from django.urls import path
from .views import *
urlpatterns = [
    path('home/', homePage, name="home" ),
    path('loginPage/', loginPage, name="login" ),
    path('', signupPage, name="signup" ),
    path('logout/', logoutPage, name="logout" ),
    path('Changepassword/', changepassword, name="changepass" ),

    path('category/',categoryPage, name="category" ),
    path('addcategory/', addcategoryPage, name="addcategory" ),
    path('edit_category/<int:id>/', editcategoryPage, name="edit_category" ),
    path('delete_category/<int:id>/', deletecategoryPage, name="delete_category" ),
    path('view_category/<int:id>/', viewcategoryPage, name="view_category" ),
   
    path('recipie/',recipiePage, name="recipie" ),
    path('addrecipie/', addrecipiePage, name="addrecipie" ),
    path('edit_recipie/<int:id>/', editrecipiePage, name="edit_recipe" ),
    path('delete_recipe/<int:id>/', deleterecipiePage, name="delete_recipe" ),
    path('view_recipe/<int:id>/',RecipeDetails, name="view_recipe" ),
]
