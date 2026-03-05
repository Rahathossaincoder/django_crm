from django.contrib.auth.forms import UserCreationForm  # import built-in form that handles user creation + password validation
#it creates users  # (original comment) clarifying purpose of UserCreationForm
from django.contrib.auth.models import User  # import Django's User model (the model this form will create/update)
#user is basically the super user  # (original comment) inaccurate: User represents any user account, not only superuser
from django import forms  # import Django forms module for defining form fields and widgets

class SignUpForm(UserCreationForm):  # custom form subclassing UserCreationForm to add extra fields / widgets
    email = forms.EmailField(Label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}))  # email field; NOTE: use 'label' (lowercase) not 'Label'
    first_name = forms.CharField(Label="",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))  # first name field; same note about 'label'
    last_name = forms.CharField(Label="",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))  # last name field

    class Meta:  # Meta config: tells the ModelForm which model and fields to use
        model = User  # the model tied to this form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # fields to include on the form (order defines rendering order)

    def __init__(self, *args, **kwargs):  # constructor: collects any positional/keyword args passed when instantiating the form
        super(SignUpForm, self).__init__(*args, **kwargs)  # call parent constructor to initialize default fields from UserCreationForm
        #this init calls when any instance of the class is called
        self.fields['username'].widget.attrs['class'] = 'form-control'  # add Bootstrap class to username widget
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'  # set placeholder attribute for username input
        self.fields['username'].label = ''  # remove the label text for username (renders no label)
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'  # override default help text (HTML string)

        self.fields['password1'].widget.attrs['class'] = 'form-control'  # add Bootstrap class to password1 widget
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'  # set placeholder for password1
        self.fields['password1'].label = ''  # remove label text for password1
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'  # detailed HTML help_text for password rules

        self.fields['password2'].widget.attrs['class'] = 'form-control'  # add Bootstrap class to password2 (confirmation) widget
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'  # set placeholder for password2
        self.fields['password2'].label = ''  # remove label for password confirmation
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'  # short help_text for confirmation


