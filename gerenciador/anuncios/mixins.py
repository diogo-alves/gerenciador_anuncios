from django.contrib.messages.views import messages


class SuccessMessageDeletionMixin:
    """
    Exibe uma mensagem de sucesso após a exclusão de um objeto.
    """
    success_message = ''

    def delete(self, request, *args, **kwargs):
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_message(self):
        self.object = self.get_object()
        return self.success_message % self.object.__dict__
