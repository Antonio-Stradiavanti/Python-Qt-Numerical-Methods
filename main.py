import sys
from widget import Widget
from PySide6.QtWidgets import QApplication

def main() -> int :
    app = QApplication(sys.argv)
    widget = Widget()
    widget.resize(800, 482)
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()