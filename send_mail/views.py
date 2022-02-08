from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
from .service import send
# from .tasks import send_spam_email


class ContactView(CreateView):
    """Displaying form of subscription at email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'send_mail/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
