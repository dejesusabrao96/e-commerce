document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportsChart8"), {
    series: [{
      name: 'Paid',
      data: ["{% for xx in loopingCategoory %}","{{xx.total1|floatformat:'3'}}","{% endfor %}"]
    }, {
      name: 'Panding',
      data: ["{% for xx in loopingCategoory %}","{{xx.total2|floatformat:'3'}}","{% endfor %}"]
    },{
      name: 'Process',
      data: ["{% for xx in loopingCategoory %}","{{xx.total3|floatformat:'3'}}","{% endfor %}"]
    }],
    chart: {
      height: 400,
      type: 'bar',
      toolbar: {
        show: false
      },
    },
    markers: {
      size: 12
    },
    colors: ['red', 'yellow','green'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'smooth',
      width: 1
    },
    xaxis: {
      type: 'text',
      categories: ["{% for ii in loopingCategoory %}","{{ii.name}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});
