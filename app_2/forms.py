from django import forms

class TestForm(forms.Form):
    # T = [
    #     {'id':1, 'status':'boss'},
    #     {'id':2, 'status':'std'},
	# ]
    
    position = forms.CharField(max_length=60, required=True, label='name position')
    # status = forms.ModelMultipleChoiceField(
    #     queryset=T,
    #     required=True,
    #     label='name status'
	# )