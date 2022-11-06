from django import forms


class CreateReviewForm(forms.Form):
    score = forms.IntegerField(min_value=0, max_value=5)
    review_text = forms.CharField(max_length=200)

    def clean(self):
        data = super().clean()
        cleaned_data = {}
        contains_score = False
        contains_listing = False
        contains_text = False

        for key, value in data.items():
            if key == 'score':
                contains_score = True
                cleaned_data['score'] = data['score']
            if key == 'listing':
                contains_listing = True
                cleaned_data['listing'] = data['listing']
            if key == 'text':
                contains_text = True
                cleaned_data['text'] = data['text']

        return cleaned_data
