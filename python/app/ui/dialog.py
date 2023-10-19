# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from  . import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(783, 489)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.central_stackedWidget = QStackedWidget(Dialog)
        self.central_stackedWidget.setObjectName(u"central_stackedWidget")
        self.submit_page = QWidget()
        self.submit_page.setObjectName(u"submit_page")
        self.horizontalLayout_4 = QHBoxLayout(self.submit_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.items_title_label = QLabel(self.submit_page)
        self.items_title_label.setObjectName(u"items_title_label")
        self.items_title_label.setStyleSheet(u"#items_title_label {\n"
"font-size: 14px\n"
"}")
        self.items_title_label.setIndent(4)

        self.verticalLayout_7.addWidget(self.items_title_label)

        self.renders_stacked_widget = QStackedWidget(self.submit_page)
        self.renders_stacked_widget.setObjectName(u"renders_stacked_widget")
        self.renders_stacked_widget.setStyleSheet(u"")
        self.renders_page = QWidget()
        self.renders_page.setObjectName(u"renders_page")
        self.horizontalLayout_7 = QHBoxLayout(self.renders_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.task_scroll = QScrollArea(self.renders_page)
        self.task_scroll.setObjectName(u"task_scroll")
        self.task_scroll.setStyleSheet(u"#task_scroll {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.task_scroll.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 359, 419))
        self.task_scroll.setWidget(self.contents)

        self.horizontalLayout_7.addWidget(self.task_scroll)

        self.renders_stacked_widget.addWidget(self.renders_page)
        self.no_renders_page = QWidget()
        self.no_renders_page.setObjectName(u"no_renders_page")
        self.no_renders_page.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.no_renders_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.no_renders_frame = QFrame(self.no_renders_page)
        self.no_renders_frame.setObjectName(u"no_renders_frame")
        self.no_renders_frame.setStyleSheet(u"#no_publishes_frame {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 2px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.no_renders_frame.setFrameShape(QFrame.StyledPanel)
        self.no_renders_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.no_renders_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(0, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.label_6 = QLabel(self.no_renders_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(0, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.no_renders_frame)

        self.renders_stacked_widget.addWidget(self.no_renders_page)

        self.verticalLayout_7.addWidget(self.renders_stacked_widget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_title_label = QLabel(self.submit_page)
        self.info_title_label.setObjectName(u"info_title_label")
        self.info_title_label.setStyleSheet(u"#info_title_label {\n"
"font-size: 14px\n"
"}")
        self.info_title_label.setIndent(4)

        self.verticalLayout.addWidget(self.info_title_label)

        self.groupBox = QGroupBox(self.submit_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 12, -1, -1)

        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.submit_page)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.submit_btn = QPushButton(self.submit_page)
        self.submit_btn.setObjectName(u"submit_btn")

        self.horizontalLayout.addWidget(self.submit_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.central_stackedWidget.addWidget(self.submit_page)
        self.progress_page = QWidget()
        self.progress_page.setObjectName(u"progress_page")
        self.verticalLayout_10 = QVBoxLayout(self.progress_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_7 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.title = QLabel(self.progress_page)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"#title {\n"
"font-size: 24px;\n"
"}")

        self.verticalLayout_9.addWidget(self.title)

        self.progress_details = QLabel(self.progress_page)
        self.progress_details.setObjectName(u"progress_details")
        self.progress_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.progress_details.setWordWrap(False)

        self.verticalLayout_9.addWidget(self.progress_details)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(3, 3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.central_stackedWidget.addWidget(self.progress_page)
        self.success_page = QWidget()
        self.success_page.setObjectName(u"success_page")
        self.verticalLayout_8 = QVBoxLayout(self.success_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_4 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.status_icon = QLabel(self.success_page)
        self.status_icon.setObjectName(u"status_icon")
        self.status_icon.setMinimumSize(QSize(80, 80))
        self.status_icon.setMaximumSize(QSize(80, 80))
        self.status_icon.setBaseSize(QSize(32, 32))
        self.status_icon.setPixmap(QPixmap(u":/res/success.png"))
        self.status_icon.setScaledContents(False)
        self.status_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.status_icon)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.success_status_title = QLabel(self.success_page)
        self.success_status_title.setObjectName(u"success_status_title")
        font = QFont()
        font.setPointSize(18)
        self.success_status_title.setFont(font)
        self.success_status_title.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.success_status_title)

        self.success_details = QLabel(self.success_page)
        self.success_details.setObjectName(u"success_details")
        self.success_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.success_details.setWordWrap(True)
        self.success_details.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.success_details)

        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6.setStretch(2, 3)
        self.horizontalLayout_6.setStretch(3, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.success_close_btn = QPushButton(self.success_page)
        self.success_close_btn.setObjectName(u"success_close_btn")

        self.horizontalLayout_5.addWidget(self.success_close_btn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.central_stackedWidget.addWidget(self.success_page)
        self.failure_page = QWidget()
        self.failure_page.setObjectName(u"failure_page")
        self.verticalLayout_19 = QVBoxLayout(self.failure_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_13 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.status_icon_3 = QLabel(self.failure_page)
        self.status_icon_3.setObjectName(u"status_icon_3")
        self.status_icon_3.setMinimumSize(QSize(80, 80))
        self.status_icon_3.setMaximumSize(QSize(80, 80))
        self.status_icon_3.setBaseSize(QSize(32, 32))
        self.status_icon_3.setPixmap(QPixmap(u":/res/failure.png"))
        self.status_icon_3.setScaledContents(False)
        self.status_icon_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.status_icon_3)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.failure_status_title = QLabel(self.failure_page)
        self.failure_status_title.setObjectName(u"failure_status_title")
        self.failure_status_title.setFont(font)
        self.failure_status_title.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.failure_status_title)

        self.failure_details = QLabel(self.failure_page)
        self.failure_details.setObjectName(u"failure_details")
        self.failure_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.failure_details.setWordWrap(True)
        self.failure_details.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_18.addWidget(self.failure_details)

        self.verticalLayout_18.setStretch(1, 1)

        self.horizontalLayout_15.addLayout(self.verticalLayout_18)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_15.setStretch(2, 3)
        self.horizontalLayout_15.setStretch(3, 1)

        self.verticalLayout_19.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_15 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.failure_close_btn = QPushButton(self.failure_page)
        self.failure_close_btn.setObjectName(u"failure_close_btn")

        self.horizontalLayout_14.addWidget(self.failure_close_btn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_14)

        self.central_stackedWidget.addWidget(self.failure_page)

        self.horizontalLayout_2.addWidget(self.central_stackedWidget)


        self.retranslateUi(Dialog)

        self.central_stackedWidget.setCurrentIndex(0)
        self.renders_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tank Dialog", None))
        self.items_title_label.setText(QCoreApplication.translate("Dialog", u"Choose Items to Submit:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-style:italic;\">This render does not have any optional items to choose from.</span></p></body></html>", None))
        self.info_title_label.setText(QCoreApplication.translate("Dialog", u"Job Attributes:", None))
        self.groupBox.setTitle("")
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.submit_btn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Submitting...", None))
        self.progress_details.setText(QCoreApplication.translate("Dialog", u"Please wait while submitting to the render farm.", None))
        self.status_icon.setText("")
        self.success_status_title.setText(QCoreApplication.translate("Dialog", u"Success!", None))
        self.success_details.setText(QCoreApplication.translate("Dialog", u"Submission was successfully sent to the render farm.", None))
        self.success_close_btn.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.status_icon_3.setText("")
        self.failure_status_title.setText(QCoreApplication.translate("Dialog", u"Failure!", None))
        self.failure_details.setText(QCoreApplication.translate("Dialog", u"Details...", None))
        self.failure_close_btn.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

