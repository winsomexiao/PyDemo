QWidget#WinsWidgetView{
    background: #222222;
    border: 5px;
    border-style: solid;
}

QPushButton#searchBtn{
    width: 25px;
    height: 25px;
    border-image: url(icons/search.png);
}

QPushButton#searchBtn::hover{
    width: 25px;
    height: 25px;
    border-image: url(../icons/search_hover.png);
}

QPushButton#closeBtn, QPushButton#minBtn, QPushButton#maxBtn{
    color: gray;
    font-family: "Yahei consolas Hybrid";
    font-weight: bold;
    font-size: 30px;
    border: 0px;
}

QPushButton#loginBtn{
    border: 0px;
    font-family: "Yahei consolas Hybrid";
    font-weight: bold;
    color: #BABABA;
}

QPushButton#logins{
    font-family: "Yahei consolas Hybrid";
    font-weight: bold;
    color: black;
}

QPushButton#loginBtn::hover, QPushButton#closeBtn::hover, QPushButton#minBtn::hover, QPushButton#maxBtn::hover{
    color: white;
}

QPushButton#searchBtn{
   border: 5px;
   background-color: #D3D3D3;
   border-radius: 5px;
   font: bold;

}

QPushButton#searchBtn::hover{
   border: 5px;
   background-color: gray;
   border-radius: 5px;
   font-weight: bold;
}

QPushButton#searchBtn::focus{
   border: 5px;
   background-color: gray;
   border-radius: 5px;
   font-weight: bold;
   color: #E6E8FA;
}


QLabel{
    font-family: "Yahei consolas Hybrid";
    font-weight: bold;
}

QLabel#headpic{
    border: 5px solid;
    border-radius: 25px;
}

QLabel#addBtn{
    border: 5px;
    border-width: 3px;
    border-style: solid;
    border-top-color: qradialgradient(spread:pad, cx:0.7, cy:0.5, radius:1, fx:0.7, fy:0.5,
stop:0.1 #000000, stop:1 #CD0000);
    border-left-color: #222222;
    border-right-color: #222222;
    border-bottom-color: #222222;
    color: gray;
}



}

QLineEdit#SearchInput{
    background: #000000;
    border: 5px solid;
    border-radius: 10px;
    font-weight: bold;
    color: gray;
}

QLineEdit#SearchInput::active{
    width: 200px;
    background: #000000;
    border: 5px solid;
    border-radius: 10px;
    color: gray;
}

QTableView#tableView::item:hover{
    outline: #363636;
    outline-style: none;
    background-color: #BFEFFF;
    color: #000000;
}

QTableView#tableView::item:selected{
    outline: #363636;
    outline-style: none;
    background-color: #BFEFFF;
    color: #000000;
}

QTableView#tableView{
    background-color: #222222;
    border: 5px solid;
    border-bottom: 0px;
    border-left: 0px;
    border-right: 0px;
    color: white;

}

QTableView#tableView::item{
    outline: #363636;
    outline-style: none;
    border: 0px solid #363636;
    background-color: #000000;
    color: #D6D6D6;
    border-radius: 8px;
    selection-background-color: #993333;
}

QHeaderView::section{
    background-color: #000000;
    color: white;
}

QHeaderView{
    background-color: #000000;
    color: white;
}

QScrollBar:vertical{
    background: #363636;
    width: 7px;
    margin: 0px 0 0px 0;
}

QScrollBar:horizontal{
    background: #363636;
    width: 7px;
    margin: 0 0 0 0;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: lightgray;
    min-height: 20px;
    margin: 0 0 0 0;
    border-radius: 3px;
    border: none;
}

QScrollBar::handle:hover{
    background: gray;
    min-height: 20px;
    margin: 0 0 0 0;
    border-radius: 3px;
    border: none;
}

QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal {
    background: #363636;
    height: 0px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal {
    background: #363636;
    height: 0px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical, QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
    border: 1px solid grey;
    width: 3px;
    height: 3px;
    background: white;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}


QDialog{
    background: white;
    border-radius: 10px;
    padding: 5px;
}
