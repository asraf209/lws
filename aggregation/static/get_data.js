$().ready(function () {
     var url = 'http://lws.at-band-camp.net/devices/device/data/time/json?devid=1b7239de&startdate=0307201315045&enddate=03072013150744&celc=False';             
     $.get(url, function (data) {
     	var data_json = jQuery.parseJSON(data);
    	console.log(data_json) 
    });
});
google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
var data = google.visualization.arrayToDataTable([
                                                 ['Year', 'Sales', 'Expenses'],
                                                 ['2004',1000,400],
                                                 ['2005',1170,460],
                                                 ['2006',660,1120],
                                                 ['2007',1030,540]
                                                ]);
                
var options = {
           title: 'Company Performance'
};
var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
chart.draw(data, options);
}

