$().ready(function () {
     var url = 'http://lws.at-band-camp.net/devices/device/data/time/json?devid=1b7239de&startdate=0307201315045&enddate=03072013150744&celc=False';             
     $.get(url, function (data) {
     	var data_json = jQuery.parseJSON(data);
	console.log(data_json)
	for (var i = 0; i < data_json.length; i++) {
		console.log(data_json[i])
		for (var key in data_json[i]) {
  			if (data_json[i].hasOwnProperty(key)) {
    				console.log(key + " -> " + data_json[i][key]);
  			}
		}
	}
    });
});

data_chart("test","Month Sensor Data","month_sensor_data")
data_chart("test","Day Sensor Data","day_sensor_data")
data_chart("test","Year Sensor Data","year_sensor_data")

function data_chart(json_data,chart_title,div_tag){
	var now = new Date();
	console.log(now)

	google.load("visualization", "1", {packages:["corechart"]});
	google.setOnLoadCallback(drawChart);
	function drawChart() {
		var data = google.visualization.arrayToDataTable([]);
                
		var options = {
        		title: chart_title
		};
		var chart = new google.visualization.LineChart(document.getElementById(div_tag));
		chart.draw(data, options);
	}
}

