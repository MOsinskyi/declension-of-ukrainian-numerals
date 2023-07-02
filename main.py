import customtkinter as ctk
from random import randint

DECLENSIONS = ["H.", "P.", "Д.", "З.", "О.", "М."]
CASE_LABELS = ["nominative", "genitive", "dative", "accusative", "ablative", "local"]

MAX_NUMBER = 999999

# Fonts
HEADER_FONT = ("Ubuntu", 22)
ELEMENTS_FONT = ("Ubuntu", 15)
BUTTON_FONT = ("Ubuntu", 12)

# Window
window = ctk.CTk()
window.geometry("600x310")
window.title("Declension of Ukrainian numerals")

# Settings Frame
settings_frame = ctk.CTkFrame(window)

ctk.CTkLabel(settings_frame, text="Налаштування", font=HEADER_FONT).grid(row=0, column=0, padx=5, pady=5)
ctk.CTkLabel(settings_frame, text="Мінімальне число", font=ELEMENTS_FONT).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkLabel(settings_frame, text="Максимальне число", font=ELEMENTS_FONT).grid(row=4, column=0, padx=5, pady=5)

min_random_number = MAX_NUMBER // 2
max_random_number = MAX_NUMBER // 2

min_number_label = ctk.CTkLabel(settings_frame, text=str(min_random_number), font=ELEMENTS_FONT)
min_number_label.grid(row=2, column=0, padx=5, pady=5)
max_number_label = ctk.CTkLabel(settings_frame, text=str(max_random_number), font=ELEMENTS_FONT)
max_number_label.grid(row=5, column=0, padx=5, pady=5)


def min_slider_event(value):
    min_number_label.configure(text=str(round(value)))
    global min_random_number
    min_random_number = round(value)


def max_slider_event(value):
    max_number_label.configure(text=str(round(value)))
    global max_random_number
    max_random_number = round(value)


min_number_slider = ctk.CTkSlider(settings_frame, from_=0, to=MAX_NUMBER, number_of_steps=MAX_NUMBER,
                                  command=min_slider_event)
min_number_slider.grid(row=3, column=0, padx=5, pady=5)

max_number_slider = ctk.CTkSlider(settings_frame, from_=0, to=MAX_NUMBER, number_of_steps=MAX_NUMBER,
                                  command=max_slider_event)
max_number_slider.grid(row=6, column=0, padx=5, pady=5)

settings_frame.grid(row=0, column=1, padx=10, pady=10)

# Input Frame
input_frame = ctk.CTkFrame(window)

random_number_label = ctk.CTkLabel(input_frame, text="000000", font=HEADER_FONT)
random_number_label.grid(row=0, column=0, columnspan=2)

for i in range(len(DECLENSIONS)):
    ctk.CTkLabel(input_frame, text=DECLENSIONS[i], font=ELEMENTS_FONT).grid(row=i+1, column=0, sticky='w', padx=5,
                                                                            pady=5)

case_entries = []

for i, case_label in enumerate(CASE_LABELS):
    case_entry = ctk.CTkEntry(input_frame, width=300, height=15)
    case_entry.grid(row=i+1, column=1, padx=5, pady=5)
    case_entries.append(case_entry)


def generate_number():
    random_number = randint(min_random_number, max_random_number)
    random_number_label.configure(text=str(random_number))


start_button = ctk.CTkButton(input_frame, text="Згенерувати число", font=BUTTON_FONT,
                             command=generate_number)
start_button.grid(row=7, column=0, padx=5, pady=5, columnspan=2, sticky='w')

check_button = ctk.CTkButton(input_frame, text="Перевірити", font=BUTTON_FONT)
check_button.grid(row=7, column=1, padx=5, pady=5, sticky='e')

input_frame.grid(row=0, column=0, padx=10, pady=10)


# Close Window
window.mainloop()
