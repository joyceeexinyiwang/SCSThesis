Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['2018-10-27 12 AM','2018-10-27 12 PM','2018-10-28 12 AM','2018-10-28 12 PM','2018-10-29 12 AM','2018-10-29 12 PM',],
datasets : [
{
label: 'Indira_L',
fill: false,
borderColor: 'rgba(255,0,0,1)',
pointHoverBackgroundColor: 'rgba(255,0,0,1)',
pointBorderColor: 'rgba(255,0,0,1)',
lineTension: 0.0,
data : [0,0.082228,0.0341836,0.0360613,0.0137064,0.039677,]
},
{
label: 'PittsburghPG',
fill: false,
borderColor: 'rgba(0,255,0,1)',
pointHoverBackgroundColor: 'rgba(0,255,0,1)',
pointBorderColor: 'rgba(0,255,0,1)',
lineTension: 0.0,
data : [0,0.0711428,0.00823167,0.0075189,0,0.0129439,]
},
{
label: 'SEberson_pg',
fill: false,
borderColor: 'rgba(0,0,255,1)',
pointHoverBackgroundColor: 'rgba(0,0,255,1)',
pointBorderColor: 'rgba(0,0,255,1)',
lineTension: 0.0,
data : [0,0,0,0.040453,0.00832158,0.0436633,]
},
{
label: 'BrookeBCNN',
fill: false,
borderColor: 'rgba(240,230,140,1)',
pointHoverBackgroundColor: 'rgba(240,230,140,1)',
pointBorderColor: 'rgba(240,230,140,1)',
lineTension: 0.0,
data : [0,0.127067,0.00668918,0.00937242,0,0.0152368,]
},
{
label: 'FranceBedos',
fill: false,
borderColor: 'rgba(240,128,128,1)',
pointHoverBackgroundColor: 'rgba(240,128,128,1)',
pointBorderColor: 'rgba(240,128,128,1)',
lineTension: 0.0,
data : [0,0.0876208,0,0.0262891,0,0,]
},
]
}
var context = document.getElementById('All Measures by Category-contributionCentrality-graph-Agent x Agent - Common Hashtags-overtime').getContext("2d");
var chart = new Chart(context, {
		autowidth:false,
		type: 'line',
		data: data,
});

