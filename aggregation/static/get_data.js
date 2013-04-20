$().ready(function () {
     var url = 'http://lws.at-band-camp.net/devices/device/data/time/json?devid=1b7239de&startdate=0307201315045&enddate=03072013150744&celc=False';             
     $.get(url, function (data) {
     	var data_json = jQuery.parseJSON(data);
	//console.log(data_json)
	var sensor_data_list = new Array();
	var data_to_table = { cols:[],rows:[] }
	var temp_list = new Array();
	for (var i = 0; i < data_json.length; i++) {
		sensor_data_list.push(data_json[i].sensor_data);
		for (var key in data_json[i]) {
  			if (data_json[i].hasOwnProperty(key)) {
					
  			}
		}
	}
	for (var i=0; i< sensor_data_list.length ; i++){
		temp_list.push(sensor_data_list[i]["Temperature Sensor"])
	}	

	console.log(temp_list)
	data_chart(temp_list,"Month Sensor Data","month_sensor_data")
    });
});

function data_chart(json_data,chart_title,div_tag){
	var now = new Date();
	//console.log(now)

	google.load("visualization", "1", {packages:["corechart"]});
	google.setOnLoadCallback(drawChart);
	function drawChart() {
		var data = google.visualization.DataTable(json_data);
                
		var options = {
        		title: chart_title
		};
		var chart = new google.visualization.LineChart(document.getElementById(div_tag));
		chart.draw(data, options);
	}
}

