import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

### I used Python PyQt Framework to develop this app ###
### Tasks Fullfilled
# - Kontinuierliche Eingabe von Fließkommazahlen
# - Bestätigung nach jeder Zahl mit z.B. "ENTER" oder Button
# - Nach jeder Eingabe wird der neue Mittelwert aus allen zuvor eingegebenen Zahlen
# Zahlen und der neuen Zahl berechnet und angezeigt
# - Ende der Eingabe/des Programms bei Eingabe von "x" oder alternativ extra
# Taste für "Beenden"
# - Um den Speicherplatz zu minimieren, werden die einzelnen eingegebenen Zahlenwerte nicht gespeichert.
# Zahlenwerte nicht gespeichert werden (nicht auf Diskette, nicht in einem Array)
# Berechnung der neuen

class ContinuousMeanCalculator:
    def __init__(self):
        self.sum = 0.0   ## sum of all the values input
        self.count = 0    ## to keep track of how many numbers have been inputted

    def add_number(self, number: float) -> float:    ## Mean value output  always outputting float values
        self.sum += number    # the new number added to the total sum
        self.count += 1
        return self.sum / self.count        ## Basic formula used to calculate the mean https://www.calculatorsoup.com/calculators/statistics/average.php
                                            ## https://de.wikipedia.org/wiki/Mittelwert


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   ## to load the app components first.
        self.calc = ContinuousMeanCalculator()   ## initialize the instance for calculating average

    def initUI(self):
        self.setWindowTitle('Fortlaufenden Mittelwertberechnung')
        self.setGeometry(200, 200, 400, 300)

        self.main_layout = QVBoxLayout()   ## this is the main Layout

        self.number_label = QLabel('Enter a number:')
        self.number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)   ## just to make it to the center
        self.main_layout.addWidget(self.number_label)

        self.input = QLineEdit(self)
        self.main_layout.addWidget(self.input)

        self.result_label = QLabel('Current Mean: N/A')     ## Display the updated mean
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.result_label)

        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_average)
        self.main_layout.addWidget(self.calculate_button)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)
        self.main_layout.addWidget(self.exit_button)

        self.setLayout(self.main_layout)

        self.input.returnPressed.connect(self.calculate_average)

    def calculate_average(self):     ### This method is directly connected to the input when return is pressed or "Calculate Button" is pressed it reads the inserted value and calculates the average
        input_value = self.input.text()   ## read the input value from the user
        if input_value.lower() == 'x':    ## For exiting the application
            self.close()
        else:
            try:      ### The try and else block is to capture if the user uses a number or not if it doesn't the user is notified to please enter a number

                number = float(input_value)    ## to keep all the values in Floating numbers
                new_average = self.calc.add_number(number)
                self.result_label.setText(f'Current Mean: {new_average:.2f}')
                self.input.clear()   ## to reload the input field ##
            except ValueError:
                self.result_label.setText('Invalid input! Please enter a number.')


if __name__ == '__main__':
    try:
       app = QApplication(sys.argv)
       ex = App()
       ex.show()
       sys.exit(app.exec())

    except Exception as e:
        print(e)
