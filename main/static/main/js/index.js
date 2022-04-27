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

function openAdd() {
  document.getElementsByClassName("add-new-task")[0].style.opacity = "1";
  document.getElementsByClassName("add-new-task")[0].style.visibility = "visible";
}

function closeAdd(){
  document.getElementsByClassName("add-new-task")[0].style.opacity = "0";
  document.getElementsByClassName("add-new-task")[0].style.visibility = "hidden";
}
