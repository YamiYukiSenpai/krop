# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(949, 736)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabBasic = QtGui.QWidget()
        self.tabBasic.setObjectName(_fromUtf8("tabBasic"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tabBasic)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupBox = QtGui.QGroupBox(self.tabBasic)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editFile = QtGui.QLineEdit(self.groupBox)
        self.editFile.setObjectName(_fromUtf8("editFile"))
        self.gridLayout.addWidget(self.editFile, 0, 0, 1, 1)
        self.buttonFileSelect = QtGui.QToolButton(self.groupBox)
        self.buttonFileSelect.setText(_fromUtf8(""))
        self.buttonFileSelect.setAutoRaise(True)
        self.buttonFileSelect.setObjectName(_fromUtf8("buttonFileSelect"))
        self.gridLayout.addWidget(self.buttonFileSelect, 0, 1, 1, 1)
        self.labelFileHelp = QtGui.QLabel(self.groupBox)
        self.labelFileHelp.setWordWrap(True)
        self.labelFileHelp.setObjectName(_fromUtf8("labelFileHelp"))
        self.gridLayout.addWidget(self.labelFileHelp, 1, 0, 1, 2)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupRotation = QtGui.QGroupBox(self.tabBasic)
        self.groupRotation.setFlat(False)
        self.groupRotation.setObjectName(_fromUtf8("groupRotation"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupRotation)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.comboRotation = QtGui.QComboBox(self.groupRotation)
        self.comboRotation.setObjectName(_fromUtf8("comboRotation"))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.comboRotation.addItem(_fromUtf8(""))
        self.verticalLayout_8.addWidget(self.comboRotation)
        self.verticalLayout_9.addWidget(self.groupRotation)
        self.groupWhichPages = QtGui.QGroupBox(self.tabBasic)
        self.groupWhichPages.setObjectName(_fromUtf8("groupWhichPages"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupWhichPages)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.editWhichPages = QtGui.QLineEdit(self.groupWhichPages)
        self.editWhichPages.setObjectName(_fromUtf8("editWhichPages"))
        self.verticalLayout.addWidget(self.editWhichPages)
        self.labelWhichPagesEg = QtGui.QLabel(self.groupWhichPages)
        self.labelWhichPagesEg.setWordWrap(True)
        self.labelWhichPagesEg.setObjectName(_fromUtf8("labelWhichPagesEg"))
        self.verticalLayout.addWidget(self.labelWhichPagesEg)
        self.verticalLayout_9.addWidget(self.groupWhichPages)
        spacerItem = QtGui.QSpacerItem(
            20, 484, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.tabWidget.addTab(self.tabBasic, _fromUtf8(""))
        self.tabAdvanced = QtGui.QWidget()
        self.tabAdvanced.setObjectName(_fromUtf8("tabAdvanced"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabAdvanced)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupSelectionMode = QtGui.QGroupBox(self.tabAdvanced)
        self.groupSelectionMode.setFlat(False)
        self.groupSelectionMode.setObjectName(_fromUtf8("groupSelectionMode"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupSelectionMode)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioSelAll = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelAll.setChecked(True)
        self.radioSelAll.setObjectName(_fromUtf8("radioSelAll"))
        self.gridLayout_2.addWidget(self.radioSelAll, 0, 0, 1, 2)
        self.radioSelEvenOdd = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelEvenOdd.setObjectName(_fromUtf8("radioSelEvenOdd"))
        self.gridLayout_2.addWidget(self.radioSelEvenOdd, 1, 0, 1, 2)
        self.radioSelIndividual = QtGui.QRadioButton(self.groupSelectionMode)
        self.radioSelIndividual.setObjectName(_fromUtf8("radioSelIndividual"))
        self.gridLayout_2.addWidget(self.radioSelIndividual, 2, 0, 1, 2)
        self.labelSelHelp = QtGui.QLabel(self.groupSelectionMode)
        self.labelSelHelp.setWordWrap(True)
        self.labelSelHelp.setObjectName(_fromUtf8("labelSelHelp"))
        self.gridLayout_2.addWidget(self.labelSelHelp, 3, 0, 1, 2)
        self.labelSelExceptions = QtGui.QLabel(self.groupSelectionMode)
        self.labelSelExceptions.setObjectName(_fromUtf8("labelSelExceptions"))
        self.gridLayout_2.addWidget(self.labelSelExceptions, 4, 0, 1, 1)
        self.editSelExceptions = QtGui.QLineEdit(self.groupSelectionMode)
        self.editSelExceptions.setObjectName(_fromUtf8("editSelExceptions"))
        self.gridLayout_2.addWidget(self.editSelExceptions, 4, 1, 1, 1)
        self.labelSelExceptionsHelp = QtGui.QLabel(self.groupSelectionMode)
        self.labelSelExceptionsHelp.setObjectName(
            _fromUtf8("labelSelExceptionsHelp"))
        self.gridLayout_2.addWidget(self.labelSelExceptionsHelp, 5, 0, 1, 2)
        self.verticalLayout_6.addWidget(self.groupSelectionMode)
        self.groupDevice = QtGui.QGroupBox(self.tabAdvanced)
        self.groupDevice.setObjectName(_fromUtf8("groupDevice"))
        self.formLayout = QtGui.QFormLayout(self.groupDevice)
        self.formLayout.setFieldGrowthPolicy(
            QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboDevice = QtGui.QComboBox(self.groupDevice)
        self.comboDevice.setEditable(False)
        self.comboDevice.setSizeAdjustPolicy(
            QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.comboDevice.setObjectName(_fromUtf8("comboDevice"))
        self.formLayout.setWidget(
            0, QtGui.QFormLayout.SpanningRole, self.comboDevice)
        self.labelAspectRatio = QtGui.QLabel(self.groupDevice)
        self.labelAspectRatio.setObjectName(_fromUtf8("labelAspectRatio"))
        self.formLayout.setWidget(
            1, QtGui.QFormLayout.LabelRole, self.labelAspectRatio)
        self.editAspectRatio = QtGui.QLineEdit(self.groupDevice)
        self.editAspectRatio.setObjectName(_fromUtf8("editAspectRatio"))
        self.formLayout.setWidget(
            1, QtGui.QFormLayout.FieldRole, self.editAspectRatio)
        self.labelDeviceHelp = QtGui.QLabel(self.groupDevice)
        self.labelDeviceHelp.setWordWrap(True)
        self.labelDeviceHelp.setObjectName(_fromUtf8("labelDeviceHelp"))
        self.formLayout.setWidget(
            2, QtGui.QFormLayout.SpanningRole, self.labelDeviceHelp)
        self.verticalLayout_6.addWidget(self.groupDevice)
        self.groupTrimMargins = QtGui.QGroupBox(self.tabAdvanced)
        self.groupTrimMargins.setObjectName(_fromUtf8("groupTrimMargins"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupTrimMargins)
        self.formLayout_2.setFieldGrowthPolicy(
            QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelPadding = QtGui.QLabel(self.groupTrimMargins)
        self.labelPadding.setObjectName(_fromUtf8("labelPadding"))
        self.formLayout_2.setWidget(
            0, QtGui.QFormLayout.LabelRole, self.labelPadding)
        self.editPadding = QtGui.QLineEdit(self.groupTrimMargins)
        self.editPadding.setText(_fromUtf8(""))
        self.editPadding.setObjectName(_fromUtf8("editPadding"))
        self.formLayout_2.setWidget(
            0, QtGui.QFormLayout.FieldRole, self.editPadding)
        self.labelTrimMarginsEg = QtGui.QLabel(self.groupTrimMargins)
        self.labelTrimMarginsEg.setWordWrap(True)
        self.labelTrimMarginsEg.setObjectName(_fromUtf8("labelTrimMarginsEg"))
        self.formLayout_2.setWidget(
            1, QtGui.QFormLayout.SpanningRole, self.labelTrimMarginsEg)
        self.labelAllowedChanges = QtGui.QLabel(self.groupTrimMargins)
        self.labelAllowedChanges.setEnabled(True)
        self.labelAllowedChanges.setObjectName(
            _fromUtf8("labelAllowedChanges"))
        self.formLayout_2.setWidget(
            2, QtGui.QFormLayout.LabelRole, self.labelAllowedChanges)
        self.editAllowedChanges = QtGui.QLineEdit(self.groupTrimMargins)
        self.editAllowedChanges.setEnabled(True)
        self.editAllowedChanges.setObjectName(_fromUtf8("editAllowedChanges"))
        self.formLayout_2.setWidget(
            2, QtGui.QFormLayout.FieldRole, self.editAllowedChanges)
        self.labelSensitivity = QtGui.QLabel(self.groupTrimMargins)
        self.labelSensitivity.setEnabled(True)
        self.labelSensitivity.setObjectName(_fromUtf8("labelSensitivity"))
        self.formLayout_2.setWidget(
            3, QtGui.QFormLayout.LabelRole, self.labelSensitivity)
        self.editSensitivity = QtGui.QLineEdit(self.groupTrimMargins)
        self.editSensitivity.setEnabled(True)
        self.editSensitivity.setObjectName(_fromUtf8("editSensitivity"))
        self.formLayout_2.setWidget(
            3, QtGui.QFormLayout.FieldRole, self.editSensitivity)
        self.verticalLayout_6.addWidget(self.groupTrimMargins)
        spacerItem1 = QtGui.QSpacerItem(
            20, 339, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.tabWidget.addTab(self.tabAdvanced, _fromUtf8(""))
        self.tabHelp = QtGui.QWidget()
        self.tabHelp.setObjectName(_fromUtf8("tabHelp"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabHelp)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelHelp = QtGui.QLabel(self.tabHelp)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelHelp.sizePolicy().hasHeightForWidth())
        self.labelHelp.setSizePolicy(sizePolicy)
        self.labelHelp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelHelp.setBaseSize(QtCore.QSize(0, 0))
        self.labelHelp.setTextFormat(QtCore.Qt.RichText)
        self.labelHelp.setWordWrap(True)
        self.labelHelp.setOpenExternalLinks(True)
        self.labelHelp.setObjectName(_fromUtf8("labelHelp"))
        self.verticalLayout_3.addWidget(self.labelHelp)
        spacerItem2 = QtGui.QSpacerItem(
            20, 524, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.labelHelpLicense = QtGui.QLabel(self.tabHelp)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelHelpLicense.sizePolicy().hasHeightForWidth())
        self.labelHelpLicense.setSizePolicy(sizePolicy)
        self.labelHelpLicense.setTextFormat(QtCore.Qt.RichText)
        self.labelHelpLicense.setWordWrap(True)
        self.labelHelpLicense.setOpenExternalLinks(True)
        self.labelHelpLicense.setObjectName(_fromUtf8("labelHelpLicense"))
        self.verticalLayout_3.addWidget(self.labelHelpLicense)
        self.tabWidget.addTab(self.tabHelp, _fromUtf8(""))
        self.frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setMargin(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.documentView = QtGui.QGraphicsView(self.frame)
        self.documentView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.documentView.setFrameShadow(QtGui.QFrame.Sunken)
        self.documentView.setObjectName(_fromUtf8("documentView"))
        self.verticalLayout_2.addWidget(self.documentView)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonFirst = QtGui.QPushButton(self.frame_2)
        self.buttonFirst.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonFirst.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonFirst.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonFirst.setText(_fromUtf8(""))
        self.buttonFirst.setFlat(True)
        self.buttonFirst.setObjectName(_fromUtf8("buttonFirst"))
        self.horizontalLayout_2.addWidget(self.buttonFirst)
        self.buttonPrevious = QtGui.QPushButton(self.frame_2)
        self.buttonPrevious.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonPrevious.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonPrevious.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonPrevious.setText(_fromUtf8(""))
        self.buttonPrevious.setFlat(True)
        self.buttonPrevious.setObjectName(_fromUtf8("buttonPrevious"))
        self.horizontalLayout_2.addWidget(self.buttonPrevious)
        self.editCurrentPage = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editCurrentPage.sizePolicy().hasHeightForWidth())
        self.editCurrentPage.setSizePolicy(sizePolicy)
        self.editCurrentPage.setMinimumSize(QtCore.QSize(40, 23))
        self.editCurrentPage.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editCurrentPage.setInputMask(_fromUtf8(""))
        self.editCurrentPage.setAlignment(QtCore.Qt.AlignCenter)
        self.editCurrentPage.setObjectName(_fromUtf8("editCurrentPage"))
        self.horizontalLayout_2.addWidget(self.editCurrentPage)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.editMaxPage = QtGui.QLineEdit(self.frame_2)
        self.editMaxPage.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editMaxPage.sizePolicy().hasHeightForWidth())
        self.editMaxPage.setSizePolicy(sizePolicy)
        self.editMaxPage.setMinimumSize(QtCore.QSize(40, 23))
        self.editMaxPage.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMaxPage.setAutoFillBackground(False)
        self.editMaxPage.setInputMask(_fromUtf8(""))
        self.editMaxPage.setFrame(True)
        self.editMaxPage.setAlignment(QtCore.Qt.AlignCenter)
        self.editMaxPage.setReadOnly(True)
        self.editMaxPage.setObjectName(_fromUtf8("editMaxPage"))
        self.horizontalLayout_2.addWidget(self.editMaxPage)
        self.buttonNext = QtGui.QPushButton(self.frame_2)
        self.buttonNext.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonNext.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonNext.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNext.setText(_fromUtf8(""))
        self.buttonNext.setFlat(True)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.horizontalLayout_2.addWidget(self.buttonNext)
        self.buttonLast = QtGui.QPushButton(self.frame_2)
        self.buttonLast.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonLast.setMaximumSize(QtCore.QSize(24, 24))
        self.buttonLast.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonLast.setText(_fromUtf8(""))
        self.buttonLast.setFlat(True)
        self.buttonLast.setObjectName(_fromUtf8("buttonLast"))
        self.horizontalLayout_2.addWidget(self.buttonLast)
        spacerItem4 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionZoomIn = QtGui.QAction(MainWindow)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionPreviousPage = QtGui.QAction(MainWindow)
        self.actionPreviousPage.setObjectName(_fromUtf8("actionPreviousPage"))
        self.actionNextPage = QtGui.QAction(MainWindow)
        self.actionNextPage.setObjectName(_fromUtf8("actionNextPage"))
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionFitInView = QtGui.QAction(MainWindow)
        self.actionFitInView.setCheckable(True)
        self.actionFitInView.setObjectName(_fromUtf8("actionFitInView"))
        self.actionKrop = QtGui.QAction(MainWindow)
        self.actionKrop.setEnabled(False)
        self.actionKrop.setObjectName(_fromUtf8("actionKrop"))
        self.actionDeleteSelection = QtGui.QAction(MainWindow)
        self.actionDeleteSelection.setObjectName(
            _fromUtf8("actionDeleteSelection"))
        self.actionFirstPage = QtGui.QAction(MainWindow)
        self.actionFirstPage.setObjectName(_fromUtf8("actionFirstPage"))
        self.actionLastPage = QtGui.QAction(MainWindow)
        self.actionLastPage.setObjectName(_fromUtf8("actionLastPage"))
        self.actionTrimMargins = QtGui.QAction(MainWindow)
        self.actionTrimMargins.setObjectName(_fromUtf8("actionTrimMargins"))
        self.actionSelectFile = QtGui.QAction(MainWindow)
        self.actionSelectFile.setObjectName(_fromUtf8("actionSelectFile"))
        self.actionTrimMarginsAll = QtGui.QAction(MainWindow)
        self.actionTrimMarginsAll.setEnabled(False)
        self.actionTrimMarginsAll.setObjectName(
            _fromUtf8("actionTrimMarginsAll"))
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionKrop)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)
        self.toolBar.addAction(self.actionFitInView)
        self.toolBar.addAction(self.actionPreviousPage)
        self.toolBar.addAction(self.actionNextPage)
        self.toolBar.addAction(self.actionTrimMarginsAll)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonPrevious, QtCore.SIGNAL(
            _fromUtf8("clicked()")), self.actionPreviousPage.trigger)
        QtCore.QObject.connect(self.buttonNext, QtCore.SIGNAL(
            _fromUtf8("clicked()")), self.actionNextPage.trigger)
        QtCore.QObject.connect(self.buttonFirst, QtCore.SIGNAL(
            _fromUtf8("clicked()")), self.actionFirstPage.trigger)
        QtCore.QObject.connect(self.buttonLast, QtCore.SIGNAL(
            _fromUtf8("clicked()")), self.actionLastPage.trigger)
        QtCore.QObject.connect(self.buttonFileSelect, QtCore.SIGNAL(
            _fromUtf8("clicked()")), self.actionSelectFile.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "krop: A tool to crop your PDFs", None))
        self.groupBox.setTitle(_translate("MainWindow", "Save to", None))
        self.labelFileHelp.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is where the cropped version of your pdf will be saved; once you choose <span style=\" font-style:italic;\">Krop!</span> in the menu.</p></body></html>", None))
        self.groupRotation.setTitle(_translate(
            "MainWindow", "Rotate final PDF", None))
        self.comboRotation.setItemText(
            0, _translate("MainWindow", "no rotation", None))
        self.comboRotation.setItemText(1, _translate(
            "MainWindow", "rotate left (90° counterclockwise)", None))
        self.comboRotation.setItemText(2, _translate(
            "MainWindow", "rotate right (90° clockwise)", None))
        self.comboRotation.setItemText(
            3, _translate("MainWindow", "upside down", None))
        self.groupWhichPages.setTitle(_translate(
            "MainWindow", "Which pages to include", None))
        self.labelWhichPagesEg.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; margin: 0; }\n"
                                                  "</style></head>\n"
                                                  "<body>\n"
                                                  "<p><i>Eg:</i> 1-5 for the first 5 pages</p>\n"
                                                  "<p><i>Eg:</i> 2- for all but the first page</p>\n"
                                                  "<p><i>Eg:</i> 1,4-5,7- to omit pages 2,3,6</p>\n"
                                                  "</body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabBasic), _translate("MainWindow", "Basic", None))
        self.groupSelectionMode.setTitle(_translate(
            "MainWindow", "Selections apply to", None))
        self.radioSelAll.setText(_translate("MainWindow", "all pages", None))
        self.radioSelEvenOdd.setText(_translate(
            "MainWindow", "even/odd pages", None))
        self.radioSelIndividual.setText(_translate(
            "MainWindow", "individual page", None))
        self.labelSelHelp.setText(_translate(
            "MainWindow", "Should all pages be cropped based on the same selections? Maybe you want to treat even and odd pages differently? For full control you can crop each page using individual selections.", None))
        self.labelSelExceptions.setText(
            _translate("MainWindow", "Exceptions:", None))
        self.labelSelExceptionsHelp.setText(_translate(
            "MainWindow", "List pages which require individual selections.", None))
        self.groupDevice.setTitle(_translate(
            "MainWindow", "Fit screen of device", None))
        self.labelAspectRatio.setText(_translate(
            "MainWindow", "Aspect ratio:", None))
        self.labelDeviceHelp.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Eg:</span> 600:730 (ratio of width to height)</p></body></html>", None))
        self.groupTrimMargins.setTitle(_translate(
            "MainWindow", "Settings for trimming margins", None))
        self.labelPadding.setText(_translate("MainWindow", "Padding:", None))
        self.labelTrimMarginsEg.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Eg:</span> 2 or 5,2 or 5,2,5,5 (interpreted as in CSS)</p><p>Right-click a selection to automatically trim it.</p></body></html>", None))
        self.labelAllowedChanges.setText(_translate(
            "MainWindow", "Allowed changes:", None))
        self.labelSensitivity.setText(_translate(
            "MainWindow", "Color sensitivity:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabAdvanced), _translate("MainWindow", "Advanced", None))
        self.labelHelp.setText(_translate("MainWindow", "<h3>Getting started</h3>\n"
                                          "<p>Using your mouse, create one or more selections on the pdf document. These are the regions that will be included into the cropped file.\n"
                                          "<p>When you are done, click Krop! in the menu to create a cropped version of your document.\n"
                                          "<h3>Hints</h3>\n"
                                          "<p>Right-click a selection to delete it.\n"
                                          "<p>You can choose to create individual selections for each page.\n"
                                          "<p>If you have an eReader that is not good at scrolling documents, you can have each page automatically broken into parts to optimally fit the screen of your eReader.\n"
                                          "<p>Some examples can be found at: <a href=\'http://arminstraub.com/software/krop\'>arminstraub.com</a>\n"
                                          "", None))
        self.labelHelpLicense.setText(_translate("MainWindow", "Copyright (C) 2010-2016 Armin Straub\n"
                                                 "<br><a href=\'http://arminstraub.com\'>http://arminstraub.com</a>\n"
                                                 "<p>This program is free software and available to you in the hope that it will be useful; but without any warranty. It is distributed under the terms of the GNU General Public License (GPLv3+). See the accompanying files for more information.\n"
                                                 "", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabHelp), _translate("MainWindow", "Help", None))
        self.label.setText(_translate("MainWindow", "of", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionZoomIn.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoomIn.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionZoomOut.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionZoomOut.setShortcut(
            _translate("MainWindow", "Ctrl+-", None))
        self.actionPreviousPage.setText(
            _translate("MainWindow", "Previous Page", None))
        self.actionPreviousPage.setShortcut(
            _translate("MainWindow", "Ctrl+Left", None))
        self.actionNextPage.setText(
            _translate("MainWindow", "Next Page", None))
        self.actionNextPage.setShortcut(
            _translate("MainWindow", "Ctrl+Right", None))
        self.actionOpenFile.setText(_translate("MainWindow", "Open", None))
        self.actionFitInView.setText(
            _translate("MainWindow", "Fit In View", None))
        self.actionKrop.setText(_translate("MainWindow", "Krop!", None))
        self.actionDeleteSelection.setText(
            _translate("MainWindow", "Delete Selection", None))
        self.actionFirstPage.setText(
            _translate("MainWindow", "First Page", None))
        self.actionLastPage.setText(
            _translate("MainWindow", "Last Page", None))
        self.actionTrimMargins.setText(
            _translate("MainWindow", "Trim Margins", None))
        self.actionSelectFile.setText(
            _translate("MainWindow", "Select File", None))
        self.actionTrimMarginsAll.setText(
            _translate("MainWindow", "Trim Margins", None))
        self.actionTrimMarginsAll.setToolTip(
            _translate("MainWindow", "Trim Margins", None))
