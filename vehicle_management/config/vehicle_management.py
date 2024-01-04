from frappe import _

def get_data():
    return [
        {
            "label": _("Vehicle Management"),
            "icon": "fa fa-car",
            "items": [
                {
                    "type": "doctype",
                    "name": "Vehicle",
                    "label": _("Vehicle"),
                    "description": _("Manage vehicles."),
                },
                # Add more doctypes as needed
            ],
        },
    ]
