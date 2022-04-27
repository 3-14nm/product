var closeChoose = 0;
function openNewTask() {
  document.getElementsByClassName("new-task-class")[0].style.opacity = "1";
  document.getElementsByClassName("new-task-class")[0].style.visibility = "visible";
}

function closeNewTask(){
  document.getElementsByClassName("new-task-class")[0].style.opacity = "0";
  document.getElementsByClassName("new-task-class")[0].style.visibility = "hidden";
}

function openChooseStatus(){

if(closeChoose==1){
  document.getElementsByClassName("change-status")[0].style.visibility = "hidden";
  document.getElementsByClassName("change-status")[0].style.opacity = "0";
  closeChoose=0

}
  else if(closeChoose==0) {

  document.getElementsByClassName("change-status")[0].style.opacity = "1";
  document.getElementsByClassName("change-status")[0].style.visibility = "visible";
  closeChoose=1

  }

  //https://learn.javascript.ru/form-elements
  }

var closeExit = 0
function close(){
  if(closeExit==1){
  document.getElementsByClassName("log")[0].style.visibility = "hidden";
  document.getElementsByClassName("log")[0].style.opacity = "0";
  closeExit=0

}
  else if(closeExit==0) {

  document.getElementsByClassName("log")[0].style.opacity = "1";
  document.getElementsByClassName("log")[0].style.visibility = "visible";
  closeExit=1

  }
}

function processDone(){
   var elem=document.getElementsByClassName("done-ul");

    var my = '<h3>MYMYMYMYMY</h3>'
    elem.innerHTML=my
    console.log(elem)
    var done = '<div id="done"><li> <div class="name-task"><div class="name"><p>{{aim.title}}</p></div><div class="name-button"><a  href="javascript:onclick=openChooseStatus()"><button><img src="https://img.icons8.com/ios/30/000000/menu-2.png" height="22px;"/></button></a></div></div><div class="exp"><p>{{aim.description}}</p></div><div class="date-task"><img src="https://img.icons8.com/material-outlined/48/000000/clock--v1.png" width="15px;"/>{{aim.date}}</div></li></div>'

}
processDone()
