from django import forms

from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        exclude = ["created_on", "updated_on", "author"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']


JobFormSet = forms.inlineformset_factory(
    Commission, Job, form=JobForm, extra=1, can_delete=False)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        # 'applicant' is automatically set to the logged-in user
        fields = ['job', 'status']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = 'Pending'  # Initial status
