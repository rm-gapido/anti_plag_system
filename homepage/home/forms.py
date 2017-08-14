from django import forms

class DocumentForm(forms.Form):
    doc_title = forms.CharField(max_length=250)
    doc_type = forms.CharField(max_length=10)
    doc_pages = forms.IntegerField()

    # def __str__(self):
        # return "Title: %s, Type: %s, Pages: %d" % (self.doc_title, self.doc_type, self.doc_pages)