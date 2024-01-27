# Function to add an outline to a layout
def add_outline(layout):
    container_widget = QWidget()
    container_layout = QVBoxLayout(container_widget)
    container_layout.addLayout(layout)

    container_widget.setContentsMargins(5, 5, 5, 5)  # Set margins
    container_widget.setObjectName("outlinedLayout")  # Set an object name for styling
    container_widget.setStyleSheet(
        "#outlinedLayout { border: 2px solid rgb(211, 211, 211); border-radius: 5px; }")

    return container_widget

import sys
print(sys.executable)
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QDateEdit, \
    QRadioButton, QComboBox, QPushButton, QLabel, QGridLayout, QSpacerItem, QSizePolicy, QTableWidget, QTextEdit, QFrame, QHeaderView

from PyQt6.QtGui import  QColor, QPainter, QFont, QBrush, QIcon
from PyQt6.QtCore import Qt, QDate, QElapsedTimer, QTimer, QCoreApplication  # Add QDate to the import statement
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis  # Import necessary chart classes

# Import statements for labjacku3.py and proximity.py
#from labjacku3 import write_data_to_file  # Replace 'labjack_function' with the actual function name
#from proximity import read_proximity_sensor  # Replace 'ProximitySensor' with the actual class name

class MainWindow(QMainWindow):



    def print_chart(self):
        # Create a folder named 'chart_print' if it doesn't exist
        folder_name = 'chart_print'
        os.makedirs(folder_name, exist_ok=True)

        # Get the current date as a string
        current_date = QDate.currentDate().toString("yyyy-MM-dd")

        # Construct the file name with the current date
        base_file_name = f"{current_date}_chart.jpg"

        # Check if the file already exists
        file_name = base_file_name
        count = 1
        while os.path.exists(os.path.join(folder_name, file_name)):
            file_name = f"{current_date}_chart_{count}.jpg"
            count += 1

        # Create a QPixmap of the chart view
        chart_view = self.findChild(QChartView)
        chart_pixmap = chart_view.grab()

        # Save the QPixmap as a JPG file in the 'chart_print' folder
        file_path = os.path.join(folder_name, file_name)
        chart_pixmap.save(file_path, "JPG")

        print(f"Chart saved to: {file_path}")

    def create_chart(self):
        # Create a line chart

        chart = QChart()

        # Create axes for x and y
        axis_x = QValueAxis()
        axis_y = QValueAxis()

        # Set ranges for the axes
        axis_x.setRange(1, 10)
        axis_y.setRange(0, 5000)  # Adjust the range based on your data

        # Set labels for the axes
        axis_x.setTitleText("Test")
        axis_y.setTitleText("RPM")

        # Add axes to the chart
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        # Create line series for NE, NC, NOCC, and Ratio
        ne_series = QLineSeries()
        nc_series = QLineSeries()
        nocc_series = QLineSeries()
        ratio_series = QLineSeries()

        # Add data points to the series (assuming you have data for each point)
        # Replace the following lines with your actual data
        # Assuming you have data for each point
        ne_value = [200, 300, 600, 800, 900, 2000, 2000,1500, 1500, 1500, 1500, 1500]  # Replace 'your_ne_data' with your NE data
        nc_value = [500, 500, 700, 600, 800, 3000, 2000, 2000, 2000, 2000, 2000, 2000]  # Replace 'your_nc_data' with your NC data
        nocc_value = [300, 100, 400, 700, 400, 1000, 3000, 3000, 3000, 3000, 3000, 3000]  # Replace 'your_nocc_data' with your NOCC data
        ratio_value = [200, 400, 200, 200, 500, 4000, 3000, 3500, 3500, 3500, 3500,3500]  # Replace 'your_ratio_data' with your Ratio data

        # Ensure that each series has data points for x values from 1 to 10
        ne_value += [0] * (10 - len(ne_value))
        nc_value += [0] * (10 - len(nc_value))
        nocc_value += [0] * (10 - len(nocc_value))
        ratio_value += [0] * (10 - len(ratio_value))

        # Add data points to the NE series
        data_points_ne = [(i, val) for i, val in enumerate(ne_value, start=1)]
        for x, y in data_points_ne:
            ne_series.append(x, y)

        # Add data points for NC
        data_points_nc = [(i, val) for i, val in enumerate(nc_value, start=1)]
        for x, y in data_points_nc:
            nc_series.append(x, y)

        # Add data points for NOCC
        data_points_nocc = [(i, val) for i, val in enumerate(nocc_value, start=1)]
        for x, y in data_points_nocc:
            nocc_series.append(x, y)

        # Add data points for Ratio
        data_points_ratio = [(i, val) for i, val in enumerate(ratio_value, start=1)]
        for x, y in data_points_ratio:
            ratio_series.append(x, y)

        # Add series to the chart
        chart.addSeries(ne_series)
        chart.addSeries(nc_series)
        chart.addSeries(nocc_series)
        chart.addSeries(ratio_series)

        # Attach axes to the series
        ne_series.attachAxis(axis_x)
        ne_series.attachAxis(axis_y)

        nc_series.attachAxis(axis_x)
        nc_series.attachAxis(axis_y)

        nocc_series.attachAxis(axis_x)
        nocc_series.attachAxis(axis_y)

        ratio_series.attachAxis(axis_x)
        ratio_series.attachAxis(axis_y)

        # Set chart title and show legend
        # chart.setTitle("Multiline Chart")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.legend().setVisible(False)

        # Customize the appearance of the x-axis
        axis_x.setTitleBrush(QBrush(Qt.GlobalColor.green))  # Set the color of the x-axis label
        axis_x.setTitleFont(QFont("Arial", 10, QFont.Weight.Bold))  # Set font for x-axis label
        axis_x.setLabelsBrush(QBrush(Qt.GlobalColor.blue))  # Set the color of x-axis tick labels
        axis_x.setLabelsFont(QFont("Arial", 8))  # Set font for x-axis tick labels

        # Customize the appearance of the y-axis
        axis_y.setTitleBrush(QBrush(Qt.GlobalColor.red))  # Set the color of the y-axis label
        axis_y.setTitleFont(QFont("Arial", 10, QFont.Weight.Bold))  # Set font for y-axis label
        axis_y.setLabelsBrush(QBrush(Qt.GlobalColor.magenta))  # Set the color of y-axis tick labels
        axis_y.setLabelsFont(QFont("Arial", 8))  # Set font for y-axis tick labels

        print(data_points_ne)
        print(data_points_nc)
        print(data_points_nocc)
        print(data_points_ratio)

        return chart

    # Add this method to your MainWindow class
    def start_stopwatch_and_update_indicators(self):
        try:
            if not self.elapsed_timer.isValid():
                self.elapsed_timer.start()
                self.display_timer.start()
                self.update_color_indicators()
        except Exception as e:
            print(f"Error in start_stopwatch_and_update_indicators: {e}")

    # Add this method to your MainWindow class
    def reset_indicators(self):
        self.buttonNE.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 30px; }")
        self.buttonNE1.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 30px; }")
        self.buttonNE2.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 30px; }")

        self.buttonNC.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")
        self.buttonNC1.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")
        self.buttonNC2.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")

        self.buttonNOCC.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")
        self.buttonNOCC1.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")
        self.buttonNOCC2.setStyleSheet("QFrame { background-color: grey; border: 2px solid grey; border-radius: 13px; }")

    def create_indicator(self, color):
        # Create a QVBoxLayout to hold the indicator elements
        indicator_layout = QVBoxLayout()

        # Create indicator_frame
        indicator_frame = QFrame()
        indicator_frame.setFixedWidth(80)
        indicator_frame.setFixedHeight(25)
        indicator_frame.setStyleSheet("QFrame { background-color: grey; border-radius: 13px; }")

        # Add the square to the layout
        indicator_layout.addWidget(indicator_frame)

        indicator_layout.setContentsMargins(0, 0, 0, 0)


        # Create a QRadioButton to hold the layout
        indicator_button = QRadioButton()
        indicator_button.setLayout(indicator_layout)

        # Set a fixed size for the indicator button
        indicator_button.setFixedSize(90, 25)

        return indicator_button

    def clear_indicator_frame_background(self):
        # Clear the background-color of the indicator_frame
        self.buttonNE.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNE1.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNE2.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")

        self.buttonNC.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNC1.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNC2.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")

        self.buttonNOCC.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNOCC1.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")
        self.buttonNOCC2.layout().itemAt(0).widget().setStyleSheet("QFrame { background-color: ; }")

    def update_color_indicators(self):
        ne_color = "grey" if self.buttonNE.isChecked() else "green"
        ne_color1 = "grey" if self.buttonNE1.isChecked() else "green"
        ne_color2 = "grey" if self.buttonNE2.isChecked() else "green"


        nc_color = "grey" if self.buttonNC.isChecked() else "green"
        nc_color1 = "grey" if self.buttonNC1.isChecked() else "green"
        nc_color2 = "grey" if self.buttonNC2.isChecked() else "green"

        nocc_color = "grey" if self.buttonNOCC.isChecked() else "green"
        nocc_color1 = "grey" if self.buttonNOCC1.isChecked() else "green"
        nocc_color2 = "grey" if self.buttonNOCC2.isChecked() else "green"

        self.buttonNE.setStyleSheet(
            f"QFrame {{ border: 2px solid {ne_color}; border-radius: 30px; background-color: {ne_color}; }}"
        )
        self.buttonNE1.setStyleSheet(
            f"QFrame {{ border: 2px solid {ne_color1}; border-radius: 30px; background-color: {ne_color1}; }}"
        )
        self.buttonNE2.setStyleSheet(
            f"QFrame {{ border: 2px solid {ne_color2}; border-radius: 30px; background-color: {ne_color2}; }}"
        )



        self.buttonNC.setStyleSheet(
            f"QFrame {{ border: 2px solid {nc_color}; border-radius: 13px; background-color: {nc_color}; }}"
        )
        self.buttonNC1.setStyleSheet(
            f"QFrame {{ border: 2px solid {nc_color1}; border-radius: 13px; background-color: {nc_color1}; }}"
        )
        self.buttonNC2.setStyleSheet(
            f"QFrame {{ border: 2px solid {nc_color2}; border-radius: 13px; background-color: {nc_color2}; }}"
        )



        self.buttonNOCC.setStyleSheet(
            f"QFrame {{ border: 2px solid {nocc_color}; border-radius: 13px; background-color: {nocc_color}; }}"
        )
        self.buttonNOCC1.setStyleSheet(
            f"QFrame {{ border: 2px solid {nocc_color1}; border-radius: 13px; background-color: {nocc_color1}; }}"
        )
        self.buttonNOCC2.setStyleSheet(
            f"QFrame {{ border: 2px solid {nocc_color2}; border-radius: 13px; background-color: {nocc_color2}; }}"
        )

        # Clear the background-color of the indicator_frame
        self.clear_indicator_frame_background()

    # Function to update button style based on the toggle state
    # Modify the update_button_style function to take an optional color argument
    def update_button_style(self, button, color="green"):
        if button.isChecked():
            button.setStyleSheet(
                f"QPushButton {{"
                f"   background-color: {color};"
                f"   border: 2px solid {color};"
                f"   color: white;"
                f"   border-radius: 5px;"
                f"}}"
            )
        else:
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: transparent;"
                "   border: none;"
                "   color: black;"
                "   border-radius: 5px;"
                "}"
            )
    def __init__(self):
        super().__init__()

        # Add this function to your MainWindow class

        self.setWindowTitle("Rotary Encoder Data Logger")
        self.resize(1366, 768)  # Set initial size

        # Create central widget and layout
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)  # Use QVBoxLayout for the main layout
        self.setCentralWidget(central_widget)

        # Create the first combined layout on the top
        combined_layout_top = QHBoxLayout()

        # Create the second combined layout on the bottom
        combined_layout_bottom = QHBoxLayout()

        # Create the second combined layout on the bottom
        combined_layout_bottom1 = QHBoxLayout()

        # Create the second combined layout on the bottom
        combined_layout_bottom2 = QHBoxLayout()

        # Create the left layout
        combined_layout_left = QVBoxLayout()

        # Create dynamic labels
        self.dynamic_labels = []  # Make it an instance variable

        # Function to update dynamic labels
        def update_dynamic_labels(radio_button):
            if radio_button.isChecked():
                self.row_label0.setText(radio_button.text())
                # Toggle visibility of the notes input based on the selected radio button
                self.notes_input.setVisible(radio_button is self.radio_buttonOT)

        # Add date input form
        self.date_input = QDateEdit()
        self.date_input.setObjectName("date_input")
        self.date_input.setMinimumSize(250, 32)
        self.date_input.setMaximumSize(250, 32)
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())  # Set initial date to the current date
        combined_layout_left.addWidget(self.date_input)

        # Add layout for the text_input and radio_button pair
        row_layout = QHBoxLayout()
        row_label = QLabel("Model")
        row_label.setFixedWidth(150)
        text_input = QLineEdit()
        text_input.setFixedWidth(250)

        # Add an empty QLabel to introduce some blank space between the label and radio button
        spacer_label = QLabel("")
        spacer_label.setFixedWidth(150)

        radio_buttonID = QRadioButton("IDLE")
        radio_buttonID.toggled.connect(lambda: update_dynamic_labels(radio_buttonID))
        row_layout.addWidget(row_label)
        row_layout.addWidget(text_input)
        row_layout.addWidget(spacer_label)
        row_layout.addWidget(radio_buttonID)
        combined_layout_left.addLayout(row_layout)

        # Add layout for the text_input1 and radio_button1 pair
        row_layout1 = QHBoxLayout()
        row_label1 = QLabel("Engine No.")
        row_label1.setFixedWidth(150)
        text_input1 = QLineEdit()
        text_input1.setFixedWidth(250)

        # Add an empty QLabel to introduce some blank space between the label and radio button
        spacer_label1 = QLabel("")
        spacer_label1.setFixedWidth(150)

        radio_buttonCI = QRadioButton("CLUTCH IN")
        radio_buttonCI.toggled.connect(lambda: update_dynamic_labels(radio_buttonCI))
        row_layout1.addWidget(row_label1)
        row_layout1.addWidget(text_input1)
        row_layout1.addWidget(spacer_label1)
        row_layout1.addWidget(radio_buttonCI)
        combined_layout_left.addLayout(row_layout1)

        # Add layout for the text_input1 and radio_button1 pair
        row_layout2 = QHBoxLayout()
        row_label2 = QLabel("Frame No.")
        row_label2.setFixedWidth(150)
        text_input2 = QLineEdit()
        text_input2.setFixedWidth(250)

        # Add an empty QLabel to introduce some blank space between the label and radio button
        spacer_label2 = QLabel("")
        spacer_label2.setFixedWidth(150)

        radio_buttonTA = QRadioButton("TOP ALL LOAD RATIO")
        radio_buttonTA.toggled.connect(lambda: update_dynamic_labels(radio_buttonTA))
        row_layout2.addWidget(row_label2)
        row_layout2.addWidget(text_input2)
        row_layout2.addWidget(spacer_label2)
        row_layout2.addWidget(radio_buttonTA)
        combined_layout_left.addLayout(row_layout2)

        # Add layout for the text_input1 and radio_button1 pair
        row_layout3 = QHBoxLayout()
        row_label3 = QLabel("Distance")
        row_label3.setFixedWidth(150)
        text_input3 = QLineEdit()
        text_input3.setFixedWidth(250)

        # Add an empty QLabel to introduce some blank space between the label and radio button
        spacer_label3 = QLabel("")
        spacer_label3.setFixedWidth(150)

        radio_buttonCS = QRadioButton("CLUTCH STALL")
        radio_buttonCS.toggled.connect(lambda: update_dynamic_labels(radio_buttonCS))
        row_layout3.addWidget(row_label3)
        row_layout3.addWidget(text_input3)
        row_layout3.addWidget(spacer_label3)
        row_layout3.addWidget(radio_buttonCS)
        combined_layout_left.addLayout(row_layout3)

        # Add layout for the text_input1 and radio_buttonOT pair
        row_layout4 = QHBoxLayout()
        row_label4 = QLabel("PIC")
        row_label4.setFixedWidth(150)
        text_input4 = QLineEdit()
        text_input4.setFixedWidth(250)
        self.radio_buttonOT = QRadioButton("OTHER")  # Use self.radio_buttonOT
        self.radio_buttonOT.toggled.connect(lambda: update_dynamic_labels(self.radio_buttonOT))

        # Add an empty QLabel to introduce some blank space between the label and radio button
        spacer_label4 = QLabel("")
        spacer_label4.setFixedWidth(150)

        row_layout4.addWidget(row_label4)
        row_layout4.addWidget(text_input4)
        row_layout4.addWidget(spacer_label4)
        row_layout4.addWidget(self.radio_buttonOT)
        combined_layout_left.addLayout(row_layout4)

        # Create notes input textbox
        self.notes_input = QTextEdit()
        self.notes_input.setFixedWidth(980)
        self.notes_input.setFixedHeight(150)
        self.notes_input.setPlaceholderText("Enter notes here...")
        self.notes_input.setVisible(False)  # Initially set to invisible

        # Set the fixed width for the left layout
        combined_widget_left = add_outline(combined_layout_left)
        combined_widget_left.setFixedWidth(740)  # Set the fixed width for the left layout
        combined_widget_left.setFixedHeight(250)  # Set the fixed width for the left layout

        # Create the right layout
        combined_layout_right = QVBoxLayout()

        # Add widgets to the right layout (similar structure as the left one)
        # Add line chart if QtCharts is available

        # Create a container widget for the chart view and print button
        chart_and_print_container = QWidget()
        chart_and_print_layout = QVBoxLayout(chart_and_print_container)


        # Call create_chart to create the chart and add it to the layout
        chart = self.create_chart()

        # Create axes for x and y
        axis_x = QValueAxis()
        axis_y = QValueAxis()

        # Set font size for the axis labels
        label_font = QFont("Arial", 10)  # Change "Arial" to your desired font family and 10 to the desired font size
        axis_x.setLabelsFont(label_font)
        axis_y.setLabelsFont(label_font)

        # Create a chart view and set the chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)  # Optional: Enable antialiasing

        # Create a print button with a printing icon
        print_button = QPushButton()
        print_button.setIcon(QIcon('icon/icons8-print-48.png'))  # Replace 'path/to/print_icon.png' with the actual path
        print_button.setToolTip('Print Chart')  # Optional: Add tooltip
        print_button.setFixedSize(30, 30)  # Set a fixed size for the button
        print_button.clicked.connect(self.print_chart)

        # Create a container widget for the chart view and print button
        chart_container = QWidget()
        chart_container_layout = QVBoxLayout(chart_container)
        chart_container_layout.addWidget(chart_view)
        chart_and_print_layout.addWidget(print_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Set margins to 0 for the container widget
        chart_container_layout.setContentsMargins(0, 0, 0, 0)

        # Add chart view to layout or widget as needed
        combined_layout_right.addWidget(chart_container)

        # Add chart view to layout or widget as needed
        combined_layout_right.addWidget(chart_view)

        # Set the fixed width for the right layout
        combined_widget_right = add_outline(combined_layout_right)
        combined_widget_right.setFixedWidth(620)  # Set the fixed width for the right layout
        combined_widget_right.setFixedHeight(250)  # Set the fixed width for the left layout

        # Add both combined layouts to the top layout
        combined_layout_top.addWidget(combined_widget_left)
        combined_layout_top.addWidget(combined_widget_right)

        # SECOND ROW BOX
        # Repeat the process for the second set of layouts (box2 and box3)
        combined_layout_box2 = QGridLayout()

        # Add "Empty" label and radio button to the third column
        # Add dynamic label for IDLE with bold text and adjustable font size
        self.row_label0 = QLabel("IDLE")  # Make it an instance variable
        font = self.row_label0.font()  # Get the current font
        font.setBold(True)  # Set the font to bold
        font.setPointSize(18)  # Set the desired font size
        self.row_label0.setFont(font)  # Apply the modified font to the label
        self.row_label0.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.row_label0.setStyleSheet("color: blue;")  # Set the font color to blue
        combined_layout_box2.addWidget(self.row_label0, 1, 0, 2, 2)

        # Font for the label
        font_duration_label = QFont("Arial", 14)  # Adjust the font family and size as needed

        # Add "Duration" label and radio button to the first column
        row_label = QLabel("Duration:")
        row_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        row_label.setFont(font_duration_label)  # Set the font for the label
        combined_layout_box2.addWidget(row_label, 3, 0, 2, 1)

        # Add dropdown menu to the second column
        dropdown = QComboBox()
        dropdown.addItems([str(i) for i in range(1, 11)])

        # Set the default selected value to 3
        default_index = dropdown.findText("3")
        if default_index != -1:
            dropdown.setCurrentIndex(default_index)

        # Set font size for the default item
        font = dropdown.font()
        font.setPointSize(14)  # Set the desired font size for the default item
        dropdown.setFont(font)

        dropdown.setFixedWidth(100)  # Set the desired fixed width
        combined_layout_box2.addWidget(dropdown, 3, 1, 2, 1)

        radio_button = QRadioButton("Auto Test")
        font = radio_button.font()  # Get the current font
        font.setPointSize(14)  # Set the desired font size
        font.setBold(True)  # Make the text bold
        radio_button.setFont(font)  # Apply the modified font to the radio button
        combined_layout_box2.addWidget(radio_button, 4, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add "Empty" label and radio button to the third column
        row_label1 = QLabel("")
        row_label1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box2.addWidget(row_label1, 4, 0)

        # Font for the label
        font_time_label = QFont("Arial", 14)  # Adjust the font family and size as needed

        row_label1 = QLabel("Time Limit:")
        row_label1.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        row_label1.setFont(font_time_label)  # Set the font for the label
        combined_layout_box2.addWidget(row_label1, 5, 0, 2, 1)

        # Add dropdown menu to the fourth column
        dropdown1 = QComboBox()
        dropdown1.addItems([str(i) for i in range(1, 11)])
        combined_layout_box2.addWidget(dropdown1, 5, 1, 2, 1)
        # Set font size for the default item
        font = dropdown1.font()
        font.setPointSize(14)  # Set the desired font size for the default item
        dropdown1.setFont(font)


        radio_button1 = QRadioButton("Manual Test")
        font = radio_button1.font()  # Get the current font
        font.setPointSize(14)  # Set the desired font size
        font.setBold(True)  # Make the text bold
        radio_button1.setFont(font)  # Apply the modified font to the radio button
        combined_layout_box2.addWidget(radio_button1, 4, 3, alignment=Qt.AlignmentFlag.AlignLeft)

        # Add "Empty" label and radio button to the third column
        row_labelRPM = QLabel("RPM COUNTER DEVICE")
        row_labelRPM.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        # Set font size for the label
        font = row_labelRPM.font()
        font.setPointSize(14)  # Set the desired font size
        row_labelRPM.setFont(font)

        combined_layout_box2.addWidget(row_labelRPM, 1, 4, 1, 3)

        # Set the font to bold
        font = row_labelRPM.font()
        font.setBold(True)
        row_labelRPM.setFont(font)

        # Create the indicators for NE, NC, and NOCC with labels
        self.buttonNE = self.create_indicator("grey")
        self.buttonNE1 = self.create_indicator("grey")
        self.buttonNE2 = self.create_indicator("grey")


        self.buttonNC = self.create_indicator("grey")
        self.buttonNC1 = self.create_indicator("grey")
        self.buttonNC2 = self.create_indicator("grey")

        self.buttonNOCC = self.create_indicator("grey")
        self.buttonNOCC1 = self.create_indicator("grey")
        self.buttonNOCC2 = self.create_indicator("grey")

        # Add the indicators to the layout with merged columns
        combined_layout_box2.addWidget(self.buttonNE, 2, 4)
        combined_layout_box2.addWidget(self.buttonNE1, 3, 4)
        combined_layout_box2.addWidget(self.buttonNE2, 4, 4)


        combined_layout_box2.addWidget(self.buttonNC, 2, 5)
        combined_layout_box2.addWidget(self.buttonNC1, 3, 5)
        combined_layout_box2.addWidget(self.buttonNC2, 4, 5)


        combined_layout_box2.addWidget(self.buttonNOCC, 2, 6)
        combined_layout_box2.addWidget(self.buttonNOCC1, 3, 6)
        combined_layout_box2.addWidget(self.buttonNOCC2, 4, 6)

        # Print statements for debugging
        print("Indicator NE size:", self.buttonNE.sizeHint())
        print("Indicator NC size:", self.buttonNC.sizeHint())
        print("Indicator NOCC size:", self.buttonNOCC.sizeHint())

        # Font for the labels
        font1 = QFont("Arial", 19)  # You can adjust the font family and size
        font1.setBold(True)  # Set the font weight to bold

        # Font color for the labels
        font_color = "white"

        # Add "Empty" label and radio button to the third column
        row_labelNE = QLabel("NE ")
        row_labelNE.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)  # Set alignment
        combined_layout_box2.addWidget(row_labelNE, 2, 4, 3, 1)
        row_labelNE.setFont(font1)  # Set the font for the label
        row_labelNE.setStyleSheet(f"color: {font_color};")  # Set the font color


        # Add "Empty" label and radio button to the third column
        row_labelNC = QLabel("NC ")
        row_labelNC.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)  # Set alignment
        combined_layout_box2.addWidget(row_labelNC, 2, 5, 3, 1)
        row_labelNC.setFont(font1)  # Set the font for the label
        row_labelNC.setStyleSheet(f"color: {font_color};")  # Set the font color


        # Add "Empty" label and radio button to the third column
        row_labelNOCC = QLabel("NOCC ")
        row_labelNOCC.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)  # Set alignment
        combined_layout_box2.addWidget(row_labelNOCC, 2, 6, 3, 1)
        row_labelNOCC.setFont(font1)  # Set the font for the label
        row_labelNOCC.setStyleSheet(f"color: {font_color};")  # Set the font color

        # Font for the labels
        font2 = QFont("Arial", 20)  # You can adjust the font family and size

        # Add "Empty" label and radio button to the third column
        row_labelNE0 = QLabel("0000 ")
        row_labelNE0.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box2.addWidget(row_labelNE0, 5, 4, 3, 1)
        row_labelNE0.setFont(font2)  # Set the font for the label


        # Add "Empty" label and radio button to the third column
        row_labelNC0 = QLabel("0000 ")
        row_labelNC0.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box2.addWidget(row_labelNC0, 5, 5, 3, 1)
        row_labelNC0.setFont(font2)  # Set the font for the label

        # Add "Empty" label and radio button to the third column
        row_labelNOCC0 = QLabel("0000 ")
        row_labelNOCC0.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box2.addWidget(row_labelNOCC0, 5, 6, 3, 1)
        row_labelNOCC0.setFont(font2)  # Set the font for the label

###### # Example of calling a function from labjacku3.py
        #result = write_data_to_file()
        #print(f"Result from labjack_function: {result}")

###### # Example of using a class from proximity.py
        #proximity_sensor = read_proximity_sensor()
        #proximity_value = proximity_sensor.get_reading()
        #print(f"Proximity sensor reading: {proximity_value}")

        # STOPWATCH AREA
        # Label "Stopwatch:"
        stopwatch_label = QLabel("Stopwatch:")
        stopwatch_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        # Set font size for the label
        font_stopwatch_label = stopwatch_label.font()
        font_stopwatch_label.setPointSize(14)  # Set the desired font size
        font_stopwatch_label.setBold(True)  # Set the font to bold
        stopwatch_label.setFont(font_stopwatch_label)

        combined_layout_box2.addWidget(stopwatch_label, 2, 9, 2, 1)

        # Label "00:00"
        stopwatch_display = QLabel("00:00")
        stopwatch_display.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        # Set font size for the label
        font_stopwatch_display = stopwatch_display.font()
        font_stopwatch_display.setPointSize(14)  # Set the desired font size
        font_stopwatch_display.setBold(True)  # Set the font to bold
        stopwatch_display.setFont(font_stopwatch_display)

        combined_layout_box2.addWidget(stopwatch_display, 4, 9, 2,1)

        # Chart printing button
        # Add the print button to the layout near the stopwatch_label
        combined_layout_box2.addWidget(print_button, 1, 10)


        # Create an instance of QElapsedTimer for measuring elapsed time
        self.elapsed_timer = QElapsedTimer()

        # Function to update stopwatch display
        def update_stopwatch_display():
            try:
                elapsed_time = self.elapsed_timer.elapsed()
                elapsed_seconds = elapsed_time // 1000
                seconds = elapsed_seconds % 60
                minutes = (elapsed_seconds // 60) % 60
                hours = elapsed_seconds // 3600
                stopwatch_display.setText(f"{minutes:02d}:{seconds:02d}")
            except Exception as e:
                print(f"Error in update_stopwatch_display: {e}")

        # Set up a timer to periodically update the display (every second)
        self.display_timer = QTimer(self)
        self.display_timer.timeout.connect(update_stopwatch_display)

        # Set the fixed width for the box2 layout
        combined_widget_box2 = add_outline(combined_layout_box2)
        combined_widget_box2.setFixedWidth(1366)  # Set the fixed width for the left layout
        # Remove the fixed height for now to let it adjust dynamically
        combined_widget_box2.setFixedHeight(155)  # Set the fixed width for the left layout



        # Add both combined layouts to the bottom layout
        combined_layout_bottom.addWidget(combined_widget_box2)

        # THIRD ROW BOX

        # Repeat the process for the second set of layouts (box2 and box3)
        combined_layout_box2 = QGridLayout()

        # Create table layout and NE table
        table_layout = QVBoxLayout()
        self.ne_table = QTableWidget()
        self.ne_table.setColumnCount(11)
        self.ne_table.setRowCount(4)
        self.ne_table.setHorizontalHeaderLabels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "AVERAGE"])
        self.ne_table.setVerticalHeaderLabels(["NE", "NC", "NOCC", "RATIO"])

        # Set font size for horizontal header
        font_horizontal_header = self.ne_table.horizontalHeader().font()
        font_horizontal_header.setPointSize(16)  # Set the desired font size
        self.ne_table.horizontalHeader().setFont(font_horizontal_header)

        # Set font size for vertical header
        font_vertical_header = self.ne_table.verticalHeader().font()
        font_vertical_header.setPointSize(16)  # Set the desired font size
        self.ne_table.verticalHeader().setFont(font_vertical_header)

        # Set resize mode for each column
        column_stretch_factors = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]  # Adjust the values as needed

        for col, stretch_factor in enumerate(column_stretch_factors):
            self.ne_table.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)

        table_layout.addWidget(self.ne_table)

        # Set background color for column headers using hex code
        header_color = QColor("#D3D3D3")  # Replace with your hex code
        for i in range(self.ne_table.columnCount()):
            item = self.ne_table.horizontalHeaderItem(i)
            item.setBackground(header_color)

        # Set background color for row headers using hex code
        row_header_color = QColor("#D3D3D3")  # Replace with your hex code
        for i in range(self.ne_table.rowCount()):
            item = self.ne_table.verticalHeaderItem(i)
            item.setBackground(row_header_color)

        # Set background color for the table using hex code
        table_color = QColor("#EFEFEF")  # Replace with your hex code
        self.ne_table.setStyleSheet(f"QTableWidget {{ background-color: {table_color.name()}; }}")


        # Repeat the process for the second set of layouts (box2 and box3)
        combined_layout_box3 = QVBoxLayout()

        # Add the table layout to the bottom layout
        combined_layout_box3.addLayout(table_layout)

        # Add the notes input to the layout
        combined_layout_box3.addWidget(self.notes_input)

        # Set the fixed width for the left layout
        combined_widget_box3 = add_outline(combined_layout_box3)
        combined_widget_box3.setFixedWidth(1366)  # Set the fixed width for the left layout
        combined_widget_box3.setFixedHeight(285)  # Set the fixed width for the left layout

        # Add both combined layouts to the bottom layout
        combined_layout_bottom1.addWidget(combined_widget_box3)

        # Add Edit and Save buttons on the same row
        edit_button = QPushButton("EDIT")
        save_button = QPushButton("SAVE")
        # Set fixed width for the buttons
        edit_button.setFixedWidth(100)
        save_button.setFixedWidth(100)
        # Apply stylesheet to set blue outline and text color
        button_style = (
            "QPushButton {"
            "   border: 2px solid #1e96fc;"  # Set border color to the specified blue
            "   color: #1e96fc;"  # Set text color to the specified blue
            "   background-color: transparent;"  # Set a transparent background
            "   font-weight: bold;"  # Make the text bold
            "   font-size: 12pt;"  # Set the font size to 12 points
            "   border-radius: 5px;"  # Add a corner radius of 5 pixels
            "}"
            "QPushButton:hover {"
            "   background-color: #a7d0f7;"  # Change background color on hover to a lighter shade of blue
            "}"
        )

        edit_button.setStyleSheet(button_style)
        save_button.setStyleSheet(button_style)

        # Create a horizontal layout for the buttons
        button_row_layout = QHBoxLayout()
        button_row_layout.addWidget(edit_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        button_row_layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        button_row_layout1 = QHBoxLayout()

        button_row_layout1.addWidget(edit_button)
        button_row_layout1.addWidget(save_button)


        # Set the layout for combined_widget_box3
        combined_widget_box3.setLayout(combined_layout_box3)

        # Add the button layout to the combined_layout_box3
        combined_layout_box3.addLayout(button_row_layout)

        # Set the alignment for the button_row_layout to be at the right
        button_row_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box3.addLayout(button_row_layout1)

        # FOURTH column box
        # Repeat the process for the second set of layouts (box2 and box3)
        combined_layout_box4 = QVBoxLayout()

        # Set the fixed width for the box4 layout
        combined_widget_box4 = add_outline(combined_layout_box4)
        combined_widget_box4.setFixedWidth(1366)  # Set the fixed width for the left layout
        combined_widget_box4.setFixedHeight(95)  # Set the fixed width for the left layout

        # Add both combined layouts to the bottom layout
        combined_layout_bottom2.addWidget(combined_widget_box4)


        # Add Start, Stop, Simulasi, View Data and Exit buttons
        start_button = QPushButton("START")
        stop_button = QPushButton("STOP")

        view_button = QPushButton("VIEW DATA")
        exit_button = QPushButton("EXIT")
        start_button.setFixedWidth(100)
        stop_button.setFixedWidth(100)
        view_button.setFixedWidth(100)
        exit_button.setFixedWidth(100)


        start_button.setStyleSheet(button_style)
        stop_button.setStyleSheet(button_style)

        view_button.setStyleSheet(button_style)
        exit_button.setStyleSheet(button_style)

        # Create a horizontal layout for the buttons
        button_row_layout2 = QHBoxLayout()
        button_row_layout2.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        button_row_layout2.addWidget(stop_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        button_row_layout2.addWidget(view_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        button_row_layout2.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        button_row_layout4 = QHBoxLayout()
        button_row_layout4.addWidget(start_button)
        button_row_layout4.addWidget(stop_button)

        button_row_layout4.addWidget(view_button)
        button_row_layout4.addWidget(exit_button)


        # Set the layout for combined_widget_box3
        combined_widget_box4.setLayout(combined_layout_box4)

        # Add the button layout to the combined_layout_box3
        combined_layout_box4.addLayout(button_row_layout2)

        # Set the alignment for the button_row_layout to be at the right
        button_row_layout2.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        combined_layout_box4.addLayout(button_row_layout4)

        # Connect the "Start" button to start the stopwatch and the display timer
        #start_button.clicked.connect(self.elapsed_timer.start)
        #start_button.clicked.connect(self.display_timer.start)

        # Connect the "Start" button to start the stopwatch and the display timer
        start_button.clicked.connect(self.start_stopwatch_and_update_indicators)

        # Connect the "Start" button to the new method
        #start_button.clicked.connect(self.start_button_clicked)


        # Connect the "Stop" button to stop the stopwatch, the display timer, and reset the indicators
        stop_button.clicked.connect(self.elapsed_timer.invalidate)
        stop_button.clicked.connect(self.display_timer.stop)
        stop_button.clicked.connect(self.reset_indicators)

        # Connect radio_buttonOT toggled signal to update_notes_visibility function
        self.radio_buttonOT.toggled.connect(self.update_notes_visibility)

        # Connect the "Exit" button to quit the application
        exit_button.clicked.connect(QCoreApplication.quit)



        # Add top and bottom layouts to the main layout
        central_layout.addLayout(combined_layout_top)
        central_layout.addLayout(combined_layout_bottom)
        central_layout.addLayout(combined_layout_bottom1)
        central_layout.addLayout(combined_layout_bottom2)



        # Set the fixed width for the left layout
        combined_widget_left = add_outline(combined_layout_left)
        combined_widget_left.setFixedWidth(550)  # Set the fixed width for the left layout
        combined_widget_left.setFixedHeight(300)  # Adjusted height to accommodate the notes input

        # Function to update the visibility of the notes input based on the state of radio_buttonOT
    def update_notes_visibility(self):
        # Hide or show ne_table based on the state of radio_buttonOT
        self.ne_table.setVisible(not self.radio_buttonOT.isChecked())


    def update_row_label(self, label, new_text):
       label.setText(new_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
