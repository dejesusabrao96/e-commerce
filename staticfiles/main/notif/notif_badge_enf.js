setInterval(function(){
    $.get('/api/notification/enfermaria/badge/',function(data) {
        document.getElementById("notifbadgeenf").innerHTML = data.value;
    });
}, 100);
console.log(data.value)