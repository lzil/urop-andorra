$(document).ready(function() {
	$('.tab').hide();
	$('#tab-stats').show();
	$('.tab-links li').click(function() {
		$('.tab-links li').removeClass('active');
		$(this).addClass('active');
		$('.tab').hide();
		console.log(this)
		var id = $(this).attr('id')
		console.log(id)
		$('#tab-' + id).show();

	})
})

google.load("visualization", "1", {packages:["corechart", 'line', 'bar']});
google.setOnLoadCallback(drawChart);
function drawChart() {

var data = google.visualization.arrayToDataTable([
  ['Language', 'percent'],
  ['es',     1891],
  ['pt',      1394],
  ['en',  		842],
  ['fr', 408],
  ['it', 98],
  ['nl', 45],
  ['ro', 37],
  ['other', 190]
]);

var options = {
  title: 'Language Distribution'
};

var chart = new google.visualization.PieChart(document.getElementById('piechart'));

chart.draw(data, options);
}

google.setOnLoadCallback(drawBackgroundColor);

function drawBackgroundColor() {
      var data = new google.visualization.DataTable();
      data.addColumn('number', 'X');
      data.addColumn('number', 'Calls');

      data.addRows([
        [0, 94],   [1, 160],  [2, 120],  [3, 127],  [4, 89],  [5, 95],
        [6, 151],  [7, 143],  [8, 164],  [9, 182],  [10, 182], [11, 234],
        [12, 234], [13, 244], [14, 234], [15, 262], [16, 311], [17, 250],
        [18, 293], [19, 341], [20, 379], [21, 368], [22, 287], [23, 185]
      ]);

      var options = {
        hAxis: {
          title: 'Number of Calls'
        },
        vAxis: {
          title: 'Hour'
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('hours'));
      chart.draw(data, options);
    }

google.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = google.visualization.arrayToDataTable([
        ['Platform', 'Number',],
        ['Web Client', 1743],
        ['Android', 1528],
        ['Instagram', 779],
        ['iPhone', 649],
        ['iPad', 171],
        ['Other', 218]
      ]);

      var options = {
        title: 'Platforms for Tweeting',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Number',
          minValue: 0
        },
        vAxis: {
          title: 'Platform'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('platform'));

      chart.draw(data, options);
    }