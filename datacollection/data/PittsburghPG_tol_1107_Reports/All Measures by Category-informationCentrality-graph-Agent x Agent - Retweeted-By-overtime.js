Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['2018-10-27 12 AM','2018-10-27 12 PM','2018-10-28 12 AM','2018-10-28 12 PM','2018-10-29 12 AM','2018-10-29 12 PM',],
datasets : [
{
label: 'PittsburghPG',
fill: false,
borderColor: 'rgba(255,0,0,1)',
pointHoverBackgroundColor: 'rgba(255,0,0,1)',
pointBorderColor: 'rgba(255,0,0,1)',
lineTension: 0.0,
data : [0,0.121627,0.0717655,0.0653297,0.132855,0.0979768,]
},
{
label: 'asmeltz',
fill: false,
borderColor: 'rgba(0,255,0,1)',
pointHoverBackgroundColor: 'rgba(0,255,0,1)',
pointBorderColor: 'rgba(0,255,0,1)',
lineTension: 0.0,
data : [0,0,0.0671063,0.0555243,0.0176016,0.100236,]
},
{
label: 'brianstelter',
fill: false,
borderColor: 'rgba(0,0,255,1)',
pointHoverBackgroundColor: 'rgba(0,0,255,1)',
pointBorderColor: 'rgba(0,0,255,1)',
lineTension: 0.0,
data : [0,0,0.0726888,0.0221582,0.0175762,0.00545513,]
},
{
label: 'PaulaReedWard',
fill: false,
borderColor: 'rgba(240,230,140,1)',
pointHoverBackgroundColor: 'rgba(240,230,140,1)',
pointBorderColor: 'rgba(240,230,140,1)',
lineTension: 0.0,
data : [0,0,0.0215946,0.0606856,0.0226003,0.0147254,]
},
{
label: 'GHMansfield',
fill: false,
borderColor: 'rgba(240,128,128,1)',
pointHoverBackgroundColor: 'rgba(240,128,128,1)',
pointBorderColor: 'rgba(240,128,128,1)',
lineTension: 0.0,
data : [0,0,0,0.0400128,0.0900252,0.0225392,]
},
]
}
var context = document.getElementById('All Measures by Category-informationCentrality-graph-Agent x Agent - Retweeted-By-overtime').getContext("2d");
var chart = new Chart(context, {
		autowidth:false,
		type: 'line',
		data: data,
});

