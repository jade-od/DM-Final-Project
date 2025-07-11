# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AttendanceTracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import InputPopup
import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


###################################################################
#                                                                 #
#                       UI Generation                             #
#                                                                 #
###################################################################


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(849, 625)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 811, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tblAttendance = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tblAttendance.setObjectName("tblAttendance")
        self.tblAttendance.setColumnCount(4)
        self.tblAttendance.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.tblAttendance)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 0, 141, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnInfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnInfo.setFont(font)
        self.btnInfo.setObjectName("btnInfo")
        self.verticalLayout.addWidget(self.btnInfo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tblAttendance_2 = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tblAttendance_2.setObjectName("tblAttendance_2")
        self.tblAttendance_2.setColumnCount(8)
        self.tblAttendance_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttendance_2.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_2.addWidget(self.tblAttendance_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(664, 0, 141, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblDay = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDay.setFont(font)
        self.lblDay.setObjectName("lblDay")
        self.verticalLayout_2.addWidget(self.lblDay)
        self.dateEditStart = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEditStart.setCalendarPopup(True)
        self.dateEditStart.setObjectName("dateEditStart")
        self.verticalLayout_2.addWidget(self.dateEditStart)
        self.dateEditEnd = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEditEnd.setCalendarPopup(True)
        self.dateEditEnd.setObjectName("dateEditEnd")
        self.verticalLayout_2.addWidget(self.dateEditEnd)
        self.lblStudent = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblStudent.setFont(font)
        self.lblStudent.setObjectName("lblStudent")
        self.verticalLayout_2.addWidget(self.lblStudent)
        self.cmbStudentID = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmbStudentID.setObjectName("cmbStudentID")
        self.verticalLayout_2.addWidget(self.cmbStudentID)
        self.lblCRN = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCRN.setFont(font)
        self.lblCRN.setObjectName("lblCRN")
        self.verticalLayout_2.addWidget(self.lblCRN)
        self.cmbCRN = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmbCRN.setObjectName("cmbCRN")
        self.verticalLayout_2.addWidget(self.cmbCRN)
        self.lblCourseName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCourseName.setFont(font)
        self.lblCourseName.setObjectName("lblCourseName")
        self.verticalLayout_2.addWidget(self.lblCourseName)
        self.cmbCourseName = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cmbCourseName.setObjectName("cmbCourseName")
        self.verticalLayout_2.addWidget(self.cmbCourseName)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lblTotPresent = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lblTotPresent.setObjectName("lblTotPresent")
        self.verticalLayout_2.addWidget(self.lblTotPresent)
        self.totPresentLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.totPresentLineEdit.setEnabled(False)
        self.totPresentLineEdit.setText("")
        self.totPresentLineEdit.setReadOnly(True)
        self.totPresentLineEdit.setObjectName("totPresentLineEdit")
        self.verticalLayout_2.addWidget(self.totPresentLineEdit)
        self.lblTotAbsent = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lblTotAbsent.setObjectName("lblTotAbsent")
        self.verticalLayout_2.addWidget(self.lblTotAbsent)
        self.totAbsentlineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.totAbsentlineEdit.setEnabled(False)
        self.totAbsentlineEdit.setReadOnly(True)
        self.totAbsentlineEdit.setObjectName("totAbsentlineEdit")
        self.verticalLayout_2.addWidget(self.totAbsentlineEdit)
        self.btnSubmit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnSubmit.setObjectName("btnSubmit")
        self.verticalLayout_2.addWidget(self.btnSubmit)
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout_2.addWidget(self.btnClear)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    
#-------------SET UP------------- #
        self.initialSetup()
#-------------------------------- #


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tblAttendance.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student ID"))
        item = self.tblAttendance.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "CRN"))
        item = self.tblAttendance.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date"))
        item = self.tblAttendance.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Attendance"))
        self.btnInfo.setText(_translate("Dialog", "Input Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Attendance"))
        item = self.tblAttendance_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Student ID"))
        item = self.tblAttendance_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Student First"))
        item = self.tblAttendance_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Sutudent Last"))
        item = self.tblAttendance_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "CRN"))
        item = self.tblAttendance_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Course Name"))
        item = self.tblAttendance_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Date"))
        item = self.tblAttendance_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Start/End Time"))
        item = self.tblAttendance_2.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Attendance"))
        self.lblDay.setText(_translate("Dialog", "Sort by Day/Week/Month"))
        self.lblStudent.setText(_translate("Dialog", "Filter by Student ID"))
        self.lblCRN.setText(_translate("Dialog", "Filter by CRN"))
        self.lblCourseName.setText(_translate("Dialog", "Filter by Course Name"))
        self.lblTotPresent.setText(_translate("Dialog", "Total Present:"))
        self.lblTotAbsent.setText(_translate("Dialog", "Total Absent:"))
        self.btnSubmit.setText(_translate("Dialog", "Submit"))
        self.btnClear.setText(_translate("Dialog", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Report"))

     ####################      End UI Generation   ########################




    def initialSetup(self):
        self.SetUpEventsTab1()
        self.SetUpEventsTab2()
        self.setupDatabase()

        self.refreshTbl1()
        self.refreshTbl2()





    #########################################################
    #                                                       #
    #                   Events FOR TAB 1                    #
    #                                                       #
    #########################################################
        
    def SetUpEventsTab1(self):
         #Input Info Button Intialization
        self.btnInfo.clicked.connect(self.btnInfo_clicked) 
    
    # Input Info button is clicked
    def btnInfo_clicked(self): 
        Dialog = QtWidgets.QDialog()
        form = InputPopup.Ui_Dialog()
        form.setupUi(Dialog, None) #None --> no need to send data when creating 
        result = Dialog.exec_()

        if result == 1 : 
            listValues = form.getValues()
            rowCount = self.tblAttendance.rowCount()
            self.tblAttendance.insertRow(rowCount) 

            student_id = listValues[0]
            student_first = listValues[1]
            student_last = listValues[2]
            course_name = listValues[3]
            crn = listValues[4]
            start_end_time = listValues[5]
            attendance = listValues[6]
            date_attendance = listValues[7]

            # Insert data into the database (see functions in database section)
            self.insert_students((student_id, student_first, student_last))
            self.insert_courses(crn, course_name, start_end_time)
            self.insert_attendance((student_id, crn, date_attendance, attendance))



            #insert the into tables 
            self.refreshTbl1()
            self.refreshTbl2()





    #########################################################
    #                                                       #
    #                   Events FOR TAB 2                    #
    #                                                       #
    #########################################################
            

    def SetUpEventsTab2(self):
        pass

        # Connect the submit button to everything ???????
    

    #self.refreshTbl2() 






#########################################################################
#                                                                       #
#                              DATABASE                                 #
#                                                                       #
#########################################################################
            

            
        
    def setupDatabase(self):
        self.connect()
        self.refreshTbl1()
        self.refreshTbl2()
        


#############################################################################
#                           CHANGE YOUR PASSWORD                            #   
#############################################################################
    def connect(self):                                                      #
        self.cnx = mysql.connector.connect(user = 'root',                   #
                                        password = 'quinnfricko',           #
                                        host = '127.0.0.1',                 #    
                                        database = 'AttendanceTracker')     #   
#############################################################################

    #REFRESH TABLE 1
    def refreshTbl1(self):
        
        self.tblAttendance.setRowCount(0)
        cursor = self.cnx.cursor()

        query = """SELECT a.Student_ID, a.CRN, a.Date_of_attendance, a.Attended
                FROM attendance a"""
        cursor.execute(query)

        #insert vals into table1 in database
        for (student_id, crn, date_attended, attended) in cursor:
            rowCount = self.tblAttendance.rowCount()
            self.tblAttendance.insertRow(rowCount)
            self.tblAttendance.setItem(rowCount, 0, QTableWidgetItem(str(student_id)))
            self.tblAttendance.setItem(rowCount, 1, QTableWidgetItem(str(crn)))
            self.tblAttendance.setItem(rowCount, 2, QTableWidgetItem(date_attended.strftime("%Y-%m-%d")))
            self.tblAttendance.setItem(rowCount, 3, QTableWidgetItem(attended))

        cursor.close()


    #REFRESH TABLE 2
    def refreshTbl2(self):
        self.tblAttendance_2.setRowCount(0)

        cursor = self.cnx.cursor()
        query = """
            SELECT s.Student_ID, s.Student_First_name, s.Student_last_name,c.CRN,
                c.course_name,  a.Date_of_attendance,  c.start_end_time, a.Attended
            FROM attendance a
            left JOIN students s ON a.Student_ID = s.Student_ID
            Left JOIN courses c ON a.CRN = c.CRN """
        
        cursor.execute(query)

        #insert vals into table2 in database
        for (student_id, first_name, last_name, crn, course_name, date_attended, start_end_time, attended) in cursor:
            rowCount = self.tblAttendance_2.rowCount()
            self.tblAttendance_2.insertRow(rowCount)
            self.tblAttendance_2.setItem(rowCount, 0, QTableWidgetItem(str(student_id)))
            self.tblAttendance_2.setItem(rowCount, 1, QTableWidgetItem(first_name))
            self.tblAttendance_2.setItem(rowCount, 2, QTableWidgetItem(last_name))
            self.tblAttendance_2.setItem(rowCount, 3, QTableWidgetItem(str(crn)))
            self.tblAttendance_2.setItem(rowCount, 4, QTableWidgetItem(course_name))
            self.tblAttendance_2.setItem(rowCount, 5, QTableWidgetItem(date_attended.strftime("%Y-%m-%d")))
            self.tblAttendance_2.setItem(rowCount, 6, QTableWidgetItem(start_end_time))
            self.tblAttendance_2.setItem(rowCount, 7, QTableWidgetItem(attended))

        cursor.close()


################# INSERT INFO INTO DATABASE TABLES #######################
        
    def insert_students(self, student_data):
        cursor = self.cnx.cursor()
        query = """
            INSERT INTO students (Student_ID, Student_First_name, Student_last_name)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            Student_First_name = %s,
            Student_last_name = %s"""
        
        #multiple to handle the On duplicate key updatre
        student_id, student_first, student_last = student_data
        cursor.execute(query, (student_id, student_first, student_last, student_first, student_last))
        self.cnx.commit()
        cursor.close()

        

    def insert_courses(self, crn, course_name, start_end_time):
        cursor = self.cnx.cursor()
        query = """
            INSERT INTO courses (CRN, course_name, start_end_time)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            course_name = %s,
            start_end_time = %s"""
        cursor.execute(query, (crn, course_name, start_end_time, course_name, start_end_time))
        self.cnx.commit()
        cursor.close()

    def insert_attendance(self, attendance_data):
        cursor = self.cnx.cursor()
        query = """
            INSERT INTO attendance (Student_ID, CRN, Date_of_attendance, Attended)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            Attended = %s"""
        
        #handles the On Duplicate Key Update
        cursor.execute(query, attendance_data + (attendance_data[3],))
        self.cnx.commit()
        cursor.close()



        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



#Sources: 
#On Duplicate Key Update:
#https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update
