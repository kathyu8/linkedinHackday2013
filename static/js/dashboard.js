$(document).ready(function() {  

	$("#saveBtn").on("click", function() {
		console.log("clicked");
		$("#saveBtn").css("opacity", 1);
	});

    $('#university').click(function() {
        var $this = $(this);
        if ($this.is(':checked')) {
            console.log('check');
        } else {
            console.log('uncheck');
        }
    });
});

