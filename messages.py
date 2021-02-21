class UIMessages:

    def __init__(self, lang: str):
        self.msg = {
            "apptitle": {
                "en": "DEV Activities tracker",
                "es": "DEV Registro de actividades",
                "pt": "DEV Registro de atividades"
            },
            "task": {
                "en": "Task",
                "es": "Actividad",
                "pt": "Atividade"
            },
            "duedate": {
                "en": "Due date",
                "es": "Fecha/hora límite",
                "pt": "Data/hora limite"
            },
            "info": {
                "en": "Additional information",
                "es": "Información adicional",
                "pt": "Informação adicional"
            }
        }
        self.lang = lang

    def __getitem__(self, string: str):
        return self.msg[string][self.lang]
