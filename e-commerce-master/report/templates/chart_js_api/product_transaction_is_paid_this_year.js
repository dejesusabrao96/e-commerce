
var endpoint = '/api/g/product-is-paid/stock/bank/this-year/'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        const dt = {
            labels: data.label,
            datasets: [
            {
                label: data.obj1a,
                data: data.obj1,
                backgroundColor: 'rgba(225, 92, 92, 1)',
                borderWidth: 1
            },
            {
                label: data.obj2a,
                data: data.obj2,
                backgroundColor: 'rgba(0, 0, 9, 0.5)',
                borderWidth: 1
            },
        
            ]
        };
        
        const config_gbloodbankedusedoutstockbankthisyear = {
            type: 'bar',
            data: dt,
            options: groupoption
        };
        const gbloodbankedusedoutstockbankthisyear_data = new Chart(
            document.getElementById('gbloodbankedusedoutstockbankthisyear_data'),
            config_gbloodbankedusedoutstockbankthisyear
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
