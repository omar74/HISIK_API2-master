from django.shortcuts import render,redirect
from .models import User
from .serializer import UserSerializer
from rest_framework import generics
from user.filter import UserFilter
'''
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

'''
# Create your views here.


class UserListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  User.objects.all()
    serializer_class       =  UserSerializer
    filterset_class        =  UserFilter
    search_fields          = ('id','UserName','Email',)

    # def get_queryset(self):
    #     name = self.request.GET.get('Cname')
    #     qs = User.objects.filter(UserName=name)
    #     return qs
     
 

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  User.objects.all()
    serializer_class       =  UserSerializer
    lookup_field = 'id'
    


'''
class UserFormView (View):
    form_class = UserForm
    template_name = 'user/registeration_form.html'

    def get (self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post (self,request):
        form=self.form_class(request.Post)

        if form.is_valid():
            user = form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user = authenticate(username=username,password=password)

            if user is not None :
                if user.is_active:
                    login(request,user)
                    return redirect ('user:index')

        return render(request,self.template_name,{'form':form})
'''
