import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QPushButton, QCheckBox, QLabel, QWidget, QLineEdit
from functions import (
    deep_folders, rename_and_relocation, rename_and_relocation_without_arch,
    del_empty_dirs, result_sorting_with_arch, result_sorting_without_arch,
)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Папка для сортування:'
        self.initUI()

    def initUI(self):

        
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 500, 300)  # Set the size of the window
        self.setStyleSheet(
        """
                QWidget {
                background-color: #333333;
                color: #FFFFFF;
                font-size: 12px;
                font-weight: 500;
            }

            QPushButton {
                border: 1px solid #AAAAAA;
                padding: 5px;
                border-radius: 10px;
                color: #FFFFFF;
            }

            QPushButton:hover {
                color: #ff4b4b;
                border: 1px solid #ff4b4b;
            }

            QPushButton:pressed {
                border: 1px solid #ff4b4b;
                background-color: #ff4b4b;
            }
            
            QLineEdit {
                background-color: #555555;
                border: 1px solid #555555;
                padding: 5px;
                border-radius: 10px;
                color: rgb(255, 255, 194);
            }

            QCheckBox {
                spacing: 5px;
            }

            QCheckBox::indicator{
                border: 1px solid #555555;
            }

            QCheckBox::indicator:unchecked {
                background-color: #333333;
            }

            QCheckBox::indicator:checked {
                background-color: #a3a3a3; 
            }

            QLabel {
                background-color:rgba(255, 227, 18, 0.2);
                border-radius: 5px;
                padding: 5px;
                color: #FFFFFF;
            }

            """)

        layout = QVBoxLayout()

        self.address = QLineEdit(self)
        self.address.setFixedHeight(40)  # Increase the height of the QLineEdit
        layout.addWidget(self.address)

        self.select_folder = QPushButton('Вибрати папку', self)
        self.select_folder.setFixedHeight(40)  # Increase the height of the QPushButton
        self.select_folder.clicked.connect(self.on_select_folder_click)
        layout.addWidget(self.select_folder)

        self.unpack_var = QCheckBox('Розпаковка архівів', self)
        self.unpack_var.setFixedHeight(40)  # Increase the height of the QCheckBox
        layout.addWidget(self.unpack_var)

        self.deep_var = QCheckBox('Сортувати у вкладених папках', self)
        self.deep_var.setFixedHeight(40)  # Increase the height of the QCheckBox
        layout.addWidget(self.deep_var)

        self.sort_button = QPushButton('Сортувати!', self)
        self.sort_button.setFixedHeight(40)  # Increase the height of the QPushButton
        self.sort_button.clicked.connect(self.on_sort_click)
        layout.addWidget(self.sort_button)

        self.warning = QLabel("ПОПЕРЕДЖЕННЯ! Назви файлів з кириличними символами будуть транслітеровані!")
        self.warning.setFixedHeight(60)  # Increase the height of the QLabel
        layout.addWidget(self.warning)

        self.setLayout(layout)

    def on_select_folder_click(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.address.setText(folder_selected)

    def on_sort_click(self):
        try:
            if self.unpack_var.isChecked() and self.deep_var.isChecked():
                deep_folders(self.address.text())
                rename_and_relocation(self.address.text())
                result_sorting_with_arch(self.address.text())
            elif self.unpack_var.isChecked() and not self.deep_var.isChecked():
                rename_and_relocation(self.address.text())
                result_sorting_with_arch(self.address.text())
            elif not self.unpack_var.isChecked() and self.deep_var.isChecked():
                deep_folders(self.address.text())
                rename_and_relocation_without_arch(self.address.text())
                result_sorting_without_arch(self.address.text())
            else:
                rename_and_relocation_without_arch(self.address.text())
                del_empty_dirs(self.address.text())
                result_sorting_without_arch(self.address.text())
        except Exception as e:
            self.warning.setText(f"Помилка: {str(e)}")

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
