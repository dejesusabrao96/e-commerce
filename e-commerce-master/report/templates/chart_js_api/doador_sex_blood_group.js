document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportsChart1"), {
    series: [{
      name: 'Mane',
      data: ["{% for xx in loopingdoadorBlood %}","{{xx.doadorM|floatformat:'3'}} ","{% endfor %}"]
    }, {
      name: 'Feto',
      data: ["{% for xx in loopingdoadorBlood %}","{{xx.doadorF|floatformat:'3'}}","{% endfor %}"]
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
    colors: ['red', '#283593'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 0,
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
      categories: ["{% for ii in loopingdoadorBlood %}","{{ii.name}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});
