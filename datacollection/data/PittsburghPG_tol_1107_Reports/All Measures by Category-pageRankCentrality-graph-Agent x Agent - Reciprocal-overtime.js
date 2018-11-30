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
data : [0,0.0325204,0.0235764,0.0264749,0.0187524,0.0261435,]
},
{
label: 'PGVisuals',
fill: false,
borderColor: 'rgba(0,255,0,1)',
pointHoverBackgroundColor: 'rgba(0,255,0,1)',
pointBorderColor: 'rgba(0,255,0,1)',
lineTension: 0.0,
data : [0,0.00487805,0.00687328,0.0135725,0.00753204,0.00800236,]
},
{
label: 'AllanMargolin',
fill: false,
borderColor: 'rgba(0,0,255,1)',
pointHoverBackgroundColor: 'rgba(0,0,255,1)',
pointBorderColor: 'rgba(0,0,255,1)',
lineTension: 0.0,
data : [0,0,0.00826737,0.00636094,0.00143955,0.00969047,]
},
{
label: 'ShellyBradbury',
fill: false,
borderColor: 'rgba(240,230,140,1)',
pointHoverBackgroundColor: 'rgba(240,230,140,1)',
pointBorderColor: 'rgba(240,230,140,1)',
lineTension: 0.0,
data : [0,0.00487805,0.011024,0.00783661,0.00959646,0.00123103,]
},
{
label: 'RetProf77',
fill: false,
borderColor: 'rgba(240,128,128,1)',
pointHoverBackgroundColor: 'rgba(240,128,128,1)',
pointBorderColor: 'rgba(240,128,128,1)',
lineTension: 0.0,
data : [0,0,0,0,0.0140054,0,]
},
]
}
var context = document.getElementById('All Measures by Category-pageRankCentrality-graph-Agent x Agent - Reciprocal-overtime').getContext("2d");
var chart = new Chart(context, {
		autowidth:false,
		type: 'line',
		data: data,
});

