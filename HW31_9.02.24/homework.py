import sys
import cloud_service_module # Якобы модуль для работы с облачным сервисом
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QMessageBox, QPushButton, QFileDialog
import requests
import os
from contact_links_dialog import ContactLinksDialog # Якобы диалоговое окно для добавления связей контактов

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

        self.upload_button = QPushButton("Загрузить фотографии")
        self.upload_button.clicked.connect(self.upload_photos)
        self.layout.addWidget(self.upload_button)

        self.central_widget.setLayout(self.layout)

    def add_contact_links(self):
        dialog = ContactLinksDialog(self)
        if dialog.exec() == ContactLinksDialog.Accepted:
            selected_contacts = dialog.get_selected_contacts()

    def save_to_cloud(self):
        data = self.response_output.toPlainText()
        success = cloud_service_module.upload_data(data)
        if success:
            QMessageBox.information(self, "Сохранение в облако", "Данные успешно сохранены в облаке")
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить данные в облаке")

    def upload_photos(self):
        options = QFileDialog.Options()
        file_names, _ = QFileDialog.getOpenFileNames(self, "Выбрать фотографии", "",
                                                     "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_names:
            QMessageBox.information(self, "Загрузка фотографий", f"Выбрано {len(file_names)} файлов")

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