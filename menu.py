from PyQt5.QtWidgets import *

import main

app = QApplication([])
window = QWidget()



play_btn = QPushButton("Грати")
seetings_btn = QPushButton("Налаштування")
levels_btn = QPushButton("Рівні")
shop_btn = QPushButton("Магазин")

main_line = QVBoxLayout()
main_line.addWidget(play_btn)
main_line.addWidget(seetings_btn)
main_line.addWidget(levels_btn)
main_line.addWidget(shop_btn)

play_btn.clicked.connect(main.game)



window.setLayout(main_line)
window.show()
app.exec()