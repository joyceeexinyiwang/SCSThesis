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
data : [0,0.114731,0.0338297,0.0156297,0.0131305,0.0244174,]
},
{
label: 'shyduroff',
fill: false,
borderColor: 'rgba(0,255,0,1)',
pointHoverBackgroundColor: 'rgba(0,255,0,1)',
pointBorderColor: 'rgba(0,255,0,1)',
lineTension: 0.0,
data : [0,0.114731,0,0,0,0,]
},
{
label: 'lorakolodny',
fill: false,
borderColor: 'rgba(0,0,255,1)',
pointHoverBackgroundColor: 'rgba(0,0,255,1)',
pointBorderColor: 'rgba(0,0,255,1)',
lineTension: 0.0,
data : [0,0.114731,0,0,0,0,]
},
{
label: 'neelaeast',
fill: false,
borderColor: 'rgba(240,230,140,1)',
pointHoverBackgroundColor: 'rgba(240,230,140,1)',
pointBorderColor: 'rgba(240,230,140,1)',
lineTension: 0.0,
data : [0,0.114731,0,0,0,0,]
},
{
label: 'irishzionist',
fill: false,
borderColor: 'rgba(240,128,128,1)',
pointHoverBackgroundColor: 'rgba(240,128,128,1)',
pointBorderColor: 'rgba(240,128,128,1)',
lineTension: 0.0,
data : [0,0.114731,0,0,0,0,]
},
]
}
var context = document.getElementById('All Measures by Category-eigenvectorCentrality-graph-Agent x Agent - Common Hashtags-overtime').getContext("2d");
var chart = new Chart(context, {
		autowidth:false,
		type: 'line',
		data: data,
});

