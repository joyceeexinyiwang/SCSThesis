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
data : [0,0.00130015,0.00679451,0.00206524,0.00705445,0.0041614,]
},
{
label: 'PittsburghPG',
fill: false,
borderColor: 'rgba(0,255,0,1)',
pointHoverBackgroundColor: 'rgba(0,255,0,1)',
pointBorderColor: 'rgba(0,255,0,1)',
lineTension: 0.0,
data : [0,0.000540732,0.00128026,0.0025121,0.00172192,0.00347949,]
},
{
label: 'SEberson_pg',
fill: false,
borderColor: 'rgba(0,0,255,1)',
pointHoverBackgroundColor: 'rgba(0,0,255,1)',
pointBorderColor: 'rgba(0,0,255,1)',
lineTension: 0.0,
data : [0,0,0,0.00312606,0.00518432,0.00445481,]
},
{
label: 'BrookeBCNN',
fill: false,
borderColor: 'rgba(240,230,140,1)',
pointHoverBackgroundColor: 'rgba(240,230,140,1)',
pointBorderColor: 'rgba(240,230,140,1)',
lineTension: 0.0,
data : [0,0.00099778,0.00276656,0.000284791,0,0.00078073,]
},
{
label: 'shyduroff',
fill: false,
borderColor: 'rgba(240,128,128,1)',
pointHoverBackgroundColor: 'rgba(240,128,128,1)',
pointBorderColor: 'rgba(240,128,128,1)',
lineTension: 0.0,
data : [0,0.00130015,0,0,0,0,]
},
]
}
var context = document.getElementById('All Measures by Category-bonacichPowerCentrality-graph-Agent x Agent - Common Hashtags-overtime').getContext("2d");
var chart = new Chart(context, {
		autowidth:false,
		type: 'line',
		data: data,
});

