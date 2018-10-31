Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['AJEnglish','atoker','ClaudiaWolfgang','123Tatiana','60Macc','1stAbu','ricfouad','RealNewsLine','MaryAnnAlbright','mikeymikedoha','0ok','M_S_S_Q','johnhendren','chapachula','JonAbs_Mom','Amoonlight7',],
datasets : [
{
label: 'Agent (Twitter JSON #JamalKhashoggi_AJEnglish_tweets_1_max10000000)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [56.25,37.5,25,25,25,25,18.75,18.75,12.5,12.5,12.5,6.25,6.25,6.25,6.25,6.25,]
},
]
}
var context = document.getElementById('All Measures by Category-Twitter_JSON__JamalKhashoggi_AJEnglish_tweets_1_max10000000--Agent-overall-top-ranked-barchart').getContext("2d");
var chart = new Chart(context, {
		type: 'bar',
		data: data,
		options: {
			autowidth:false,
			scales: {
			yAxes: [{
				ticks: {
					beginAtZero:true
				}
			}]
		}
	}
});

