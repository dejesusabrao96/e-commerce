
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('orderChart').getContext('2d');
    var data = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [{
            label: 'Total Price per Month',
            data: ["{% for xx in loopingpriceeyears %}","{{xx.total1|floatformat:'3'}} ","{% endfor %}"],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    var options = {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    };

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: options
    });
});
