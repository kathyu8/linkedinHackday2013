jQuery(document).ready(function($) {

	$("#jobOptions").on("click", applyForm);

	$("#applySelectedJobs").on('click', function(e){
		var jobPosts = $(".jobPost");
		jobPosts.each(function(i, jobPost){
			if($("#willApply").is(':checked')) {
				applyForm(e);
			}
		});
		return false;
	});

	$("#applyAllJobs").on('click', function(e){
		var jobPosts = $(".jobPost");
		$(".jobPost").each(function(i, jobPost){
			applyForm(e);
		});
		return false;
	});

    $('#university').click(function() {
        var $this = $(this);
        if ($this.is(':checked')) {
            var filter = $("#uni-options :selected").text();
            $('.job-uni').each(function(i, obj) {
                 if ($(this).html().indexOf(filter) == -1) {
                    $(this).parents(".jobPost").hide();
                 }
            });
        } else {
            $('.job-uni').each(function(i, obj) {
                $(this).parents(".jobPost").show();
            });
        }
    });

    $('#uni-options').change(function() {
        var filter = $("#uni-options :selected").text();
        $('.job-uni').each(function(i, obj) {
             if ($(this).html().indexOf(filter) == -1) {
                $(this).parents(".jobPost").hide();
             } else {
                $(this).parents(".jobPost").show();
             }
        });
    });

});

function applyForm(e){
	console.log("applying!");
	$("#apply").attr("id","applied");
	$("#apply").html("Applied");
	$("#checkmark").show();
	$("#checkmark").attr("display", "inline");
	e.preventDefault();
	return false;
}