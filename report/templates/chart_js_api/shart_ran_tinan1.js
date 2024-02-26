document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#reportrantinan1"), {
    series: [{
      name: 'AB⁺',
      data: ["{% for xx in loopingetinanRAnTama %}","{{xx.total5|floatformat:'3'}}","{% endfor %}"]
    },{
      name: 'ABˉ',
      data: ["{% for xx in loopingetinanRAnTama %}","{{xx.total6|floatformat:'3'}}","{% endfor %}"]
    },{
      name: 'O⁺',
      data: ["{% for xx in loopingetinanRAnTama %}","{{xx.total7|floatformat:'3'}}","{% endfor %}"]
    }, {
      name: 'Oˉ',
      data: ["{% for xx in loopingetinanRAnTama %}","{{xx.total8}}","{% endfor %}"]
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
    colors: ['#33FFE0','#33FF39','red','#AAB7B8','yellow', '#F1C40F','#CB4335 ','#2874A6',],
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
      categories: ["{% for ii in loopingetinanRAnTama %}","{{ii.donationdate__year}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});
