Chart.defaults.global.legend.position = 'bottom'

var data = {
labels:['1051116280348987392','1050974410520363010','1050808321010069504','1051199739524513792','1051197580741357568','1051197245943701505','1050764472611196928','1051199680602730496','1051149810324201473','1051298965721899009','1051201653205098497','1051177129872900096','1051145202960912386',],
datasets : [
{
label: 'Tweet (Twitter JSON #JamalKhashoggi_AJEnglish_tweets_1_max10000000)',
backgroundColor: 'rgba(255,0,0,0.2)',
borderColor: 'rgba(255,0,0,1)',
borderWidth: 1,
data : [56.25,50,50,25,25,25,18.75,12.5,12.5,6.25,6.25,6.25,6.25,]
},
]
}
var context = document.getElementById('All Measures by Category-Twitter_JSON__JamalKhashoggi_AJEnglish_tweets_1_max10000000--Tweet-overall-top-ranked-barchart').getContext("2d");
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

