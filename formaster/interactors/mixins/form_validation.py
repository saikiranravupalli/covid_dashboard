class FormValidationMixin:

    def validate_for_live_form(self, form_id: int):
        self.storage.validate_for_live_form(form_id)
