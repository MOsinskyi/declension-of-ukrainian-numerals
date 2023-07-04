import customtkinter as ctk
from random import randint
from declension_system import *
from CTkMessagebox import CTkMessagebox


DECLENSIONS = ["H.", "P.", "Д.", "З.", "О.", "М."]
CASE_LABELS = ["nominative", "genitive", "dative", "accusative", "ablative", "local"]

MAX_NUMBER = 999999

# Fonts
HEADER_FONT = ("Ubuntu", 22)
ELEMENTS_FONT = ("Ubuntu", 15)
BUTTON_FONT = ("Ubuntu", 12)

# Window
window = ctk.CTk()


# Settings Frame
class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.min_random_number = MAX_NUMBER // 2
        self.max_random_number = MAX_NUMBER // 2
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Налаштування", font=HEADER_FONT).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Мінімальне число", font=ELEMENTS_FONT).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Максимальне число", font=ELEMENTS_FONT).grid(row=4, column=0, padx=5, pady=5)

        self.min_number_label = ctk.CTkLabel(self, text=str(self.min_random_number), font=ELEMENTS_FONT)
        self.min_number_label.grid(row=2, column=0, padx=5, pady=5)
        self.max_number_label = ctk.CTkLabel(self, text=str(self.max_random_number), font=ELEMENTS_FONT)
        self.max_number_label.grid(row=5, column=0, padx=5, pady=5)

        self.min_number_slider = ctk.CTkSlider(self, from_=0, to=MAX_NUMBER, number_of_steps=MAX_NUMBER,
                                               command=self.min_slider_event)
        self.min_number_slider.grid(row=3, column=0, padx=5, pady=5)

        self.max_number_slider = ctk.CTkSlider(self, from_=0, to=MAX_NUMBER, number_of_steps=MAX_NUMBER,
                                               command=self.max_slider_event)
        self.max_number_slider.grid(row=6, column=0, padx=5, pady=5)

    def min_slider_event(self, value):
        self.min_number_label.configure(text=str(round(value)))
        self.min_random_number = round(value)

    def max_slider_event(self, value):
        self.max_number_label.configure(text=str(round(value)))
        self.max_random_number = round(value)


settings_frame = SettingsFrame(window)
settings_frame.grid(row=0, column=1, padx=10, pady=10)


# Input Frame
class InputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.random_number = 0
        self.case_entries = []
        self.create_widgets()
        self.nominative_number = ''
        self.genitive_number = ''
        self.dative_number = ''
        self.accusative_number = ''
        self.ablative_number = ''
        self.local_number = ''

    def create_widgets(self):
        self.random_number_label = ctk.CTkLabel(self, text="000000", font=HEADER_FONT)
        self.random_number_label.grid(row=0, column=0, columnspan=2)

        for i in range(len(DECLENSIONS)):
            ctk.CTkLabel(self, text=DECLENSIONS[i], font=ELEMENTS_FONT).grid(row=i + 1, column=0, sticky='w', padx=5,
                                                                             pady=5)

        for i in range(len(CASE_LABELS)):
            case_entry = ctk.CTkEntry(self, width=300, height=15)
            case_entry.grid(row=i + 1, column=1, padx=5, pady=5)
            self.case_entries.append(case_entry)

        start_button = ctk.CTkButton(self, text="Згенерувати число", font=BUTTON_FONT,
                                     command=self.generate_number)
        start_button.grid(row=len(CASE_LABELS) + 1, column=0, padx=5, pady=5, columnspan=2, sticky='w')

        check_button = ctk.CTkButton(self, text="Перевірити", font=BUTTON_FONT, command=self.check_solution)
        check_button.grid(row=len(CASE_LABELS) + 1, column=1, padx=5, pady=5, sticky='e')

    def generate_number(self):

        self.random_number = randint(settings_frame.min_random_number, settings_frame.max_random_number)
        self.random_number_label.configure(text=str(self.random_number))

        self.nominative_number, self.genitive_number, self.dative_number, self.accusative_number, self.ablative_number, \
            self.local_number = declension_number(self.random_number)

        print(self.nominative_number, self.genitive_number, self.dative_number, self.accusative_number,
              self.ablative_number, self.local_number)

    def check_solution(self):
        if(self.case_entries[0].get() == self.nominative_number and self.case_entries[1].get() == self.genitive_number
                and self.case_entries[2].get() == self.dative_number and self.case_entries[3].get() ==
                self.accusative_number and self.case_entries[4].get() == self.ablative_number and
                self.case_entries[5].get() == self.local_number):
            CTkMessagebox(title="Результат", message="Все правильно, так тримати!", icon="check")


input_frame = InputFrame(window)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Close Window
window.mainloop()
