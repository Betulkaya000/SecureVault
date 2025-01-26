import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QFormLayout, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QTextEdit
from PyQt5.QtGui import QFont, QClipboard
from PyQt5.QtCore import Qt, QTimer
from password_manager import set_master_password, verify_master_password, load_passwords, save_passwords, generate_key, load_key, save_key, MASTER_PASSWORD_FILE
import os

class PasswordManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 5px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                padding: 10px;
                font-size: 14px;
                background-color: #5cb85c;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
            QPushButton:disabled {
                background-color: #d3d3d3;
                color: #a9a9a9;
            }
            QTableWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #f3f3f3;
                padding: 5px;
                border: 1px solid #ddd;
            }
            QTextEdit {
                background-color: #f3f3f3;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
        """)

        self.layout = QVBoxLayout()

        self.label = QLabel('Ana Şifre:')
        self.layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton('Giriş Yap')
        self.login_button.clicked.connect(self.handle_password)
        self.layout.addWidget(self.login_button)

        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.layout.addWidget(self.console)

        self.setLayout(self.layout)

    def handle_password(self):
        master_password = self.password_input.text()
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists(MASTER_PASSWORD_FILE):
            set_master_password(master_password)
            self.console.append('Başarılı: Ana şifre oluşturuldu!')
        elif verify_master_password(master_password):
            self.console.append('Başarılı: Giriş başarılı!')
            self.login_button.setEnabled(False)  # Butonu devre dışı bırak
            QTimer.singleShot(2000, lambda: self.hide_login_widgets(master_password))  # 2 saniye bekle
        else:
            self.console.append('Hatalı: Hatalı ana şifre!')

    def hide_login_widgets(self, master_password):
        self.login_button.hide()
        self.label.hide()
        self.password_input.hide()
        self.show_main_buttons(master_password)

    def show_main_buttons(self, master_password):
        self.master_password = master_password
        key = load_key()
        if key is None:
            key = generate_key(master_password)
            save_key(key)

        self.key = key
        self.passwords = load_passwords(key)

        self.add_password_button = QPushButton('Yeni Şifre Ekle')
        self.add_password_button.clicked.connect(self.toggle_add_password_section)
        self.layout.addWidget(self.add_password_button)

        self.show_passwords_button = QPushButton('Kayıtlı Şifreleri Göster')
        self.show_passwords_button.clicked.connect(self.toggle_show_passwords)
        self.layout.addWidget(self.show_passwords_button)

        self.password_widgets = []

    def toggle_add_password_section(self):
        if hasattr(self, 'add_password_widgets'):
            for widget in self.add_password_widgets:
                widget.setVisible(not widget.isVisible())
        else:
            self.add_password_section()

    def add_password_section(self):
        self.add_password_widgets = []

        self.add_password_label = QLabel('Yeni Şifre Ekle:')
        self.layout.addWidget(self.add_password_label)
        self.add_password_widgets.append(self.add_password_label)

        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText('Hizmet Adı')
        self.layout.addWidget(self.service_input)
        self.add_password_widgets.append(self.service_input)

        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText('Şifre')
        self.layout.addWidget(self.new_password_input)
        self.add_password_widgets.append(self.new_password_input)

        self.add_button = QPushButton('Ekle')
        self.add_button.clicked.connect(self.add_password)
        self.layout.addWidget(self.add_button)
        self.add_password_widgets.append(self.add_button)

    def add_password(self):
        service = self.service_input.text()
        new_password = self.new_password_input.text()

        if service in self.passwords:
            self.console.append(f'Hata: {service} zaten mevcut!')
        elif service and new_password:
            self.passwords[service] = new_password
            save_passwords(self.key, self.passwords)
            self.console.append(f'{service} için şifre başarıyla eklendi!')
            self.service_input.clear()
            self.new_password_input.clear()
            self.show_passwords()  # Yeni eklenen şifreleri hemen göster
        else:
            self.console.append('Hata: Hizmet adı ve şifre boş olamaz!')

    def toggle_show_passwords(self):
        # Yeni şifre ekleme alanını gizle
        if hasattr(self, 'add_password_widgets'):
            for widget in self.add_password_widgets:
                widget.hide()

        if self.password_widgets:
            for widget in self.password_widgets:
                widget.setVisible(not widget.isVisible())
        else:
            self.show_passwords()

    def show_passwords(self):
        # Önce mevcut şifrelerin görüntülendiği alanları temizleyelim
        for widget in self.password_widgets:
            self.layout.removeWidget(widget)
            widget.deleteLater()
        self.password_widgets.clear()

        # Güncel şifreleri tablo halinde yazdır
        self.passwords_table = QTableWidget()
        self.passwords_table.setRowCount(len(self.passwords))
        self.passwords_table.setColumnCount(2)
        self.passwords_table.setHorizontalHeaderLabels(['Hizmet', 'Şifre'])
        self.passwords_table.horizontalHeader().setStretchLastSection(True)
        self.passwords_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.passwords_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.passwords_table.cellClicked.connect(self.copy_to_clipboard)

        for row, (service, password) in enumerate(self.passwords.items()):
            self.passwords_table.setItem(row, 0, QTableWidgetItem(service))
            self.passwords_table.setItem(row, 1, QTableWidgetItem(password))

        self.layout.addWidget(self.passwords_table)
        self.password_widgets.append(self.passwords_table)

    def copy_to_clipboard(self, row, column):
        item = self.passwords_table.item(row, column)
        if item:
            clipboard = QApplication.clipboard()
            clipboard.setText(item.text())
            if column == 1:
                self.console.append('Şifre başarıyla kopyalandı!')
            else:
                self.console.append(f'{item.text()} kopyalandı!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordManagerApp()
    ex.show()
    sys.exit(app.exec_())