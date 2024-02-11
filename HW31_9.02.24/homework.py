import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox
import requests
import os

class JSONPlaceholderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSONPlaceholder Request Tool")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.id_label = QLabel("ID пользователя:")
        self.layout.addWidget(self.id_label)
        self.id_input = QLineEdit()
        self.layout.addWidget(self.id_input)

        self.send_button = QPushButton("Отправить запрос")
        self.send_button.clicked.connect(self.send_request)
        self.layout.addWidget(self.send_button)

        self.response_label = QLabel("Ответ:")
        self.layout.addWidget(self.response_label)
        self.response_output = QTextEdit()
        self.layout.addWidget(self.response_output)

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_response)
        self.layout.addWidget(self.save_button)

        self.central_widget.setLayout(self.layout)

    def send_request(self):
        user_id = self.id_input.text()
        try:
            response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
            data = response.json()
            self.response_output.setPlainText(str(data))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка запроса", str(e))

    def save_response(self):
        data = self.response_output.toPlainText()
        foldername = 'saved_data'
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        with open(os.path.join(foldername, 'data.json'), 'w') as file:
            file.write(data)
            QMessageBox.information(self, "Данные сохранены", "Данные успешно сохранены.")

def main():
    app = QApplication(sys.argv)
    window = JSONPlaceholderApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()