setInterval(function(){
    $.get('/api/notification/enf/empty/blood-stock',function(data) {
        document.getElementById("notifEmptybloodStock").innerHTML = data.value;
    });
}, 100);
console.log(data.value)