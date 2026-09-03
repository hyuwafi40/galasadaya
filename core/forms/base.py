from django import forms


class BaseFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if widget.__class__.__module__.startswith("django_ckeditor_5"):
                continue
            attrs = widget.attrs
            if isinstance(widget, forms.CheckboxInput):
                attrs["class"] = "toggle-switch"
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                attrs["class"] = "tag-checkbox-list"
            elif isinstance(widget, forms.DateInput):
                attrs.update(
                    {
                        "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                        "type": "date",
                    }
                )
            elif isinstance(
                widget,
                (
                    forms.TextInput,
                    forms.EmailInput,
                    forms.URLInput,
                    forms.PasswordInput,
                    forms.Textarea,
                    forms.Select,
                    forms.SelectMultiple,
                    forms.NumberInput,
                ),
            ):
                attrs["class"] = (
                    "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800"
                )
