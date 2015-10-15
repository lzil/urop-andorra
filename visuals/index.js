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